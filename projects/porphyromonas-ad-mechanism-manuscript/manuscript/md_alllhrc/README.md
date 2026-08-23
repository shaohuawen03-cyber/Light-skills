# Standalone ALLLHRC–AChE molecular-dynamics manuscript package

This package contains four separate, titleless and figure-free manuscripts derived from the user-designated 100-ns `md_alllhrc` result:

- `full/English.docx` and `full/English.md`
- `full/Chinese.docx` and `full/Chinese.md`
- `concise/English.docx` and `concise/English.md`
- `concise/Chinese.docx` and `concise/Chinese.md`

The complete version contains two three-line tables and a detailed evidence-boundary discussion. The concise version contains one three-line table and retains all principal RMSD, RMSF, RDF, SASA, secondary-structure and hydrogen-bond observations. Chinese and English files are separate and synchronized by content; the concise package is shorter rather than less cautious.

## Scientific scope

The manuscripts interpret a single 100-ns computation-only output. Atanasova et al. (2020), doi:10.2478/cait-2020-0068, supplies the analytical framework but not ALLLHRC data. The manuscripts do not import that article’s Aβ contact residues, AChE residence region, PAS movements or 1-μs stability conclusion.

The user assigns the output to ALLLHRC–AChE and the directory name agrees, but the source chart retains an inherited AChE–Aβ heading. This discrepancy is disclosed. Identity remains provisional until topology and trajectory identifiers are matched. The preserved RMSD diagnostic was calculated from a digitized trace rather than a raw trajectory. Non-RMSD ranges were read conservatively from the supplied axes.

The current evidence supports limited AChE backbone deviation, two internal ALLLHRC conformational transitions, preferred center-of-mass separation ranges, narrow SASA bands and intermittent hydrogen bonding. It does not establish binding affinity, PAS residence, catalytic inhibition, altered Aβ aggregation, BBB transport, toxicity or AD causality.

## Formatting

All four DOCX files:

- begin with a one-paragraph unstructured abstract and do not display the article title;
- contain no header, footer, page number, figure or embedded media;
- use 12-point journal body text, double spacing, one-inch margins and first-line-indented ordinary body paragraphs;
- contain no Statistical analysis subsection and no standalone Conclusion section;
- place References directly after Discussion;
- use editable three-line tables without vertical or full-grid borders;
- contain static numbered citation text generated from the BibTeX-linked Markdown source and are not represented as Zotero-live files.

## Deterministic rebuild

From the project root:

```bash
for variant in full concise; do
  for language in English Chinese; do
    python3 scripts/build_docx_stdlib.py --clean-manuscript \
      --timestamp 2026-08-23T00:00:00Z \
      --bibliography references/references.bib \
      --input "manuscript/md_alllhrc/${variant}/${language}.md" \
      --output "manuscript/md_alllhrc/${variant}/${language}.docx" \
      --title "${language}"
  done
done
```

Run `python3 scripts/audit_md_alllhrc_package.py` to validate the four Markdown/DOCX pairs and reproduce the DOCX files in an isolated temporary directory.
