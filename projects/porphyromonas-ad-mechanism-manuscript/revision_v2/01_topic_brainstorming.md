# Stage 1 — Scientific brainstorming and topic critique / 科学选题重构与严审

Date: 2026-08-12

## 1. Why the current manuscript is far from a competitive SCI paper

上一版解决了“不编造”和“不过度宣称”，但没有解决高质量原创研究必须回答的四个问题：

1. **中心科学问题不够尖锐。** 当前工作本质上是把多个现成预测器串成漏斗，回答“剩下多少条”，而不是检验一个能被推翻的生物学假设。
2. **创新增量偏工程拼接。** BBB、神经毒性、金属结合和 CHEL/FRS 均为已有模型；若没有新数据资产、新评价体系、模型校准或实验机制，审稿人会认为只是工具堆叠。
3. **统计单位缺失。** 11,721,988 条 sORF 或数万条肽不是天然独立生物学重复。若以肽为 n 比较健康与牙周炎，会产生严重伪重复。合理的独立单位应优先是受试者、样本或预先定义的非冗余肽家族；当前缺少样本—肽映射。
4. **AD 机制链没有被检验。** 预测 BBB、预测神经毒性和预测金属结合并不能建立脑暴露、氧化损伤、Aβ/AChE 作用或 AD 因果关系。

因此，单纯采用 Nature 风格语言不会把当前分析变成 Nature 水平研究；必须先改变研究问题和证据结构。

## 2. Recommended central question

### Recommended question / 推荐中心问题

> **Do periodontitis-associated oral micropeptides exhibit subject-level enrichment and reproducible cross-model convergence for predicted BBB permeability, neurotoxicity and metal interaction relative to matched healthy controls, after accounting for peptide length, composition, taxonomic origin and model applicability domain?**
>
> **在控制肽长度、组成、分类学来源和模型适用域后，牙周炎相关口腔微肽是否在受试者层面呈现相对于健康对照的富集，并在 BBB 渗透、神经毒性和金属相互作用预测中表现出可重复的跨模型汇聚？**

这比“把牙周炎候选依次筛到 12 条”更接近可发表问题，因为它包含：

- 明确比较：牙周炎 vs 健康；
- 正确统计层级：受试者/样本优先，而非把每条肽当独立 n；
- 可证伪结果：可以不富集、模型可以不一致、效应可以在控制长度后消失；
- 方法学增量：适用域、校准、阴性/乱序对照和跨模型稳健性；
- 候选排序只是次级输出，不再冒充主科学发现。

## 3. Candidate topic cards

### Option A — Moonshot / 冲刺型：金属依赖性神经毒性机制

**Working title**  
Periodontitis-derived oral micropeptides as metal-dependent neurotoxic mediators: from cohort-resolved discovery to BBB transport and neuronal validation

**核心主张**  
在牙周炎队列中发现并实验验证特定微肽，其可跨 BBB、结合 Cu/Fe/Zn，并在金属存在时诱导 ROS、脂质过氧化和神经细胞损伤。

**真正创新来源**  
新机制 + 新实验范式，而非模型拼接。

**最低判别实验**

- 受试者层面牙周炎富集和分类学归属；
- 靶向/非靶向 LC–MS/MS 谱图验证；
- BBB 转运模型；
- Cu/Fe/Zn 结合及配位实验；
- 金属依赖性 ROS、脂质过氧化、神经细胞毒性；
- scrambled peptide、metal-only、peptide-only、阳性/阴性对照；
- 视结果再做 Aβ/AChE/BChE，而不是先用对接代替表型。

**Kill criterion / 否决条件**  
候选在牙周炎受试者中不富集，或无谱图支持，或金属存在与否不改变神经毒性/氧化损伤，则核心机制不成立。

**可行性**：低，除非能够补做湿实验。  
**潜在层次**：证据完整时可冲刺高影响跨学科期刊；仅计算结果无法成立。

### Option B — Solid, recommended / 稳妥推荐：受试者分辨的口腔微肽图谱与模型稳健性

**Working title**  
A cohort-resolved atlas of periodontitis-associated oral micropeptides reveals robust and model-dependent neuroactive feature convergence

**核心主张**  
建立健康/牙周炎受试者分辨的微肽图谱，结合质谱、分类学、长度/组成匹配对照、模型适用域和多模型一致性，识别可重复的疾病相关候选。

**真正创新来源**

- 新数据资产：可公开、可查询的 cohort-resolved micropeptidome；
- 新测量：模型适用域和一致性而不是简单二值阳性；
- 新分析：受试者层面的效应、长度/组成匹配和敏感性分析；
- 可复现候选证据链：sequence→sample→taxon→spectrum→score→decision。

**最低数据要求**

- 全部候选序列和稳定 SeqID；
- 每条序列的样本/受试者映射和健康/牙周炎标签；
- 短肽/长肽来源和去重规则；
- 质谱命中、谱图及 FDR/唯一性信息；
- UniDL4BioPep、NTxPred2、mebipred、AnOxPePred 的逐行原始分数；
- 模型版本、访问日期、脚本和数据库快照；
- 受试者协变量（可用时）及缺失说明。

**Primary endpoint / 主终点**  
每位受试者中预先定义的“跨模型汇聚候选”比例或负担，比较牙周炎与健康组，并报告效应量、95% CI 和多重比较校正。

**关键敏感性分析**

- 按长度和氨基酸组成匹配；
- 乱序肽/组成保持 decoy；
- 每次移除一个模型；
- 不同阈值和连续分数分析；
- 按受试者、肽家族及数据来源重复；
- 排除 PXD003151/PXD026727 后重复，检验异质外部质谱集的影响。

**Kill criterion / 否决条件**  
若受试者层面的组间效应在长度/组成控制或适用域过滤后消失，则只能报告模型/序列偏差，不能报告疾病相关富集。

**可行性**：中等；这是当前最推荐路线。  
**潜在层次**：数据和复现充分时可形成严谨的计算/资源型原创研究；是否 Q1 取决于谱图、样本层面效应和外部验证。

### Option C — Safe / 保底型：预测器适用域和稳定性审计

**Working title**  
Applicability-domain and threshold sensitivity of peptide bioactivity predictors in ultra-short oral metagenomic peptides

**核心主张**  
系统评价现有肽预测模型在 5–50 aa 口腔宏基因组肽上的长度偏差、组成偏差、阈值稳定性和模型间一致性。

**创新来源**  
新测量/系统化评价，而不是声称新的 AD 机制。

**最低数据要求**  
候选序列及全部连续模型分数；最好补充实验阳性/阴性或可靠外部 benchmark。

**优势**  
不需要把牙周炎—AD 机制作为主结论，可正面处理“短肽模型是否适用”的审稿问题。

**风险**  
如果没有实验标签或外部验证，仍可能被认为只是描述模型输出。

**可行性**：中等。  
**潜在层次**：生物信息学方法/资源类期刊；一般不适合高影响机制期刊。

### Option D — Aggregate-only / 仅现有材料：初步描述性筛选

**Working title**  
A preliminary aggregate multi-model screen of periodontitis-branch oral peptide candidates

**可支持内容**  
仅能报告已有计数漏斗、限制和未来验证方案。

**Fatal flaw / 致命缺陷**  
无候选序列、无样本层面统计、无模型校准、无外部验证、无机制实验。语言再好也难成为有竞争力的原创 SCI 全文。

**可行性**：高。  
**潜在层次**：内部报告、预研究说明或方法附录；不建议作为本轮目标。

## 4. Preliminary ranking

| Route | Scientific impact | Novelty source | Feasibility with current package | Evidence needed | Preliminary decision |
| --- | ---: | --- | ---: | --- | --- |
| A Mechanistic validation | 5/5 | New mechanism + experiment | 1/5 | Full row-level data + substantial wet lab | Moonshot; only if experiments are feasible |
| B Cohort-resolved atlas | 4/5 | New data asset + robust measurement | 2/5 | Full sequence/sample/score/spectrum matrix | **Recommended** |
| C Model applicability audit | 3/5 | New measurement/systematization | 2/5 | Full sequences and continuous scores; benchmark desirable | Safe alternative |
| D Aggregate screen | 1/5 | Engineering combination | 5/5 | Existing package | Reject as competitive SCI target |

These are preliminary judgments, not final novelty verdicts. Stage 2 must perform explicit prior-art collision searches before any route is called novel.

## 5. Top three likely reviewer rejections of the current route

1. **“This is merely a serial application of existing predictors.”**  
   目前无法有效反驳；需 Option B 的新数据资产/适用域分析或 Option A 的实验机制。

2. **“Peptide-level counts are pseudoreplicated and do not establish a periodontitis effect.”**  
   目前无法反驳；需要受试者/样本映射和层级统计模型。

3. **“The AD framing is speculative and unsupported by the presented results.”**  
   目前只能承认并降级；若走 Option B，应把 AD 置于 secondary biological motivation；若走 Option A，必须补 BBB/神经/金属实验。

## 6. User decision and locked framing / 用户决策与冻结定位

用户选择：

- **Route:** Option D, aggregate-only.
- **Additional data:** none available.
- **Target:** a realistic, evidence-bounded SCI submission rather than a high-impact mechanistic paper.
- **Principal source correction:** `材料与方法及结果_机制研究版.docx` is the sole results source. The two mistakenly supplied unrelated files are excluded from every stage and documented only in the dedicated exclusion record.

Accordingly, the earlier subject-level enrichment question is **not answerable** and is withdrawn from the present manuscript. It remains a future-study question only.

### Locked research question / 冻结研究问题

> **How does a prespecified serial combination of sequence-evidence filters and established peptide predictors reduce an aggregate periodontitis-cohort oral sORF candidate space, which candidate-feature combinations remain at each decision threshold, and which claims remain testable rather than established?**
>
> **预先设定的序列证据过滤与现有肽预测器串联流程如何在聚合层面缩小牙周炎队列口腔 sORF 候选空间，不同判定阈值下保留哪些候选特征组合，以及哪些结论仍只是待检验假设？**

### Locked article position / 冻结文章定位

- Original, hypothesis-generating, aggregate-level computational prioritization study.
- The contribution is **workflow transparency and evidence-bounded prioritization**, not a new predictor, disease association test or AD mechanism.
- Healthy-group values provide descriptive pipeline context only. They are not treated as independent subject-level comparative statistics.
- The 12-candidate and 8-candidate endpoints are reported as source-recorded aggregate outputs; absent sequences and row-level scores prevent independent reproduction.
- AD is retained only as downstream biological motivation in the Introduction/Discussion, not in the primary result claim.

### Locked working title / 冻结工作标题

**Evidence-Bounded Multi-Model Prioritization of Periodontitis-Cohort Oral Micropeptides with Predicted Blood–Brain Barrier, Neurotoxicity and Metal-Interaction Features: An Aggregate-Level In Silico Study**

**牙周炎队列口腔微肽的证据约束型多模型优先排序：预测血脑屏障、神经毒性与金属相互作用特征的聚合层面计算研究**

### Fatal limitations accepted rather than hidden / 明确接受而不掩盖的限制

1. No sequence-level candidate table, sample mapping, model scores or executable original pipeline.
2. No valid inferential statistics across subjects; peptide counts cannot be treated as biological replicates.
3. No independent validation, wet-lab evidence, taxonomic assignment or AD-mechanism experiment.
4. Submission strategy must target journals/article formats open to exploratory computational work. A high-impact mechanism journal is not a defensible target.

**Stage 1 verdict:** proceed to bounded literature search and manuscript rebuilding under the locked aggregate-level frame. Do not return to Option B/A language unless new data are supplied.
