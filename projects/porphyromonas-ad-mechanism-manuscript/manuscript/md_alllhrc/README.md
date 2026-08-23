# Standalone ALLLHRC–AChE molecular-dynamics report package

This package contains only the separate full English and Chinese reports derived from the user-designated 100-ns `md_alllhrc` result:

- `full/English.docx` and `full/English.md`
- `full/Chinese.docx` and `full/Chinese.md`

No concise or intermediate MD version is delivered. The former concise directory was intentionally deleted. The standalone reports remain separate from the full, intermediate and concise oral-smORF screening manuscripts; no MD result is imported into those manuscripts.

## Report structure

Each language report contains exactly three top-level sections, in this order:

1. Analysis methods / 分析方法
2. Results / 结果
3. Discussion / 讨论

The reports have no displayed title, abstract, keywords, Introduction, citation markers, reference list, Statistical analysis section or standalone Conclusion. Both versions retain detailed simulation and analysis methods, the full descriptive numerical results, two editable three-line tables, interpretation, the comparison framework and explicit limitations.

## Scientific scope

The reports interpret a single 100-ns computation-only output. Atanasova et al. (2020), doi:10.2478/cait-2020-0068, informed the analytical framework but supplies no ALLLHRC data; the article is discussed descriptively rather than cited through a manuscript citation apparatus. No Aβ-specific sequence, contact residue, AChE residence region, PAS movement or 1-μs stability conclusion is transferred to ALLLHRC.

The user assigns the output to ALLLHRC–AChE and the directory name agrees, but the source chart retains an inherited AChE–Aβ heading. This discrepancy is disclosed. Identity remains provisional until topology and trajectory identifiers are matched. The preserved RMSD diagnostic was calculated from a digitized trace rather than a raw trajectory. Non-RMSD ranges were read conservatively from the supplied axes.

The current evidence supports limited AChE backbone deviation, two internal ALLLHRC conformational transitions, preferred center-of-mass separation ranges, narrow SASA bands and intermittent hydrogen bonding. It does not establish binding affinity, PAS residence, catalytic inhibition, altered Aβ aggregation, BBB transport, toxicity or AD causality.

## DOCX formatting

Both DOCX files:

- begin directly with `Analysis methods` or `分析方法` and display no article title;
- contain no header, footer, page number, comment, figure or embedded media;
- use 12-point journal body text, double spacing, one-inch margins and first-line-indented ordinary body paragraphs;
- contain two editable three-line tables without vertical or full-grid borders;
- contain no citation fields, numbered citation text or bibliography and are not represented as Zotero-live files.

## Deterministic rebuild

From the project root:

```bash
for language in English Chinese; do
  python3 scripts/build_docx_stdlib.py --clean-manuscript \
    --timestamp 2026-08-23T00:00:00Z \
    --input "manuscript/md_alllhrc/full/${language}.md" \
    --output "manuscript/md_alllhrc/full/${language}.docx" \
    --title "${language}"
done
```

Run `python3 scripts/audit_md_alllhrc_package.py` to validate both Markdown/DOCX pairs, verify that the concise directory is absent, confirm that all six screening DOCX files remain byte-identical to their frozen hashes and reproduce the two MD DOCX files in an isolated temporary directory.
