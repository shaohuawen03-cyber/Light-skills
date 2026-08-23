## Abstract

Acetylcholinesterase (AChE) is a structurally and biologically relevant target in Alzheimer’s disease research, but a docking score alone cannot establish whether a short peptide remains associated with the enzyme in an explicit-solvent trajectory. We therefore interpreted a 100-ns molecular-dynamics (MD) output assigned to the AChE–ALLLHRC complex using the analytical framework of the published AChE–amyloid-β study by Atanasova and colleagues, while keeping the two peptide systems scientifically distinct. The configured workflow used GROMACS, the Amber99SB-ILDN force field, TIP3P water, physiological ionic strength, staged equilibration, and a 100-ns production run. AChE backbone RMSD averaged 0.1803 ± 0.0220 nm in the available diagnostic export. Peptide self-fitted backbone RMSD occupied three plateaus: 0.0582 ± 0.0091 nm at 0.0–22.6 ns, 0.1432 ± 0.0161 nm at 23.4–55.6 ns, and 0.2694 ± 0.0148 nm at 57.0–100.0 ns. The distance distribution showed preferred peptide–AChE center-of-mass separations near 1.2 and 1.4 nm; complex and peptide solvent-accessible surface areas remained approximately 210–223 and 10–12 nm², respectively. Intermolecular hydrogen bonds fluctuated from 0 to 11 and were generally less numerous late in the trajectory. The supplied data did not include independent replicas, a residue-resolved interface map, binding free energies, experimental AChE activity, or a complete raw trajectory archive.

**Keywords:** ALLLHRC; acetylcholinesterase; molecular dynamics; peptide–protein complex; RMSD; radial distribution function; hydrogen bonds; Alzheimer’s disease

## Introduction

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder involving amyloid-β (Aβ), tau, synaptic dysfunction, neuroinflammation, vascular factors, and age-dependent loss of resilience [@scheltens2021alzheimer]. Acetylcholinesterase (AChE) is clinically relevant because it hydrolyses acetylcholine and remains a symptomatic drug target in AD [@hampel2018cholinergic]. AChE also has non-catalytic interactions with Aβ assembly, and its peripheral region has been implicated in acceleration of amyloid fibril formation [@inestrosa1996ache]. These observations justify structural investigation of AChE-interacting molecules, but they do not mean that a computationally prioritized peptide binds AChE, inhibits catalysis, changes Aβ aggregation, or affects AD biology.

Short peptides are especially challenging structural ligands. Their terminal states, protonation, starting conformers, internal flexibility, receptor placement, and solvent exposure can strongly influence docking and MD behavior. A favorable docking score is therefore a starting hypothesis rather than a binding measurement. MD can test whether a prepared system remains within a defined conformational regime under a stated force field and solvent model, while backbone deviation, residue fluctuation, solvent exposure, distance distributions, secondary-structure fractions, and hydrogen bonds provide complementary descriptions of the trajectory.

The present analysis concerns the heptapeptide ALLLHRC in complex with human AChE. The parent structural workflow identifies the human AChE crystal structure represented by PDB 4EY6 as its receptor framework [@cheung2012ache]. The exact prepared starting coordinate file was not included in the available result package, however, so receptor preparation, peptide termini, protonation, chain naming, and starting-site assignment could not be independently checked.

Atanasova and colleagues used a 1-μs all-atom trajectory to study an AChE–Aβ complex and evaluated backbone motion, peptide residence, radial distribution, solvent-accessible surface area, secondary structure, contacts, hydrogen bonding, and water-mediated bridges [@atanasova2020md]. That work provides a useful analysis framework, not a transferable result set. ALLLHRC is a distinct seven-residue peptide, the present trajectory is 100 ns rather than 1 μs, and no Aβ residue contact, AChE residence region, or mechanistic conclusion from the reference study was assigned to ALLLHRC. The objective was to describe only the supplied ALLLHRC–AChE trajectory outputs, identify internally consistent patterns, and define what additional data are required before a binding or functional claim can be made.

## Materials and methods

### Study design and evidence scope

This was a computation-only, descriptive analysis of an existing MD output. The available evidence comprised a six-panel trajectory summary and an RMSD diagnostic export associated with the `md_alllhrc` system directory. The panels reported backbone RMSD, backbone RMSF, peptide–AChE center-of-mass radial distribution, solvent-accessible surface area (SASA), secondary-structure fractions, and intermolecular hydrogen-bond counts over 100 ns. No wet-laboratory experiment, new docking calculation, new MD production run, statistical comparison, or biological assay was performed for this manuscript.

System identity was assigned from the ALLLHRC directory label and the explicit system description supplied with the result. The graphical header retained an inherited “AChE–Aβ” label. This was treated as a provisional labeling discrepancy rather than evidence that the simulated peptide was Aβ. No Aβ-specific sequence, contact residue, surface region, or interaction described in the reference article was imported into the ALLLHRC result. A topology-to-trajectory manifest and matching coordinate hashes are still required to close this identity-provenance gap.

### Configured molecular-dynamics protocol

The parent workflow specifies GROMACS for trajectory generation and analysis [@abraham2015gromacs]. Its executable 100-ns configuration uses the Amber99SB-ILDN force field, which refines side-chain torsion potentials within the Amber ff99SB family [@lindorfflarsen2010amber]. The system was configured in a triclinic periodic box with a 1.0-nm solute-to-boundary distance, TIP3P-compatible water coordinates, neutralizing ions, and 0.15 mol/L NaCl. These are reported as configured parameters because the complete run logs and binary input files were not available for independent confirmation.

The configured preparation comprised 2,000 steepest-descent minimization steps with 1,255 kJ mol⁻¹ nm⁻² heavy-atom positional restraints, 1.0 ns of restrained NVT heating from 10 to 300 K, 1.0 ns of restrained NPT equilibration, and 1.0 ns of unrestrained NPT equilibration at 300 K and 1 bar. The production stage was configured for 100 ns with a 2-fs time step, LINCS constraints on hydrogen-containing bonds, 1.2-nm real-space cutoffs, force-switched van der Waals interactions from 1.0 nm, particle-mesh Ewald electrostatics, velocity-rescale temperature coupling, and Berendsen pressure coupling. Coordinates were scheduled every 20 ps, corresponding to 5,000 planned frames. Exact GROMACS version, generated velocity seed, hardware, run completion log, energy file, checkpoint, topology, and final coordinates were not supplied.

### Trajectory observables and interpretation rules

AChE was defined in the available RMSD diagnostic as residues 1–530 and ALLLHRC as residues 531–537. Peptide backbone RMSD was calculated after fitting the peptide backbone to itself, so it measures internal deviation from the starting peptide conformation while removing whole-peptide translation and rotation. The diagnostic summaries were calculated from a digitized RMSD trace rather than a raw GROMACS time series; they are therefore descriptive estimates and do not substitute for coordinate-based reanalysis. The complex trace was interpreted qualitatively because whole-complex fitting can be sensitive to periodic-boundary imaging when receptor and peptide are treated as one fitting group.

RMSF was used to identify relatively mobile sequence positions. The center-of-mass radial distribution function, g(r), was interpreted as a distribution of peptide–AChE center-of-mass separation rather than an atomic contact distance or binding affinity. SASA traces were used to assess large changes in solvent exposure. Secondary-structure fractions were transcribed as plotted; because the structural selection underlying that panel was not supplied, those fractions were not assumed to be ALLLHRC-specific. Intermolecular hydrogen-bond counts were treated as instantaneous geometric contacts. No residue-level donor–acceptor identities, occupancy threshold, distance/angle definition, lifetime distribution, or water-bridge output was available in the supplied six-panel result.

Exact values were reported only where they were present in the diagnostic export. Approximate ranges for RMSF, RDF, SASA, secondary structure, and hydrogen bonds were read conservatively from the plotted axes. No means, confidence intervals, hypothesis tests, or convergence claims were reconstructed from image pixels.

## Results

### AChE remained within a narrow backbone-deviation range while ALLLHRC underwent two transitions

The AChE backbone RMSD was 0.1803 ± 0.0220 nm across the available diagnostic series, with a reported maximum of 0.2320 nm (Table 1). The plotted complex and AChE traces were closely aligned for most of the 100-ns trajectory and remained predominantly around 0.10–0.20 nm after the initial rise. Within the resolution of the supplied output, this pattern did not indicate a large global rearrangement of the receptor backbone.

The peptide behaved differently. Across the full trajectory, self-fitted ALLLHRC backbone RMSD was 0.1789 ± 0.0870 nm, with a range of 0.0151–0.3141 nm. The trace occupied three successive plateaus. From 0.0 to 22.6 ns, the mean was 0.0582 ± 0.0091 nm; from 23.4 to 55.6 ns, it was 0.1432 ± 0.0161 nm; and from 57.0 to 100.0 ns, it was 0.2694 ± 0.0148 nm. The transitions occurred over approximately 23–24 ns and 56–58 ns. Because the peptide was fitted to its own backbone, these steps describe internal conformational rearrangement rather than simple rigid-body translation through the periodic box. The narrow final plateau indicates persistence of a new internal conformation relative to frame 0, but it does not by itself establish continued binding to AChE.

**Table 1. Descriptive ALLLHRC–AChE molecular-dynamics outputs.**

| Observable | Supplied result | Supported interpretation |
| --- | --- | --- |
| AChE backbone RMSD | 0.1803 ± 0.0220 nm; maximum 0.2320 nm | Limited receptor-backbone deviation over 100 ns |
| ALLLHRC self-fitted RMSD, full trajectory | 0.1789 ± 0.0870 nm; 0.0151–0.3141 nm | Peptide internal conformation changed substantially relative to frame 0 |
| ALLLHRC plateau 1 | 0.0582 ± 0.0091 nm, 0.0–22.6 ns | Initial low-deviation regime |
| ALLLHRC plateau 2 | 0.1432 ± 0.0161 nm, 23.4–55.6 ns | First rearranged regime |
| ALLLHRC plateau 3 | 0.2694 ± 0.0148 nm, 57.0–100.0 ns | Persistent second rearranged regime |
| Peptide–AChE COM RDF | Main peak near 1.2 nm; secondary peak near 1.4 nm | Two preferred center-of-mass separation ranges |
| Complex SASA | Approximately 210–223 nm² | No large loss or gain of global solvent exposure |
| Peptide SASA | Approximately 10–12 nm² | Peptide solvent exposure remained within a narrow plotted band |
| Intermolecular H bonds | 0–11; mostly approximately 1–4 late in the run | Intermittent polar contacts with reduced late counts |

### RMSF indicated localized receptor mobility and an asymmetric peptide profile

Most AChE backbone RMSF values were below approximately 0.10 nm. Localized peaks reached roughly 0.2–0.4 nm, and the terminal region showed the largest plotted excursion, approaching 0.60 nm. Such peaks identify flexible positions in this trajectory but cannot be assigned to a structural loop or chain terminus with confidence without the residue mapping and starting structure.

For ALLLHRC, most plotted backbone RMSF values were approximately 0.05–0.10 nm, whereas one peptide endpoint approached approximately 0.21 nm. This asymmetric profile indicates that mobility was not evenly distributed across the seven-residue backbone. The plot alone does not establish whether the more mobile endpoint was the N terminus or C terminus, because peptide orientation and residue-name mapping were not supplied.

### Distance distribution showed two preferred center-of-mass separations

The peptide–AChE center-of-mass RDF had a sharp principal peak at approximately 1.2 nm with g(r) above 200 and a secondary peak around 1.4 nm with g(r) around 80–90. The distribution returned close to zero beyond approximately 1.6 nm in the plotted range. These peaks are consistent with concentrated occupancy in two center-of-mass separation ranges. They do not identify a binding residue, an atomic contact distance, a peripheral-anionic-site pose, or a dissociation constant. The unusually high normalized peak height also depends on the finite-system normalization and should not be compared directly with a bulk-solvent RDF without the calculation details.

### Solvent exposure and secondary-structure fractions showed no large global transition

Complex SASA fluctuated within approximately 210–223 nm², with a modest upward drift late in the trajectory. Peptide SASA remained near 10–12 nm². The supplied traces therefore did not show the sustained SASA decrease that would be required to argue, from this metric alone, for progressive compaction of the complex. Conversely, stable SASA does not prove constant interface burial because global receptor exposure can dominate the complex value.

The secondary-structure traces were comparatively stable: helix remained approximately 0.33–0.37, coil 0.19–0.23, sheet 0.14–0.17, bend 0.12–0.15, and turn 0.09–0.13. No abrupt system-wide secondary-structure conversion accompanied the peptide RMSD transitions. The analysis selection for this panel was not documented. If calculated over the whole complex, the fractions would be dominated by the 530-residue enzyme and cannot be interpreted as the secondary structure of a seven-residue peptide.

### Intermolecular hydrogen bonds persisted intermittently but became less numerous late in the trajectory

The instantaneous AChE–ALLLHRC hydrogen-bond count varied between 0 and 11. Early and middle portions of the trajectory frequently contained approximately 3–7 bonds, with occasional higher values. After approximately 65–70 ns, counts were more often 1–4, although contacts remained intermittent through the end of the run and occasional zero-bond frames occurred throughout. The lower late counts coincide temporally with the high-RMSD peptide plateau and are compatible with interface reorganization. A causal relation cannot be established without synchronized numeric series, residue-level donor–acceptor identities, and contact lifetimes.

**Table 2. Evidentiary boundaries of the supplied 100-ns trajectory.**

| Observation | Supported statement | Statement not supported by the current data |
| --- | --- | --- |
| Low AChE RMSD | The receptor backbone showed limited deviation in this trajectory | AChE was experimentally stabilized or functionally inhibited |
| Three peptide RMSD plateaus | ALLLHRC underwent two internal rearrangements | The peptide dissociated, rebound, or changed a specific binding pose |
| RDF peaks near 1.2 and 1.4 nm | Two preferred center-of-mass separations were sampled | Direct atomic contact, PAS residence, or binding affinity |
| Narrow SASA bands | No large global solvent-exposure transition was visible | Constant buried interface area or progressive complex compaction |
| Stable secondary fractions | No system-wide secondary-structure transition was visible | ALLLHRC adopted a defined helix or sheet |
| Intermittent hydrogen bonds | Polar contacts occurred repeatedly | Persistent residue-specific bonding or biochemical inhibition |

## Discussion

### Principal interpretation

The supplied 100-ns output is most consistent with a structurally restrained AChE backbone and a flexible short peptide that reorganized twice before occupying a distinct late conformational regime. The AChE RMSD remained below approximately 0.23 nm, whereas ALLLHRC self-fitted RMSD moved from a low-deviation plateau to two progressively more displaced plateaus. Because self-fitting removes peptide translation and rotation, the steps are not explained by movement of an intact rigid peptide across the periodic boundary. They indicate internal backbone rearrangement relative to the starting conformation.

RDF and hydrogen-bond traces add interface-level context but do not convert the RMSD pattern into proof of stable binding. The RDF concentrated around two center-of-mass distances, and intermolecular hydrogen bonds continued to occur after the second peptide transition. At the same time, late hydrogen-bond counts were generally lower. A parsimonious description is therefore dynamic association with interface reorganization, not preservation of a single rigid docking pose. Whether ALLLHRC remained in one surface pocket, moved between neighboring regions, or partially disengaged cannot be determined without AChE-fitted peptide positional RMSD, minimum-distance traces, residue contacts, representative structures, and trajectory visualization.

### Relationship to the reference AChE–Aβ study

The Atanasova study is valuable because it demonstrates that peptide motion on the AChE surface can coexist with receptor stability and that RMSD alone is insufficient to define residence [@atanasova2020md]. Their 1-μs AChE–Aβ analysis incorporated snapshots, residue contacts, hydrogen bonds, hydrophobic interactions, SASA, secondary structure, RDF, and water-mediated bridges. The present result uses the same categories as an organizational framework but does not reproduce that study.

Several differences prevent direct transfer. ALLLHRC is a seven-residue sequence rather than Aβ, the production interval is one tenth as long, and the configured force field and run implementation differ. The supplied ALLLHRC output contains no validated residue contact map, water-bridge analysis, peptide residence region, or experimentally linked phenotype. It would therefore be incorrect to assign the AChE 344–361 residence region, PAS migration, Aβ aggregation behavior, or any Aβ-specific interaction to ALLLHRC. The inherited Aβ text in the plot title further requires correction in the source analysis package and confirmation against topology and trajectory identifiers.

### Structural and biological limitations

This analysis is based on one trajectory. No independent seeds, replicate simulations, apo-AChE comparator, alternative starting poses, or other peptide complexes were supplied. Plateau persistence within one 100-ns run is not ensemble convergence, and a single force-field trajectory cannot estimate uncertainty across initialization or model choices. Berendsen pressure coupling and an unfixed generated velocity seed in the configured workflow should be reported exactly and addressed prospectively in replicate production runs rather than changed after viewing the result.

The current output also lacks complete reproducibility materials: exact GROMACS version, starting coordinates, terminal and protonation states, topology, TPR, XTC/TRR, EDR, LOG, CPT, index groups, analysis commands, and file hashes. The whole-complex RMSD is particularly sensitive to periodic-boundary imaging. Future analysis should make the fitting and centering sequence explicit and provide receptor-fitted peptide RMSD in addition to peptide self-fitted RMSD. RMSF residue names, secondary-structure selection, RDF normalization, hydrogen-bond geometry, and frame exclusions must also be frozen.

No binding free energy, kinetic residence time, AChE catalytic activity, competition with a known ligand, Aβ aggregation assay, BBB transport, cytotoxicity, or AD-relevant phenotype was measured. The trajectory cannot show that ALLLHRC inhibits AChE, binds the peripheral anionic site, alters amyloid assembly, reaches the brain, or contributes to disease. Those questions require a verified system identity, independently seeded trajectories, residue-level structural analysis, biochemical binding and enzyme assays, and appropriate peptide controls.

## References

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
3. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
4. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
5. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
6. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
7. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
