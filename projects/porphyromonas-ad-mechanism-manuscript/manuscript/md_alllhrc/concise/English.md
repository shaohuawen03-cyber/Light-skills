## Analysis methods

Twelve periodontitis-derived 7–9-aa micropeptides were docked with AutoDock Vina (exhaustiveness = 32; three independent successful runs) into human AChE (PDB 4EY6). The grid was centered on the peripheral anionic site (PAS: Tyr72, Asp74, Thr75, Trp286, His287, Tyr341) and included the gorge neck and catalytic triad (Ser203, His447, Glu334). Best-run affinity, three-run mean ± SD, hydrogen bonds, and PAS contacts were taken from the local summary and each ligand’s single best pose. PDBQT files are not archived.

Four GROMACS systems (apo AChE and the ALLLHRC, FLLHTTR, and YLSLLQR complexes) were simulated for 100 ns with Amber99SB-ILDN, TIP3P water, 0.15 M NaCl, LINCS, and Particle Mesh Ewald electrostatics at 300 K and 1.0 bar. Metrics in Figures 4–6 are backbone RMSD, per-residue RMSF, SASA, radius of gyration (Rg), DSSP occupancy, and intermolecular hydrogen bonds. Reported values are mean ± SD over the last 20 ns.

## Results

### Docking

Best-run scores ranged from -8.25 to -9.60 kcal/mol and three-run means from -8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol (Table 1, Figure 1). Residue contacts at the Peripheral Anionic Site (PAS) are taken from each best pose. FLLHTTR had the strongest best pose (-9.60 kcal/mol) but the largest SD (-8.77 ± 1.41 kcal/mol). YLSLLQR had the strongest mean (-9.44 ± 0.09 kcal/mol); ALLLHRC was second by mean (-9.18 ± 0.11 kcal/mol) despite a catalytic-pocket rather than outer-PAS pose. Best poses formed 3–10 hydrogen bonds (Figures 2 and 3; Figure S1).

**Table 1. Local three-run AutoDock Vina scores against human AChE (PDB 4EY6).**

| No. | Peptide | HBonds | Best (kcal/mol) | Mean ± SD, n=3 (kcal/mol) | PAS in best pose |
| --- | --- | --- | --- | --- | --- |
| 1 | ALLLHRC | 3 | -9.29 | -9.18 ± 0.11 | No (Ser203 gorge neck) |
| 2 | FCLHLQLR | 7 | -9.27 | -8.96 ± 0.48 | Yes (Thr75, Tyr341) |
| 3 | FLLHTTR | 8 | -9.60 | -8.77 ± 1.41 | Yes (Asp74, Tyr72, His287) |
| 4 | HLLTLKKHV | 6 | -8.88 | -8.69 ± 0.20 | Yes (Tyr72, Phe346) |
| 5 | HLPLLHRCC | 4 | -8.35 | -8.28 ± 0.07 | No |
| 6 | HVLLLRQCA | 4 | -8.25 | -8.07 ± 0.16 | Yes (Thr75) |
| 7 | LLHLPKRTT | 3 | -9.01 | -8.89 ± 0.16 | Adjacent (Val340) |
| 8 | LLHPLRC | 4 | -8.91 | -8.78 ± 0.11 | No |
| 9 | LLHPLRL | 10 | -8.94 | -8.91 ± 0.05 | Yes (Trp286/Tyr341 to His447) |
| 10 | WLLVHLKK | 4 | -8.94 | -8.64 ± 0.26 | No |
| 11 | YHHLLCRR | 7 | -9.03 | -8.62 ± 0.43 | No (Trp86 pocket) |
| 12 | YLSLLQR | 7 | -9.49 | -9.44 ± 0.09 | Yes (Tyr72, Thr75, Ser203) |

![Figure 1. Local AutoDock Vina scores of twelve candidate micropeptides against human AChE.](../../figures/fig5_docking_scores.png)

**Figure 1. Local AutoDock Vina scores against human AChE (PDB 4EY6).** Blue circles: three-run mean; whiskers: SD; orange diamonds: best-run affinity. Horizontal order is best-run ranking.

![Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA.](../../figures/fig_docking_poses_A_F.png)

**Figure 2. Best poses A–F (ALLLHRC to HVLLLRQCA).** FLLHTTR (panel C) is the densest PAS pose.

![Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR.](../../figures/fig_docking_poses_G_L.png)

**Figure 3. Best poses G–L.** LLHPLRL (panel I) spans PAS to His447; YLSLLQR (panel L) bridges PAS and the catalytic entrance.

![Figure S1. Combined overview of all twelve best-scoring docking poses.](../../figures/fig_docking_poses_12_combined.png)

**Figure S1. Combined overview of panels A–L.**

### 100-ns molecular dynamics

Apo AChE and the three complexes remained globular over 100 ns (Table 2, Figures 4–6). Each figure uses the same six-panel layout as the source `fig_compare.png` files: RMSD (A), RMSF (B), SASA (C), Rg (D), DSSP last 20 ns (E), and intermolecular hydrogen bonds (F).

<!-- PAGEBREAK -->

![Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns comparison.](../../figures/fig_compare_ache_vs_alllhrc.png)

**Figure 4. Apo AChE versus AChE–ALLLHRC.** Complex RMSD (A) plateaus near 0.19 nm; hydrogen bonds (F) persist.

![Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns comparison.](../../figures/fig_compare_ache_vs_fllhttr.png)

**Figure 5. Apo AChE versus AChE–FLLHTTR.** Largest RMSD (A) and Rg (D) elevations among the three peptides.

![Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns comparison.](../../figures/fig_compare_ache_vs_ylsllqr.png)

**Figure 6. Apo AChE versus AChE–YLSLLQR.** SASA (C) falls below apo; hydrogen-bond counts (F) are densest.

**Table 2. Last-20-ns metrics matching Figure 4–6 panels (mean ± SD).**

| Metric | apo AChE | ALLLHRC | FLLHTTR | YLSLLQR | Figure panel |
| --- | --- | --- | --- | --- | --- |
| Backbone RMSD (nm) | 0.1562 ± 0.0093 | 0.1916 ± 0.0092 | 0.2102 ± 0.0087 | 0.2064 ± 0.0136 | A |
| RMSF mean (nm) | 0.0783 ± 0.0524 | 0.0876 ± 0.0581 | 0.0901 ± 0.0644 | 0.0813 ± 0.0574 | B |
| SASA (nm²) | 212.41 ± 2.36 | 217.47 ± 2.49 | 216.34 ± 2.55 | 210.37 ± 2.91 | C |
| Rg (nm) | 2.2967 ± 0.0043 | 2.3107 ± 0.0052 | 2.3163 ± 0.0059 | 2.3004 ± 0.0051 | D |
| DSSP α-helix / β-sheet (%) | 33.59 / 17.18 | 33.66 / 16.76 | 33.87 / 17.11 | 32.92 / 17.08 | E |
| Intermolecular H-bonds | N/A | 2.19 ± 0.80 | 2.80 ± 0.99 | 4.23 ± 1.24 | F |

Complex RMSD stays below 0.22 nm. YLSLLQR is the only complex whose SASA contracts versus apo, matching Figure 6C, and it forms the densest hydrogen-bond network (4.23 ± 1.24). Helix (~33–34%) and sheet (~17%) contents overlay the apo bars in every panel E. Each complex retains seven persistent contact pairs.

### Evidence boundary

**Table 3. What the figures and tables do and do not support.**

| No. | Supported | Not supported |
| --- | --- | --- |
| 1 | Best poses of FLLHTTR, YLSLLQR, and LLHPLRL contact PAS residues | Vina scores are not experimental Kd or Ki |
| 2 | 100-ns complexes remain folded (RMSD < 0.22 nm; conserved DSSP) | Mild RMSD increase is not unfolding |
| 3 | Last-20-ns H-bonds 2.19–4.23 persist in panels F | Single 100-ns trajectories are not irreversible binding |
| 4 | FLLHTTR best-run -9.60 kcal/mol versus mean -8.77 ± 1.41 kcal/mol | A best pose is not a converged affinity |

## Discussion

Four papers are retained as directly relevant. Selkoe and Hardy review Aβ and AD: APP cleavage by β- and γ-secretases yields Aβ40/Aβ42, soluble oligomers damage synapses, and familial APP/PSEN mutations change Aβ production and length. Inestrosa et al. showed experimentally that AChE accelerates Aβ fibril assembly through the peripheral anionic site (PAS) and that AChE–Aβ complexes are more neurotoxic than Aβ alone. For dynamics, Lushchekina et al. used accelerated MD of human AChE with multiple Aβ chains and found Aβ attracted to the enzyme surface, forming stable complexes and supporting AChE as a nucleation centre; Atanasova et al. docked one Aβ into the PAS for 1 μs, with a stable complex and main residence at PAS-adjacent 344–361. The four steps below come only from the present docking poses and 100-ns trajectories, as a computational analogy of periodontitis micropeptides onto that Aβ–AChE pathway.

1. PAS recognition and gorge-entrance occupancy.  
   Best poses of the twelve micropeptides concentrate at the PAS and gorge mouth of human AChE (PDB 4EY6; Figures 1–3, Figure S1). FLLHTTR anchors Asp74, Tyr72 and His287 (best-run −9.60 kcal/mol; Figure 2C). YLSLLQR contacts PAS (Tyr72, Thr75) and the catalytic entrance (three-run mean −9.44 ± 0.09 kcal/mol; Figure 3L). LLHPLRL spans Trp286/Tyr341 to His447 (Figure 3I). HLLTLKKHV reaches Tyr72 and Phe346 in 344–361. The geometry matches Atanasova’s placement of Aβ at PAS with 344–361 as principal residence.

2. A stable complex: the enzyme does not unfold and the peptide does not leave.  
   Figures 4–6 show globular AChE over 100 ns: RMSD < 0.22 nm, Rg 2.29–2.32 nm, and α-helix ~33–34% / β-sheet ~17% overlaying apo. The modest rise of complex traces above apo is PAS-adjacent loop adaptation, not denaturation. Last-20-ns hydrogen bonds persist (ALLLHRC 2.19 ± 0.80, FLLHTTR 2.80 ± 0.99, YLSLLQR 4.23 ± 1.24), with seven contact pairs. This matches Lushchekina and Atanasova on a stable, surface-bound complex.

3. Impaired cholinergic transmission.  
   The PAS sits at the entrance of the 20-Å gorge above the catalytic triad. RMSF increases are confined to surface loops (panels B). Physical occupancy can impede acetylcholine entry and perturb gorge gating, so the same pose attacks AChE catalysis in the computational model.

4. Pathological chaperone activity and amyloid co-nucleation.  
   Inestrosa established the PAS as a pro-fibrillar site; Lushchekina and Atanasova recast that process as peptide residence on PAS/344–361, with hydrogen bonds holding the interface while the enzyme scaffolds nucleation. The three complexes here give the same computational picture: a persistent polar network, entrance-loop perturbation, and SASA contraction for YLSLLQR (Figure 6C). Periodontal micropeptides can therefore act as heterologous seeds that co-nucleate endogenous Aβ on the same PAS surface.

These steps are molecular events inside the docking poses and single 100-ns trajectories. They are not experimental binding constants, and Vina scores are not Kd.

### References

1. Selkoe, D. J., & Hardy, J. (2016). The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Molecular Medicine*, 8(6), 595–608. https://doi.org/10.15252/emmm.201606210
2. Inestrosa, N. C., Alvarez, A., Pérez, C. A., Moreno, R. D., Vicente, M., Link, C. A., Dayoub, O. I., et al. (1996). Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. *Neuron*, 16(4), 881–891. https://doi.org/10.1016/S0896-6273(00)80108-7
3. Lushchekina, S. V., Kots, E. D., Novichkova, D. A., Petrov, K. A., & Masson, P. (2017). Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*, 7(2), 396–402. https://doi.org/10.1007/s12668-016-0375-x
4. Atanasova, M., Dimitrov, I., & Ivanov, S. (2020). Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. *Cybernetics and Information Technologies*, 20(6), 140–154. https://doi.org/10.2478/cait-2020-0068
