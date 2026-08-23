# ALLLHRC–AChE 100-ns result interpretation record

Review date: 2026-08-23

## Scope

The user designated the attached six-panel display as the result from `F:\0wsh\asd\gromacs_md\md_alllhrc` for the ALLLHRC–AChE complex and requested independent full/concise English/Chinese manuscripts. The user selected text-only DOCX output; the figure must not be embedded.

The analysis follows Atanasova, Dimitrov and Ivanov (2020), doi:10.2478/cait-2020-0068, as an organizational precedent. Its Aβ-specific measurements are not a data source for ALLLHRC.

## Directly reportable observations

- Production interval displayed: 100 ns.
- AChE backbone RMSD remains within a comparatively narrow range; the digitized diagnostic reports 0.1803 ± 0.0220 nm and a 0.2320-nm maximum.
- Peptide self-fitted backbone RMSD has two transitions and three reported plateaus: 0.0582 ± 0.0091 nm at 0.0–22.6 ns; 0.1432 ± 0.0161 nm at 23.4–55.6 ns; and 0.2694 ± 0.0148 nm at 57.0–100.0 ns.
- Most AChE RMSF values are visually below about 0.10 nm, with localized peaks and a terminal excursion approaching 0.60 nm.
- Most peptide RMSF values are visually about 0.05–0.10 nm, with one endpoint around 0.21 nm.
- Peptide–AChE center-of-mass RDF has a principal peak near 1.2 nm and a secondary peak near 1.4 nm.
- Complex and peptide SASA remain approximately 210–223 and 10–12 nm².
- Plotted secondary-structure fractions are stable: helix about 0.33–0.37, coil 0.19–0.23, sheet 0.14–0.17, bend 0.12–0.15, and turn 0.09–0.13. The structural selection is unavailable, so these cannot be assigned to ALLLHRC.
- Intermolecular hydrogen bonds span 0–11 and are visually less numerous late in the trajectory.

## Interpretation boundaries

The supported description is limited receptor-backbone deviation accompanied by two internal ALLLHRC rearrangements and intermittent peptide–AChE polar contacts. The data are compatible with dynamic association and interface reorganization but do not prove a single stable pose, PAS residence, binding affinity, catalytic inhibition, altered Aβ aggregation, BBB transport, toxicity, or AD causality.

The RMSD numeric series preserved here was digitized from a plot. It is not raw trajectory output. No inferential statistics, convergence claim, or between-system ranking may be based on it.

## Required unresolved data

- corrected plot title and a topology/trajectory manifest confirming ALLLHRC identity;
- exact starting coordinates, chain labels, termini and protonation;
- GROMACS version, TPR, XTC/TRR, EDR, LOG, CPT, topology and hashes;
- index groups, centering/PBC/fitting commands and analysis selections;
- independently seeded trajectories and an apo-AChE comparator;
- AChE-fitted peptide positional RMSD, minimum distances, contacts, structures and trajectory inspection;
- residue-resolved hydrogen bonds, occupancy/lifetimes and water bridges;
- biochemical AChE binding/activity and appropriate peptide controls.
