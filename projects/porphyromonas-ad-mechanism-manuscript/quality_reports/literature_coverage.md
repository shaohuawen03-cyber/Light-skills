# Literature coverage and verification report — revision v3

Date: 2026-08-12

## Scope

This was a targeted, identifier-driven evidence search for an original computational manuscript, not a systematic review. The final 53-reference corpus covers:

1. microbiome smORF discovery, annotation, translation and multi-omics detection;
2. oral metagenomics/metatranscriptomics, HOMD/eHOMD and metaproteomics;
3. UniDL4BioPep, BBB-peptide prediction, NTxPred2, mebipred and AnOxPePred;
4. AD overview, cholinergic biology, human AChE structures, PAS and AChE–Aβ studies;
5. metal dyshomeostasis, Cu–tau/Aβ chemistry and short neuroactive peptides;
6. periodontitis–AD observational evidence, Mendelian-randomization counterevidence and current primers;
7. organism-specific virulence/vesicle studies used only as bounded context;
8. AutoDock Vina interpretation and flexible peptide-docking methods.

## Curation approach

The prior active corpus and user-designated external v0.4 bibliography were reviewed record by record. Duplicate entries, an erroneous correction-note identifier, material associated only with excluded sources, and references unused by the revised argument were omitted. The canonical inventory is in `references/verified_references.md`; 53 BibTeX entries are in `references/references.bib`.

DOI inventory parity is deterministic and currently passes across English, Chinese, the verification record and BibTeX. This is not a certificate that all publications are free from later correction, expression of concern or retraction. Accountable authors must repeat DOI resolution and Crossmark/retraction checks immediately before submission.

## Coverage achieved

- Current smORF literature supports the distinction among prediction, translation, proteomic detection and function.
- Oral-omics literature supports the need for subject/sample provenance and limits exact-match interpretation across heterogeneous resources.
- Predictor papers support tool identity but not calibration or biological validation in the current candidate domain.
- AChE/PAS literature supports a structural question without transferring binding or Aβ-modulating activity to the current sequences.
- Metal/tau/curli studies provide experimental precedents without serving as analogical proof.
- Periodontitis–AD framing now balances observational association with Mendelian-randomization counterevidence.
- Vina/FlexPepDock literature supports explicit requirements for docking interpretation and reproduction.

## Unresolved items

1. PRJEB65451 remains unresolved in this drafting environment.
2. Principal-source candidate rows, sample mappings, spectra, taxonomy and model-run provenance remain absent.
3. The external twelve strings cannot be linked to the principal screening rows or stricter eight.
4. External docking inputs, exact configuration, seeds, raw runs, logs and poses remain absent.
5. The long-branch evidence class and NTxPred2→mebipred handoff require clarification.
6. Final publication-integrity status and exact 2026 pagination require author verification.

## Bias and completeness

The search was purposive rather than PRISMA-compliant. It may omit negative results, non-English studies, newly indexed work and corrections. The corpus is sufficient for a conservative original-article Introduction and Discussion; it cannot upgrade aggregate/model outputs or source-reported docking summaries into mechanistic, causal, taxonomic or experimental findings.
