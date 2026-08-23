# 口腔微肽与牙周炎—阿尔茨海默病机制研究稿件包

## 当前版本

v3.11.0在完整稿与简洁稿之间新增一套用于本次提交的口腔smORF筛选论文中间版；现有完整稿、简洁稿和独立ALLLHRC–AChE动力学稿均保持不变。全部版本均提供彼此分离的英文、中文DOCX及Markdown源文件：

- `manuscript/full/English.docx`
- `manuscript/full/Chinese.docx`
- `manuscript/intermediate/English.docx`
- `manuscript/intermediate/Chinese.docx`
- `manuscript/concise/English.docx`
- `manuscript/concise/Chinese.docx`
- `manuscript/md_alllhrc/full/English.docx`
- `manuscript/md_alllhrc/full/Chinese.docx`
- `manuscript/md_alllhrc/concise/English.docx`
- `manuscript/md_alllhrc/concise/Chinese.docx`

新增中间版不包含新的动力学结果，独立MD包也不增加中间版。十份当前DOCX均从单段非结构式摘要开始，摘要不设背景、目的、方法、结果或结论标签。稿件不显示论文标题，不含页眉、页脚、页码、批注或图像。英文稿保留可发表Research Article的Introduction、Materials and methods、Results、Discussion和References核心结构，使用无编号标题、≤250词摘要、12磅Times New Roman、双倍行距和1英寸页边距；中文稿保持同步结构。正文普通段落采用480 twip（24磅，约两个汉字）首行缩进，摘要、标题、关键词、表题、表格和参考文献不缩进。筛选完整稿含6个三线表、约6,900个英文正文词和55条参考文献；中间稿含4个三线表、约4,600个英文正文词和40条参考文献；精简稿含3个三线表、约3,700个英文正文词和22条参考文献。MD完整稿含2个三线表和7条参考文献；MD简洁稿含1个三线表和5条参考文献。所有表格仅保留顶线、表头下横线和底线，不使用竖线、内部正文横线或表头底色。稿件不设独立“统计分析”小节或“结论”章节，Discussion之后直接进入References，也不含Declarations或其他管理性章节。

## 科学定位

项目以`source_materials/材料与方法及结果_机制研究版.docx`为主要科学材料，报告纯计算、汇总层面的口腔smORF候选优选。候选级联包括UniDL4BioPep的ESM-2/CNN、NTxPred2肽模式的ESM2-t30微调模型、mebipred两级人工神经网络和AnOxPePred多任务一维CNN。

筛选稿的完整、中间和简洁版本均支持描述性漏斗、12条独立序列的组成核对及现有AChE Vina评分排序，但不支持牙周炎特异性、*Porphyromonas gingivalis*来源、当前队列表达、BBB通过、神经毒性、金属化学、AChE结合/功能、AD机制或因果关系。中间版保留完整的22项长/短肽多维结果、级联计数、12条序列与评分及长肽流失局限，但压缩文献综合和验证细节；它不纳入新的动力学结果。独立MD包仅解释用户指定的ALLLHRC–AChE单条100 ns输出：AChE骨架偏差有限，ALLLHRC约在23和56 ns发生两次内部构象转变，并呈现优选质心间距、较窄SASA范围和间歇氢键。该结果不自动整合至原筛选稿，也不能证明结合亲和力、PAS驻留、AChE抑制、Aβ聚集改变或AD相关作用；其他复合物及比较性MD分析仍待完成与质量控制。

主源中的长肽和短肽多维功能输出均已恢复。流程局限同时明确披露：牙周炎标记分支中72条经宏蛋白质组支持、去重且BBB高分的31–50 aa长肽均未进入NTxPred2阳性集合；923条NTxPred2阳性序列全部≤30 aa，因而后续金属结合与CHEL/FRS网页预测及最终12条汇总候选只保留短肽。这不能证明长肽没有神经毒性或金属相关活性，而可能反映串行阈值、模型适用性/校准和网页预测器实现方式。

正文不报告具体参与者、标本、组装分析或MAG总数。用户说明的296个MAG在`evidence/mag_count_audit.md`中保留为待核查信息，未进入稿件。

## 图和表

`manuscript/figures/`保留历史SVG/PNG源文件，便于项目内部追踪，但它们不是当前稿件DOCX的一部分。按用户选择，ALLLHRC–AChE结果图仅作为解读证据，不嵌入新增MD稿。十份当前DOCX经OpenXML检查均不含`word/media/`、drawing对象或图像关系。

## 引文与Zotero

十份Markdown正文使用Pandoc格式的真实BibTeX键，例如`[@scheltens2021alzheimer]`和`[@atanasova2020md]`，统一链接到`references/references.bib`。标准库DOCX构建器依据各版本参考文献表自动生成连续编号的Vancouver式缓存文字。

本环境未暴露Pandoc或正在运行的Better BibTeX端点，因此提交的DOCX不被误称为Zotero-live。严格的Better BibTeX探针、官方`zotero.lua`过滤器构建和OpenXML字段检查位于：

- `scripts/test_better_bibtex.py`
- `scripts/build_zotero_live_docx.py`
- `references/ZOTERO_WORD_ACCEPTANCE.md`
- `quality_reports/zotero_live_status.json`

桌面Word/Zotero刷新和Add/Edit Bibliography是尚待用户执行的验收门。普通`[N]`文字不能通过Zotero Refresh自动变为live fields。

## 可重复构建

从项目根目录运行：

```bash
python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/full/English.md \
  --output manuscript/full/English.docx \
  --title English

python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/full/Chinese.md \
  --output manuscript/full/Chinese.docx \
  --title Chinese

for language in English Chinese; do
  python3 scripts/build_docx_stdlib.py --clean-manuscript \
    --timestamp 2026-08-23T00:00:00Z \
    --bibliography references/references.bib \
    --input "manuscript/intermediate/${language}.md" \
    --output "manuscript/intermediate/${language}.docx" \
    --title "${language}"
done

python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/concise/English.md \
  --output manuscript/concise/English.docx \
  --title English

python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/concise/Chinese.md \
  --output manuscript/concise/Chinese.docx \
  --title Chinese

for variant in full concise; do
  for language in English Chinese; do
    python3 scripts/build_docx_stdlib.py --clean-manuscript \
      --timestamp 2026-08-23T00:00:00Z \
      --bibliography references/references.bib \
      --input "manuscript/md_alllhrc/${variant}/${language}.md" \
      --output "manuscript/md_alllhrc/${variant}/${language}.docx" \
      --title "${language}"
  done
done
```

## 当前审计

```bash
python3 scripts/audit_submission_manuscripts.py
python3 scripts/audit_full_manuscripts.py
python3 scripts/audit_intermediate_package.py
python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
python3 scripts/audit_full_docx_reproducibility.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py
python3 scripts/audit_md_alllhrc_package.py
python3 scripts/generate_artifact_checksums.py
python3 scripts/build_repository_inventory.py
```

`quality_reports/submission_manuscript_audit.json`检查完整、中间和简洁筛选稿共六份DOCX的无标题单段摘要起始、“统计分析”/“结论”章节缺失、正文首行缩进、Discussion后直接进入References、长短肽多维功能结果完整性、长肽流失与最终12条仅含短肽的局限说明、无图、三线表、敏感数量省略、科学边界、BibTeX键和引用清单，并要求正文长度满足“完整稿>中间稿>简洁稿”。`quality_reports/intermediate_package_audit.json`专门核验中间版中英文同步、40条参考文献、4个三线表及既有完整/简洁/MD DOCX哈希不变。`quality_reports/full_docx_reproducibility.json`要求六份筛选DOCX隔离重建后逐字节一致。`quality_reports/md_alllhrc_package_audit.json`继续单独检查MD四稿的关键轨迹数值、数字化RMSD来源、Aβ标题标注差异、解释边界、中英文结构、无图DOCX、三线表以及隔离重建。

## 证据和历史材料

内部证据记录、哈希、版本提交、排除材料和复现边界保留在`evidence/`、`revision_v2/`、`revision_v3/`和`VERSION_HISTORY.md`中。此类管理信息用于项目追踪，不进入当前SCI稿件正文。历史双语组合稿、补充表和图件不属于当前独立中英文DOCX交付物。
