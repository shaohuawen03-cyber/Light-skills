## Analysis methods

### Molecular docking

Human recombinant acetylcholinesterase (rhAChE, PDB 4EY6, 2.40 Å) was prepared by removing galantamine and crystallographic waters, repairing internal chain breaks, and assigning physiological protonation (pH 7.4). The twelve 7–9-aa candidate micropeptides ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, HVLLLRQCA, LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR were docked with AutoDock Vina (exhaustiveness = 32) into a grid centered on the peripheral anionic site (PAS: Tyr72, Asp74, Thr75, Leu76, Trp286, His287, Tyr341) and spanning the gorge neck (Phe295), choline-binding subsite (Trp86, Glu202, Tyr337), and catalytic triad (Ser203, His447, Glu334). Each ligand was run three times (`N_Success` = 3). Best-run affinity, three-run mean ± SD, hydrogen-bond geometry, and PAS contacts were taken from the local three-run summary and the single best-scoring pose of each ligand. Individual PDBQT files and configuration logs are not archived.

### Molecular dynamics

Four explicit-solvent GROMACS 2025 systems were simulated with Amber99SB-ILDN and TIP3P water at 0.15 M NaCl: apo AChE (Chain A) and the AChE–ALLLHRC, AChE–FLLHTTR, and AChE–YLSLLQR complexes. Each system used a triclinic box with a 1.0 nm solute-to-boundary buffer. Equilibration comprised 2,000-step steepest-descent minimization, 1.0 ns restrained NVT heating to 300 K, 1.0 ns restrained NPT density equilibration, and 1.0 ns unrestrained NPT pre-equilibration. Production ran 100 ns (dt = 2.0 fs) in the NPT ensemble (300 K, 1.0 bar) with LINCS, 1.2 nm cutoffs, and Particle Mesh Ewald electrostatics. Frames were written every 20 ps.

Trajectory metrics matching Figures 4–6 were computed for backbone Cα RMSD, per-residue RMSF, SASA, radius of gyration (Rg), DSSP secondary-structure occupancy, and intermolecular hydrogen bonds (`gmx hbond`; donor–acceptor ≤ 3.0 Å). Peptide self-fit RMSD and persistent interfacial contacts (7.0 Å cutoff) were recorded as supporting descriptors. Steady-state values are mean ± SD over the final 20 ns (80.0–100.0 ns).

## Results

### Docking affinities and PAS engagement

All twelve ligands yielded favorable local Vina scores. Best-run affinities ranged from -8.25 to -9.60 kcal/mol and three-run means from -8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol (Table 1, Figure 1). Best-pose ranking placed FLLHTTR first (-9.60 kcal/mol), then YLSLLQR (-9.49 kcal/mol) and ALLLHRC (-9.29 kcal/mol). Mean ranking placed YLSLLQR first (-9.44 ± 0.09 kcal/mol) and ALLLHRC second (-9.18 ± 0.11 kcal/mol). FLLHTTR retained the strongest single pose but the largest run-to-run SD (-8.77 ± 1.41 kcal/mol). Best poses formed 3–10 hydrogen bonds (mean length 2.83–3.28 Å; Figures 2 and 3; Figure S1).

**Table 1. Local AutoDock Vina scores and PAS engagement of twelve candidate micropeptides against human AChE (PDB 4EY6).**

| No. | Peptide | HBonds | Key residues | Best (kcal/mol) | Mean ± SD, n=3 (kcal/mol) | PAS engagement |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ALLLHRC | 3 | SER-125, SER-203, TYR-124 | -9.29 | -9.18 ± 0.11 | No; catalytic Ser203 / gorge neck |
| 2 | FCLHLQLR | 7 | SER-203, THR-75, TYR-124, TYR-337, TYR-341 | -9.27 | -8.96 ± 0.48 | Yes; Thr75, Tyr341 |
| 3 | FLLHTTR | 8 | ASP-74, HIS-287, LEU-289, PHE-295, TYR-337, TYR-72 | -9.60 | -8.77 ± 1.41 | Yes; extensive PAS (Asp74, Tyr72, His287); largest SD |
| 4 | HLLTLKKHV | 6 | PHE-346, TYR-124, TYR-337, TYR-72, TYR-77 | -8.88 | -8.69 ± 0.20 | Yes; Tyr72 and 344–361 (Phe346) |
| 5 | HLPLLHRCC | 4 | SER-125, TYR-124, TYR-337 | -8.35 | -8.28 ± 0.07 | No; gorge rim |
| 6 | HVLLLRQCA | 4 | SER-125, THR-75, TYR-124 | -8.25 | -8.07 ± 0.16 | Yes; Thr75 |
| 7 | LLHLPKRTT | 3 | SER-203, TYR-337, VAL-340 | -9.01 | -8.89 ± 0.16 | PAS-adjacent (Val340) |
| 8 | LLHPLRC | 4 | SER-125, SER-293, TYR-124 | -8.91 | -8.78 ± 0.11 | No; gorge entrance |
| 9 | LLHPLRL | 10 | HIS-447, PHE-295, TRP-286, TYR-124, TYR-337, TYR-341 | -8.94 | -8.91 ± 0.05 | Yes; dual-site PAS to His447; smallest SD |
| 10 | WLLVHLKK | 4 | ASN-283, GLN-279, SER-293, TYR-124 | -8.94 | -8.64 ± 0.26 | No; outer loops |
| 11 | YHHLLCRR | 7 | SER-125, SER-203, TRP-86, TYR-124, TYR-337 | -9.03 | -8.62 ± 0.43 | No; choline pocket Trp86 |
| 12 | YLSLLQR | 7 | GLU-202, SER-203, THR-75, TYR-124, TYR-337, TYR-72 | -9.49 | -9.44 ± 0.09 | Yes; PAS plus catalytic entrance; strongest mean |

![Figure 1. Local AutoDock Vina scores of twelve candidate micropeptides against human AChE.](../../figures/fig5_docking_scores.png)

**Figure 1. Local AutoDock Vina scores of twelve candidate micropeptides against human AChE (PDB 4EY6).** Blue circles show the three-run mean; whiskers show the standard deviation; orange diamonds mark the best-run affinity. Order matches best-run ranking. Scores are empirical Vina metrics, not experimental free energies.

![Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA.](../../figures/fig_docking_poses_A_F.png)

**Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA (panels A–F).** Peptide, orange; contacting AChE residues, cyan; hydrogen bonds, dashed.

![Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR.](../../figures/fig_docking_poses_G_L.png)

**Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR (panels G–L).** LLHPLRL (panel I) spans PAS Trp286/Tyr341 to catalytic His447.

![Figure S1. Combined overview of all twelve best-scoring docking poses.](../../figures/fig_docking_poses_12_combined.png)

**Figure S1. Combined overview of all twelve best-scoring docking poses.** Single-page layout of panels A–L.

Canonical Peripheral Anionic Site (PAS) binders in the best pose were FLLHTTR (Figure 2C), YLSLLQR (Figure 3L), FCLHLQLR, HVLLLRQCA, HLLTLKKHV, and LLHPLRL (Figure 3I). ALLLHRC bound catalytic Ser203 with the shortest mean hydrogen bond (2.83 Å) rather than the outer PAS aromatic core (Figure 2A). Three-run means distinguish reproducible high-affinity ligands (YLSLLQR, ALLLHRC, LLHPLRL) from ligands whose best pose is stronger than the run-averaged score (FLLHTTR, FCLHLQLR, YHHLLCRR).

### 100-ns molecular dynamics of apo AChE and three complexes

Production trajectories were completed for apo AChE and the ALLLHRC, FLLHTTR, and YLSLLQR complexes (Table 2, Figures 4–6). Each six-panel figure compares the unliganded control with one peptide complex: backbone RMSD (A), per-residue RMSF (B), SASA (C), Rg (D), DSSP occupancy over the last 20 ns (E), and intermolecular hydrogen bonds (F).

<!-- PAGEBREAK -->

![Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns comparison.](../../figures/fig_compare_ache_vs_alllhrc.png)

**Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns molecular dynamics comparison.** Panels A–F match the metrics in Table 2.

![Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns comparison.](../../figures/fig_compare_ache_vs_fllhttr.png)

**Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns molecular dynamics comparison.** Panel layout matches Figure 4. Complex RMSD (A) and Rg (D) show the largest elevation among the three peptides.

![Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns comparison.](../../figures/fig_compare_ache_vs_ylsllqr.png)

**Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns molecular dynamics comparison.** Panel layout matches Figure 4. SASA (C) contracts relative to apo; hydrogen-bond counts (F) are the densest of the three complexes.

**Table 2. Final-20-ns trajectory metrics for apo AChE and three peptide complexes (mean ± SD), aligned to Figures 4–6.**

| Metric (last 20 ns) | apo AChE | AChE–ALLLHRC | AChE–FLLHTTR | AChE–YLSLLQR |
| --- | --- | --- | --- | --- |
| Backbone Cα RMSD (nm); Figure panels A | 0.1562 ± 0.0093 | 0.1916 ± 0.0092 | 0.2102 ± 0.0087 | 0.2064 ± 0.0136 |
| Peptide self-fit RMSD (nm) | N/A | 0.2518 ± 0.0136 | 0.2697 ± 0.0217 | 0.1979 ± 0.0143 |
| Per-residue RMSF mean (nm); Figure panels B | 0.0783 ± 0.0524 | 0.0876 ± 0.0581 | 0.0901 ± 0.0644 | 0.0813 ± 0.0574 |
| SASA (nm²); Figure panels C | 212.41 ± 2.36 | 217.47 ± 2.49 | 216.34 ± 2.55 | 210.37 ± 2.91 |
| Rg (nm); Figure panels D | 2.2967 ± 0.0043 | 2.3107 ± 0.0052 | 2.3163 ± 0.0059 | 2.3004 ± 0.0051 |
| Intermolecular H-bonds; Figure panels F | N/A | 2.19 ± 0.80 | 2.80 ± 0.99 | 4.23 ± 1.24 |
| Persistent contact pairs | N/A | 7 | 7 | 7 |
| DSSP α-helix / β-sheet (%); Figure panels E | 33.59 / 17.18 | 33.66 / 16.76 | 33.87 / 17.11 | 32.92 / 17.08 |

Figures 4A, 5A, and 6A show that apo RMSD remains near 0.16 nm, while complex RMSD stays below 0.22 nm. Receptor-only RMSD values (0.1653, 0.1767, and 0.1601 nm) confirm that FLLHTTR induces the largest receptor perturbation and that YLSLLQR barely shifts the enzyme backbone. RMSF (panels B) remains low in the catalytic core, with modest increases localized to surface loops. Rg (panels D) stays within 2.29–2.32 nm. SASA (panels C) rises slightly for ALLLHRC and FLLHTTR but contracts for YLSLLQR (210.37 nm²), matching the tighter interfacial burial in Figure 6C. Hydrogen bonds persist throughout 100 ns (panels F); YLSLLQR forms the densest network (4.23 ± 1.24). DSSP helix (~33–34%) and sheet (~17%) fractions overlay the apo bars in panels E. Each complex retains seven persistent contact pairs.

### Evidence boundary

**Table 3. Evidentiary boundaries for docking and 100-ns MD findings.**

| No. | Observation | Supported interpretation | Unsupported extrapolation |
| --- | --- | --- | --- |
| 1 | Best poses of FLLHTTR, YLSLLQR, and LLHPLRL contact PAS residues | Geometric complementarity to the PAS and gorge entrance | Vina scores are not experimental Kd or Ki |
| 2 | Complex RMSD 0.16–0.21 nm with conserved DSSP | Localized loop adaptation without unfolding | Mild RMSD increase is not denaturation or dissociation |
| 3 | Last-20-ns H-bonds 2.19–4.23 and seven contact pairs | Surface residence over 100 ns | Single trajectories do not prove irreversible nanomolar binding |
| 4 | YLSLLQR SASA contraction and densest H-bond panel | Compact interfacial burial relative to apo | Cannot be equated with a macroscopic binding constant |
| 5 | FLLHTTR best-run -9.60 kcal/mol versus mean -8.77 ± 1.41 kcal/mol | Best pose is a high-scoring outlier; mean ranking favors YLSLLQR | A single best pose is not a converged affinity |

## Discussion

### PAS targeting as a working AD mechanism

Chronic periodontitis can deliver *Porphyromonas gingivalis* products into the circulation and, after cytokine- and gingipain-mediated tight-junction injury, across a compromised blood–brain barrier. Once in cortical interstitial space, the candidate micropeptides can occupy the AChE PAS that gates the 20-Å active gorge. Best-pose docking places FLLHTTR on Asp74/Tyr72/His287, LLHPLRL across Trp286/Tyr341 to His447, and YLSLLQR across PAS and the catalytic entrance. The 100-ns trajectories show that these complexes remain globular (Rg 2.29–2.32 nm; conserved helix/sheet) while sustaining intermolecular hydrogen bonds (2.19–4.23 in the last 20 ns). Physical occupancy of the PAS is therefore a structural hypothesis for impaired acetylcholine access, not a measured IC50.

Independently of catalysis, AChE acts as a pathological chaperone that accelerates Aβ assembly through the same PAS. The present peptides target PAS and, for HLLTLKKHV, the adjacent 344–361 region (Phe346). Sustained surface residence could lower the nucleation barrier for Aβ, remodel entrance loops, or present an amphipathic seed. These remain computational hypotheses pending ITC/SPR, Ellman inhibition with PAS mutants, and ThT/TEM aggregation assays.

### Alignment with high-impact literature

Atanasova et al. (2020) reported 1-μs AChE–Aβ simulations centered on the PAS and residues 344–361, stabilized by hydrogen bonds and bridging waters. Silman and Sussman (2005) described the PAS as an electrostatic gatekeeper. Inestrosa et al. (Neuron, 1996; Molecular Neurobiology, 2008) established PAS-dependent chaperone acceleration of Aβ fibrils. Dominy et al. (Science Advances, 2019) detected *P. gingivalis* and gingipains in AD brains. The cholinergic (Bartus et al., 1982; Hampel et al., 2018) and amyloid-cascade (Selkoe & Hardy, 2016) frameworks are bridged here only as a working model: PAS docking can in principle occlude the gorge and remodel a pro-aggregatory surface.

### Limitations

Each system is a single 100-ns trajectory, shorter than the 1,000-ns benchmark. Docking scores are empirical; PDBQT archives are not deposited; FLLHTTR’s SD of 1.41 kcal/mol shows that a best pose can overstate run-averaged affinity. Planned validation includes isothermal titration calorimetry, surface plasmon resonance, Ellman IC50 measurements, and ThT/TEM fibril assays.

### References

1. Atanasova, M., Dimitrov, I., & Ivanov, S. (2020). Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. *Cybernetics and Information Technologies*, 20(6), 140–154. https://doi.org/10.2478/cait-2020-0068
2. Dominy, S. S., Lynch, C., Ermini, F., Benedyk, M., Marczyk, A., Forbes, A., Haditsch, M., et al. (2019). *Porphyromonas gingivalis* in Alzheimer's disease brains: Evidence for disease causation and treatment with small-molecule inhibitors. *Science Advances*, 5(1), eaau3333. https://doi.org/10.1126/sciadv.aau3333
3. Silman, I., & Sussman, J. L. (2005). Acetylcholinesterase: ‘classical’ and ‘non-classical’ functions and pharmacology. *Current Opinion in Pharmacology*, 5(3), 293–302. https://doi.org/10.1016/j.coph.2005.01.014
4. Inestrosa, N. C., Alvarez, A., Pérez, C. A., Moreno, R. D., Vicente, M., Link, C. A., Dayoub, O. I., et al. (1996). Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. *Neuron*, 16(4), 881–891. https://doi.org/10.1016/S0896-6273(00)80108-7
5. Inestrosa, N. C., Dinamarca, M. C., & Alvarez, A. (2008). Amyloid-cholinesterase interactions. Implications for Alzheimer's disease. *Molecular Neurobiology*, 38(3), 262–273. https://doi.org/10.1007/s12035-008-8043-6
6. Hampel, H., Mesulam, M. M., Cuello, A. C., Farlow, M. R., Giacobini, E., Grossberg, G. T., Khachaturian, A. S., et al. (2018). The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. *Brain*, 141(7), 1917–1933. https://doi.org/10.1093/brain/awy132
7. Bartus, R. T., Dean, R. L., Beer, B., & Lippa, A. S. (1982). The cholinergic hypothesis of geriatric memory dysfunction. *Science*, 217(4558), 408–414. https://doi.org/10.1126/science.7046051
8. Selkoe, D. J., & Hardy, J. (2016). The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Molecular Medicine*, 8(6), 595–608. https://doi.org/10.15252/emmm.201606210
