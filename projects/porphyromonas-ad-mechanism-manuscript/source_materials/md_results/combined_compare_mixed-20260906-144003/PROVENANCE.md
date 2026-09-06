# Mixed 100-ns comparison used in `manuscript/sci_combined/`

Source repository: `shaohuawen03-cyber/asd`  
Branch: `arena/01a03d09-asd`  
Commit: `1712c4a66ac947b8addfb789ea99efec1d7dac1c` (`Sync final mixed comparison results`)  
Directory: `gromacs_md/combined_compare_mixed-20260906-144003/`

## Combination

| System | Origin in the mixed package |
| --- | --- |
| ALLLHRC complex | First production run |
| apo AChE | Last successful rerun |
| FLLHTTR complex | Last successful rerun |
| YLSLLQR complex | Last successful rerun |

Only analysis outputs (figures, CSV) were copied. Trajectories (`*.xtc`, `*.trr`, `*.tpr`, `*.edr`, `*.cpt`, `*.gro`) were not imported.

## Authority for the SCI article

Last-20-ns statistics in Table 4 follow the three `compare_summary.csv` files in this folder (complex-level columns that match `fig_compare.png` panels A–F). AChE-only RMSD quoted in the results paragraph follows `md_*/figures/SCI_Table1_Comprehensive_MD_Metrics.csv`.

Manuscript figures:

- `manuscript/figures/fig_compare_mixed_ache_vs_alllhrc.png`
- `manuscript/figures/fig_compare_mixed_ache_vs_fllhttr.png`
- `manuscript/figures/fig_compare_mixed_ache_vs_ylsllqr.png`

The older `fig_compare_ache_vs_*.png` files remain frozen for `manuscript/md_alllhrc/` and are not used in `sci_combined`.

## What changed versus the superseded comparison

| Metric (last 20 ns) | Old apo / ALLLHRC / FLLHTTR / YLSLLQR | Mixed apo / ALLLHRC / FLLHTTR / YLSLLQR |
| --- | --- | --- |
| Backbone RMSD (nm) | 0.1562 / 0.1916 / 0.2102 / 0.2064 | 0.1897 / 0.1916 / 0.1640 / 0.1625 |
| Peptide self-fit RMSD (nm) | — / 0.2518 / 0.2697 / 0.1979 | — / 0.2518 / 0.1752 / 0.0911 |
| SASA (nm²) | 212.41 / 217.47 / 216.34 / 210.37 | 212.25 / 217.47 / 213.88 / 209.71 |
| Intermolecular H-bonds | — / 2.19 / 2.80 / 4.23 | — / 2.19 / **7.03** / 2.93 |

FLLHTTR and YLSLLQR complexes now lie *below* apo in late RMSD. FLLHTTR, not YLSLLQR, holds the densest hydrogen-bond network. YLSLLQR remains the only SASA contraction and has the most rigid peptide.
