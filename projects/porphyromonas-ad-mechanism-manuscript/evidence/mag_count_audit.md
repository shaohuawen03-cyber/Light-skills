# MAG-count audit and reporting hold

Audit date: 2026-08-17

## Question

Can the user-reported total of 296 high-quality metagenome-assembled genomes (MAGs) be independently recounted from the public accession records or the active manuscript repository?

## Checks performed

1. Queried the ENA Portal API for analyses under PRJEB65451 using the `analysis_accession`, `analysis_title`, and `submitted_ftp` fields.
2. Confirmed that the public records expose metagenome-assembly FASTA files associated with analysis accessions.
3. Searched the active manuscript project for a MAG/bin manifest, a bin directory, a bin-to-assembly or bin-to-sample map, and per-bin quality metrics such as completeness and contamination.
4. Rechecked the principal-source extraction, which records 296 high-quality MAGs as part of the supplied workflow description.
5. Recorded the user’s clarification that the value came from their raw-data mapping rather than from the public project description.

## Determination

A metagenome-assembly FASTA is not itself an auditable MAG inventory. The public ENA analysis records do not expose the bin boundaries, stable MAG identifiers, dereplication rule, completeness/contamination thresholds, or bin-quality table needed to reconstruct the reported total. The active manuscript repository likewise lacks recountable MAG files or a manifest.

Therefore:

- `296` is retained in the evidence ledger as a user-provided, raw-mapping-derived value;
- it is not rejected;
- it cannot yet be independently recounted from the materials available here;
- it is not reported in the v3.5.0 English or Chinese article body;
- participant and specimen totals are also omitted from those article bodies;
- a later release may report the total after a stable MAG manifest or recountable bin directory, source mapping, dereplication rule, and quality-control table are archived.

## Recountable minimum package

A valid recount requires at least:

- one stable identifier per MAG;
- the corresponding FASTA/bin file or checksum;
- source assembly and sample identifiers;
- binning and dereplication software, versions, commands, and thresholds;
- completeness and contamination estimates with tool/database versions;
- inclusion/exclusion flags;
- a deterministic script that counts retained unique MAG identifiers.
