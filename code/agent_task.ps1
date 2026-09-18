# agent_task.ps1 - Local machine task: generate ML umami peptide docx
# ASCII-only on purpose (Windows PowerShell 5.1 decodes .ps1 as ANSI/GBK)
# This file is executed by watch.ps1 when agent requests a check (hands-free)
# and also can be run manually: powershell -File code\agent_task.ps1

$ErrorActionPreference = "Continue"
Set-Location (Join-Path $PSScriptRoot "..")
Write-Output "== agent_task.ps1 start $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

# 1. Fix auth - pin to correct account if needed (shaohuawen03-cyber owns this repo)
Write-Output "== step 1: check auth"
try {
    $accounts = & .\auth.ps1 -Accounts 2>&1 | Out-String
    Write-Output $accounts
    # If active is mqgg but repo is shaohuawen, pin to shaohuawen
    if ($accounts -match "shaohuawen03-cyber" -and $accounts -match "active.*mqgg") {
        Write-Output "Detected active=mqgg but repo owner=shaohuawen, pinning to shaohuawen03-cyber"
        & .\auth.ps1 -Account shaohuawen03-cyber 2>&1 | Out-String | Write-Output
        & .\auth.ps1 -Verify 2>&1 | Out-String | Write-Output
    }
} catch {
    Write-Output "auth check failed: $_"
}

# 2. Show conda envs and lark
Write-Output "== step 2: conda envs and lark"
try {
    conda env list 2>&1 | Out-String | Write-Output
} catch { Write-Output "conda not in PATH, trying E:\hermes\..." }
try {
    Get-ChildItem E:\0mcp-agv\agents\cnki_agent -ErrorAction SilentlyContinue | Format-Table Name, Length | Out-String | Write-Output
} catch { Write-Output "cnki_agent dir not accessible" }
try {
    python -c "import lark; print('lark', lark.__version__)" 2>&1 | Out-String | Write-Output
} catch { Write-Output "lark not in base env" }
try {
    conda run -n lark python -c "import lark, docx; print('lark env ok')" 2>&1 | Out-String | Write-Output
} catch { Write-Output "conda run -n lark failed" }

# 3. Generate docx via python
Write-Output "== step 3: generate docx"
$pyCandidates = @("python", "python3", "py -3")
$py = $null
foreach ($c in $pyCandidates) {
    try {
        $null = Invoke-Expression "$c -c 'import sys; sys.exit(0)' 2>&1"
        if ($LASTEXITCODE -eq 0) { $py = $c; break }
    } catch {}
}
if (-not $py) { $py = "python" }
Write-Output "Using python: $py"

# Ensure python-docx installed
& $py -m pip install python-docx lark -q 2>&1 | Out-String | Write-Output

# Run generator
$genScript = "code\generate_umami_docx.py"
if (Test-Path -LiteralPath $genScript) {
    & $py $genScript 2>&1 | Out-String | Write-Output
    if ($LASTEXITCODE -eq 0) {
        Write-Output "gen script succeeded"
    } else {
        Write-Output "gen script failed with $LASTEXITCODE"
    }
} else {
    Write-Output "gen script not found: $genScript"
}

# 4. Also try cnki_agent if exists
$cnki = "E:\0mcp-agv\agents\cnki_agent"
if (Test-Path -LiteralPath $cnki) {
    Write-Output "== step 4: try cnki_agent"
    $cnkiMain = Join-Path $cnki "main.py"
    $cnkiAgent = Join-Path $cnki "agent.py"
    if (Test-Path -LiteralPath $cnkiMain) {
        Write-Output "Found $cnkiMain, attempting to run with thesis template"
        try {
            & $py $cnkiMain --help 2>&1 | Out-String | Write-Output
        } catch { Write-Output "cnki_agent main.py --help failed" }
    }
    # List files
    Get-ChildItem -LiteralPath $cnki -Recurse -Depth 2 | Select-Object -First 20 FullName | Out-String | Write-Output
}

# 5. Verify deliverables
Write-Output "== step 5: verify deliverables"
$deliverable = "deliverable"
if (Test-Path -LiteralPath $deliverable) {
    Get-ChildItem -LiteralPath $deliverable | Format-Table Name, Length, LastWriteTime | Out-String | Write-Output
    $docx = Get-ChildItem -LiteralPath $deliverable -Filter *.docx -ErrorAction SilentlyContinue
    if ($docx) {
        Write-Output "Found docx: $($docx.Name) size $($docx.Length)"
    } else {
        Write-Output "No docx found in deliverable"
    }
} else {
    Write-Output "deliverable dir missing, creating"
    New-Item -ItemType Directory -Force -Path $deliverable | Out-Null
}

# 6. Write success criteria via python (to keep this .ps1 ASCII-only)
$statusDir = "results\status"
New-Item -ItemType Directory -Force -Path $statusDir | Out-Null
$critPath = Join-Path $statusDir "success_criteria.json"
# Use python to write JSON with UTF-8 Chinese to avoid non-ASCII in .ps1
# Chinese file name is encoded as \uXXXX to keep .ps1 ASCII
$pyWrite = @"
import json, pathlib
p = pathlib.Path(r"results/status/success_criteria.json")
p.parent.mkdir(parents=True, exist_ok=True)
cn = "\u673a\u5668\u5b66\u4e60\u7b5b\u9009\u9c9c\u5473\u80bd\u6bd5\u4e1a\u8bba\u6587.docx"
data = {
    "description": "ML umami peptide thesis docx generated via local self-loop",
    "require_files": [
        f"deliverable/{cn}",
        "deliverable/ML_Umami_Peptide_Screening_Thesis.docx"
    ],
    "min_bytes": {
        f"deliverable/{cn}": 10000
    }
}
p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Wrote {p}")
"@
$tmpPy = "results\status\_write_criteria.py"
Set-Content -LiteralPath $tmpPy -Value $pyWrite -Encoding UTF8
& $py $tmpPy 2>&1 | Out-String | Write-Output
Remove-Item -LiteralPath $tmpPy -ErrorAction SilentlyContinue
Write-Output "Wrote $critPath via python"

Write-Output "== agent_task.ps1 end $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') exit 0"
exit 0
