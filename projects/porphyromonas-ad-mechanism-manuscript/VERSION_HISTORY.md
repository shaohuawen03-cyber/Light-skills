# Manuscript version history / 稿件版本记录

> Purpose: maintain one authoritative index of every material manuscript revision, its Git checkpoint, evidence status, deliverables, and recovery method.  
> 用途：以单一权威文件记录每次实质性稿件版本、Git检查点、证据状态、交付物和恢复方法。

## 1. Versioning convention / 版本规则

Tag pattern / 标签格式：

```text
porphyromonas-ad-manuscript-vMAJOR.MINOR.PATCH
```

- **MAJOR / 主版本：** evidence architecture, research question, or manuscript structure changes materially. / 证据架构、研究问题或全文结构发生实质改变。
- **MINOR / 次版本：** new analyses, figures, references, submission documents, or evidence-controlled external integration. / 新增分析、图件、文献、投稿材料或受控外部整合。
- **PATCH / 修订版本：** wording, translation, formatting, metadata, or non-substantive corrections. / 措辞、翻译、格式、元数据或非实质性修正。

Rules / 规则：

1. Update this file before creating a release tag. / 创建标签前先更新本文件。
2. Use annotated tags and push them explicitly. / 使用带说明的annotated tag并显式推送。
3. Never move, overwrite, or reuse an existing release tag. / 不移动、不覆盖、不复用既有版本标签。
4. A tag freezes a recoverable project snapshot; later edits require a new version. / 标签冻结可恢复快照，后续修改必须使用新版本。
5. Manuscript version numbers are independent of the external repository’s “v0.4” label. / 本稿版本号与外部仓库“v0.4”标签相互独立。

## 2. Version ledger / 版本台账

| Manuscript version | Date | Git checkpoint | Release tag | Status | Main content |
| --- | --- | --- | --- | --- | --- |
| **v0.1.0 — source intake** | 2026-08-12 | `f6a020a5c98b243b13963a8de83cd859f52e132d` | Untagged historical checkpoint | Superseded | Initial project materials entered Git management. / 初始研究材料纳入Git管理。 |
| **v0.2.0 — source parsing** | 2026-08-12 | `956210917503cfd2f521c80feeb4eb9aecbf8028` | Untagged historical checkpoint | Superseded | Principal documents parsed and source provenance registered. / 解析主要文档并登记来源。 |
| **v1.0.0 — first bilingual draft** | 2026-08-12 | `1fd8ab3bdf616fd1ab7b0e70d7c71046fb43da58` | Untagged historical checkpoint | Superseded | First English–Chinese SCI draft and initial quality review. / 首版中英文SCI稿与质量检查。 |
| **v2.0.0 — nine-stage aggregate rebuild** | 2026-08-12 | `a31d29466dc8d376d6012abd916152eb82e017f1` | Untagged historical checkpoint | Superseded | Nine-stage reconstruction, 25-reference corpus, aggregate-only evidence boundary, figures, DOCX and submission package. / 九阶段重建、25条文献、汇总证据边界、图件、DOCX及投稿包。 |
| **v3.0.0 — external-v0.4 evidence integration** | 2026-08-12 | Manuscript content commit `2a7573604b6e12bd1d51b897d52c58f0d9ead077`; release-management commit `012d0cbcd3c45a26aed0adf9ba9bce2f70e4844b` | `porphyromonas-ad-manuscript-v3.0.0` | **Frozen prior full release** | Expanded 53-reference parallel manuscript; twelve externally reported sequences; independently recomputed composition; source-reported AChE docking summary; three figures; six supplementary tables; revision-v3 workflow, provenance controls and deterministic audits. / 扩展至53条文献；整合12条外部报告序列、组成审计、来源报告AChE对接汇总、三幅主图、六个补充表、revision-v3工作流及确定性审计。 |
| **v3.1.0 — initial concise package** | 2026-08-14 | `ef8493c8d26f31fefef6ad6e79ca31a412d4af0a` | `porphyromonas-ad-manuscript-v3.1.0` | **Frozen prior concise release** | Added separate short English and Chinese SCI-style DOCX files with two tables, one figure and 20 selected references. / 新增英文、中文独立DOCX精简稿，保留两表、一图和20条精选文献。 |
| **v3.2.0 — provenance-verified clean concise package** | 2026-08-14 | `273e352a5b92620df66e482b30fbd759472fad8b` | `porphyromonas-ad-manuscript-v3.2.0` | **Frozen prior concise release** | Renamed deliverables to `English.docx` and `Chinese.docx`; removed headers, footers, page-number fields and workflow metadata; rebuilt the AD–*P. gingivalis* Introduction; documented predictor algorithms; and corrected the PRJNA678453/PRJEB65451 provenance to 11 healthy plus 11 periodontitis participants and 66 specimens. / 采用中性文件名，删除页眉页脚页码及流程元数据，重构AD—*P. gingivalis*引言，补充预测算法，并核正来源队列为11名健康对照、11名牙周炎患者及66份标本。 |
| **v3.3.0 — SCI-style Introduction and deep-learning-guided Methods** | 2026-08-14 | `e8c16c630d658424e8656ea89aa1c9c52cc33966` | `porphyromonas-ad-manuscript-v3.3.0` | **Frozen prior concise release** | Rewrote the Introduction with individually bracketed references [1]–[10]; reorganized Methods into conventional SCI subsections; and emphasized the relevant deep-learning peptide modes—ESM-2/CNN, fine-tuned ESM2-t30 and multi-task 1D CNN—while retaining the neural-network and evidence boundaries. / 引言采用[1]–[10]逐篇独立引用；方法按SCI结构重组；突出ESM-2/CNN、微调ESM2-t30和多任务一维CNN等肽分析深度学习模式，同时保留神经网络及证据边界。 |
| **v3.4.0 — separate provenance-corrected full manuscripts** | 2026-08-17 | `918f7f9abf531c467b83a409ba5ccd4e86cd4c76` | `porphyromonas-ad-manuscript-v3.4.0` | **Frozen prior full release** | Added separate neutral `English.docx` and `Chinese.docx` full manuscripts with abstract, AD-first Introduction, complete Methods/Results/Discussion/Conclusions, declarations, four tables, three figures, and 53 verified references; carried forward the corrected PRJNA678453/PRJEB65451 provenance and model-specific architecture descriptions; removed headers, footers, page fields, draft notes, purpose-facing text, and the unsupported cohort/assembly summary. / 新增中性命名的独立英文、中文完整稿，含摘要、AD起始引言、完整方法/结果/讨论/结论、声明、四表、三图和53条核验文献；继承来源与模型架构修正，并删除页眉、页脚、页码域、草稿说明、用途性文字及无依据的队列/组装汇总。 |
| **v3.5.0 — review-grade Introduction and prospective MD methods** | 2026-08-17 | The annotated tag resolves the final v3.5.0 release commit | `porphyromonas-ad-manuscript-v3.5.0` | **Frozen prior full release** | Replaced the abstract with a concise high-impact-SCI narrative; expanded the Introduction through evidence-class synthesis; omitted participant, specimen, assembly-analysis and MAG totals from the article bodies; registered the user-derived 296-MAG value as pending audit; added a versioned prospective 100-ns GROMACS protocol without MD results; hid the visible article title; retained no headers, footers, page fields or comments; and audited editable-text SVG sources. / 采用高水平SCI叙事摘要和证据综合型扩展引言；正文省略参与者、标本、组装分析和MAG总数；将用户原始映射所得296个MAG登记为待审计；新增版本化100 ns GROMACS前瞻性方案但不加入MD结果；隐藏正文标题并保持无页眉、页脚、页码和批注；审计可编辑文字SVG。 |
| **v3.6.0 — clean full and concise submission variants** | 2026-08-17 | The annotated tag resolves the final v3.6.0 release commit | `porphyromonas-ad-manuscript-v3.6.0` | **Frozen prior release** | Rebuilt complete and concise English/Chinese manuscripts; converted every table to a three-line structure; removed figures from all four DOCX files; ended each article at Conclusion followed directly by References; removed evidence-tier, hash, commit, archive, acceptance and workflow-governance prose from article bodies; and converted source citations to Pandoc/BibTeX keys with an explicit Better BibTeX/Word acceptance gate. / 重建完整与精简中英文稿；全部表格改为三线表；四份DOCX移除所有图像；结论后直接进入参考文献；正文删除证据分层、哈希、提交、归档、接纳和工作流治理表述；正文引文改为Pandoc/BibTeX键，并设置明确的Better BibTeX/Word验收门。 |
| **v3.7.0 — journal-aligned manuscripts and expanded concise variants** | 2026-08-17 | The annotated tag resolves the final v3.7.0 release commit | `porphyromonas-ad-manuscript-v3.7.0` | **Frozen prior release** | Reframed the ongoing MD work as a pending analysis extension whose trajectory measurements will be integrated after completion; removed “no MD result” wording; expanded the concise English body by approximately 74% with synchronized Chinese content; adopted structured abstracts, unnumbered IMRaD headings, 12-point Times New Roman, double spacing and one-inch margins; retained figure-free DOCX files, three-line tables and Conclusion-to-References order. / 将MD表述修正为正在进行、完成后补充轨迹指标的分析扩展，删除“不报告MD结果”措辞；精简英文正文扩展约74%并同步中文；采用结构式摘要、无编号IMRaD标题、12磅Times New Roman、双倍行距和1英寸页边距；继续保持DOCX无图、三线表及结论后直接进入参考文献。 |
| **v3.8.0 — single-paragraph abstracts and simplified article ending** | 2026-08-17 | The annotated tag resolves the final v3.8.0 release commit | `porphyromonas-ad-manuscript-v3.8.0` | **Current full and concise release** | Converted all four abstracts to one unlabelled paragraph and removed their Conclusions components; removed the Statistical analysis subsection and standalone Conclusion section; made Discussion proceed directly to References; added a 480-twip first-line indent to ordinary main-text paragraphs while retaining unindented abstracts and non-body elements; preserved synchronized science, ongoing-MD language, figure-free DOCX files and three-line tables. / 四稿摘要改为单段无标签形式并删除摘要结论内容；删除“统计分析”小节和独立“结论”章节，使讨论后直接进入参考文献；正文普通段落增加480 twip首行缩进，摘要及非正文元素保持顶格；继续保持中英文科学同步、MD正在分析、DOCX无图和三线表。 |

## 3. Scientific status and package relationship / 科学状态与版本关系

**v3.0.0–v3.8.0 full manuscripts support / 完整稿可支持：**

- principal-source aggregate funnel and recomputed descriptive percentages;
- twelve externally reported 7–9-aa sequence strings and independently recomputed composition;
- externally reported Vina mean±SD ordering against human AChE PDB 4EY6;
- a versioned 100-ns GROMACS extension whose trajectory analysis is ongoing and whose measurements await completion and quality control;
- a provenance-aware, hypothesis-generating validation roadmap.

**v3.0.0–v3.8.0 do not support / 不支持：**

- row-level linkage between the twelve strings and the principal screening funnel or stricter eight;
- independently reproduced docking, verified poses/contacts, affinity, free energy, or completed molecular dynamics;
- measured expression, BBB transport, toxicity, metal chemistry, AChE/Aβ function, disease specificity, or AD causality.

**v3.1.0–v3.3.0 relationship / 精简稿关系：** v3.1.0 and v3.2.0 are frozen prior concise packages. v3.3.0 superseded them after SCI-structure revision and is now itself frozen after v3.6.0; none of these versions strengthens the underlying evidence. / v3.1.0和v3.2.0为冻结的既往精简稿；v3.3.0曾在SCI结构修订后取代它们，现也已被v3.6.0冻结；这些版本均不提高底层证据强度。

**v3.5.0 full-package relationship / 完整稿关系：** v3.5.0 superseded v3.4.0 as the prior full release. Its historical deliverables remain frozen. / v3.5.0曾取代v3.4.0成为上一版完整稿，其历史交付物保持冻结。

**v3.8.0 package relationship / 当前版本关系：** v3.8.0 supersedes v3.7.0 as the current release for both full and expanded concise variants. The four current deliverables are the separate English and Chinese DOCX files under `manuscript/full/` and `manuscript/concise/`; historical bilingual manuscripts, supplementary files and figures are not v3.8.0 manuscript deliverables. / v3.8.0取代v3.7.0，成为完整稿与扩展精简稿的当前版本；当前交付物仅为`manuscript/full/`和`manuscript/concise/`下的四份独立中英文DOCX，历史双语稿、补充文件和图件不属于v3.8.0稿件交付。

**v3.2.0 provenance correction / v3.2.0来源修正：** PRJNA678453 is reported as a 22-participant cohort (11 orally healthy and 11 with periodontitis) producing 66 oral specimens; PRJEB65451 is reported as the derived EBI-EMG/MGnify TPA assembly project. / PRJNA678453按22名参与者（11名口腔健康、11名牙周炎）和66份口腔标本报告；PRJEB65451按衍生TPA组装项目报告。

**v3.3.0 scientific-writing correction / v3.3.0科学写作修正：** Introduction references [1]–[10] are cited one paper per bracket. Methods emphasize the relevant deep-learning peptide modes and retain the absence of row-level model, lineage and docking inputs as a reproducibility limitation. / 引言文献[1]–[10]采用每个括号一篇文献；方法突出与肽分析相关的深度学习模式，并继续把逐行模型输出、来源链和对接输入缺失列为可重复性局限。

**v3.4.0 historical carry-forward / v3.4.0历史修正：** The frozen v3.4.0 English and Chinese manuscripts report the then-adopted public-cohort counts and distinguish UniDL4BioPep, NTxPred2 peptide mode, mebipred, and AnOxPePred by their documented architectures. Introduction citation brackets contain one reference each. / 冻结的v3.4.0中英文稿保留当时采用的公共队列数量，按文献架构区分四类预测工具，且引言每个引文括号仅含一篇文献。

**v3.5.0 reporting and MD boundary / v3.5.0数量与MD边界：** The current article bodies omit all participant, specimen, assembly-analysis and MAG totals. The user-derived 296-MAG value is held in the evidence ledger pending a recountable manifest. A prospective GROMACS protocol is described from the referenced repository at commit `f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`, but incomplete trajectory artefacts are excluded and no MD result is reported. / 当前正文省略参与者、标本、组装分析和MAG总数；用户原始映射所得296个MAG在证据台账中暂存，等待可重计清单；方法引用指定仓库提交中的前瞻性GROMACS方案，但排除未完成轨迹产物，不报告MD结果。

## 4. Create and push the current tag / 创建并推送本次标签

The repository includes a guarded cross-platform helper: / 仓库提供带保护检查的跨平台脚本：

```bash
python3 scripts/manage_version_tag.py create \
  --version 3.8.0 \
  --message "v3.8.0: single-paragraph abstracts, simplified endings, and indented body text" \
  --push
```

Equivalent native Git commands / 等价Git命令：

```bash
git status --short
git tag -a porphyromonas-ad-manuscript-v3.8.0 \
  -m "v3.8.0: single-paragraph abstracts, simplified endings, and indented body text"
git push origin refs/tags/porphyromonas-ad-manuscript-v3.8.0
```

The helper refuses to tag a dirty working tree, the wrong branch, or an existing tag. / 脚本会拒绝脏工作区、错误分支或重复标签。

## 5. Verify a tag / 核验标签

```bash
python3 scripts/manage_version_tag.py verify --version 3.8.0
git show --no-patch --decorate porphyromonas-ad-manuscript-v3.8.0
git rev-list -n 1 porphyromonas-ad-manuscript-v3.8.0

# Earlier immutable baselines remain independently verifiable:
python3 scripts/manage_version_tag.py verify --version 3.7.0
python3 scripts/manage_version_tag.py verify --version 3.6.0
python3 scripts/manage_version_tag.py verify --version 3.5.0
python3 scripts/manage_version_tag.py verify --version 3.2.0
python3 scripts/manage_version_tag.py verify --version 3.1.0
python3 scripts/manage_version_tag.py verify --version 3.0.0
```

## 6. Safe recovery / 安全恢复

### 6.1 Inspect the tagged release without changing the active checkout

Recommended: create a separate worktree. / 推荐创建独立worktree，不改变当前工作目录：

```powershell
Set-Location 'E:\0writing\Light-skills'
git fetch origin --tags
git worktree add 'E:\0writing\Light-skills-restore-v3.8.0' porphyromonas-ad-manuscript-v3.8.0

# To inspect an earlier immutable baseline instead:
git worktree add 'E:\0writing\Light-skills-restore-v3.4.0' porphyromonas-ad-manuscript-v3.4.0
git worktree add 'E:\0writing\Light-skills-restore-v3.3.0' porphyromonas-ad-manuscript-v3.3.0
git worktree add 'E:\0writing\Light-skills-restore-v3.2.0' porphyromonas-ad-manuscript-v3.2.0
git worktree add 'E:\0writing\Light-skills-restore-v3.1.0' porphyromonas-ad-manuscript-v3.1.0
git worktree add 'E:\0writing\Light-skills-restore-v3.0.0' porphyromonas-ad-manuscript-v3.0.0
```

Remove it after inspection / 检查后移除：

```powershell
git worktree remove 'E:\0writing\Light-skills-restore-v3.8.0'
# Or remove an earlier baseline worktree if one was created:
git worktree remove 'E:\0writing\Light-skills-restore-v3.4.0'
git worktree remove 'E:\0writing\Light-skills-restore-v3.3.0'
git worktree remove 'E:\0writing\Light-skills-restore-v3.2.0'
git worktree remove 'E:\0writing\Light-skills-restore-v3.1.0'
git worktree remove 'E:\0writing\Light-skills-restore-v3.0.0'
```

### 6.2 Restore one file from the tag

```bash
git restore --source=porphyromonas-ad-manuscript-v3.8.0 -- \
  projects/porphyromonas-ad-mechanism-manuscript/manuscript/full/English.docx
```

Review the diff before committing the restored file. / 提交恢复文件前先检查差异。

### 6.3 Compare the current branch with v3.0.0

```bash
git fetch origin --tags
git diff --stat porphyromonas-ad-manuscript-v3.0.0..arena/019ff377-light-skills
git diff porphyromonas-ad-manuscript-v3.0.0..arena/019ff377-light-skills -- \
  projects/porphyromonas-ad-mechanism-manuscript/
```

### 6.4 Recover an older untagged historical version

Use a separate worktree with the exact checkpoint, for example v2.0.0: / 使用精确提交在独立worktree中恢复，例如v2.0.0：

```powershell
git worktree add 'E:\0writing\Light-skills-restore-v2.0.0' a31d29466dc8d376d6012abd916152eb82e017f1
```

Do not use `git reset --hard` for routine recovery; it can discard uncommitted work. / 常规恢复不要使用`git reset --hard`，以免丢失未提交内容。

## 7. Template for the next version / 下一版本记录模板

Copy one row into the ledger and complete: / 在台账中复制一行并补齐：

```text
Version:
Date:
Scientific change:
Evidence added or removed:
Files changed:
Audits and verdicts:
Known limitations:
Content commit:
Release tag:
Push verification:
```
