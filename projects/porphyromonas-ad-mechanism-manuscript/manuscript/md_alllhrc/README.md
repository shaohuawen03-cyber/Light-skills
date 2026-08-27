# Standalone molecular docking and molecular dynamics report package

This package contains separate full English and Chinese reports for the molecular docking of 12 periodontitis candidate micropeptides against human acetylcholinesterase (rhAChE, PDB 4EY6) and subsequent 100-ns all-atom GROMACS molecular dynamics (MD) simulations (apo AChE vs. ALLLHRC, FLLHTTR, and YLSLLQR):

- `full/English.docx` and `full/English.md`
- `full/Chinese.docx` and `full/Chinese.md`

No concise or intermediate MD version is delivered. The standalone reports remain separate from the full, intermediate, and concise oral-smORF screening manuscripts; no docking/MD result is imported into those screening manuscripts.

## Report structure

Each language report contains exactly three top-level sections, in this order:

1. Analysis methods / 分析方法
2. Results / 结果
3. Discussion / 讨论

The reports have no displayed title, abstract, keywords, or Introduction. Methods and Results contain no in-text citation markup. The Discussion section cites high-impact SCI literature to elucidate the molecular mechanisms linking periodontal micropeptides, peripheral anionic site (PAS) binding, active gorge occlusion, and AChE-mediated pathological chaperone amyloid co-nucleation in Alzheimer's disease (AD). Both versions retain three editable three-line tables, in-text citations of docking and MD comparison figures (Figures 1–4 / 图1–4), and explicit evidentiary boundaries.

## Scientific scope

- **Molecular Docking**: 12 candidate micropeptides (7–9 aa) prioritized from the periodontitis cohort were docked into the active gorge and PAS of human AChE (PDB 4EY6). Poses, Vina scores (-8.25 to -9.60 kcal/mol), intermolecular hydrogen bonds (3–10 bonds), and residue-specific PAS engagement are systematically analyzed.
- **PAS Engagement**: Directly identifies micropeptides that dock into the canonical PAS (FLLHTTR, YLSLLQR, FCLHLQLR, HVLLLRQCA, HLLTLKKHV, LLHPLRL) versus those localized to the catalytic pocket or gorge entrance.
- **100-ns Molecular Dynamics**: Evaluates 100-ns production trajectories for unliganded apo AChE and three pathogenic complexes (AChE–ALLLHRC, AChE–FLLHTTR, AChE–YLSLLQR) using Amber99SB-ILDN force field in explicit TIP3P solvent with 0.15 M NaCl. Quantifies backbone RMSD, per-residue RMSF, radius of gyration (Rg), SASA, intermolecular hydrogen bonds, contact pairs, DSSP secondary structure fractions, and radial distribution functions (RDF).
- **Alzheimer's Disease Mechanistic Pathway**: Explains how pathogenic peptides cross the compromised blood–brain barrier (BBB), dock to the AChE PAS, physically block substrate entry (driving cholinergic deficits), and exploit AChE's pathological chaperone activity to nucleate Aβ aggregation and amplify neurotoxicity.

## DOCX formatting

Both DOCX files:

- begin directly with `Analysis methods` or `分析方法` and display no article title;
- contain no header, footer, page number, comment, figure, or embedded media (figures are cited and delivered separately in `manuscript/figures/`);
- use 12-point journal body text, double spacing, one-inch margins, and first-line-indented ordinary body paragraphs;
- contain three editable three-line tables without vertical or full-grid borders;
- compile deterministically using stdlib Python tooling.

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

Run `python3 scripts/audit_md_alllhrc_package.py` to validate both Markdown/DOCX pairs, verify that the concise directory is absent, confirm that all six screening DOCX files remain byte-identical to their frozen hashes, and reproduce the two DOCX deliverables.
