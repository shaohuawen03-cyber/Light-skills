# 基于来源边界的牙周炎队列口腔微肽多模型优选

## 项目定位

本项目以`source_materials/材料与方法及结果_机制研究版.docx`为**主要筛选结果来源**，并按用户要求整合指定外部v0.4项目中的12条序列和AChE对接汇总。两类结果始终分层报告：主要来源定义筛选漏斗；外部记录仅提供“来源报告”的序列/分数，不能追溯填补逐行筛选数据，也不代表已独立复现对接。

项目维护一套中英文分节对照的原创研究型SCI科学内容包。研究定位为**汇总层面、保留来源边界的描述性计算优选与假设生成**。不声称牙周炎特异性、当前队列表达、特定微生物来源、实测BBB转运/毒性/金属结合、经验证的AChE结合、完成的MD、AD机制或因果关系。

误传且无关的材料已从活动语料、参考文献、图形和质量主张中删除；其身份和原始哈希仅保留在专用排除记录中供审计。

## 主要交付物

- `VERSION_HISTORY.md` — 各版稿件、精确Git检查点、标签及安全恢复命令的唯一版本台账。
- `scripts/manage_version_tag.py` — 创建和核验不可覆盖annotated tag的跨平台脚本。
- `manuscript/manuscript_en.md`、`manuscript_zh.md` — 扩展英文稿与平行中文稿。
- `manuscript/concise/English.docx`、`Chinese.docx` — v3.2.0精简SCI稿，英文和中文独立成卷；无页眉、页脚或页码域。
- `manuscript/manuscript_bilingual.md`、`.docx` — 分节对照双语完整主稿及Word包。
- `manuscript/supplementary_tables_bilingual.md`、`.docx` — S1–S6双语补充表。
- `manuscript/figures/` — 三幅活动主图的SVG/PNG；外部对接PDF仅作来源存档。
- `submission/` — 期刊定位、预投稿询问、投稿信模板、标题页、Highlights及就绪清单。
- `revision_v2/` — 聚合材料九阶段科学重建记录。
- `revision_v3/01_*.md`至`09_*.md` — 外部v0.4整合后的九阶段工作流记录。

## 证据与参考文献

- `evidence/source_understanding_and_scope.md` — 主要来源理解和范围。
- `evidence/external_v04_integration.md` — 外部提交身份、文件哈希、接纳/拒绝决策及报告规则。
- `evidence/prjna678453_prjeb65451_provenance.md` — PRJNA678453来源队列与PRJEB65451衍生TPA组装关系核验。
- `evidence/prediction_tool_methods.md` — UniDL4BioPep及下游预测工具的算法和版本边界核验。
- `evidence/claim_evidence_ledger.md` — 主张—证据—措辞边界。
- `references/verified_references.md` — 53条记录级整理文献及分组使用边界。
- `references/references.bib` — 与英文/中文DOI清单一致的53条BibTeX。
- `revision_v2/statistics_audit.json` — 主要来源汇总算术审计。
- `revision_v3/external_docking_audit.json` — 外部序列组成与分数转录审计。
- `ARTIFACT_SHA256SUMS.txt` — 项目产物相对路径哈希。
- `quality_reports/repository_inventory.json` — 项目树文件大小与SHA-256清单。

## 当前科学结论

- 主要来源支持从原始smORF到证据过滤、BBB高分、NTxPred2和CHEL/FRS计数的描述性漏斗。
- 外部v0.4报告12条互不重复的7–9 aa序列；其组成可由字符串独立重算。
- 外部报告针对人AChE PDB 4EY6的Vina均值为−9.60至−8.25 kcal/mol，SD为0.04至0.12；数值可核验转录与排序，但因缺少输入、配置、日志和构象而不能复现对接。
- 经核验，PRJNA678453来源队列为11名口腔健康对照和11名牙周炎患者，共66份口腔标本；PRJEB65451是该项目经metaSPAdes v3.15.3构建的衍生TPA组装资源，而非另一临床队列。
- UniDL4BioPep、NTxPred2、mebipred和AnOxPePred采用的算法并不相同，不能统称为同一深度学习流程。
- 候选计数不是独立生物学重复，故不进行肽层面的健康—牙周炎推断检验。
- 序列与主要来源逐行链路、严格8/12成员、表达/暴露/表型/机制仍未解决。

## 原始材料保护与哈希验证

`source_materials/`中的原始DOCX/PDF不被覆盖。使用：

```bash
python3 scripts/verify_source_checksums.py
```

## 可重复构建与审计

```bash
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py
python3 scripts/generate_funnel_figure.py
python3 scripts/generate_docking_score_figure.py
python3 scripts/generate_evidence_ladder.py
python3 scripts/build_bilingual_markdown.py
python3 scripts/audit_manuscript_consistency.py > quality_reports/manuscript_consistency.json
python3 scripts/audit_language_structure.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_manuscript_word_counts.py
python3 scripts/audit_text_quality.py

python3 scripts/build_docx_stdlib.py \
  --input manuscript/manuscript_bilingual.md \
  --output manuscript/manuscript_bilingual.docx \
  --title "Provenance-Aware Multi-Model Prioritization / 基于来源边界的口腔微肽多模型优选"

python3 scripts/build_docx_stdlib.py \
  --input manuscript/supplementary_tables_bilingual.md \
  --output manuscript/supplementary_tables_bilingual.docx \
  --title "Bilingual supplementary tables / 中英文补充表"

python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-14T00:00:00Z \
  --input manuscript/concise/English.md \
  --output manuscript/concise/English.docx \
  --title "Aggregate Prioritization of Oral Micropeptides at the Periodontitis–Alzheimer’s Disease Interface"

python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-14T00:00:00Z \
  --input manuscript/concise/Chinese.md \
  --output manuscript/concise/Chinese.docx \
  --title "牙周炎—阿尔茨海默病界面口腔微肽的汇总优选"

python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
```

质量审计、文档包检查、哈希和清单须在任何内容修改后重跑。当前环境无法进行Word/LibreOffice逐页渲染；DOCX包审计不能替代作者的人工版式检查。

## 投稿边界

扩展稿可交责任作者审核，也可在作者补齐信息并批准后用于坦诚的预投稿询问；不代表保证满足目标期刊要求。正式投稿前必须完成作者/单位/伦理/经费/利益冲突/CRediT/AI声明、期刊格式和文献Crossmark检查，并由编辑判断逐行筛选链路与原始对接产物缺失是否可接受。科学上仍需恢复来源链路、复现对接并开展表达、BBB、毒理、金属及AChE/Aβ实验。
