# Local AutoDock Vina docking package

This directory archives the user-uploaded local docking summary and pose composites for twelve periodontitis candidate micropeptides against human recombinant acetylcholinesterase (rhAChE, PDB 4EY6).

## Archived files

| File | Role |
| --- | --- |
| `Summary_Vina_Docking.csv` | Local three-run Vina summary (best affinity, mean, SD, `N_Success = 3`). The `Best_PDBQT` column records original compute-node paths and is not copied into manuscripts. |
| `sci_composite_figures/Figure_4_Part1_A-F_300dpi.png` | Best-pose composites for ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, HVLLLRQCA (panels A–F). |
| `sci_composite_figures/Figure_4_Part2_G-L_300dpi.png` | Best-pose composites for LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, YLSLLQR (panels G–L). |
| `sci_composite_figures/Figure_S1_12_Combined_300dpi.png` | Single-page overview of all twelve best poses. |

A path-sanitized copy of the numeric summary is stored at `source_materials/md_results/local_vina_docking_summary.csv`. Publication copies of the pose figures and the regenerated score chart live under `manuscript/figures/`.

## Reporting rule

The standalone docking/MD reports use this local three-run summary as the docking score authority:

- **Best affinity** = the strongest successful run (`Best_Affinity_kcal_mol`).
- **Mean ± SD** = arithmetic mean and reported standard deviation across three successful runs.
- Residue-level hydrogen-bond and PAS engagement statements describe the **best-scoring pose** shown in the composite figures.

Individual PDBQT coordinate files, grid configuration files, and Vina stdout logs are not present in this package. Do not describe the summary table as a fully deposited raw docking archive. Vina scores remain empirical ranking metrics, not experimental binding free energies.
