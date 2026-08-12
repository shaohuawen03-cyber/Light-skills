# 牙周炎队列口腔微肽的证据约束型多模型优先排序

## 项目定位

本项目以 `source_materials/材料与方法及结果_机制研究版.docx` 为唯一结果证据源，维护一套中英文分节对照的原创研究型 SCI 科学内容包。研究定位为**聚合层面的描述性计算优先排序与审计**，不声称已证明疾病特异性、候选实验活性、牙龈卟啉单胞菌来源、神经退行性机制或因果关系。

两份误传且无关的文件已从活动语料、提取物、参考文献、图形和校验清单中删除；其身份和原始哈希仅保留在 `evidence/excluded_source_record.md` 供审计。

## 主要交付物

- `manuscript/manuscript_bilingual.docx` — 中英文分节对照主稿。
- `manuscript/manuscript_bilingual.md` — 可追踪、可重建的双语源稿。
- `manuscript/manuscript_en.md`、`manuscript/manuscript_zh.md` — 英文、中文完整稿。
- `manuscript/supplementary_tables_bilingual.docx`、`.md` — 双语补充表。
- `manuscript/figures/` — 两幅主图的 SVG 与 PNG。
- `submission/` — 期刊定位、预投稿询问、投稿信模板、标题页、Highlights 和就绪清单。
- `revision_v2/01_*.md` 至 `09_*.md` — 九阶段科学工作流记录。

## 证据与参考文献

- `evidence/source_understanding_and_scope.md` — 来源理解、范围和禁用外推。
- `evidence/claim_evidence_ledger.md` — 主张—证据—措辞边界。
- `evidence/extracted/` — 三份范围内 DOCX 的标准库提取文本和结构 JSON。
- `references/verified_references.md` — 25 条参考文献的核验元数据和 claim-use 边界。
- `references/references.bib` — 与两种语言稿件 DOI 集合一致的 BibTeX。
- `revision_v2/statistics_audit.json` — 聚合算术审计；`all_checks_pass=true`。
- `ARTIFACT_SHA256SUMS.txt` — 项目产物（不含原始材料和自引用清单）的相对路径哈希。
- `quality_reports/repository_inventory.json` — 完整项目树的文件大小与 SHA-256 清单（仅排除自身）。

## 当前质量结论

详见 `quality_reports/quality_summary.md`。当前确定性结果包括：

- 4/4 范围内原始文件哈希通过；
- 中英文核心数值、禁用主张、占位符和参考文献序号检查通过；
- 两种语言均在参考文献表前引用 1–25，结构均为八个顶层章节；
- 英文、中文、核验记录和 BibTeX 的 25 个 DOI 集合一致；
- 两种语言的 final-mode draft lint 均无 FAIL；
- 主稿与补充材料 DOCX 的 ZIP CRC、XML、内部关系、预期正文 token、表格和媒体结构检查通过；
- 当前环境无 Office/LibreOffice/PDF 渲染器，**未完成逐页视觉审阅或验证 PDF 导出**。

## 原始材料保护与哈希验证

`source_materials/` 中的原始 DOCX/PDF 不被覆盖。`SHA256SUMS.txt` 保留用户提交时的裸文件名格式，须使用项目脚本从 `source_materials/` 验证：

```bash
python3 scripts/verify_source_checksums.py
```

## 标准库可重复构建

以下核心构建与审计命令只依赖 Python 标准库；图形脚本另使用当前环境可用的本地绘图工具：

```bash
python3 scripts/stage5_statistics_audit.py
python3 scripts/build_bilingual_markdown.py
python3 scripts/audit_manuscript_consistency.py > quality_reports/manuscript_consistency.json
python3 scripts/audit_language_structure.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_manuscript_word_counts.py

python3 scripts/build_docx_stdlib.py \
  --input manuscript/manuscript_bilingual.md \
  --output manuscript/manuscript_bilingual.docx \
  --title "Evidence-Bounded Multi-Model Prioritization / 牙周炎队列口腔微肽的证据约束型多模型优先排序"

python3 scripts/build_docx_stdlib.py \
  --input manuscript/supplementary_tables_bilingual.md \
  --output manuscript/supplementary_tables_bilingual.docx \
  --title "Bilingual supplementary tables / 中英文补充表"

python3 scripts/audit_docx_packages.py
```

Light 写作检查的当前 JSON/文本输出保存在 `quality_reports/draft_lint_{en,zh}.*` 与 `mechanical_check_{en,zh}.*`。

## 投稿边界

包件可交责任作者审阅，并可在通讯作者补齐信息和批准后用于坦诚的预投稿询问；**尚不适合立即进入正式投稿系统**。主要阻断项为：候选序列/身份/逐行分数、样本映射和原始分析代码不可用；部分来源与交接仍需澄清；作者、机构伦理、经费、利益冲突、CRediT、最终数据/代码/AI 声明和期刊格式尚未完成；DOCX 仍需在 Word/LibreOffice 中逐页人工检查。
