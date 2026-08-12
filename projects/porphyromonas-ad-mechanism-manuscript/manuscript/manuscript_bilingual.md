# Evidence-Bounded Multi-Model Prioritization of Periodontitis-Cohort Oral Micropeptides with Predicted Blood–Brain Barrier Penetration, Neurotoxicity, and Metal-Interaction Features: An Aggregate-Level In Silico Study

# 牙周炎队列口腔微肽的证据约束型多模型优先排序：预测血脑屏障穿透、神经毒性与金属相互作用特征的聚合层面计算研究

**Bilingual section-parallel scientific-content draft / 中英文分节对照科学内容草案**

**Article type:** Original Research Article  
**Draft status:** Submission-oriented scientific-content draft for accountable-author review. Author names, affiliations, correspondence details, journal-specific formatting, and author-approved declarations were not supplied and are not inferred.

**文章类型：** 原创研究论文  
**稿件状态：** 面向投稿、供责任作者审核的科学内容草案。因未提供作者姓名、单位、通讯信息、期刊特定格式及经作者批准的声明，本稿不作推定或虚构补写。

## Abstract / 摘要

### English

**Background:** Microbiome small open reading frames (smORFs) are incompletely characterized. Serial sequence predictors can reduce large candidate spaces, but cannot establish translation, exposure, toxicity, mechanism, or disease causality. We reconstructed and audited an aggregate workflow that prioritized oral smORF-derived candidates from a periodontitis cohort branch.

**Methods:** The principal source supplied aggregate counts, thresholds, and workflow descriptions for 4–50-amino-acid sORFs. UniDL4BioPep output ≥0.80 defined a blood–brain barrier (BBB)-high set, followed by NTxPred2, mebipred (threshold 0.50), and AnOxPePred chelating (CHEL)/free-radical-scavenging (FRS) outputs. Analyses were descriptive. Sequences, subject/sample mappings, row-level scores, and original code were unavailable; the primary pipeline was not rerun.

**Results:** The source reported 11,269,961 healthy-branch and 11,721,988 periodontitis-branch sORFs, reduced to 31,510 and 33,786 evidence-filtered candidates. BBB-high outputs were 3,359/30,557 (10.99%) and 3,446/32,754 (10.52%) in healthy and periodontitis short branches, and 40/953 (4.20%) and 72/1,032 (6.98%) in long branches. The 3,518-candidate periodontitis set was 97.95% short. NTxPred2 evaluated 3,299 candidates; 219 were outside its length range and 923/3,299 (27.98%) evaluated candidates were positive. The source next reported 111 metal-binding-positive candidates: 15 (13.51%) met CHEL≥0.25, 12 (10.81%) also met FRS<0.50, and 8 (7.21%) met FRS<0.45.

**Conclusions:** The workflow provides an auditable aggregate reduction record and source-reported 12-candidate main set with an 8-candidate stricter subset. It establishes neither disease specificity nor experimental activity. Candidate identities and row-level provenance must be released before synthesis, validation, or neurodegenerative interpretation.

**Keywords:** oral microbiome; small open reading frame; micropeptide; periodontitis; blood–brain barrier; neurotoxicity prediction; metal-binding prediction; aggregate analysis; hypothesis generation

### 中文

**背景：** 微生物组短开放阅读框（smORF）尚未得到充分表征。顺序使用序列预测器可以缩小候选空间，但不能证明翻译、暴露、毒性、机制或疾病因果性。本研究重建并审计一套从牙周炎队列分支中优先排序口腔 sORF 候选的聚合流程。

**方法：** 主证据源提供了 4–50 aa sORF 的聚合计数、阈值和流程描述。以 UniDL4BioPep 输出≥0.80 定义血脑屏障（BBB）高分集合，随后使用 NTxPred2、mebipred（阈值 0.50）和 AnOxPePred 的螯合（CHEL）/自由基清除（FRS）输出。分析仅为描述性分析。由于缺少序列、受试者/样本映射、逐行分数和原始代码，未重跑主分析流程。

**结果：** 来源报告健康分支和牙周炎分支分别含 11,269,961 和 11,721,988 条 sORF，缩减为 31,510 和 33,786 条证据过滤候选。健康和牙周炎短分支 BBB 高分输出分别为 3,359/30,557（10.99%）和 3,446/32,754（10.52%），长分支分别为 40/953（4.20%）和 72/1,032（6.98%）。牙周炎集合共 3,518 条，其中 97.95% 为短候选。NTxPred2 评价了 3,299 条；219 条超出其长度范围，已评价候选中 923/3,299（27.98%）阳性。来源随后报告 111 条金属结合阳性候选：15 条（13.51%）满足 CHEL≥0.25，12 条（10.81%）同时满足 FRS<0.50，8 条（7.21%）满足 FRS<0.45。

**结论：** 该流程形成了可审计的聚合缩减记录，并报告 12 条主候选和 8 条严格子集，但不能证明疾病特异性或实验活性。在开展合成、验证或神经退行性解释之前，必须公开候选身份和逐行来源信息。

**关键词：** 口腔微生物组；短开放阅读框；微肽；牙周炎；血脑屏障；神经毒性预测；金属结合预测；聚合分析；假设生成

## 1. Introduction / 1 引言

### English

Small open reading frames are frequently missed or misannotated because short coding sequences are difficult to distinguish from chance ORFs and are poorly represented in conventional annotation pipelines. Large-scale human-microbiome analyses nevertheless indicate that smORFs encode a substantial and incompletely characterized small-protein space [1]. Methodological work has since combined profile hidden Markov models, deep learning, evolutionary information, and ribosome-profiling evidence to improve annotation [2]. More recently, high-resolution multi-omics has integrated smORF prediction with metatranscriptomics and deep metaproteomic detection [3]. Together, these studies support smORFs as a legitimate discovery space while making clear that a predicted ORF is not automatically a translated or functional peptide.

Periodontitis is accompanied by ecological and functional changes in the oral microbiome. Paired metagenomic and metatranscriptomic studies have identified compartment- and species-specific activity associated with periodontitis [4], and a cross-study metatranscriptome analysis has demonstrated the value of subject/sample-resolved data, normalization, and false-discovery control [5]. Sequence resources such as HOMD/eHOMD provide curated oral microbial references [6,7], whereas metaproteomic datasets provide context-dependent evidence of peptide detection [8,9]. Dedicated oral metaproteomic workflows now emphasize host depletion, microbial enrichment, peptide- and protein-level false-discovery control, taxonomic assignment, and raw-data deposition [10]. Exact matching to these resources can narrow a search space, but a match from another cohort or disease context does not establish expression or disease specificity in the cohort under analysis.

A second challenge is to prioritize a tractable validation set without converting model outputs into biological claims. UniDL4BioPep provides a common deep-learning architecture for multiple peptide-bioactivity labels [11]. The BBB-peptide prediction literature illustrates both the utility and the limitations of this approach: available positive sets are modest, class imbalance is common, and different models can trade sensitivity against specificity [12,13]. NTxPred2, mebipred, and AnOxPePred respectively estimate sequence-based neurotoxicity, metal-binding potential, and antioxidant-related chelating/free-radical-scavenging features [14–16]. Because these models use overlapping sequence-derived information, serial agreement is useful for operational ranking but does not constitute independent biological confirmation. Stronger microbiome-peptide discovery studies have followed computational prioritization with synthesis and functional assays [17].

Neurodegenerative disease provides one possible downstream context for BBB-, toxicity-, and metal-related hypotheses, but the causal evidence must be represented accurately. Observational syntheses have reported associations between periodontitis and cognitive disorders, with effect estimates varying by disease definition, severity, population, and study design [18,19,22]. Clinical oral-bacteria findings are also heterogeneous [20]. Experimental work involving *Porphyromonas gingivalis* supports biological plausibility for selected pathogen-derived products [21], but cannot be transferred to taxonomically unassigned peptides. Recent Mendelian-randomization analyses found no convincing genetic causal relationship between periodontal disease and Alzheimer’s disease (AD) [23], and a 2026 synthesis of Mendelian-randomization studies likewise found no substantial causal association with AD [24]. Current reviews therefore retain biological plausibility while recognizing that direct human causality remains unproven [25].

Against this background, the present study asks a bounded question: how does the source-reported combination of sequence-evidence filters and established peptide predictors reduce an aggregate periodontitis-cohort oral sORF candidate space, which candidate-feature combinations remain at each threshold, and which interpretations remain untested? The contribution is a transparent descriptive reconstruction and statistical/claim audit. It is not a new predictor, a healthy-versus-periodontitis association test, or a validated disease mechanism.

### 中文

短开放阅读框容易被遗漏或错误注释，因为短编码序列难以与随机 ORF 区分，且在常规注释流程中的代表性不足。然而，人体微生物组的大规模分析表明，smORF 编码了规模可观且尚未得到充分表征的小蛋白空间 [1]。后续方法学研究结合了谱隐马尔可夫模型、深度学习、进化信息和核糖体测序证据，以改进注释 [2]。近期高分辨率多组学研究又把 smORF 预测与宏转录组和深度宏蛋白质组检测相结合 [3]。这些研究共同支持把 smORF 视为合理的发现空间，同时也明确指出：预测到 ORF 并不等于该序列必然被翻译或具有功能。

牙周炎伴随口腔微生物组生态和功能改变。配对宏基因组/宏转录组研究发现了与牙周炎相关、且依赖口腔部位和物种的微生物活性 [4]；跨研究宏转录组分析则显示了受试者/样本分辨数据、标准化和假发现率控制的重要性 [5]。HOMD/eHOMD 等序列资源提供经整理的口腔微生物参考 [6,7]，宏蛋白质组数据集则提供依赖具体场景的肽检测证据 [8,9]。目前专门的口腔宏蛋白质组流程强调去除宿主干扰、富集微生物、在肽和蛋白层面控制假发现率、分类学归属及原始数据存储 [10]。与这些资源进行精确匹配可以缩小搜索空间，但来自另一队列或疾病场景的匹配并不能证明该序列在本队列中表达或具有疾病特异性。

第二个挑战是在不把模型输出转化为生物学事实的前提下，得到规模可处理的验证集合。UniDL4BioPep 为多种肽生物活性标签提供统一深度学习框架 [11]。BBB 肽预测文献同时展示了此类方法的用途和局限：可用阳性样本集较小、类别不平衡常见，而且不同模型可能在灵敏度和特异度之间作出不同权衡 [12,13]。NTxPred2、mebipred 和 AnOxPePred 分别估计基于序列的神经毒性、金属结合潜力，以及与抗氧化相关的螯合/自由基清除特征 [14–16]。由于这些模型使用相互重叠的序列信息，串联一致性有助于操作性排序，但不构成相互独立的生物学确证。证据更强的微生物组肽发现研究会在计算优先排序后继续开展肽合成与功能实验 [17]。

神经退行性疾病可以为 BBB、毒性和金属相关假设提供一种后续背景，但必须准确呈现因果证据。观察性证据综合报告牙周炎与认知障碍之间存在关联，但效应估计会随疾病定义、严重程度、人群和研究设计改变 [18,19,22]；口腔细菌的临床研究结果也有异质性 [20]。涉及牙龈卟啉单胞菌的实验研究为特定病原产物提供生物学合理性 [21]，但不能把相关结论转移给缺少分类学归属的肽。近期孟德尔随机化研究没有发现令人信服的牙周病与阿尔茨海默病（AD）遗传因果关系 [23]；2026 年对孟德尔随机化研究的综合也未发现牙周炎与 AD 存在实质性因果关联 [24]。因此，当前综述在保留生物学合理性的同时，仍承认直接人类因果性尚未得到证实 [25]。

基于上述背景，本研究提出一个有边界的问题：来源报告的序列证据过滤和现有肽预测器组合，如何在聚合层面缩小牙周炎队列口腔 sORF 候选空间；各阈值下保留哪些候选特征组合；哪些解释仍未接受检验？本研究的贡献是透明的描述性重建以及统计与主张审计，而不是开发新预测器、检验健康—牙周炎关联或验证疾病机制。

## 2. Materials and Methods / 2 材料与方法

### English

#### 2.1 Study design, principal source, and scope

This study is an aggregate-level descriptive reconstruction of a source-reported computational analysis. The sole source of study methods, thresholds, and results was `材料与方法及结果_机制研究版.docx` (SHA-256: `f4132a02cb9955c808739c3cbf15edd947f6203d577e8586490933a5d2daa4b5`). The corresponding PDF was retained as an original file but was not independently parsed page by page in the drafting environment. Contextual documents did not supply study results.

The principal record named PRJNA678453 and PRJEB65451 and stated that 296 high-quality metagenome-assembled genomes represented 24 healthy participants and 26 participants with periodontitis. PRJNA678453 could be linked to a published oral metagenomic/metatranscriptomic study [4]. PRJEB65451 could not be independently resolved during drafting and is retained as an unresolved provenance element rather than represented as verified metadata.

No new participant recruitment, specimen collection, wet-laboratory experiment, docking, molecular dynamics, or clinical analysis was performed. Only aggregate counts, thresholds, and narrative workflow descriptions were available. Candidate nucleotide/amino-acid sequences, genomic coordinates, sample-to-sequence mappings, taxonomic assignments, peptide-spectrum matches, row-level model scores, run logs, random seeds, database snapshots, and original executable code were not supplied. Accordingly, the present analysis audits aggregate arithmetic and reporting boundaries; it does not independently reproduce the primary bioinformatics workflow.

#### 2.2 Source-reported sORF construction and sequence-evidence filtering

According to the principal record, sample-specific mapping was used to construct healthy and periodontitis sORF libraries, after which translated sequences 4–50 amino acids long were retained. The raw healthy and periodontitis libraries contained 11,269,961 and 11,721,988 sORFs, respectively.

The workflow then used hash-indexed exact sequence matching against named oral sequence/proteomic resources and removed duplicate sequences. The short-candidate resource set included PXD003151, PXD004319, and PXD026727. PXD004319 contains salivary samples from individuals with periodontitis, dental caries, and oral health [8]. PXD026727 is a lung-cancer oral metaproteomics dataset [9]. PXD003151 has been used in an oral dysbiosis/caries-risk context. These resources may support prior observation of an exact sequence in a named oral dataset, but they cannot by themselves establish expression in the metagenomic cohort or periodontitis specificity. The source labelled the 31–50-amino-acid branch as HOMD-derived [6,7]. Because HOMD/eHOMD are sequence/taxonomy resources rather than mass-spectrometry repositories, the expression-evidence status of this branch remains ambiguous.

After source-reported evidence filtering and deduplication, 31,510 healthy candidates and 33,786 periodontitis candidates remained. These totals were divided into short (5–30 amino acids: healthy, 30,557; periodontitis, 32,754) and long (31–50 amino acids: healthy, 953; periodontitis, 1,032) branches. Although the initial rule included 4-amino-acid sequences, downstream branches began at 5 amino acids; the disposition of 4-amino-acid sequences was not documented.

#### 2.3 Multi-activity and BBB-related prediction

The source reported use of UniDL4BioPep [11] with ESM2-derived sequence representations (`esm2_t6_8M_UR50D`) to score more than 20 peptide-bioactivity classes. An output of at least 0.80 was used as a common operational high-score threshold. No calibration or external validation specific to the present sequence domain was available. We therefore use "model-positive" or "high-output", not "confirmed activity" or "probability".

The BBB-related output defined the downstream candidate set. Counts from healthy and periodontitis branches were retained for descriptive orientation, but no between-group hypothesis was tested. Restricting later steps to the periodontitis branch creates a periodontitis-cohort prioritization set, not a demonstrated periodontitis-specific set.

#### 2.4 Neurotoxicity, metal-binding, and CHEL/FRS prioritization

The periodontitis BBB-high set was next evaluated with NTxPred2 [14]. The source described an accepted sequence range of 7–50 amino acids. Candidates below this range were classified as not evaluated, not as negative. NTxPred2 outputs were summarized as predicted positive or negative among eligible candidates.

The source narrative subsequently described mebipred analysis at an output threshold of 0.50 for Cu-, Fe-, or Zn-binding potential [15]. Mebipred predicts sequence-level metal-binding potential; it does not provide a binding constant, ion-specific stoichiometry, residue-level site, oxidation-state preference, or coordination geometry. Although the narrative places this step after the NTxPred2-positive set, no row-level handoff file was available. The count of 111 is therefore reported as a source-reported downstream result, and 111/923 is not treated as an independently audited transition rate.

Mebipred-positive candidates were evaluated with AnOxPePred [16]. According to the source, chelating (CHEL) and free-radical-scavenging (FRS) files were joined by sequence identifier. Three operational outputs were retained: CHEL≥0.25; CHEL≥0.25 with FRS<0.50 (main set); and CHEL≥0.25 with FRS<0.45 (stricter subset). These cutoffs were source-prespecified ranking rules, not experimentally calibrated clinical or mechanistic thresholds. In particular, high predicted CHEL with lower predicted FRS does not establish pro-oxidant activity.

#### 2.5 Descriptive statistics and reproducibility audit

Counts were transcribed from the principal record. Percentages were deterministically recomputed as 100×n/N with the denominator stated for each quantity. Candidate sequences were units of computational accounting, not independent biological replicates. Because sample-to-candidate mappings and row-level participant outcomes were unavailable, no p value, confidence interval, effect estimate, power analysis, receiver-operating-characteristic analysis, or multiple-testing correction was calculated for healthy-versus-periodontitis comparisons.

Arithmetic and monotonicity checks were implemented in Python standard-library code (`scripts/stage5_statistics_audit.py`). Prespecified checks required branch counts to sum to their evidence-filtered totals, model-positive counts not to exceed their denominators, NTxPred2 evaluated and non-evaluated counts to sum to the BBB-high total, and downstream threshold counts to be nested. The stricter FRS threshold was treated as the only reconstructable threshold-sensitivity contrast.

### 中文

#### 2.1 研究设计、主证据源与范围

本研究是对来源报告计算分析进行的聚合层面描述性重建。研究方法、阈值和结果的唯一证据源为 `材料与方法及结果_机制研究版.docx`（SHA-256：`f4132a02cb9955c808739c3cbf15edd947f6203d577e8586490933a5d2daa4b5`）。对应 PDF 作为原件保留，但当前写作环境未对其进行独立逐页解析。其他背景材料未提供本研究结果。

主记录列出 PRJNA678453 和 PRJEB65451，并称 296 个高质量宏基因组组装基因组来自 24 名健康参与者和 26 名牙周炎参与者。PRJNA678453 可与已发表的口腔宏基因组/宏转录组研究对应 [4]；写作期间未能独立解析 PRJEB65451，因此把它保留为尚未解决的来源要素，而不写成已核实元数据。

本研究未新增参与者招募、样本采集、湿实验、分子对接、分子动力学或临床分析。可用材料仅含聚合计数、阈值和叙述性流程，未提供候选核苷酸/氨基酸序列、基因组坐标、样本—序列映射、分类学归属、肽谱匹配、逐行模型分数、运行日志、随机种子、数据库快照或原始可执行代码。因此，本研究只审计聚合算术和报告边界，并不构成对原始生物信息学流程的独立复现。

#### 2.2 来源报告的 sORF 构建与序列证据过滤

根据主记录，流程采用样本特异性映射构建健康和牙周炎 sORF 库，随后保留翻译长度为 4–50 aa 的序列。健康和牙周炎原始库分别含 11,269,961 和 11,721,988 条 sORF。

随后，流程使用基于哈希索引的精确序列匹配，将候选与指定口腔序列/蛋白质组资源比对，并去除重复序列。短候选资源集包括 PXD003151、PXD004319 和 PXD026727。PXD004319 包含牙周炎、龋病和口腔健康受试者的唾液样本 [8]；PXD026727 是肺癌口腔宏蛋白质组数据集 [9]；PXD003151 曾用于口腔生态失调/龋病风险场景。这些资源可以支持某一精确序列曾在指定口腔数据集中出现，但不能单独证明其在当前宏基因组队列中表达或具有牙周炎特异性。来源将 31–50 aa 分支标记为 HOMD 来源 [6,7]；由于 HOMD/eHOMD 是序列/分类学资源而非质谱仓库，该分支的表达证据性质仍不明确。

经来源报告的证据过滤和去重后，健康和牙周炎分支分别保留 31,510 和 33,786 条候选。这些总数被分成短分支（5–30 aa：健康 30,557；牙周炎 32,754）和长分支（31–50 aa：健康 953；牙周炎 1,032）。尽管初始规则包含 4 aa 序列，后续分支从 5 aa 开始；4 aa 序列的去向没有记录。

#### 2.3 多活性与 BBB 相关预测

来源报告使用 UniDL4BioPep [11] 和 ESM2 序列表征（`esm2_t6_8M_UR50D`）对 20 余类肽生物活性评分，并对所有类别统一采用不低于 0.80 的操作性高分阈值。由于缺少针对当前序列域的校准和外部验证，本稿使用“模型阳性”或“高分输出”，而不使用“已确认活性”或“概率”。

BBB 相关输出定义了后续候选集。健康和牙周炎分支计数仅用于描述性背景，不进行组间假设检验。把后续步骤限制于牙周炎分支，只能产生“牙周炎队列优先排序集合”，不能产生已经证明的“牙周炎特异性集合”。

#### 2.4 神经毒性、金属结合和 CHEL/FRS 优先排序

随后使用 NTxPred2 评价牙周炎 BBB 高分集合 [14]。来源所述接受序列范围为 7–50 aa。低于该范围的候选被归为“未评价”，而不是阴性；NTxPred2 输出在符合长度要求的候选中汇总为预测阳性或阴性。

来源叙述接着说明，以 0.50 为阈值使用 mebipred 预测 Cu、Fe 或 Zn 结合潜力 [15]。Mebipred 预测的是序列层面金属结合潜力，并不提供结合常数、离子特异性化学计量、残基位点、氧化态偏好或配位几何。虽然叙述把此步骤置于 NTxPred2 阳性集合之后，但缺少逐行交接文件。因此，111 条仅作为来源报告的后续结果；本稿不把 111/923 当作经独立审计的转化率。

随后用 AnOxPePred 评价 mebipred 阳性候选 [16]。根据来源，按序列标识符合并螯合（CHEL）和自由基清除（FRS）文件，并保留三个操作性输出：CHEL≥0.25；CHEL≥0.25 且 FRS<0.50（主集合）；CHEL≥0.25 且 FRS<0.45（严格子集）。这些阈值是来源预设的排序规则，而不是经实验校准的临床或机制阈值。特别是，预测 CHEL 较高且 FRS 较低并不能证明促氧化作用。

#### 2.5 描述性统计与可重复性审计

计数转录自主记录，比例按 100×n/N 确定性重算，并对每项数值明确分母。候选序列只是计算记账单位，不是相互独立的生物学重复。由于缺少样本—候选映射和参与者层面逐行结果，本研究没有对健康—牙周炎比较计算 p 值、置信区间、效应估计、效能、受试者工作特征或多重检验校正。

使用 Python 标准库脚本（`scripts/stage5_statistics_audit.py`）完成算术和单调性检查。预设检查要求：长度分支之和等于证据过滤总数；模型阳性数不超过相应分母；NTxPred2 已评价与未评价数之和等于 BBB 高分总数；后续阈值计数保持嵌套关系。更严格 FRS 阈值是唯一可以重建的阈值敏感性对照。

## 3. Results / 3 结果

### English

#### 3.1 Candidate-space reduction and branch accounting

The source-reported healthy and periodontitis branches began with 11,269,961 and 11,721,988 sORFs. Evidence filtering and deduplication retained 31,510 healthy candidates (0.2796% of the raw healthy library) and 33,786 periodontitis candidates (0.2882% of the raw periodontitis library). The short and long branch counts summed exactly to their respective evidence-filtered totals. These values describe computational retention; they are not participant-level rates.

**Table 1. Aggregate candidate libraries and BBB-high outputs**

| Branch | Raw sORFs | Evidence-filtered candidates | Short background (5–30 aa) | BBB-high short, n (%) | Long background (31–50 aa) | BBB-high long, n (%) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 30,557 | 3,359 (10.99) | 953 | 40 (4.20) |
| Periodontitis | 11,721,988 | 33,786 | 32,754 | 3,446 (10.52) | 1,032 | 72 (6.98) |

#### 3.2 Descriptive BBB and multi-activity outputs

BBB-high outputs comprised 3,359/30,557 healthy short candidates (10.99%) and 3,446/32,754 periodontitis short candidates (10.52%). In the long branches, the corresponding counts were 40/953 (4.20%) and 72/1,032 (6.98%). These side-by-side percentages were not tested inferentially.

The supplementary activity tables preserve all source-reported UniDL4BioPep class counts. One notable output-distribution feature was the antimicrobial label in the short branches: 30,537/30,557 healthy candidates (99.93%) and 32,721/32,754 periodontitis candidates (99.90%) were model-positive at the common 0.80 threshold. The near-universal output is not interpreted as measured biological prevalence; instead, it highlights the need for task- and domain-specific calibration before using model-positive proportions biologically.

#### 3.3 Periodontitis-branch downstream prioritization

Combining 3,446 short and 72 long BBB-high outputs yielded 3,518 periodontitis-branch candidates. The short branch contributed 97.95% (3,446/3,518). Within the source-reported short-candidate length summary, 547 were 5–7 amino acids, 2,893 were 8–15 amino acids, and 6 were 16–30 amino acids; all 72 long candidates were 31–50 amino acids.

NTxPred2 evaluated 3,299/3,518 candidates (93.77%). The remaining 219 candidates (6.23%) were below the stated accepted length range and were not evaluated. Among evaluated candidates, 923/3,299 (27.98%) were predicted positive. The source stated that all 923 were no longer than 30 amino acids.

The source next reported 111 candidates positive for Cu/Fe/Zn-binding potential at the mebipred threshold. Within that source-reported set, 15/111 (13.51%) had CHEL≥0.25. Twelve of 111 (10.81%) additionally met FRS<0.50, and 8/111 (7.21%) met the stricter FRS<0.45 rule. Tightening FRS from <0.50 to <0.45 retained 8/12 (66.67%) of the main set and removed four candidates. Candidate identities could not be listed because the corresponding sequences were absent.

**Table 2. Aggregate periodontitis-branch prioritization record**

| Stage | Operational rule | Reported count | Denominator/evidence note |
| --- | --- | ---: | --- |
| BBB-high short | UniDL4BioPep BBB output ≥0.80; 5–30 aa | 3,446 | 32,754 short candidates |
| BBB-high long | UniDL4BioPep BBB output ≥0.80; 31–50 aa | 72 | 1,032 long candidates |
| BBB-high combined | Union of length branches | 3,518 | Periodontitis downstream set |
| NTxPred2 evaluated | Accepted range 7–50 aa | 3,299 | 219 not evaluated |
| NTxPred2 predicted positive | Model-positive | 923 | 3,299 evaluated |
| Metal-binding positive | mebipred output ≥0.50 | 111 | Source-reported downstream count; row-level handoff unavailable |
| CHEL-prioritized | CHEL≥0.25 | 15 | 111 source-reported metal-positive candidates |
| Main operational set | CHEL≥0.25 and FRS<0.50 | 12 | 111 source-reported metal-positive candidates |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | 111 source-reported metal-positive candidates |

![Figure 1. Evidence-bounded aggregate computational prioritization.](figures/prioritization_funnel.png)

**Figure 1.** Evidence-bounded aggregate computational prioritization. Counts and operational thresholds were transcribed from the principal source record. Healthy-branch values are descriptive context only. The dashed transition indicates that the row-level handoff to mebipred was unavailable; 111/923 is therefore not presented as an audited transition rate. The 12-candidate main set and 8-candidate stricter subset are source-reported predictions, not experimentally validated peptides.

### 中文

#### 3.1 候选空间缩减与分支核算

来源报告的健康和牙周炎分支分别从 11,269,961 和 11,721,988 条 sORF 开始。经证据过滤和去重，保留 31,510 条健康候选（占健康原始库 0.2796%）和 33,786 条牙周炎候选（占牙周炎原始库 0.2882%）。短、长分支之和均与各自证据过滤总数完全一致。这些数值描述的是计算保留率，而不是参与者层面的比例。

**表 1 聚合候选库与 BBB 高分输出**

| 分支 | 原始 sORF | 证据过滤候选 | 短分支背景（5–30 aa） | BBB 高分短候选，n（%） | 长分支背景（31–50 aa） | BBB 高分长候选，n（%） |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 健康 | 11,269,961 | 31,510 | 30,557 | 3,359（10.99） | 953 | 40（4.20） |
| 牙周炎 | 11,721,988 | 33,786 | 32,754 | 3,446（10.52） | 1,032 | 72（6.98） |

#### 3.2 BBB 和多活性输出的描述性结果

BBB 高分输出包括健康短候选 3,359/30,557（10.99%）和牙周炎短候选 3,446/32,754（10.52%）；长分支相应计数为 40/953（4.20%）和 72/1,032（6.98%）。本研究没有对这些并列比例进行推断性检验。

补充活性表保留了来源报告的全部 UniDL4BioPep 类别计数。短分支的抗菌标签是值得注意的输出分布特征：在统一 0.80 阈值下，健康候选 30,537/30,557（99.93%）和牙周炎候选 32,721/32,754（99.90%）为模型阳性。本稿不把接近全阳性的输出解释为实测生物活性流行率；相反，它提示在赋予模型阳性比例生物学含义之前，需要开展任务和序列域特异的校准。

#### 3.3 牙周炎分支后续优先排序

合并 3,446 条短 BBB 高分输出和 72 条长 BBB 高分输出后，牙周炎分支共有 3,518 条候选，其中短分支贡献 97.95%（3,446/3,518）。在来源报告的短候选长度汇总中，547 条为 5–7 aa、2,893 条为 8–15 aa、6 条为 16–30 aa；72 条长候选均为 31–50 aa。

NTxPred2 评价了 3,518 条候选中的 3,299 条（93.77%）；其余 219 条（6.23%）低于所述接受长度范围，未被评价。在已评价候选中，923/3,299（27.98%）预测阳性；来源称这 923 条均不超过 30 aa。

来源随后报告 mebipred 阈值下有 111 条候选呈 Cu/Fe/Zn 结合阳性。在该来源报告集合中，15/111（13.51%）满足 CHEL≥0.25；12/111（10.81%）进一步满足 FRS<0.50；8/111（7.21%）满足更严格的 FRS<0.45。把 FRS 从<0.50 收紧至<0.45 后，保留主集合中的 8/12（66.67%），并移除 4 条候选。由于缺少相应序列，无法列出候选身份。

**表 2 聚合层面的牙周炎分支优先排序记录**

| 阶段 | 操作性规则 | 报告计数 | 分母/证据说明 |
| --- | --- | ---: | --- |
| BBB 高分短候选 | UniDL4BioPep BBB 输出≥0.80；5–30 aa | 3,446 | 32,754 条短候选 |
| BBB 高分长候选 | UniDL4BioPep BBB 输出≥0.80；31–50 aa | 72 | 1,032 条长候选 |
| BBB 高分合并集合 | 合并两个长度分支 | 3,518 | 牙周炎后续集合 |
| NTxPred2 已评价 | 接受范围 7–50 aa | 3,299 | 219 条未评价 |
| NTxPred2 预测阳性 | 模型阳性 | 923 | 已评价 3,299 条 |
| 金属结合阳性 | mebipred 输出≥0.50 | 111 | 来源报告后续计数；缺少逐行交接 |
| CHEL 优先候选 | CHEL≥0.25 | 15 | 111 条来源报告金属阳性候选 |
| 操作性主集合 | CHEL≥0.25 且 FRS<0.50 | 12 | 111 条来源报告金属阳性候选 |
| 严格子集 | CHEL≥0.25 且 FRS<0.45 | 8 | 111 条来源报告金属阳性候选 |

![图 1 证据约束的聚合层面计算优先排序。](figures/prioritization_funnel.png)

**图 1** 证据约束的聚合层面计算优先排序。计数和操作性阈值转录自主证据记录；健康分支仅作描述性背景。虚线表示缺少进入 mebipred 的逐行交接，因此不把 111/923 写成经审计的转化率。12 条主集合和 8 条严格子集是来源报告的预测结果，并非实验验证肽。

## 4. Discussion / 4 讨论

### English

#### 4.1 Principal finding and bounded contribution

This study reconstructs a source-reported funnel from more than 11.7 million periodontitis-branch sORFs to 33,786 evidence-filtered candidates, 3,518 BBB-high outputs, 923 NTxPred2-positive outputs among 3,299 eligible candidates, 111 source-reported metal-binding-positive candidates, a 12-candidate main set, and an 8-candidate stricter subset. The arithmetic is internally consistent, and the funnel makes eligibility, positivity, non-evaluation, threshold sensitivity, and a missing row-level handoff explicit.

The contribution is nevertheless narrow. Serial use of established tools is not methodological innovation equivalent to a new predictor, and the aggregate record cannot support participant-level association. Most importantly, “12 candidates” is currently a count, not an actionable candidate table: the source package does not contain their sequences or scores. The present endpoint is therefore a transparent hypothesis-generation record rather than a validated discovery claim.

#### 4.2 Position relative to current smORF and oral-omics standards

Contemporary smORF studies combine complementary computational evidence with direct translation or proteomic measurements [1–3]. Durrant and Bhatt assessed enrichment for Ribo-seq/MetaRibo-seq signals rather than relying only on classifier agreement [2]. Davin et al. integrated smORF prediction with sample-resolved metatranscriptomics and deep metaproteomics [3]. In oral metaproteomics, Yuan et al. used microbial enrichment, explicit false-discovery control, taxonomic assignment, and deposited raw mass-spectrometry data [10]. Torres et al. illustrate a different but equally important principle: computationally prioritized microbiome peptides were synthesized and functionally tested before biological activity was claimed [17].

The present record does not meet those validation standards because it lacks sequence-level evidence, spectra, subject/sample mapping, and experiments. Exact matching to heterogeneous oral datasets remains useful as a search-space filter, but prior detection in a caries-risk, mixed oral-status, or lung-cancer dataset is not evidence of expression in the present periodontitis cohort. Likewise, a HOMD match is sequence/taxonomic evidence, not mass-spectrometric confirmation. These distinctions should guide both peer-review interpretation and any future reconstruction of the pipeline.

#### 4.3 Why aggregate group counts are not comparative statistics

The healthy and periodontitis candidate percentages are deterministic summaries of two computational branches. Peptides within a participant, homologous sequences across participants, and candidates produced by the same assembly are likely correlated. The millions of raw sORFs and tens of thousands of filtered candidates therefore cannot be treated as independent biological replicates. A nominal test using candidate counts would create pseudoreplication and an artificially large effective sample size.

A valid healthy-versus-periodontitis analysis would require participant/sample identifiers, a prespecified unit-level outcome, common processing denominators, candidate clustering/deduplication rules, and a statistical model that accounts for repeated sequences and participant-level covariates. None of these data were supplied. The descriptive differences in Table 1 consequently support no claim of enrichment, depletion, prevalence, risk, or disease specificity.

#### 4.4 Interpretation of serial predictor outputs

Cross-model filtering can improve operational tractability, but it does not turn correlated sequence descriptors into orthogonal evidence. UniDL4BioPep, NTxPred2, mebipred, and AnOxPePred were trained for different labels and have different applicability domains [11,14–16]. BBB-prediction studies themselves report challenges arising from small positive sets, class imbalance, threshold choices, and external-validation performance [12,13]. Short or compositionally unusual microbial candidates may differ from training distributions. The near-universal short-branch antimicrobial output further cautions against interpreting a common threshold as uniformly calibrated across tasks.

Model compatibility also structures the final set. The 219 BBB-high candidates outside the NTxPred2 length range are not negative; they are unclassified by that step. Downstream candidates are thus selected not only for predicted properties but also for acceptance by each model. Without row-level scores, alternative predictors, calibration data, or threshold curves, rank stability and domain shift cannot be quantified.

Metal-related outputs require similarly restrained language. Mebipred estimates binding potential rather than affinity or coordination chemistry [15]. AnOxPePred estimates antioxidant-related CHEL and FRS features [16]. CHEL≥0.25 with FRS<0.50 therefore denotes only a source-defined computational pattern. It does not demonstrate metal-dependent reactive-oxygen-species generation or a pro-oxidant mechanism.

#### 4.5 Neurodegenerative context without causal overreach

The study did not measure cognition, dementia, AD biomarkers, brain exposure, or an AD-relevant molecular target. Observational meta-analyses can motivate inquiry, particularly where severe periodontitis is associated with dementia outcomes [18,19,22], but heterogeneity and residual confounding limit causal interpretation. Oral-bacteria findings in AD remain inconsistent [20]. Mechanistic results involving *P. gingivalis* cannot establish that unassigned candidates originate from that species [21].

The causal boundary has become more important as genetic analyses have matured. Hu et al. reported no convincing genetic causal relationship between periodontal disease and AD in two-sample Mendelian-randomization analyses [23]. Zhao et al. reached a similar overall conclusion for AD in a 2026 systematic review and meta-analysis of Mendelian-randomization studies [24]. These findings do not exclude every non-genetic biological pathway, but they rule out presenting the present computational pattern as support for established periodontitis-to-AD causation. Here, BBB, toxicity, and metal-interaction labels define possible follow-up questions only.

#### 4.6 Evidence ladder and future validation

The most immediate requirement is not a complex disease experiment; it is recovery and release of candidate identities, row-level scores, and provenance. Sequence identity is needed to inspect duplicates, assign taxonomy, assess model applicability, reproduce predictions, and synthesize candidates. Translation/expression should then be tested with cohort-matched metatranscriptomics, ribosome profiling, or false-discovery-controlled targeted metaproteomics. Only expression-confirmed candidates should advance to BBB transport/permeability assays and neuronal toxicity tests.

Metal-related hypotheses require orthogonal binding measurements, ion-specific competition, stoichiometry/affinity estimation, metal-dependent reactive-oxygen-species assays, and appropriate peptide-only, metal-only, scrambled-sequence, positive, and negative controls. Disease-related experiments should be considered only after identity, exposure, phenotype, and biochemical mechanism are established. This ordering prevents later-stage plausibility from being used to compensate for missing earlier-stage evidence.

![Figure 2. Evidence ladder for interpretation.](figures/evidence_ladder.png)

**Figure 2.** Evidence ladder for interpretation. The current source package reaches aggregate computational prioritization only. Candidate identities and row-level scores are unavailable, and translation/expression, BBB transport, cellular toxicity, metal-dependent biochemical effects, and disease association/causality were not tested.

#### 4.7 Strengths and limitations

The study’s strengths are transparency and restraint. It provides explicit denominators, distinguishes non-evaluation from negativity, preserves a stricter threshold subset, makes the unauditable handoff visible, and separates prediction from mechanism. All displayed arithmetic can be reproduced with dependency-free code.

The limitations determine the allowable conclusion. First, absent sequences and row-level scores preclude independent reproduction, overlap analysis, calibration, taxonomic attribution, and candidate synthesis. Second, absent participant/sample mapping precludes biological inference and permits no uncertainty estimate for group contrasts. Third, original code, model versions, access dates, database snapshots, and random seeds were not supplied. Fourth, one named BioProject remains unresolved. Fifth, the short-branch evidence resources are heterogeneous, and the long-branch expression-evidence class is ambiguous. Sixth, the mebipred handoff denominator cannot be audited row by row. Seventh, threshold performance and predictor dependence cannot be assessed. Finally, no translational, proteomic, BBB, toxicological, metal-binding, oxidative, animal, or clinical endpoint was measured. These limitations cannot be corrected by statistical or linguistic refinement alone.

### 中文

#### 4.1 主要发现与有边界的贡献

本研究重建了一条来源报告的漏斗：从超过 1,172 万条牙周炎分支 sORF 缩减至 33,786 条证据过滤候选、3,518 条 BBB 高分输出、在 3,299 条符合长度要求的候选中得到 923 条 NTxPred2 阳性输出，随后得到来源报告的 111 条金属结合阳性候选、12 条主集合和 8 条严格子集。算术结果内部一致，且漏斗明确区分了模型适用、模型阳性、未评价、阈值敏感性和缺失的逐行交接。

然而，本研究的贡献范围较窄。串联使用现有工具不等同于开发新预测器的方法学创新，聚合记录也不能支持参与者层面的关联分析。更关键的是，“12 条候选”目前只是一个计数，而不是可操作的候选表：来源包不含其序列或分数。因此，当前终点是一份透明的假设生成记录，而不是已经验证的发现。

#### 4.2 与当前 smORF 和口腔组学标准的比较

当前 smORF 研究把互补计算证据与直接翻译或蛋白质组测量相结合 [1–3]。Durrant 和 Bhatt 评价了 Ribo-seq/MetaRibo-seq 信号富集，而不是只依赖分类器一致性 [2]；Davin 等把 smORF 预测与样本分辨的宏转录组及深度宏蛋白质组整合 [3]。在口腔宏蛋白质组领域，Yuan 等采用了微生物富集、明确的假发现率控制、分类学归属和原始质谱数据存储 [10]。Torres 等则说明了另一项同样重要的原则：对计算优先排序的微生物组肽完成合成和功能实验后，才主张其生物活性 [17]。

当前记录缺少序列级证据、谱图、受试者/样本映射和实验，因而没有达到上述验证标准。与异质口腔数据集的精确匹配仍可作为搜索空间过滤器，但在龋病风险、混合口腔状态或肺癌数据集中曾被检测到，并不能证明其在当前牙周炎队列中表达。同样，HOMD 匹配属于序列/分类学证据，而不是质谱确证。同行评审及未来重建流程时均应保留这些区分。

#### 4.3 为什么聚合组计数不能作为比较统计

健康和牙周炎候选比例只是两个计算分支的确定性汇总。来自同一参与者的肽、跨参与者同源序列，以及同一组装过程产生的候选很可能相关。因此，数百万条原始 sORF 和数万条过滤候选不能被当作相互独立的生物学重复。直接以候选计数进行名义检验会造成伪重复，并人为夸大有效样本量。

有效的健康—牙周炎分析需要参与者/样本标识、预设的单位层面结局、一致的处理分母、候选聚类/去重规则，以及能够处理重复序列和参与者协变量的统计模型。当前材料均未提供这些数据。因此，表 1 的描述性差异不支持富集、缺失、流行率、风险或疾病特异性主张。

#### 4.4 串联预测器输出的解释

跨模型过滤可以提高操作上的可处理性，但不能把相关的序列描述符变成彼此正交的证据。UniDL4BioPep、NTxPred2、mebipred 和 AnOxPePred 针对不同标签训练，适用域也不同 [11,14–16]。BBB 预测研究本身就报告了阳性样本较少、类别不平衡、阈值选择和外部验证性能等问题 [12,13]。极短或组成异常的微生物候选可能偏离训练分布；短分支接近全阳性的抗菌输出进一步提示，不应把统一阈值视为跨任务均已校准。

模型适用性本身也塑造了最终集合。219 条超出 NTxPred2 长度范围的 BBB 高分候选不是阴性，而是在该步骤未分类。因此，后续候选既因预测特征被筛选，也因能被各模型接受而被筛选。缺少逐行分数、替代预测器、校准数据和阈值曲线时，无法量化排序稳定性或域偏移。

金属相关输出同样需要克制表述。Mebipred 估计结合潜力，而不是亲和力或配位化学 [15]；AnOxPePred 估计与抗氧化有关的 CHEL 和 FRS 特征 [16]。所以，CHEL≥0.25 且 FRS<0.50 仅表示来源定义的计算模式，不能证明金属依赖性活性氧生成或促氧化机制。

#### 4.5 不作因果过度推断的神经退行性背景

本研究没有测量认知、痴呆、AD 生物标志物、脑暴露或 AD 相关分子靶点。观察性荟萃分析可以为研究提供动机，尤其是重度牙周炎与痴呆结局的关联 [18,19,22]，但异质性和残余混杂限制了因果解释；AD 中口腔细菌的研究结果也不一致 [20]。牙龈卟啉单胞菌相关机制结果不能证明未归属候选来源于该物种 [21]。

随着遗传分析发展，因果边界更加重要。Hu 等的双样本孟德尔随机化研究未发现令人信服的牙周病与 AD 遗传因果关系 [23]；Zhao 等 2026 年对孟德尔随机化研究的系统综述和荟萃分析，对 AD 得出相近的总体结论 [24]。这些结果不能排除所有非遗传生物通路，但足以否定把本研究计算模式写成已建立牙周炎→AD 因果关系的支持证据。本研究中的 BBB、毒性和金属相互作用标签仅定义可能的后续问题。

#### 4.6 证据阶梯与未来验证

最紧迫的要求不是直接开展复杂疾病实验，而是恢复并公开候选身份、逐行分数和来源信息。只有获得序列身份，才能检查重复、进行分类学归属、评价模型适用性、复现预测并合成候选。随后应采用队列匹配的宏转录组、核糖体测序或控制假发现率的靶向宏蛋白质组确认翻译/表达。只有表达得到确认的候选才适合进入 BBB 转运/通透和神经元毒性实验。

金属相关假设需要正交结合测量、离子特异性竞争、化学计量/亲和力估计、金属依赖性活性氧实验，以及仅肽、仅金属、打乱序列、阳性和阴性对照。只有在身份、暴露、表型和生化机制建立后，才应考虑疾病相关实验。这一顺序可避免用后期生物学合理性弥补早期证据缺失。

![图 2 解释证据阶梯。](figures/evidence_ladder.png)

**图 2** 解释证据阶梯。当前来源包仅达到聚合层面计算优先排序；候选身份和逐行分数不可用，且未检验翻译/表达、BBB 转运、细胞毒性、金属依赖性生化效应及疾病关联/因果性。

#### 4.7 优势与局限

本研究的优势在于透明和克制：提供明确分母；区分未评价与阴性；保留更严格阈值子集；显式标出无法审计的交接；区分预测与机制。所有展示的算术均可通过无外部依赖的代码复算。

局限决定了可作出的结论。第一，缺少序列和逐行分数，无法独立复现、分析重叠、评估校准、进行分类学归属或合成候选。第二，缺少参与者/样本映射，无法进行生物学推断，也不能估计组间对照的不确定性。第三，未提供原始代码、模型版本、访问日期、数据库快照和随机种子。第四，一个列出的 BioProject 仍未解决。第五，短分支证据资源异质，长分支表达证据类别不明确。第六，无法逐行审计 mebipred 的交接分母。第七，无法评估阈值性能和预测器依赖。最后，本研究未测量翻译、蛋白质组、BBB、毒理、金属结合、氧化、动物或临床终点。这些局限不能仅靠统计或语言润色消除。

## 5. Conclusions / 5 结论

### English

A source-reported serial prediction workflow reduced an aggregate periodontitis-cohort oral sORF space to a 12-candidate main count and an 8-candidate stricter count. The defensible result is an auditable, hypothesis-generating prioritization record—not a disease-specific peptide atlas or validated neurodegenerative mechanism. Release of sequence-level identities, scores, sample mappings, and original code is the minimum next step. Experimental claims should await cohort-matched expression evidence and staged transport, toxicity, and metal-dependent functional validation.

### 中文

来源报告的顺序预测流程把牙周炎队列口腔 sORF 聚合空间缩减为 12 条主候选计数和 8 条严格候选计数。可辩护的结果是一份可审计、用于假设生成的优先排序记录，而不是疾病特异性肽图谱或已验证的神经退行性机制。最低限度的下一步是公开序列身份、分数、样本映射和原始代码。只有获得队列匹配的表达证据，并依次完成转运、毒性和金属依赖性功能验证后，才可强化实验性主张。

## Declarations / 声明

### English

#### Ethics statement

The available materials described aggregate secondary computational analyses of public-data-derived sequences and contained no identifiable participant data. No new recruitment, intervention, or specimen collection was conducted for this reconstruction. The accountable authors and their institution must confirm whether the original data use and the proposed submission require ethics approval or an exemption; no approval number is inferred.

#### Consent for publication

No identifiable individual material is included in this draft. Any journal-required consent statement must be confirmed by the accountable authors.

#### Data availability

The principal record names PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727, and HOMD/eHOMD. PRJNA678453, PXD004319, PXD026727, and HOMD/eHOMD were linked to public records during drafting; PRJEB65451 remains unresolved. Candidate sequences, sample mappings, peptide-spectrum matches, taxonomic assignments, row-level model outputs, and final candidate identities were not included in the supplied package. Consequently, the primary analysis and final shortlist cannot be independently reproduced from this manuscript package. These artifacts should be recovered and deposited in a persistent repository before submission whenever possible.

#### Code availability

No executable code for the original sORF discovery, exact matching, deduplication, or predictor runs was supplied. Repository code reproduces document extraction, checksum verification, deterministic aggregate arithmetic, programmatic figures, bilingual assembly, and DOCX packaging only. It must not be represented as the original analysis pipeline.

#### Funding

Funding information was not supplied. The accountable authors must provide and verify the final funding statement.

#### Competing interests

An author-approved competing-interests statement was not supplied. Each accountable author must complete the journal’s declaration before submission.

#### Author contributions

Author identities and contributions were not supplied. CRediT roles, accountability, and final manuscript approval must be completed by the named human authors; authorship is not inferred from file provenance.

#### Use of generative AI

A generative-AI assistant supported source organization, bilingual drafting, deterministic arithmetic review, figure scripting, and language editing. It was not used to generate scientific data or to replace accountable author review and is not an author. Human authors must verify every datum, citation, translation, interpretation, and declaration and adapt this disclosure to the target journal’s policy.

### 中文

#### 伦理声明

可用材料描述的是公共数据衍生序列的聚合二次计算分析，不含可识别参与者数据。本次重建没有新增招募、干预或样本采集。责任作者及所在机构必须确认原始数据使用和拟投稿是否需要伦理批准或豁免；本稿不推定伦理批准号。

#### 发表同意

本草案不含可识别个体材料。期刊要求的任何同意声明均须由责任作者确认。

#### 数据可用性

主记录列出 PRJNA678453、PRJEB65451、PXD003151、PXD004319、PXD026727 和 HOMD/eHOMD。写作期间已将 PRJNA678453、PXD004319、PXD026727 和 HOMD/eHOMD 对应到公开记录；PRJEB65451 仍未解决。所提供材料不含候选序列、样本映射、肽谱匹配、分类学归属、逐行模型输出和最终候选身份。因此，无法根据当前稿件包独立复现主分析和最终候选清单。在条件允许时，应在投稿前恢复这些材料并存入持久化仓库。

#### 代码可用性

未提供原始 sORF 发现、精确匹配、去重或预测器运行的可执行代码。仓库代码仅复现文档提取、校验和验证、确定性聚合算术、程序化图形、中英文组装和 DOCX 打包，不得把它写成原始分析流程。

#### 经费

未提供经费信息。责任作者必须补充并核验最终经费声明。

#### 利益冲突

未提供经作者批准的利益冲突声明。每位责任作者必须在投稿前完成期刊要求的声明。

#### 作者贡献

未提供作者身份和贡献。CRediT 角色、责任归属和终稿批准必须由具名人类作者完成；不得根据文件来源推定作者资格。

#### 生成式人工智能的使用

生成式人工智能助手用于支持来源整理、中英文起草、确定性算术审查、图形脚本编写和语言编辑。它没有生成科学数据，也不替代责任作者审核，且不作为作者。人类作者必须核验每项数据、引文、翻译、解释和声明，并按照目标期刊政策调整此披露。

## References / 参考文献

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
3. Davin ME, Ortís Sunyer J, Delgado LF, et al. High-resolution multi-omics enhances prediction and detection of smORF-encoded proteins in the human gut microbiome. *Nat Commun*. 2026. doi:10.1038/s41467-026-72762-5.
4. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
5. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
6. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
7. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database (eHOMD): a resource for the microbiome of the human aerodigestive tract. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
8. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
9. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
10. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
11. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
12. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
13. Liu X, Zhao Z, Guan J, et al. Prediction of blood-brain barrier-penetrating peptides using B3BPFN. *Front Mol Biosci*. 2026;13:1858506. doi:10.3389/fmolb.2026.1858506.
14. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
15. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
16. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
17. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
18. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders: systematic review and meta-analysis. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
19. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis—a systematic review and meta-analysis of evidence from observational studies. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
20. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease: a systematic review and meta-analysis. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
21. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains: evidence for disease causation and treatment with small-molecule inhibitors. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
22. Kim J, Han DH. Periodontitis as a risk factor for dementia: a systematic review and meta-analysis. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
23. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
24. Zhao Y, Zhang C, Chang X, et al. Causal association between periodontitis and systemic diseases: a systematic review and meta-analysis of Mendelian randomization studies. *BMC Oral Health*. 2026;26:383. doi:10.1186/s12903-026-07725-9.
25. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.

*The reference list is shared by both language versions. / 中英文版本共用同一参考文献表。*
