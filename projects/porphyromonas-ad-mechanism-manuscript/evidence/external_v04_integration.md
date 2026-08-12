# External v0.4 repository integration record

Date reviewed: 2026-08-12

## Repository provenance

- Repository: `shaohuawen03-cyber/Auto-Empirical-Research-Skills`
- Branch: `arena/019ff3f9-auto-empirical-research-skills`
- Reviewed commit: `e28c06db0614512eeb2bca217d2f9a760e804051`
- User-designated project: `projects/1yzy-pg-ad-mechanism/`

| Reviewed artefact | SHA-256 |
| --- | --- |
| `manuscript/sci_v04_en.md` | `1fb810458373e7d0a95403394b4a05d4e0b4cb19c1ad95a8626023ca4110efad` |
| `manuscript/references.bib` | `3b1d55971f56587197de55c2f3175ac21cd2b0967e58ebe62f90d70164a1fafc` |
| `manuscript/figures/fig5_docking_scores.png` | `44c567ea8ec77e47f3ff690490e40b9474b07aa09f87508632ca8be89d249614` |
| `manuscript/figures/fig5_docking_scores.pdf` | `3c9212380f59addb71646c5d09a2881427f3414e3d48903f1b7c7946f7c0bca9` |
| `scripts/fig5_docking_scores.py` | `fa07a6a8b60bc54d7ecd972f1409e5d0baf6278183acb30a688731dc5236ef40` |

The screening counts and thresholds remain governed by the principal source in this repository. The external repository is a secondary, user-directed revision source, not a replacement for the principal evidence record.

## Accepted additions

1. A substantially expanded literature frame covering smORF discovery, AChE/PAS biology, metal dyshomeostasis, short neuroactive-peptide precedents, and the periodontitis–AD evidence boundary.
2. A twelve-sequence list reported by the external v0.4 manuscript as the main CHEL/FRS candidate set.
3. Twelve source-reported AutoDock Vina summary values (mean and SD) against PDB 4EY6.
4. Method labels reported by v0.4: AutoDock Vina 1.2.5, a 40 × 40 × 40 Å³ PAS-centred box, and PDB 4EY6.
5. Relevant, independently identifiable bibliography entries after removing duplicates, correction-note-only identifiers, and material outside the active scope.

Sequence composition, score ordering, score range, and summary arithmetic are deterministically rechecked in `revision_v3/external_docking_audit.json`.

## Not accepted as independently reproduced results

- No receptor/ligand input files, prepared PDBQT files, grid-centre coordinates, configuration files, commands, exhaustiveness, seeds, raw replicate scores, stdout/stderr logs, pose files, interaction tables, or environment lockfile were present in the reviewed project.
- Therefore, the docking was not rerun and its mean ± SD values remain **source-reported summaries**.
- Qualitative PAS/gorge contact statements in v0.4 are retained only as reported narrative, not as independently audited residue-level observations.
- The stated molecular-dynamics attempt lacks topology, coordinate, parameter, checkpoint, trajectory, energy, and log files. It is mentioned only as an unverified, excluded attempt and is not a result of the present reconstruction.
- Peptide-level Fisher/χ² tests in v0.4 were rejected because aggregate candidate counts are not independent donor-level observations.
- Disease-specific, taxon-specific, barrier-passing, binding, pathogenic, or mechanistic wording was rejected where the available evidence supports only cohort-branch prioritisation or model output.
- The two previously excluded unrelated files and their associated citation were not copied, cited, or used for background, methods, structure, figures, or quality claims.

## Manuscript reporting rule

The revised manuscript separates three levels:

- **principal-source aggregate screening results**;
- **externally reported sequence/docking summaries with explicit provenance limitations**;
- **future experimental or computational validation requirements**.

No sentence may collapse these levels into a claim of reproduced docking, measured affinity, demonstrated BBB transport, experimental neurotoxicity, taxonomic origin, or AD mechanism.
