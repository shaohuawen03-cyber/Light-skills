# Stage 4 — Academic Research Suite coordination / 学术研究套件全流程协调

Workflow: ARS Codex adapter → `academic-pipeline`, pinned in `SKILL_PROVENANCE.md`  
Status: active coordination record for Stages 1–9.

## 1. Research contract

**Article type:** Original Research Article, exploratory computational research.  
**Evidence unit:** Aggregate outputs transcribed from `材料与方法及结果_机制研究版.docx`.  
**Allowed analysis:** Deterministic arithmetic and descriptive funnel reconstruction.  
**Prohibited analysis:** Subject-level inference, peptide-level pseudoreplication, invented sequences/scores, causal AD claims.  
**Language:** Matched English–Chinese manuscript and submission package.  
**Target:** Realistic SCI submission, not a high-impact mechanistic claim.

## 2. Pipeline state

| Gate | Required artefact | Status | Integrity decision |
| --- | --- | --- | --- |
| Scope | `01_topic_brainstorming.md` | PASS | Aggregate-only route locked by user. |
| Search | `02_literature_search_and_novelty.md` | PASS with limitation | Targeted and current, not systematic/exhaustive; OpenAlex unavailable. |
| Synthesis | `03_literature_review_and_evidence_synthesis.md` | PASS | Claim–evidence matrix and counter-evidence included. |
| Source integrity | corrected corpus + exclusion record + 4/4 checksum | PASS | Mistakenly supplied unrelated files barred from all uses. |
| Citation integrity | verified DOI/PMID bibliography | PARTIAL | Core metadata checked; final Crossmark/retraction check remains author/pre-submission task. |
| Statistics | Stage-5 audit | READY | Descriptive only; no inferential tests. |
| Figures | Stage-6 programmatic figures | PENDING | Data lineage and caption boundaries required. |
| Writing | bilingual manuscript rebuild | PENDING | Evidence-first IMRaD rewrite, not surface polishing. |
| Final review | audit scripts and submission checklist | PENDING | Must distinguish technical readiness from missing author inputs. |

## 3. Evidence and artifact registry

| Artefact class | Authoritative location | Role |
| --- | --- | --- |
| Principal evidence | `source_materials/材料与方法及结果_机制研究版.docx` | Sole source of methods, counts and thresholds. |
| Principal source hash | `SHA256SUMS.txt` | File identity. |
| Context leads | two non-principal DOCX files | Search prompts/discussion leads only. |
| Excluded sources | `evidence/excluded_source_record.md` | Audit only; prohibited content. |
| Extracted source | `evidence/extracted/材料与方法及结果_机制研究版.md` and JSON | Searchable source transcription. |
| Literature | `references/verified_references.md` + Stage 2/3 reports | Claim support and boundary. |
| Arithmetic | `scripts/stage5_statistics_audit.py` + `revision_v2/statistics_audit.json` | Deterministic count/percentage audit. |
| Manuscripts | `manuscript/manuscript_en.md`, `manuscript_zh.md`, `manuscript_bilingual.md` | Human-readable scientific content. |
| Delivery DOCX | generated from bilingual Markdown | Submission-editable format; subject to rebuild after rewrite. |

## 4. Claim integrity gates

Every Results statement must satisfy all applicable gates:

1. Traceable to the principal DOCX or deterministic arithmetic.
2. Uses a visible denominator.
3. Distinguishes model eligibility, positivity and non-evaluation.
4. Avoids disease specificity unless sequence/sample exclusivity exists (it does not).
5. Labels the 111→15→12→8 chain as source reported.
6. Does not infer biological independence from candidate counts.
7. Does not transform “predicted” into “demonstrated.”

Every Discussion statement must be tagged conceptually as one of:

- present aggregate observation;
- literature-supported context;
- interpretation;
- limitation;
- future test.

## 5. Full-process decisions

### Decision D1 — no synthetic statistics

The paper will not add p values, confidence intervals, odds ratios or machine-learning performance metrics that cannot be calculated with a valid experimental unit.

### Decision D2 — no invented reproducibility

The package will state that original analysis code, model logs, sequences and row-level outputs were not supplied. Repository scripts reproduce only extraction, arithmetic, figures and document assembly.

### Decision D3 — no “mechanism” title

The title will describe evidence-bounded prioritisation. AD is a contested motivation and downstream hypothesis only.

### Decision D4 — programme-generated scientific graphics

Data/evidence figures will be generated from explicit aggregate values with scripts. No generative image model is used for scientific content.

### Decision D5 — technically ready versus scientifically complete

Stage 9 may produce a technically organised submission package, but it must preserve a blocker list. Missing author identities, approvals/declarations, candidate sequences, original code and journal selection cannot be fabricated.

## 6. Handoff to Stage 5

Statistics will audit internal consistency and descriptive quantities only. The analysis population is the source-reported candidate set; the biological experimental unit would be the participant/sample, but its row-level outcomes are unavailable.
