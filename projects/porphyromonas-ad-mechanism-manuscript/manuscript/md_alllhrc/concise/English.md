## Abstract

A 100-ns molecular-dynamics (MD) output assigned to the acetylcholinesterase (AChE)–ALLLHRC complex was interpreted using the analytical categories of a published AChE–amyloid-β study without transferring its peptide-specific findings. The configured GROMACS workflow used Amber99SB-ILDN, explicit water, physiological salt, staged equilibration, and a 100-ns production interval. AChE backbone RMSD was 0.1803 ± 0.0220 nm. Peptide self-fitted RMSD formed three plateaus: 0.0582 ± 0.0091 nm at 0.0–22.6 ns, 0.1432 ± 0.0161 nm at 23.4–55.6 ns, and 0.2694 ± 0.0148 nm at 57.0–100.0 ns. Peptide–AChE center-of-mass distance distributions peaked near 1.2 and 1.4 nm; complex and peptide solvent-accessible surface areas remained approximately 210–223 and 10–12 nm². Intermolecular hydrogen bonds ranged from 0 to 11 and were generally fewer late in the trajectory. The output did not provide independent replicas, validated residue contacts, binding free energy, experimental AChE activity, or a complete raw trajectory archive.

**Keywords:** ALLLHRC; acetylcholinesterase; molecular dynamics; peptide–protein interaction; RMSD; hydrogen bonds

## Introduction

Acetylcholinesterase (AChE) hydrolyses acetylcholine and remains a symptomatic drug target in Alzheimer’s disease (AD) [@hampel2018cholinergic]. Its peripheral region has also been linked to acceleration of amyloid-β (Aβ) assembly [@inestrosa1996ache]. These observations support structural study of AChE-interacting molecules, but a computational peptide trajectory cannot by itself establish enzyme inhibition, altered Aβ aggregation, or disease relevance.

Atanasova and colleagues analyzed an AChE–Aβ complex over 1 μs using RMSD, RMSF, radial distribution, solvent exposure, secondary structure, contacts, hydrogen bonds, and water bridges [@atanasova2020md]. The present study used those metric categories to organize a separate 100-ns result for the seven-residue peptide ALLLHRC. No Aβ-specific contact, residence region, or mechanism from the reference article was assigned to ALLLHRC.

## Materials and methods

The available result comprised a six-panel trajectory summary and an RMSD diagnostic export associated with the `md_alllhrc` directory. The system was assigned to ALLLHRC from the directory and supplied description, although the plot retained an inherited “AChE–Aβ” header. This labeling discrepancy remains to be closed with matching topology and trajectory identifiers.

The parent workflow specifies GROMACS [@abraham2015gromacs], Amber99SB-ILDN [@lindorfflarsen2010amber], TIP3P-compatible water, neutralization, 0.15 mol/L NaCl, a 1.0-nm solute-to-box distance, minimization, 1-ns restrained NVT heating, 1-ns restrained NPT equilibration, and 1-ns unrestrained NPT equilibration. Production was configured for 100 ns at 300 K and 1 bar with a 2-fs step, LINCS, particle-mesh Ewald electrostatics, and coordinates every 20 ps. These are configured rather than independently verified run parameters because complete inputs, logs, energies, checkpoints, and raw trajectories were unavailable.

The RMSD diagnostic defined AChE as residues 1–530 and ALLLHRC as residues 531–537. Peptide RMSD was calculated after fitting the peptide backbone to itself and therefore represents internal conformational deviation rather than whole-peptide translation. RMSD summaries came from a diagnostic calculation on a digitized trace and are descriptive estimates rather than substitutes for raw-coordinate analysis; other values were read conservatively from the supplied plots. No inferential statistics were reconstructed from the image.

## Results

AChE backbone RMSD averaged 0.1803 ± 0.0220 nm and reached a maximum of 0.2320 nm, indicating limited receptor-backbone deviation in this trajectory (Table 1). ALLLHRC self-fitted RMSD underwent two transitions, near 23 and 56 ns, before occupying a higher but narrow final plateau. The full peptide series was 0.1789 ± 0.0870 nm, with a range of 0.0151–0.3141 nm. Because translation and rotation were removed by peptide self-fitting, the steps reflect internal rearrangement relative to the initial conformation; they do not establish dissociation or rebinding.

Most AChE RMSF values were below approximately 0.10 nm, with localized larger peaks and a terminal value approaching 0.60 nm. Most peptide RMSF values were approximately 0.05–0.10 nm, with one endpoint near 0.21 nm. The center-of-mass RDF had a main peak near 1.2 nm and a secondary peak near 1.4 nm, consistent with two preferred separation ranges but not with a measured affinity or residue contact.

Complex SASA stayed approximately 210–223 nm² and peptide SASA approximately 10–12 nm². The plotted secondary-structure fractions were stable, with helix highest at approximately 0.33–0.37; however, the structural selection was not supplied and whole-complex values would be AChE-dominated. AChE–ALLLHRC hydrogen bonds fluctuated between 0 and 11. Counts were commonly approximately 3–7 early and middle in the run and more often 1–4 after about 65–70 ns, consistent with interface reorganization during the late peptide plateau.

**Table 1. Concise summary of the supplied AChE–ALLLHRC trajectory.**

| Metric | Result | Interpretation boundary |
| --- | --- | --- |
| AChE backbone RMSD | 0.1803 ± 0.0220 nm; maximum 0.2320 nm | Limited deviation in one trajectory, not functional stabilization |
| ALLLHRC RMSD plateau 1 | 0.0582 ± 0.0091 nm, 0.0–22.6 ns | Initial internal-conformation regime |
| ALLLHRC RMSD plateau 2 | 0.1432 ± 0.0161 nm, 23.4–55.6 ns | First rearranged regime |
| ALLLHRC RMSD plateau 3 | 0.2694 ± 0.0148 nm, 57.0–100.0 ns | Persistent second rearranged regime |
| COM RDF | Peaks near 1.2 and 1.4 nm | Preferred separations, not atomic contacts or affinity |
| SASA | Complex ~210–223 nm²; peptide ~10–12 nm² | No large global exposure transition |
| Intermolecular H bonds | 0–11; generally fewer late | Intermittent polar contacts, not biochemical inhibition |

## Discussion

The combined pattern supports a restrained AChE backbone and a conformationally adaptive peptide. Continued hydrogen bonds and preferred center-of-mass separations are compatible with dynamic association, whereas the peptide RMSD steps and lower late hydrogen-bond counts argue against describing the trajectory as a single rigid binding pose. AChE-fitted peptide positional RMSD, minimum distances, residue contacts, representative structures, and visual inspection are needed to determine whether the peptide moved within one surface region, shifted between sites, or partly disengaged.

The reference AChE–Aβ simulation demonstrates why multiple trajectory observables are needed, but its Aβ contact residues, AChE 344–361 residence region, PAS movements, and 1-μs stability claim cannot be transferred to ALLLHRC [@atanasova2020md]. The source plot’s inherited Aβ heading should be corrected and the system identity verified against topology and trajectory hashes.

The principal limitations are the single 100-ns trajectory, absence of independent seeds and an apo control, incomplete raw files, uncertain secondary-structure selection, and lack of residue-resolved interactions. No binding free energy, residence time, catalytic inhibition, ligand competition, Aβ aggregation, BBB transport, cytotoxicity, or AD phenotype was measured. The current output therefore cannot show that ALLLHRC binds the peripheral anionic site, inhibits AChE, modifies amyloid biology, reaches the brain, or contributes to disease.

## References

1. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
2. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
3. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
4. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
5. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
