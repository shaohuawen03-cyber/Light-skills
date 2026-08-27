# Intermediate screening-manuscript package

This directory contains the submission-oriented version positioned between the existing full and concise oral-smORF screening manuscripts:

- `English.docx` and `English.md`
- `Chinese.docx` and `Chinese.md`

The package is independent of `manuscript/md_alllhrc/`. Standalone docking/MD intermediate reports live under `manuscript/md_alllhrc/intermediate/` and are not imported here.

## Content position

The English main-text counts are ordered as follows:

- full: approximately 6,900 words;
- intermediate: approximately 4,600 words;
- concise: approximately 3,700 words.

The Chinese body-character counts follow the same order. The intermediate version contains four three-line tables:

1. aggregate candidate libraries and BBB-high outputs;
2. all 22 long/short UniDL4BioPep functional categories in a compact paired table;
3. aggregate serial-prioritization counts and denominators;
4. the twelve-sequence composition and AChE docking-score summary.

It retains the complete long/short multidimensional results, exact aggregate funnel counts, twelve sequence strings, Vina ordering, prospective comparative-MD method, and the final limitation explaining why all 72 BBB-high long candidates were absent from the all-≤30-aa NTxPred2-positive set and the final 12 consisted only of short peptides.

## Formatting

Both DOCX files are titleless, figure-free, and begin with a one-paragraph abstract. They use unnumbered article headings, 12-point journal body text, double spacing, one-inch margins, first-line-indented ordinary body paragraphs, editable three-line tables, and no header, footer, page number, comments, Statistical analysis subsection, standalone Conclusion, or declarations. Discussion proceeds directly to References. The standard DOCX files contain static numbered citations generated from BibTeX-linked Markdown and are not represented as Zotero-live fields.

## Deterministic rebuild

From the project root:

```bash
for language in English Chinese; do
  python3 scripts/build_docx_stdlib.py --clean-manuscript \
    --timestamp 2026-08-23T00:00:00Z \
    --bibliography references/references.bib \
    --input "manuscript/intermediate/${language}.md" \
    --output "manuscript/intermediate/${language}.docx" \
    --title "${language}"
done
```

Run `python3 scripts/audit_intermediate_package.py` to validate the package, the length ordering, and the unchanged hashes of the pre-existing full, concise, and standalone-MD DOCX files.
