# Concise manuscript package / 精简稿件包

Version: v3.2.0
Date: 2026-08-14

## Files

- `English.docx` — standalone English SCI-style manuscript.
- `Chinese.docx` — standalone Chinese SCI-style manuscript.
- `English.md` and `Chinese.md` — version-controlled source text.

The English and Chinese Word files are separate. Each contains the same locked aggregate results, two tables, one figure and a 20-reference bibliography. The DOCX files contain no running header, footer, page-number field or workflow-purpose metadata.

## Scientific scope

The manuscripts report an exploratory, aggregate-level computational prioritization. They distinguish PRJNA678453 (22 participants: 11 orally healthy and 11 with periodontitis; 66 oral specimens) from the derived EBI-EMG/MGnify TPA assembly project PRJEB65451. The analysis does not establish candidate expression, disease specificity, *Porphyromonas gingivalis* sequence origin, BBB transport, toxicity, metal chemistry, AChE binding/function or AD causality.

## Rebuild and audit

From the project root:

```bash
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-14T00:00:00Z \
  --input manuscript/concise/English.md \
  --output manuscript/concise/English.docx \
  --title "Aggregate Prioritization of Oral Micropeptides at the Periodontitis–Alzheimer’s Disease Interface"
python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-14T00:00:00Z \
  --input manuscript/concise/Chinese.md \
  --output manuscript/concise/Chinese.docx \
  --title "牙周炎—阿尔茨海默病界面口腔微肽的汇总优选"
python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
```

Provenance and algorithm checks are documented in `../../evidence/prjna678453_prjeb65451_provenance.md` and `../../evidence/prediction_tool_methods.md`. Version and recovery information is maintained in `../../VERSION_HISTORY.md`.
