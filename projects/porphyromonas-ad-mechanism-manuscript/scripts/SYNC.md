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

## Deterministic v3.11.0 rebuild

Run from the project root:

```bash
python3 scripts/verify_source_checksums.py
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py

python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input manuscript/full/English.md --output manuscript/full/English.docx --title English
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input manuscript/full/Chinese.md --output manuscript/full/Chinese.docx --title Chinese
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --bibliography references/references.bib --input manuscript/intermediate/English.md --output manuscript/intermediate/English.docx --title English
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --bibliography references/references.bib --input manuscript/intermediate/Chinese.md --output manuscript/intermediate/Chinese.docx --title Chinese
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input manuscript/concise/English.md --output manuscript/concise/English.docx --title English
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input manuscript/concise/Chinese.md --output manuscript/concise/Chinese.docx --title Chinese

for variant in full concise; do
  for language in English Chinese; do
    python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --bibliography references/references.bib --input "manuscript/md_alllhrc/${variant}/${language}.md" --output "manuscript/md_alllhrc/${variant}/${language}.docx" --title "${language}"
  done
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

## Zotero-live acceptance gate

The standard rebuild produces automatically numbered citation text from Pandoc
citation keys and `references/references.bib`; it does not claim Zotero-live
fields. On a workstation with Pandoc, Zotero, Better BibTeX, and the Word add-in:

```bash
python3 scripts/test_better_bibtex.py scheltens2021alzheimer
python3 scripts/build_zotero_live_docx.py --input manuscript/full/English.md --output manuscript/full/English.zotero-candidate.docx --reference-doc manuscript/full/English.docx --report quality_reports/zotero_live_full_english.json
```

Repeat for the other three sources, then perform Zotero Document Preferences,
Refresh, and Add/Edit Bibliography in desktop Word. See
`references/ZOTERO_WORD_ACCEPTANCE.md`. Never describe static numbered text as
Zotero-live.

## Version tag

After committing a clean tree on the fixed branch:

```bash
python3 scripts/manage_version_tag.py create --version 3.11.0 --message "v3.11.0: add intermediate English and Chinese submission manuscripts" --push
python3 scripts/manage_version_tag.py verify --version 3.11.0
```

Existing release tags are immutable and must not be moved or overwritten.

## Scientific boundary

These commands reproduce arithmetic checks, sequence-composition checks,
reference mapping, manuscripts, and DOCX packages. They also reproduce the
standalone ALLLHRC manuscript text and deterministic DOCX packaging from the
preserved plot-derived RMSD support. They do not reproduce the original
smORF/predictor analysis, the available docking-score table, or the underlying
MD trajectory: prepared structures, complete run outputs, raw trajectories and
independently seeded replicas remain unavailable.
