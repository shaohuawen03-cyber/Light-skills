# Synchronization and reproducible rebuild

## Remote synchronization

The Arena session branch is fixed to `arena/019ff377-light-skills`.

PowerShell (run each command as one line; do not use Bash `\` continuation):

```powershell
Set-Location 'E:\0writing\Light-skills'
Test-Path '.git'
git fetch origin 'refs/heads/arena/019ff377-light-skills:refs/remotes/origin/arena/019ff377-light-skills' --tags
git switch arena/019ff377-light-skills
git pull --ff-only origin arena/019ff377-light-skills
```

`Test-Path '.git'` must return `True`. If it returns `False`, locate or clone the repository before running Git commands.

If the repository is not yet cloned:

```powershell
Set-Location 'E:\0writing'
git clone 'https://github.com/shaohuawen03-cyber/Light-skills.git' 'Light-skills'
Set-Location 'E:\0writing\Light-skills'
git fetch origin 'refs/heads/arena/019ff377-light-skills:refs/remotes/origin/arena/019ff377-light-skills' --tags
git switch --track -c arena/019ff377-light-skills origin/arena/019ff377-light-skills
```

## Project path

```text
projects/porphyromonas-ad-mechanism-manuscript/
```

## Deterministic v3.14.0 rebuild

Run from the project root:

```bash
python3 scripts/verify_source_checksums.py
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py
python3 scripts/audit_local_vina_docking.py

for language in English Chinese; do
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input "manuscript/full/${language}.md" --output "manuscript/full/${language}.docx" --title "${language}"
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --bibliography references/references.bib --input "manuscript/intermediate/${language}.md" --output "manuscript/intermediate/${language}.docx" --title "${language}"
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --bibliography references/references.bib --input "manuscript/concise/${language}.md" --output "manuscript/concise/${language}.docx" --title "${language}"
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --input "manuscript/md_alllhrc/full/${language}.md" --output "manuscript/md_alllhrc/full/${language}.docx" --title "${language}"
done

python3 scripts/audit_submission_manuscripts.py
python3 scripts/audit_full_manuscripts.py
python3 scripts/audit_intermediate_package.py
python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
python3 scripts/audit_full_docx_reproducibility.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_md_alllhrc_package.py
python3 scripts/generate_artifact_checksums.py
python3 scripts/build_repository_inventory.py
```

The MD rebuild intentionally omits `--bibliography`: those two reports contain only Analysis methods, Results, and Discussion; Methods and Results have no citation markup, while the Discussion section cites high-impact SCI literature directly. The `manuscript/md_alllhrc/concise/` directory must remain absent.

## Zotero-live acceptance gate

The standard screening rebuild produces automatically numbered citation text from Pandoc citation keys and `references/references.bib`; it does not claim Zotero-live fields. On a workstation with Pandoc, Zotero, Better BibTeX, and the Word add-in:

```bash
python3 scripts/test_better_bibtex.py scheltens2021alzheimer
python3 scripts/build_zotero_live_docx.py --input manuscript/full/English.md --output manuscript/full/English.zotero-candidate.docx --reference-doc manuscript/full/English.docx --report quality_reports/zotero_live_full_english.json
```

Repeat for the other screening sources, then perform Zotero Document Preferences, Refresh, and Add/Edit Bibliography in desktop Word. See `references/ZOTERO_WORD_ACCEPTANCE.md`. Never describe static numbered text as Zotero-live. The standalone docking/MD reports do not require Zotero conversion.

## Version tag

After committing a clean tree on the fixed branch:

```bash
python3 scripts/manage_version_tag.py create --version 3.13.0 --message "v3.13.0: expand standalone package to full docking and multi-system MD reports" --push
python3 scripts/manage_version_tag.py verify --version 3.13.0
```

Existing release tags are immutable and must not be moved or overwritten.

## Scientific boundary

These commands reproduce arithmetic checks, sequence-composition checks, the local three-run Vina summary audit, reference mapping, the six screening manuscripts, and the two expanded standalone docking and MD reports. They also reproduce the DOCX packages from versioned Markdown and the preserved multi-system MD metrics. They do not claim in vitro binding validation, cellular neurotoxicity assays, or clinical causality without dedicated prospective wet-lab experiments. No standalone docking/MD result is integrated into a screening manuscript.
