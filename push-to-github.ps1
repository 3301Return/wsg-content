# One-shot push of the curated WSG repo to a NEW GitHub repository.
#
# Before running:
#   1. Create an EMPTY repository on github.com (no README, no .gitignore, no license).
#      Suggested name: wsg-content   Visibility: your call.
#   2. If you used a different owner/name, edit $repoUrl below.
#   3. Run from PowerShell:
#      powershell -ExecutionPolicy Bypass -File "C:\Users\15162\Documents\Claude\Projects\WSG Article Example\wsg-repo\push-to-github.ps1"

$ErrorActionPreference = "Stop"
$repo    = "C:\Users\15162\Documents\Claude\Projects\WSG Article Example\wsg-repo"
$repoUrl = "https://github.com/3301Return/wsg-content.git"
$branch  = "main"

Set-Location $repo

# Identity guard (uses existing global git config when present).
if (-not (git config user.email)) {
    git config user.email "niksonalex17@gmail.com"
    git config user.name  "Nikson"
    Write-Host "Set local git identity (no global config found)."
}

if (-not (Test-Path ".git")) { git init | Out-Host }
git checkout -B $branch

if (Test-Path ".git\index.lock") {
    Remove-Item ".git\index.lock" -Force
    Write-Host "Removed stale index.lock"
}

git add -A
Write-Host ""; Write-Host "Files staged:"; git status -s; Write-Host ""

$msg = @"
Initial import: WSG content system (curated, August 12, 2026)

Structure:
- One canonical file per article; superseded draft versions and duplicate
  docx/pdf variants left in the local working folder, not imported
- published/ split by provenance: ai-written/ (60 finals, incl. the Aug 5
  and Aug 11-12 2026 batches) and human-written/ (seeded empty)
- drafts/ = latest AI draft per article (36 files)
- All deep-dive PDFs and keyword xlsx committed (redistribution policy
  removed from REPO_README as incorrect)

Tooling:
- scripts/markdown_to_docx_v2.py: Aug 2026 formatting spec
  (Title / Heading 2 / Normal styles, empty-line spacing)
- scripts/check_article.py: headline-year fix
- scripts/verified-brands.txt: +200 entities verified Aug 11, 2026
"@

git commit -m $msg
if (git remote | Select-String -Quiet "^origin$") { git remote set-url origin $repoUrl } else { git remote add origin $repoUrl }
git push -u origin $branch

Write-Host ""
Write-Host "Done. Confirm at: $($repoUrl -replace '\.git$','')"
