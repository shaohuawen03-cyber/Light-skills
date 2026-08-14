# Revision v3 — Stage 6: scientific visualization / 科学可视化

Date: 2026-08-12

## Figure set

1. **Prioritization funnel:** revised footer distinguishes absent principal-source identities from the twelve externally reported strings and states that row-level lineage remains unresolved.
2. **Docking-score summary:** new editable SVG and raster PNG plot the twelve external means±SD. Title/subtitle explicitly state “source-reported” and “raw runs and poses unavailable.” A footer warns that scores are not binding free energies.
3. **Evidence ladder:** aggregate screening is reached; identities and docking summaries are marked partial external evidence; expression, BBB, toxicity, metal chemistry and disease relevance remain untested.

## Provenance asset

The exact external Figure 5 PDF is archived in the active figure folder for provenance. It is not treated as independently generated evidence.

## Technical method

Figures are generated with Python standard-library SVG and ImageMagick primitive drawing. The environment lacks NumPy/Matplotlib and its ImageMagick cannot rasterize SVG, so the active scripts use a direct-drawing PNG fallback.

## Visual claim control

No pose, molecular contact diagram, MD trajectory, significance star, confidence band, or causal arrow was created because no supporting artefact exists.