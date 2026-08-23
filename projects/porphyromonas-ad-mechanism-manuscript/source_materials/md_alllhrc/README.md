# ALLLHRC–AChE MD source snapshot

This directory preserves the two small RMSD-support files used for the standalone ALLLHRC–AChE manuscript package.

## User-designated source

- Local source named by the user: `F:\0wsh\asd\gromacs_md\md_alllhrc`
- System assigned by the user: ALLLHRC–AChE complex
- Primary display: the six-panel image attached with the request
- User-selected DOCX treatment: the display is evidence for interpretation but is not embedded in any manuscript

## Repository mirror used for the numeric RMSD diagnostic

- Repository: `shaohuawen03-cyber/asd`
- Branch: `arena/019ff90e-asd`
- Commit: `f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`
- Upstream paths:
  - `gromacs_md/md_alllhrc/digitized_rmsd_100ns.csv`
  - `gromacs_md/md_alllhrc/peptide_rmsd_jump_diagnosis.txt`

The CSV is a digitized trace, not a raw GROMACS XVG or coordinate trajectory. The diagnostic statistics are therefore reported in the manuscripts as descriptive estimates and not as a replacement for reanalysis from TPR/XTC/EDR inputs.

## Identity and plotting discrepancy

The user explicitly identifies the system as ALLLHRC–AChE, and the directory name agrees. The attached plot retains an inherited `AChE-Aβ` title. The manuscripts disclose this mismatch and do not transfer Aβ sequence identity, contact residues, residence regions, or biological mechanisms to ALLLHRC. Matching topology, trajectory, coordinate hashes, and an updated source plot are required for final identity acceptance.
