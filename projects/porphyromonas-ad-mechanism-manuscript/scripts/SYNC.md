# Synchronization and reproducible rebuild

## Remote synchronization

The Arena session branch is fixed to `arena/019ff377-light-skills`.

```bash
cd E:\0writing\Light-skills
git fetch origin arena/019ff377-light-skills
git switch arena/019ff377-light-skills
git pull --ff-only origin arena/019ff377-light-skills
```

If the repository is not yet cloned:

```bash
cd E:\0writing
git clone git@github.com:shaohuawen03-cyber/Light-skills.git
cd Light-skills
git fetch origin arena/019ff377-light-skills
git switch --track -c arena/019ff377-light-skills origin/arena/019ff377-light-skills
```

## Project path

```text
projects/porphyromonas-ad-mechanism-manuscript/
```

## Deterministic rebuild

Run from the project root:

```bash
python3 scripts/verify_source_checksums.py
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py
python3 scripts/generate_funnel_figure.py
python3 scripts/generate_docking_score_figure.py
python3 scripts/generate_evidence_ladder.py
python3 scripts/build_bilingual_markdown.py
python3 scripts/audit_manuscript_consistency.py > quality_reports/manuscript_consistency.json
python3 scripts/audit_language_structure.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_manuscript_word_counts.py
python3 scripts/audit_text_quality.py
python3 scripts/build_docx_stdlib.py --input manuscript/manuscript_bilingual.md --output manuscript/manuscript_bilingual.docx --title "Provenance-Aware Multi-Model Prioritization / 基于来源边界的口腔微肽多模型优选"
python3 scripts/build_docx_stdlib.py --input manuscript/supplementary_tables_bilingual.md --output manuscript/supplementary_tables_bilingual.docx --title "Bilingual supplementary tables / 中英文补充表"
python3 scripts/build_docx_stdlib.py --input manuscript/interim_teacher/interim_teacher_en.md --output manuscript/interim_teacher/interim_teacher_en.docx --title "Interim Oral Micropeptide Prioritization Study"
python3 scripts/build_docx_stdlib.py --input manuscript/interim_teacher/interim_teacher_zh.md --output manuscript/interim_teacher/interim_teacher_zh.docx --title "口腔微肽优选阶段性研究简稿"
python3 scripts/audit_interim_teacher_package.py
python3 scripts/audit_docx_packages.py
python3 scripts/generate_artifact_checksums.py
python3 scripts/build_repository_inventory.py
```

## Version tags and recovery

The authoritative version ledger is `VERSION_HISTORY.md`. To create the current protected annotated tag after committing a clean tree:

```bash
python3 scripts/manage_version_tag.py create --version 3.1.0 --message "v3.1.0: separate short English and Chinese interim drafts for supervisor review" --push
python3 scripts/manage_version_tag.py verify --version 3.1.0
```

Prefer `git worktree add <separate-path> <tag>` for recovery inspection; do not use destructive reset for routine version recovery.

## Important boundary

These commands reproduce arithmetic checks, sequence-composition checks, figures, manuscripts and DOCX packages. They do not reproduce the original smORF/predictor workflow or the externally reported docking because the necessary row-level inputs and raw docking artefacts are absent.
