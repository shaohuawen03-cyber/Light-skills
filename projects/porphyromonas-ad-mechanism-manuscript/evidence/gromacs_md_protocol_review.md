# GROMACS molecular-dynamics protocol review

Review date: 2026-08-17

## Referenced repository snapshot

- Repository: `shaohuawen03-cyber/asd`
- Branch: `arena/019ff90e-asd`
- Reviewed commit: `f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`
- In-scope directory: `gromacs_md/`
- Methods file blob: `SCI_Methods_GROMACS_MD_Simulation.md` at `6b627e8381affe1fd448ea5fbbb3cec5fc4b5997`
- Input-directory tree: `23c01b18d467a7827c172723c4e5202b70e5fb11`
- URL: https://github.com/shaohuawen03-cyber/asd/tree/arena/019ff90e-asd/gromacs_md

## Evidence decision

The repository provides a prospective GROMACS workflow, shell/PowerShell orchestration, 100-ns MDP files and trajectory-analysis scripts. It is suitable for documenting a planned downstream molecular-dynamics protocol. It is **not** used as evidence for an MD result in the manuscript.

At the reviewed commit, `gromacs_md/input/` contains only `README.txt`; the three required `*_complex.pdb` starting structures are not present. The tree also does not provide a complete raw package for every planned system containing starting coordinates, topology, TPR, XTC, EDR, LOG and checkpoint files. A partial `md_alllhrc/` analysis directory exists, but the user explicitly stated that trajectory analysis is incomplete. No RMSD, RMSF, radius of gyration, SASA, RDF, secondary-structure, hydrogen-bond, contact, water-bridge or comparative conclusion from that directory is transferred into the manuscript.

## Parameter hierarchy

The repository contains inconsistent narrative descriptions of 100-ns versus 1000-ns production runs. For the manuscript, the executable `mdp/100ns/*.mdp` files and the branch-default selection in `scripts/run_all.sh` are treated as the controlling prospective protocol:

1. Target systems: human AChE PDB 4EY6 alone and AChE complexes labelled `alllhrc`, `fllhttr` and `ylsllqr`.
2. Topology default: GROMACS `amber99sb-ildn`; this is reported as the configured force field and is **not** described as identical to AMBER ff14SB.
3. Water and ions: TIP3P topology with `spc216.gro` coordinates; neutralization plus 0.15 mol/L NaCl.
4. Box: triclinic periodic box with a 1.0-nm solute-to-box distance.
5. Energy minimization: 2,000 steepest-descent steps; heavy-atom positional restraints configured at 1,255 kJ mol⁻¹ nm⁻².
6. Heating: 1.0-ns restrained NVT heating from 10 K to 300 K using velocity-rescale temperature coupling.
7. Equilibration: 1.0-ns restrained NPT followed by 1.0-ns unrestrained NPT at 300 K and 1 bar.
8. Production: 100 ns, 2-fs time step, hydrogen-bond constraints with LINCS, 1.2-nm real-space cutoffs, force-switched van der Waals interactions from 1.0 nm, PME electrostatics, velocity-rescale temperature coupling and Berendsen pressure coupling; coordinates every 20 ps, giving 5,000 planned frames.
9. Planned analysis: complex/AChE/peptide RMSD and RMSF, radius of gyration, SASA, RDF, DSSP-derived secondary structure, hydrogen bonds, residue contacts and bridging waters.

## Unresolved reproducibility fields

Before any trajectory result can be reported, the release must freeze and deposit:

- exact GROMACS version and hardware/software environment;
- the starting PDB files and their origin from the docking workflow;
- AChE chain, missing-residue and crystallographic-content decisions;
- peptide protonation, terminal states and chain identifiers;
- topology and coordinate hashes;
- actual terminal selections from `pdb2gmx`;
- random seeds and a biological/computational replicate plan;
- complete commands and standard output/error logs;
- TPR, XTC/TRR, EDR, LOG, CPT and final coordinate files;
- analysis index groups, selections, exclusion intervals and script versions.

The current MDP files use Berendsen pressure coupling during production and an unfixed generated velocity seed. These settings must be reported exactly if retained; any revised production ensemble, seed strategy or replicate design must be versioned prospectively rather than changed after inspecting outcomes.

## Manuscript reporting rule

The full English and Chinese manuscripts may include this protocol in Materials and Methods as a **prospective downstream computational protocol**. They must state that production-trajectory analysis is pending and must not add an MD Results subsection, stability claim, residue-contact claim, convergence claim or comparative ranking until the complete raw simulation package and prespecified analyses are available.
