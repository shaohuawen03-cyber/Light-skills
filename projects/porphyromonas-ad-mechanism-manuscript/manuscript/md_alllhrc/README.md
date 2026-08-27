# Standalone molecular docking and molecular dynamics report package

This package contains separate English and Chinese reports for the local AutoDock Vina docking of 12 periodontitis candidate micropeptides against human acetylcholinesterase (rhAChE, PDB 4EY6) and subsequent 100-ns all-atom GROMACS molecular dynamics (MD) simulations (apo AChE vs. ALLLHRC, FLLHTTR, and YLSLLQR). Three length variants are delivered; **every variant embeds the same seven PNG figures** and retains the same principal docking and MD numerics:

- `full/English.docx` and `full/English.md`
- `full/Chinese.docx` and `full/Chinese.md`
- `intermediate/English.docx` and `intermediate/English.md`
- `intermediate/Chinese.docx` and `intermediate/Chinese.md`
- `concise/English.docx` and `concise/English.md`
- `concise/Chinese.docx` and `concise/Chinese.md`

Version roles, figure-to-table concordance, and frozen figure hashes are recorded in `VERSIONS.md`. The standalone reports remain separate from the full, intermediate, and concise oral-smORF screening manuscripts; no docking/MD result is imported into those screening manuscripts.

## Report structure

Each language report contains exactly three top-level sections, in this order:

1. Analysis methods / 分析方法
2. Results / 结果
3. Discussion / 讨论

The reports have no displayed title, abstract, keywords, or Introduction. Methods and Results contain no in-text citation markup. The Discussion section cites high-impact SCI literature. All six files retain three editable three-line tables, in-text citations of docking and MD comparison figures (Figures 1–6 and Figure S1 / 图1–6、图S1), and explicit evidentiary boundaries.

## Scientific scope

- **Local three-run Vina docking**: 12 candidate micropeptides (7–9 aa) were docked into the active gorge and PAS of human AChE (PDB 4EY6). The local summary reports best-run affinity (-8.25 to -9.60 kcal/mol) and mean ± SD across three successful runs (-8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol). Best-pose hydrogen bonds (3–10) and residue-specific PAS engagement are analyzed from the pose composites.
- **Score versus pose ranking**: Best-pose ranking places FLLHTTR first; three-run mean ranking places YLSLLQR first. FLLHTTR has the largest run-to-run SD (1.41 kcal/mol).
- **100-ns Molecular Dynamics**: Evaluates 100-ns production trajectories for unliganded apo AChE and three pathogenic complexes (AChE–ALLLHRC, AChE–FLLHTTR, AChE–YLSLLQR) using Amber99SB-ILDN force field in explicit TIP3P solvent with 0.15 M NaCl.
- **Alzheimer's Disease Mechanistic Pathway**: Explains how pathogenic peptides may cross the compromised blood–brain barrier (BBB), occupy the AChE PAS, physically block substrate entry, and exploit AChE's pathological chaperone activity. These remain computational hypotheses, not measured affinities or proven AD causality.

## DOCX formatting

All six DOCX files:

- begin directly with `Analysis methods` or `分析方法` and display no article title;
- contain no header, footer, page number, or comment;
- embed seven PNG figures (docking scores, poses A–F, poses G–L, 12-pose overview, and three 100-ns MD comparisons) from `manuscript/figures/`;
- use 12-point journal body text, double spacing, one-inch margins, and first-line-indented ordinary body paragraphs;
- contain three editable three-line tables without vertical or full-grid borders;
- compile deterministically using stdlib Python tooling.

## Deterministic rebuild

From the project root:

```bash
for version in full intermediate concise; do
  for language in English Chinese; do
    python3 scripts/build_docx_stdlib.py --clean-manuscript --allow-images \
      --timestamp 2026-08-23T00:00:00Z \
      --input "manuscript/md_alllhrc/${version}/${language}.md" \
      --output "manuscript/md_alllhrc/${version}/${language}.docx" \
      --title "${language}"
  done
done
```

Run `python3 scripts/audit_local_vina_docking.py` and `python3 scripts/audit_md_alllhrc_package.py` to validate the local three-run summary, all six Markdown/DOCX pairs, the frozen hashes of the cited figure files, length order (full > intermediate > concise), and the frozen hashes of all six screening DOCX files.
