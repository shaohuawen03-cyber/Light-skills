# Install-Safe.ps1 - Windows safe installer for Light-skills + BrowserSkill bridge
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File Install-Safe.ps1
# Policy: E:\0github\ base, never overwrite existing dirs

param(
    [string]$BaseDir = "E:\0github"
)

$ErrorActionPreference = "Stop"

Write-Host "== Light-skills + BrowserSkill Safe Installer ==" -ForegroundColor Cyan
Write-Host "BaseDir: $BaseDir (existing dirs will NOT be overwritten)" -ForegroundColor Cyan

if (-not (Test-Path -LiteralPath $BaseDir)) {
    Write-Host "[CREATE] $BaseDir" -ForegroundColor Green
    New-Item -ItemType Directory -Force -Path $BaseDir | Out-Null
} else {
    Write-Host "[EXISTS] $BaseDir" -ForegroundColor Green
}

function SafeClone($url, $branch, $name) {
    $dest = Join-Path $BaseDir $name
    if (Test-Path -LiteralPath $dest) {
        Write-Host "[SKIP] $dest already exists, not overwriting" -ForegroundColor Yellow
        Push-Location $dest
        try {
            $cur = (git rev-parse --abbrev-ref HEAD 2>$null).Trim()
            Write-Host "       current branch: $cur" -ForegroundColor DarkGray
        } finally { Pop-Location }
        return $dest
    } else {
        Write-Host "[CLONE] $url branch $branch -> $dest" -ForegroundColor Cyan
        git clone --depth 1 -b $branch $url $dest
        if ($LASTEXITCODE -ne 0) {
            Write-Host "[RETRY] without --depth" -ForegroundColor Yellow
            git clone -b $branch $url $dest
        }
        return $dest
    }
}

# 1. Clone Light-skills (this repo's branch)
$light = SafeClone "https://github.com/shaohuawen03-cyber/Light-skills.git" "arena/01a0b489-light-skills" "Light-skills"

# 2. Clone BrowserSkill (source of git-sync + arena-local-bridge)
$browser = SafeClone "https://github.com/shaohuawen03-cyber/BrowserSkill.git" "arena/01a0b237-browserskill" "BrowserSkill-01a0b237"

Write-Host ""
Write-Host "== Bootstrap ==" -ForegroundColor Cyan
foreach ($repo in @($light, $browser)) {
    if (-not (Test-Path -LiteralPath $repo)) { continue }
    $boot = Join-Path $repo "bootstrap.ps1"
    if (Test-Path -LiteralPath $boot) {
        Write-Host "Found $boot" -ForegroundColor Green
        Write-Host "  To enable bridge: cd $repo ; .\bootstrap.ps1 -Auto" -ForegroundColor White
        Write-Host "  Then: .\doctor.ps1 ; .\watch.ps1 -Status ; .\auth.ps1 -Verify" -ForegroundColor White
    }
}

# 3. Light-skills Python bootstrap
$pyBoot = Join-Path $light "scripts\bootstrap_agent_skills.py"
if (Test-Path -LiteralPath $pyBoot) {
    Write-Host ""
    Write-Host "== Light-skills Python skills ==" -ForegroundColor Cyan
    Write-Host "cd $light ; `$env:PYTHONUTF8=`"1`" ; python scripts\bootstrap_agent_skills.py --targets agents claude opencode --mode auto --force" -ForegroundColor White
}

# 4. bsk check
Write-Host ""
Write-Host "== bsk browser bridge (optional) ==" -ForegroundColor Cyan
if (Get-Command bsk -ErrorAction SilentlyContinue) {
    Write-Host "[OK] bsk found: $(bsk --version)" -ForegroundColor Green
} else {
    Write-Host "[INFO] bsk not found. Install with:" -ForegroundColor Yellow
    Write-Host "  irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex" -ForegroundColor White
    Write-Host "  Then install Edge extension and run bsk doctor" -ForegroundColor White
}

Write-Host ""
Write-Host "Done. Existing dirs were preserved. See docs\windows_browser_bridge_setup.md for full guide." -ForegroundColor Green
