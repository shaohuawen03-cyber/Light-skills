# Revision v3 — Stage 4: research-suite coordination / 研究套件协调

Date: 2026-08-12

## Data and artefact map

| Component | Authority | Active output |
| --- | --- | --- |
| Screening funnel | Principal DOCX | Manuscript Tables 1–2; Figure 1 |
| Twelve sequence identities | External v0.4 | Manuscript Table 3; Supplement S4 |
| Composition audit | Current scripts | `external_docking_audit.json` |
| Docking summary | External v0.4 | Manuscript Table 4; Figure 2; Supplement S5 |
| Evidence boundaries | Integrated review | Figure 3; Supplement S6 |
| References | Record-level curated union | `verified_references.md`; `references.bib` |

## Coordination rules

- No Tier B datum may silently replace missing Tier A rows.
- The exact external PDF is retained for provenance, but the active SVG/PNG states that raw runs and poses are unavailable.
- English and Chinese manuscripts must have parallel top-level structure, identical numerical results and a shared 53-reference inventory.
- All generated files must be rebuilt from current Markdown/scripts before checksum manifests are refreshed.

## Reproducibility package still required from data owners

Candidate-level screening table; source assembly/sample mapping; predictor rows and versions; CHEL/FRS strict membership; receptor/ligand preparation; exact grid centre and Vina configuration; seeds; raw runs/logs/poses; interaction analysis; and any MD inputs/output.

## Coordination verdict

The expanded package is internally coordinated for accountable-author review. It does not constitute an independent reproduction of the unavailable upstream analyses.