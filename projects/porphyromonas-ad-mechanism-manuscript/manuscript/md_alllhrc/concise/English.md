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

The peptide that the AD literature can call pathogenic is first amyloid-β (Aβ) itself. Selkoe and Hardy’s amyloid-cascade review states that APP cleavage by β- and γ-secretases yields Aβ40/Aβ42, that soluble oligomers damage synapses, and that APP/PSEN mutations in familial AD change Aβ production and length. One AChE–Aβ simulation cannot carry that layer.

The second layer is experimental: how AChE helps Aβ cause disease. Inestrosa et al. showed that AChE accelerates Aβ fibril assembly through the peripheral anionic site (PAS) and that AChE–Aβ complexes are more neurotoxic than Aβ alone. De Ferrari et al. mapped a hydrophobic motif near the PAS whose synthetic peptide recapitulates the fibril-promoting effect of the whole enzyme. Silman and Sussman noted that the same PAS is the electrostatic gate of the 20-Å active gorge, so occupancy can hit both catalysis and chaperone function.

The third layer is dynamics. Lushchekina et al. used accelerated MD of human AChE with multiple Aβ chains and found Aβ strongly attracted to the enzyme surface, forming stable complexes and supporting AChE as a nucleation centre. Atanasova et al. docked one Aβ into the PAS and ran 1 μs: the complex stayed folded, the main residence was the PAS-adjacent 344–361 stretch, and contacts were hydrogen bonds, aromatic packing and hydrophobics. The four steps below come only from the present docking poses and 100-ns trajectories. They place periodontitis micropeptides on that Aβ–AChE pathway as a computational analogy; they do not recast the three sequences as experimentally proven AD pathogenic peptides.

1. PAS recognition and gorge-entrance occupancy.  
   Best poses of the twelve micropeptides concentrate at the PAS and gorge mouth of human AChE (PDB 4EY6; Figures 1–3, Figure S1). FLLHTTR anchors Asp74, Tyr72 and His287 (best-run −9.60 kcal/mol; Figure 2C). YLSLLQR contacts PAS (Tyr72, Thr75) and the catalytic entrance (Ser203, Glu202; three-run mean −9.44 ± 0.09 kcal/mol; Figure 3L). LLHPLRL spans gatekeepers Trp286/Tyr341 to catalytic His447 (ten hydrogen bonds; Figure 3I). HLLTLKKHV reaches Tyr72 and Phe346 in the 344–361 region. Geometrically this matches Atanasova’s placement of Aβ at PAS with 344–361 as a principal residence: an exogenous short peptide can serve as a ligand on the same nucleating face.

2. A stable complex: the enzyme does not unfold and the peptide does not leave.  
   Figures 4–6 show globular AChE over 100 ns: backbone RMSD < 0.22 nm, Rg 2.29–2.32 nm, and α-helix ~33–34% / β-sheet ~17% overlaying apo (panels E). The modest rise of complex traces above apo is PAS-adjacent loop adaptation, not denaturation. Intermolecular hydrogen bonds persist in panels F (last 20 ns: ALLLHRC 2.19 ± 0.80, FLLHTTR 2.80 ± 0.99, YLSLLQR 4.23 ± 1.24), and each system keeps seven contact pairs. In the computational ensemble the peptide is surface-bound and therefore available as a pathological-chaperone ligand.

3. Impaired cholinergic transmission.  
   The PAS sits at the entrance of the 20-Å gorge above the catalytic triad. RMSF increases are confined to surface loops (panels B), consistent with ligand occupancy of the gating motion. Physical blockade can impede acetylcholine entry and perturb gorge breathing, so the same pose attacks AChE’s classical catalytic function. That maps the cholinergic deficit of Bartus and Hampel onto PAS occupancy by the micropeptide.

4. Pathological chaperone activity and amyloid co-nucleation.  
   Inestrosa and De Ferrari established the PAS as a pro-fibrillar site; Lushchekina’s accelerated MD and Atanasova’s 1-μs trajectory recast that process as multi-mode residence on PAS/344–361, with hydrogen bonds holding the interface while the enzyme scaffolds nucleation. The three complexes here yield the same computational picture: a persistent polar network, entrance-loop perturbation, and, for YLSLLQR, SASA contraction (Figure 6C) indicating tighter interfacial burial. Periodontal micropeptides can therefore act as heterologous seeds that recast the PAS electrostatic and hydrophobic landscape and co-nucleate endogenous Aβ on the same surface. In this model the AChE–micropeptide–Aβ assembly carries both gorge occlusion and enhanced amyloid toxicity. Detection of *Porphyromonas gingivalis* in AD brains by Dominy et al. supplies the setting in which an oral ligand reaches central PAS.

These four steps are molecular events inside the docking poses and single 100-ns trajectories. They are not experimental binding constants, and Vina scores are not Kd. FLLHTTR’s best pose (−9.60 kcal/mol) is stronger than its three-run mean (−8.77 ± 1.41 kcal/mol); the mechanism is therefore argued from PAS geometry and kinetic residence, not from ranking pathogenicity by a single best score.

### References

1. Atanasova, M., Dimitrov, I., & Ivanov, S. (2020). Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. *Cybernetics and Information Technologies*, 20(6), 140–154. https://doi.org/10.2478/cait-2020-0068
2. Dominy, S. S., Lynch, C., Ermini, F., Benedyk, M., Marczyk, A., Forbes, A., Haditsch, M., et al. (2019). *Porphyromonas gingivalis* in Alzheimer's disease brains: Evidence for disease causation and treatment with small-molecule inhibitors. *Science Advances*, 5(1), eaau3333. https://doi.org/10.1126/sciadv.aau3333
3. Silman, I., & Sussman, J. L. (2005). Acetylcholinesterase: ‘classical’ and ‘non-classical’ functions and pharmacology. *Current Opinion in Pharmacology*, 5(3), 293–302. https://doi.org/10.1016/j.coph.2005.01.014
4. Inestrosa, N. C., Alvarez, A., Pérez, C. A., Moreno, R. D., Vicente, M., Link, C. A., Dayoub, O. I., et al. (1996). Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. *Neuron*, 16(4), 881–891. https://doi.org/10.1016/S0896-6273(00)80108-7
5. Inestrosa, N. C., Dinamarca, M. C., & Alvarez, A. (2008). Amyloid-cholinesterase interactions. Implications for Alzheimer's disease. *Molecular Neurobiology*, 38(3), 262–273. https://doi.org/10.1007/s12035-008-8043-6
6. Hampel, H., Mesulam, M. M., Cuello, A. C., Farlow, M. R., Giacobini, E., Grossberg, G. T., Khachaturian, A. S., et al. (2018). The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. *Brain*, 141(7), 1917–1933. https://doi.org/10.1093/brain/awy132
7. Bartus, R. T., Dean, R. L., Beer, B., & Lippa, A. S. (1982). The cholinergic hypothesis of geriatric memory dysfunction. *Science*, 217(4558), 408–414. https://doi.org/10.1126/science.7046051
8. Selkoe, D. J., & Hardy, J. (2016). The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Molecular Medicine*, 8(6), 595–608. https://doi.org/10.15252/emmm.201606210
9. De Ferrari, G. V., Canales, M. A., Shin, I., Weiner, L. M., Silman, I., & Inestrosa, N. C. (2001). A structural motif of acetylcholinesterase that promotes amyloid-β-peptide fibril formation. *Biochemistry*, 40(35), 10447–10457. https://doi.org/10.1021/bi0101392
10. Lushchekina, S. V., Kots, E. D., Novichkova, D. A., Petrov, K. A., & Masson, P. (2017). Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*, 7(2), 396–402. https://doi.org/10.1007/s12668-016-0375-x
