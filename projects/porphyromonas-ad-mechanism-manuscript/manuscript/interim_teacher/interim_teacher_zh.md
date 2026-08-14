# 牙周炎队列口腔微肽的汇总优选及来源报告乙酰胆碱酯酶对接随访

**文章类型：** 阶段性原创研究简稿  
**用途：** 供导师阶段性审阅；完整稿继续以已归档的v3.0.0版本维护。

## 摘要

**背景：** 小开放阅读框（smORF）是口腔微生物组中尚未被充分刻画的组成部分。计算模型可用于候选肽优选，但不能证明翻译、血脑屏障（BBB）转运、毒性、靶标结合或疾病因果关系。

**方法：** 本研究重建牙周炎队列口腔smORF筛选记录中的汇总计数。流程包括证据过滤、UniDL4BioPep BBB评分、NTxPred2、mebipred及AnOxPePred CHEL/FRS阈值，并独立重算比例。另一份外部v0.4记录提供12条肽序列及其针对人乙酰胆碱酯酶（AChE；PDB 4EY6）的AutoDock Vina均值±SD。研究核验了序列组成和分数排序；由于缺少原始输入、配置、日志和构象，未重跑对接。

**结果：** 证据过滤后，健康分支保留31,510/11,269,961条smORF，牙周炎分支保留33,786/11,721,988条。牙周炎分支包含3,518条BBB高分候选；NTxPred2评估3,299条，其中923条为阳性。来源随后报告111条金属结合阳性候选，其中15条满足CHEL≥0.25，12条同时满足CHEL≥0.25和FRS<0.50，8条满足FRS<0.45。外部记录列出12条互不重复的7–9 aa序列；11条含组氨酸，6条含半胱氨酸，全部含Arg或Lys。报告Vina均值为−9.60至−8.25 kcal/mol。

**结论：** 合并证据形成一套简短、可检验的候选集合，但不能证明牙周炎特异性、脑暴露、神经毒性、AChE结合或阿尔茨海默病机制。仍需逐行筛选链路、可复现对接产物和实验验证。

**关键词：** 口腔微生物组；smORF；微肽；牙周炎；乙酰胆碱酯酶；分子对接；计算优选

## 1. 引言

微生物组smORF编码规模巨大但注释不完整的肽空间。大规模研究发现了数千个保守小基因，专用预测系统也提高了短编码序列的识别能力 [1,2]。然而，预测smORF不一定被翻译，被翻译的肽也不一定稳定或具有生物活性。

牙周炎与口腔微生物组成及基因表达变化相关 [3,4]。疾病相关解释仍需要参与者层面的映射、适当标准化，以及对重复或同源序列的处理。与口腔数据库或异质性蛋白质组数据精确匹配可以支持序列存在，但不能独立证明当前队列表达或牙周炎特异性。

肽预测器可用于实际筛选。UniDL4BioPep预测多类肽活性标签 [5]；BBB模型估计与穿透相关的序列模式 [6]；NTxPred2预测神经毒性肽标签 [7]；mebipred估计金属结合潜力 [8]；AnOxPePred预测螯合和自由基清除特征 [9]。这些输出属于优选标签，而不是实验观察。因此，有说服力的肽发现还需化学合成和功能测定 [10]。

AChE随访具有一定生物学意义，因为胆碱能功能障碍与阿尔茨海默病（AD）相关 [11]，AChE也可通过涉及外周阴离子位点（PAS）的区域加速淀粉样β装配 [12]。人AChE结构4EY6可用于生成结构假设 [13]。金属稳态失衡同样与AD相关聚集和氧化生物学有关 [14]。这些研究可提出实验问题，但不能证明口腔肽进入脑组织或改变AChE/Aβ过程。

本阶段研究仅回答一个有限问题：现有汇总筛选记录和独立报告的序列/对接汇总能够支持怎样的候选集合？目标是简要呈现数值漏斗、可用序列和后续验证步骤，而不是建立机制。

## 2. 材料与方法

### 2.1 研究设计与证据来源

主要来源为健康和牙周炎口腔宏基因组分支的汇总计算记录，其中包含筛选计数、阈值和流程描述，但不含候选逐行数据、样本映射或可执行管线代码。用户指定的外部v0.4仓库另行提供12条序列字符串及Vina均值±SD。外部信息按作者报告汇总处理，不作为独立复现分析。

### 2.2 汇总筛选流程

据主要记录，4–50 aa翻译smORF经证据过滤和去冗余后，分为短肽（5–30 aa）和长肽（31–50 aa）分支。UniDL4BioPep BBB输出≥0.80定义为“BBB高分” [5]。牙周炎BBB高分集合在NTxPred2声明的7–50 aa范围内接受筛选 [7]，随后使用阈值0.50的mebipred [8]以及AnOxPePred CHEL/FRS阈值 [9]。主要终点为CHEL≥0.25且FRS<0.50，更严格终点使用FRS<0.45。

来源没有提供NTxPred2至mebipred的逐行交接。因此，111条仅保留为来源报告下游计数，不将111/923解释为经审计的转换率。

### 2.3 外部序列与对接汇总

研究检查12条外部序列的唯一性、标准氨基酸字符、长度、组氨酸、半胱氨酸、碱性残基（Arg+Lys）和芳香残基。外部记录称使用AutoDock Vina 1.2.5，将肽对接到人AChE PDB 4EY6的40×40×40 Å³ PAS中心盒 [13,18,19]。本研究转录均值和SD并检查排序及范围。

由于缺少受体/配体制备文件、精确网格中心、质子化和电荷设置、配置、exhaustiveness、种子、原始运行、日志及构象，本研究没有重跑对接。Vina分数不解释为结合亲和力或自由能 [18,19]。

### 2.4 统计方法

所有分析均为描述性分析，比例按100×n/N重算。由于缺少受试者/样本映射和聚类信息，候选肽不被视为独立生物学重复。因此，没有计算健康与牙周炎比较的p值或置信区间。

## 3. 结果

### 3.1 汇总优选漏斗

证据过滤后，健康分支保留31,510/11,269,961条smORF（0.2796%），牙周炎分支保留33,786/11,721,988条（0.2882%）。短肽分支BBB高分分别为3,359/30,557（10.99%）和3,446/32,754（10.52%），长肽分支分别为40/953（4.20%）和72/1,032（6.98%）。

牙周炎分支共有3,518条BBB高分候选。NTxPred2评估3,299条（93.77%），219条低于声明输入范围；已评估候选中923/3,299（27.98%）为模型阳性。下游记录报告111条mebipred阳性、15条CHEL优选、12条主候选和8条更严格候选（表1）。

**表1. 简化汇总筛选结果**

| 阶段 | 规则/状态 | 牙周炎分支，n | 解释 |
| --- | --- | ---: | --- |
| 证据过滤后 | 精确匹配过滤及去冗余 | 33,786 | 计算保留 |
| BBB高分 | UniDL4BioPep输出≥0.80 | 3,518 | 预测标签，不是实测BBB转运 |
| NTxPred2已评估 | 声明范围7–50 aa | 3,299 | 219条未评估 |
| NTxPred2阳性 | 模型阳性 | 923 | 不是实验神经毒性 |
| 金属结合阳性 | mebipred≥0.50 | 111 | 来源报告下游计数 |
| CHEL优选 | CHEL≥0.25 | 15 | 操作性过滤 |
| 主集合 | CHEL≥0.25；FRS<0.50 | 12 | 候选计数 |
| 更严格集合 | CHEL≥0.25；FRS<0.45 | 8 | 成员未知 |

### 3.2 外部报告的12条序列

外部记录列出12条互不重复的7–9 aa序列（表2）。11条含组氨酸，6条含半胱氨酸，每条至少含一个Arg或Lys。该集合较短、带正电且富亮氨酸，但组成不能证明金属结合、膜转运、毒性或分类归属。

**表2. 外部序列及来源报告Vina汇总**

| 序列 | 长度 | His | Cys | 报告Vina均值±SD（kcal/mol） |
| --- | ---: | ---: | ---: | ---: |
| FLLHTTR | 7 | 1 | 0 | −9.60±0.08 |
| YLSLLQR | 7 | 0 | 0 | −9.49±0.05 |
| ALLLHRC | 7 | 1 | 1 | −9.29±0.11 |
| FCLHLQLR | 8 | 1 | 1 | −9.27±0.09 |
| YHHLLCRR | 8 | 2 | 1 | −9.03±0.07 |
| LLHLPKRTT | 9 | 1 | 0 | −9.01±0.06 |
| LLHPLRL | 7 | 1 | 0 | −8.94±0.10 |
| WLLVHLKK | 8 | 1 | 0 | −8.94±0.04 |
| LLHPLRC | 7 | 1 | 1 | −8.91±0.08 |
| HLLTLKKHV | 9 | 2 | 0 | −8.88±0.05 |
| HLPLLHRCC | 9 | 2 | 2 | −8.35±0.12 |
| HVLLLRQCA | 9 | 1 | 1 | −8.25±0.09 |

![图1. 来源报告对接分数汇总](../figures/fig5_docking_scores.png)

**图1.** 针对人AChE PDB 4EY6的来源报告AutoDock Vina均值±SD。数值未被独立复现；运行定义和构象不可用。

### 3.3 当前证据边界

外部序列清单使合成规划成为可能，但不能说明哪些主要来源行对应这12条字符串，也不能确定更严格8条的成员。对接汇总同样只提供报告的集合内排序。翻译、BBB转运、毒性、金属依赖效应、AChE功能和疾病相关性均未测试。

## 4. 讨论

本阶段重建在保留来源局限的同时，形成了一套具体的12条序列假设集合。汇总漏斗内部算术一致，展示了串联模型如何从数百万条smORF逐步缩小范围。然而，逐行来源几乎完全缺失，因此无法进行受试者层面的组间分析，也不能独立复现候选选择。

报告的对接排序增加了一个结构问题，而不是结合结果。Vina适合快速生成构象和分数 [18,19]，但短柔性肽具有大量构象，其排序可能受端基、质子化、初始构象、受体柔性、盒位置和搜索设置影响。完整输入和构象发布后，可采用柔性肽精修方法开展进一步分析 [20]。在此之前，不应对残基接触、PAS选择性或分数差异作机制解释。

生物学假设也仍处于初步阶段。观察性研究报告牙周炎与认知障碍相关，但结果受病例定义和研究设计影响 [15]。孟德尔随机化目前不支持强牙周病—AD因果效应 [16]，近期综述也继续强调不确定性 [17]。因此，应将这些候选描述为来自牙周炎队列分析分支，而不是疾病特异性介质。

下一阶段应首先恢复序列—样本和序列—模型链路。随后可合成12条肽，检查纯度、稳定性、非特异膜破坏、BBB转运、神经毒性和Cu/Fe/Zn结合。只有具备可重复生化和暴露证据的候选才进入AChE活性和Aβ聚集实验。实验需要打乱肽、组成匹配、肽单独和金属单独对照。

主要局限包括候选逐行数据缺失、严格子集成员未知、预测器执行记录缺失以及对接输入/构象不可用。本研究没有开展实验验证。因此，当前工作属于计算优选报告，而不是机制研究。

## 5. 结论

现有记录支持一条汇总筛选漏斗，以及一套具有AChE对接分数排序的来源报告12序列清单，但不能建立靶标结合、生物活性、疾病特异性或因果关系。本阶段分析的主要价值是形成可管理的候选集合，并为下一步可重复计算和实验随访提供透明计划。

## 参考文献

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178:1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29:121–131.e4. doi:10.1016/j.chom.2020.11.002.
3. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
4. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
5. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24:bbad135. doi:10.1093/bib/bbad135.
6. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
7. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34:e70200. doi:10.1002/pro.70200.
8. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38:3532–3540. doi:10.1093/bioinformatics/btac358.
9. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
10. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187:5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
11. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397:1577–1590. doi:10.1016/S0140-6736(20)32205-4.
12. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16:881–891. doi:10.1016/s0896-6273(00)80108-7.
13. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55:10282–10286. doi:10.1021/jm300871x.
14. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
15. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52:afad015. doi:10.1093/ageing/afad015.
16. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14:e3486. doi:10.1002/brb3.3486.
17. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98:220–227. doi:10.1111/prd.12631.
18. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31:455–461. doi:10.1002/jcc.21334.
19. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61:3891–3898. doi:10.1021/acs.jcim.1c00203.
20. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
