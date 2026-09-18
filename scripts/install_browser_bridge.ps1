# install_browser_bridge.ps1 - Safe installer for BrowserSkill + Light-skills
# Windows PowerShell 5.1 compatible, ASCII-only
#
# Usage:
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts\install_browser_bridge.ps1
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts\install_browser_bridge.ps1 -BaseDir E:\0github -LightBranch arena/01a0b489-light-skills -BrowserBranch arena/01a0b237-browserskill
#
# Policy:
#   - BaseDir defaults to E:\0github
#   - NEVER overwrites existing directories
#   - If target exists, prints [SKIP] and shows where.cmd -Want hint
#   - Clones with --depth 1 for speed
#   - After clone, runs bootstrap.ps1 -Auto inside each repo to enable git-sync bridge

param(
    [string]$BaseDir = "E:\0github",
    [string]$LightUrl = "https://github.com/shaohuawen03-cyber/Light-skills.git",
    [string]$LightBranch = "arena/01a0b489-light-skills",
    [string]$LightDirName = "Light-skills",
    [string]$BrowserUrl = "https://github.com/shaohuawen03-cyber/BrowserSkill.git",
    [string]$BrowserBranch = "arena/01a0b237-browserskill",
    [string]$BrowserDirName = "BrowserSkill-01a0b237",
    [switch]$AutoBootstrap
)

$ErrorActionPreference = "Stop"

function Write-Info($msg) { Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-Skip($msg) { Write-Host "[SKIP] $msg" -ForegroundColor Yellow }
function Write-Ok($msg)   { Write-Host "[OK] $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "[WARN] $msg" -ForegroundColor Yellow }

# 1. Ensure BaseDir exists
if (-not (Test-Path -LiteralPath $BaseDir)) {
    Write-Info "Creating base dir $BaseDir"
    New-Item -ItemType Directory -Force -Path $BaseDir | Out-Null
} else {
    Write-Ok "Base dir exists: $BaseDir"
}

function Safe-Clone {
    param(
        [string]$Url,
        [string]$Branch,
        [string]$TargetPath
    )
    if (Test-Path -LiteralPath $TargetPath) {
        Write-Skip "Target already exists, will NOT overwrite: $TargetPath"
        if (Test-Path -LiteralPath (Join-Path $TargetPath ".git")) {
            try {
                Push-Location -LiteralPath $TargetPath
                $current = (git rev-parse --abbrev-ref HEAD 2>$null).Trim()
                $remote = (git remote get-url origin 2>$null).Trim()
                Write-Host "       existing: branch=$current remote=$remote" -ForegroundColor DarkGray
                Write-Host "       to update manually: cd $TargetPath ; .\sync.ps1" -ForegroundColor DarkGray
                # Optional: fetch without overwriting
                git fetch origin --quiet 2>$null
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "       fetched origin (no checkout overwritten)" -ForegroundColor DarkGray
                }
            } finally {
                Pop-Location
            }
        }
        return $false
    } else {
        Write-Info "Cloning $Url (branch $Branch) -> $TargetPath"
        git clone --quiet --depth 1 -b $Branch $Url $TargetPath
        if ($LASTEXITCODE -ne 0) {
            Write-Warn "git clone failed for $TargetPath, trying without --depth"
            git clone -b $Branch $Url $TargetPath
            if ($LASTEXITCODE -ne 0) { throw "clone failed: $Url" }
        }
        Write-Ok "Cloned $TargetPath"
        return $true
    }
}

$lightTarget = Join-Path $BaseDir $LightDirName
$browserTarget = Join-Path $BaseDir $BrowserDirName

$lightCloned = Safe-Clone -Url $LightUrl -Branch $LightBranch -TargetPath $lightTarget
$browserCloned = Safe-Clone -Url $BrowserUrl -Branch $BrowserBranch -TargetPath $browserTarget

Write-Host ""
Write-Host "== Summary ==" -ForegroundColor Cyan
Write-Host "BaseDir        : $BaseDir"
Write-Host "Light-skills   : $lightTarget (branch $LightBranch) cloned=$lightCloned"
Write-Host "BrowserSkill   : $browserTarget (branch $BrowserBranch) cloned=$browserCloned"
Write-Host ""

# 2. Bootstrap Light-skills agent skills (project-level mirrors)
if (Test-Path -LiteralPath $lightTarget) {
    Write-Info "Bootstrapping Light-skills agent discovery mirrors in $lightTarget"
    try {
        Push-Location -LiteralPath $lightTarget
        if (Test-Path -LiteralPath "scripts\bootstrap_agent_skills.py") {
            $env:PYTHONUTF8 = "1"
            python scripts\bootstrap_agent_skills.py --targets agents claude opencode --mode auto --force
            Write-Ok "Light-skills mirrors created (.agents/skills, .claude/skills, .opencode/skills)"
        } else {
            Write-Warn "bootstrap_agent_skills.py not found in $lightTarget"
        }
    } finally { Pop-Location }
}

# 3. Bootstrap BrowserSkill git-sync bridge
foreach ($repo in @($lightTarget, $browserTarget)) {
    if (-not (Test-Path -LiteralPath $repo)) { continue }
    $boot = Join-Path $repo "bootstrap.ps1"
    if (Test-Path -LiteralPath $boot) {
        Write-Info "Found bootstrap.ps1 in $repo"
        if ($AutoBootstrap) {
            Write-Info "Running bootstrap.ps1 -Auto in $repo (enables silent push + watcher)"
            try {
                Push-Location -LiteralPath $repo
                powershell -NoProfile -ExecutionPolicy Bypass -File .\bootstrap.ps1 -Auto
            } finally { Pop-Location }
        } else {
            Write-Host "  To enable local bridge, run:" -ForegroundColor DarkGray
            Write-Host "    cd $repo ; .\bootstrap.ps1 -Auto" -ForegroundColor White
            Write-Host "  Then verify:" -ForegroundColor DarkGray
            Write-Host "    .\doctor.ps1 ; .\watch.ps1 -Status ; .\auth.ps1 -Verify" -ForegroundColor White
        }
    }
}

# 4. bsk CLI check (BrowserSkill browser bridge)
Write-Host ""
Write-Host "== bsk browser bridge (optional, for arena-local-bridge skill) ==" -ForegroundColor Cyan
try {
    $bsk = Get-Command bsk -ErrorAction SilentlyContinue
    if ($bsk) {
        Write-Ok "bsk found: $($bsk.Source) ; version=$(bsk --version 2>$null)"
    } else {
        $localBsk = Join-Path $env:USERPROFILE ".local\bin\bsk.exe"
        if (Test-Path -LiteralPath $localBsk) {
            Write-Ok "bsk found at $localBsk ; version=$( & $localBsk --version 2>$null )"
        } else {
            Write-Warn "bsk not found. To install BrowserSkill browser control:"
            Write-Host "  irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex" -ForegroundColor White
            Write-Host "  Then install extension from Edge Add-ons / Chrome Web Store" -ForegroundColor White
            Write-Host "  Then: bsk doctor" -ForegroundColor White
        }
    }
} catch {
    Write-Warn "bsk check failed: $_"
}

Write-Host ""
Write-Host "== Next steps ==" -ForegroundColor Cyan
Write-Host "1. Safe clone done. Existing dirs were NOT overwritten."
Write-Host "2. To locate which clone to use for a given branch/session:"
Write-Host "   .\where.cmd -Want $BrowserBranch   (inside any clone)"
Write-Host "   .\where.cmd -Want $LightBranch"
Write-Host "3. Enable git-sync watcher (per repo, on demand, zero background by default):"
Write-Host "   cd $browserTarget ; .\watch.ps1 -Register   # activate"
Write-Host "   cd $browserTarget ; .\watch.ps1 -Status     # check heartbeat"
Write-Host "   cd $browserTarget ; .\watch.ps1 -Unregister # stop when done"
Write-Host "4. Verify silent push:"
Write-Host "   .\auth.ps1 -Setup ; .\auth.ps1 -Verify"
Write-Host "5. For Light-skills python skills:"
Write-Host "   `$env:PYTHONUTF8=`"1`" ; python scripts\bootstrap_agent_skills.py --check-only"
Write-Host ""
Write-Host "Done." -ForegroundColor Green
