# Combined SCI article (screening intermediate + docking/MD concise)

This folder holds a **new original-research article**. It is not a fourth length variant of either existing package.

Sources (read-only; not edited here):

- `manuscript/intermediate/` — oral-smORF screening cascade, aggregate funnel, twelve-sequence composition, and bounded periodontal–AD interpretation.
- `manuscript/md_alllhrc/concise/` — completed local three-run AutoDock Vina docking, 100-ns GROMACS trajectories, seven PNG figures, and the four-step computational PAS mechanism (Selkoe 2016; Inestrosa 1996; Lushchekina 2017; Atanasova 2020).
- Method/table depth for docking and MD follows `manuscript/md_alllhrc/intermediate/` so that key residues, four-stage equilibration, and last-20-ns metrics remain inspectable.

The screening manuscripts stay figure-free. The three standalone docking/MD reports (`md_alllhrc/full|intermediate|concise`) stay titleless methods–results–discussion reports. This article adds title, abstract, keywords, and introduction, replaces the screening “MD ongoing / docking unresolved” clauses with the local docking and 100-ns results, and does not import docking/MD figures back into the screening package.

Docking numerics follow `source_materials/md_results/local_vina_docking_summary.csv` (FLLHTTR best-run −9.60 kcal/mol, three-run mean −8.77 ± 1.41 kcal/mol). The older screening docking table is not reused.

## Deliverables

- `English.md` / `English.docx`
- `Chinese.md` / `Chinese.docx`

## Rebuild

From the project root:

```bash
for language in English Chinese; do
  python3 scripts/build_docx_stdlib.py --clean-manuscript --allow-images \
    --timestamp 2026-08-23T00:00:00Z \
    --bibliography references/references.bib \
    --input "manuscript/sci_combined/${language}.md" \
    --output "manuscript/sci_combined/${language}.docx" \
    --title "${language}"
done
```
