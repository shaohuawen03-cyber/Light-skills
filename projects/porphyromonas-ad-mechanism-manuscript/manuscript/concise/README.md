# Concise manuscript package / 精简稿件包

Version: v3.8.0
Date: 2026-08-17

## Files

- `English.docx` — titleless, standalone concise English SCI manuscript.
- `Chinese.docx` — titleless, standalone concise Chinese SCI manuscript.
- `English.md` and `Chinese.md` — synchronized sources using Pandoc/BibTeX citation keys.

Each DOCX begins with a single-paragraph unstructured abstract whose former
Conclusions component has been removed. Each contains two three-line tables, no
figures, no header/footer/page-number fields, and no administrative sections. The
expanded English body is approximately 3,000 words, about 63% longer than v3.6.0.
The manuscripts use unnumbered journal-style headings, 12-point Times New Roman,
double spacing, one-inch margins, and a 480-twip first-line indent for main-text
paragraphs. The standalone Statistical analysis and Conclusion sections are absent;
Discussion is followed directly by the same 22-item References list in English and
Chinese.

## Scientific scope

The package reports an exploratory, aggregate-level computational prioritization.
It omits specific participant, specimen, assembly-analysis, and MAG totals. It
distinguishes PRJNA678453 from the derived EBI-EMG/MGnify TPA assembly project
PRJEB65451 without treating the latter as a separate cohort. The analysis does
not establish candidate expression, disease specificity, *Porphyromonas
gingivalis* sequence origin, BBB transport, toxicity, metal chemistry, AChE
binding/function or AD causality. The prespecified molecular-dynamics analysis is
ongoing, and trajectory-derived measurements will be incorporated after completion
and quality control.

## Rebuild and audit

From the project root:

```bash
python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/concise/English.md \
  --output manuscript/concise/English.docx --title English
python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/concise/Chinese.md \
  --output manuscript/concise/Chinese.docx --title Chinese
python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
python3 scripts/audit_full_docx_reproducibility.py
```

The committed DOCX files contain automatically numbered citation text generated
from the BibTeX-linked source keys, but they are not represented as Zotero-live.
See `../../references/ZOTERO_WORD_ACCEPTANCE.md` for the Better BibTeX/Pandoc and
desktop Word/Zotero acceptance gate.
