# Concise manuscript package quality summary / 精简稿件包质量汇总

Date: 2026-08-14
Version: v3.2.0

## Deliverables

- Separate English DOCX: `manuscript/concise/English.docx`
- Separate Chinese DOCX: `manuscript/concise/Chinese.docx`
- Version-controlled sources: `English.md` and `Chinese.md`

## Scientific revisions

- Reconstructed the Introduction in the sequence AD → *Porphyromonas gingivalis* → plausible periodontal–AD routes → unresolved mechanism → present exploratory study.
- Distinguished the 22-participant PRJNA678453 source cohort (11 orally healthy, 11 periodontitis; 66 oral specimens) from the derived EBI-EMG/MGnify TPA assembly project PRJEB65451.
- Rejected the unsubstantiated 24-control/26-periodontitis/296-MAG statement for this accession chain.
- Added concise, algorithm-specific descriptions of UniDL4BioPep, NTxPred2, mebipred and AnOxPePred without treating all predictors as one deep-learning method.
- Preserved all aggregate counts, the separate twelve-sequence record, source-reported docking boundary and non-causal interpretation.

## Package checks

- Neutral file and directory names; old purpose-revealing filenames absent: PASS.
- English/Chinese top-level structure and 20-reference DOI parity: PASS.
- Locked counts, sequence endpoints and score ranges present in both languages: PASS.
- Verified accession and algorithm-method terms present in both languages: PASS.
- Configured administrative wording, prohibited overclaims and gap markers absent from both manuscripts: PASS.
- Separate DOCX ZIP CRC, XML relationships, expected text, two tables, one drawing and one embedded image each: PASS.
- Header parts, footer parts, page-number fields, automatic section page breaks and workflow metadata absent from both DOCX files: PASS.
- Fixed core timestamp and stable ZIP metadata produced byte-identical DOCX SHA-256 hashes across consecutive rebuilds: PASS.

## Boundary

The audits verify deterministic transcription, package structure and configured scientific boundaries. They do not reproduce the original smORF screen, model inference or docking. Page-level Word/LibreOffice visual inspection remains an author task because no canonical Office renderer is installed in the build environment.
