# setup_windows.ps1 - One-click safe setup for Windows user
# Place: E:\0github\ is base, never overwrites existing folders
# Usage: Right-click PowerShell -> Run, or:
#   powershell -NoProfile -ExecutionPolicy Bypass -File E:\0github\Light-skills\setup_windows.ps1
#   powershell -NoProfile -ExecutionPolicy Bypass -File setup_windows.ps1 -BaseDir E:\0github -AutoBootstrap

param(
    [string]$BaseDir = "E:\0github",
    [switch]$AutoBootstrap
)

$ErrorActionPreference = "Stop"
$here = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }

# If this script is already inside E:\0github\Light-skills, use its own scripts folder
$installer = Join-Path $here "scripts\install_browser_bridge.ps1"
if (Test-Path -LiteralPath $installer) {
    Write-Host "Running $installer -BaseDir $BaseDir -AutoBootstrap:$AutoBootstrap" -ForegroundColor Cyan
    & $installer -BaseDir $BaseDir -AutoBootstrap:$AutoBootstrap
} else {
    # Fallback: direct clone logic for first-time user who only has this one file
    Write-Host "Installer not found at $installer, running inline safe clone" -ForegroundColor Yellow
    if (-not (Test-Path -LiteralPath $BaseDir)) {
        New-Item -ItemType Directory -Force -Path $BaseDir | Out-Null
    }
    $targets = @(
        @{ Url="https://github.com/shaohuawen03-cyber/BrowserSkill.git"; Branch="arena/01a0b237-browserskill"; Name="BrowserSkill-01a0b237" },
        @{ Url="https://github.com/shaohuawen03-cyber/Light-skills.git"; Branch="arena/01a0b489-light-skills"; Name="Light-skills" }
    )
    foreach ($t in $targets) {
        $dest = Join-Path $BaseDir $t.Name
        if (Test-Path -LiteralPath $dest) {
            Write-Host "[SKIP] $dest exists, not overwriting" -ForegroundColor Yellow
        } else {
            Write-Host "[CLONE] $($t.Url) branch $($t.Branch) -> $dest" -ForegroundColor Cyan
            git clone --depth 1 -b $t.Branch $t.Url $dest
        }
    }
    Write-Host "Done. Now run bootstrap in each clone if needed." -ForegroundColor Green
}
