# Push local changes in this repo to its GitHub remote.
#
# Run from PowerShell inside the repo folder:
#     powershell -ExecutionPolicy Bypass -File .\push-to-github.ps1
#
# Uses your existing git identity (git config user.name / user.email).
# Nothing personal is stored in this script.

$ErrorActionPreference = "Stop"
$repo    = $PSScriptRoot
$repoUrl = "https://github.com/3301Return/wsg-content.git"
$branch  = "main"

Set-Location $repo

if (-not (git config user.email)) {
    Write-Host "No git identity found. Set one first:"
    Write-Host '    git config --global user.name  "Your Name"'
    Write-Host '    git config --global user.email "you@example.com"'
    exit 1
}

if (-not (Test-Path ".git")) { git init | Out-Host }
git checkout -B $branch

if (Test-Path ".git\index.lock") {
    Remove-Item ".git\index.lock" -Force
    Write-Host "Removed stale index.lock"
}

git add -A
Write-Host ""; Write-Host "Files staged:"; git status -s; Write-Host ""

$msg = Read-Host "Commit message"
if (-not $msg) { $msg = "Update WSG content system" }

git commit -m $msg
if (git remote | Select-String -Quiet "^origin$") { git remote set-url origin $repoUrl } else { git remote add origin $repoUrl }
git pull --rebase origin $branch
git push -u origin $branch

Write-Host ""
Write-Host "Done. Confirm at: $($repoUrl -replace '\.git$','')"
