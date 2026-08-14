# 深度学习引导的牙周炎—阿尔茨海默病界面口腔微肽多模型优选

## 摘要

**背景：** 阿尔茨海默病（Alzheimer’s disease，AD）涉及淀粉样蛋白、tau、神经免疫和血管异常的相互作用。牙周感染，特别是涉及牙龈卟啉单胞菌（*Porphyromonas gingivalis*）的感染，被认为可能参与这一多因素过程，但其在人类中的因果关系和分子链路仍未解决。

**目的：** 在由*P. gingivalis*启发、但不进行菌种来源指认的AD假设框架内，优选可供机制验证的口腔微肽候选。

**方法：** 对健康标记和牙周炎标记的口腔宏基因组候选集汇总记录实施深度学习引导的级联分析，整合蛋白质语言模型嵌入、任务特异性卷积神经网络、分层神经网络金属结合预测及多任务抗氧化预测。核查公共登录记录，以区分PRJNA678453来源队列与其衍生的EBI-EMG/MGnify第三方注释（TPA）组装项目PRJEB65451。来源报告乙酰胆碱酯酶（AChE）对接单独汇总，并仅进行描述性计算。

**结果：** 所提供漏斗始于11,269,961条健康标记和11,721,988条牙周炎标记smORF，分别保留31,510条和33,786条经蛋白质组支持的非冗余候选。后续汇总记录包含3,518条BBB高分候选；NTxPred2实际覆盖3,299条，其中923条被判为神经毒性阳性。金属结合和抗氧化筛选依次保留111、15、12和最终8条候选。另一份外部记录列出12条序列，首尾为FLLHTTR和HVLLLRQCA，并报告其针对AChE的Vina均值范围为−9.60至−8.25 kcal/mol。

**结论：** 本分析得到的是用于后续验证的紧凑计算候选集，而非已经证实的牙周炎—AD机制。序列来源链、菌种归属、独立对接复现和实验验证仍不可缺少。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微肽；宏基因组学；机器学习；乙酰胆碱酯酶

## 引言

阿尔茨海默病（Alzheimer’s disease，AD）是一种进行性神经退行性疾病，也是痴呆的首要原因，其病理连续过程可在明显认知障碍出现前多年启动[1]。当前疾病模型将淀粉样蛋白β积累置于tau病理、突触功能障碍、先天免疫激活和神经血管损伤相互作用的网络中，而不再把疾病进展归因于单一通路[2]。

牙周炎是一种与菌群失调相关的慢性炎症性疾病，其潜在神经系统影响推动了口腔—脑轴研究[3]。在失调性牙周生物膜中，牙龈卟啉单胞菌（*Porphyromonas gingivalis*）是一种具有显著免疫调节和组织破坏能力的革兰阴性厌氧条件致病菌[4]。溃疡化牙周界面可能使机体间歇性暴露于细菌、炎症介质和毒力产物，从而为局部口腔感染影响远隔组织提供生物学上合理的路径。

多条互不排斥的路径可能连接*P. gingivalis*暴露与AD相关分子过程。一项死后组织研究在AD脑组织中报告了*P. gingivalis* DNA和牙龈蛋白酶免疫反应性，但这些观察尚不足以确定方向性或因果关系[5]。在野生型小鼠中，反复口腔感染引起神经炎症和淀粉样蛋白相关改变，支持实验可行性，但不能直接外推到人类[6]。另一项小鼠研究显示，*P. gingivalis*外膜囊泡可到达脑组织，并与炎症小体激活、tau磷酸化和记忆功能障碍相关[7]。相反，一项双样本孟德尔随机化分析未发现牙周病导致AD的遗传学证据，进一步表明人类因果关系仍未解决[8]。

因此，牙周菌群失调与神经退行性改变之间的分子桥梁仍不完整。人类相关微生物组中广泛存在小开放阅读框，并编码数量庞大但尚未得到充分表征的肽分子库[9]。计算注释能够发现常规基因识别流程容易遗漏的候选小蛋白[10]。牙周炎标记口腔宏基因组候选集所代表的肽是否真实表达、能否从生物膜释放并进入循环、能否跨越血脑屏障（BBB），以及是否会影响神经元、金属/氧化还原或胆碱能过程，均属尚未解决的机制空白。为此，本研究实施深度学习引导的多模型优选，以形成可开展来源链重建和实验验证的候选集合。本分析明确保持探索性定位，不把候选归属于*P. gingivalis*，也不把模型分数视为AD机制证据。

## 材料与方法

### 研究设计与登录号来源

本研究为基于所提供汇总筛选记录的结构化描述性二次分析。记录包含健康标记和牙周炎标记候选的汇总数量，但不含参与者层面映射、登录号—分组对应表或逐行模型输出。

主要序列来源为BioProject PRJNA678453。已发表队列共22名参与者，包括11名口腔健康对照和11名牙周炎患者；共采集66份口腔标本，包括22份龈下菌斑、22份舌刮取物和22份刺激性唾液，并完成配对宏基因组和宏转录组测量[11]。PRJEB65451经核验为由PRJNA678453衍生、使用metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的第三方注释宏基因组组装项目，而不是独立临床队列。ENA记录目前在PRJEB65451下列出118项序列组装分析；这些组装记录不被解释为参与者、临床标本或宏基因组组装基因组。由于该登录号链及队列论文不支持24名健康对照、26名牙周炎患者和296个高质量宏基因组组装基因组的另一种构成，本研究不使用这些数量。经核验的临床构成仅用于说明来源，不作为候选层面推断的分母。

### 候选定义与蛋白质组证据过滤

根据归档的汇总流程，编码4–50 aa肽的推定小开放阅读框按来源提供的健康状态标签分组。候选序列与来源记录中的口腔蛋白质组资源进行精确匹配，包括PXD003151、PXD004319、PXD026727及HOMD相关蛋白序列。精确匹配结果经去重后形成非冗余、具有蛋白质组支持的候选集合。由于逐序列输入和匹配表不可得，该阶段按来源报告过滤步骤处理，未被独立重新运行。

### 深度学习引导的多模型优选

本研究采用串行架构，依次整合上下文序列表征、任务特异性深度分类、分层金属结合预测和多任务抗氧化评分。各阶段回答不同的生物学优选问题，因此下游保留代表串行决策规则，而不是相互独立的实验确证。

首先，UniDL4BioPep使用预训练ESM-2模型`esm2_t6_8M_UR50D`，将每条肽转换为320维上下文敏感嵌入。该嵌入随后输入针对不同肽活性任务分别训练的六层深度卷积神经网络[12]。预测概率≥0.8定义为高置信度模型输出，仅BBB概率≥0.8的候选进入后续级联。

其次，采用肽特异性NTxPred2架构评价神经毒性。该模型通过迁移学习，在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[13]。分析仅覆盖模型规定的7–50 aa输入范围；长度小于7 aa的序列记录为模型覆盖范围之外，而不视为阴性预测。

第三，采用mebipred评价Cu、Fe和Zn相关结合潜力。该方法将氨基酸组成、理化描述符和金属结合5-mer频率整合到两级人工神经网络框架中：先由一般金属结合网络进行判定，再进入离子特异性神经分类器[14]。来源记录中的判定阈值为0.5。

第四，采用多任务深度卷积神经网络AnOxPePred评价抗氧化相关特征。经one-hot编码的肽序列依次通过一维卷积层、平均池化和含256个单元的全连接层，最终分别输出自由基清除（FRS）和螯合（CHEL）分数[15]。首先应用CHEL≥0.25阈值，再应用来源记录中的CHEL/FRS组合标准。

本次二次分析未重新训练或微调任何模型。历史网页服务器构建版本、模型哈希、随机种子、提交输入文件及逐行输出均未被保存。因此，上述算法说明记录的是文献所述架构及与本研究相关的肽模式，而阈值和保留数量仍属于来源报告的汇总记录。

### 外部序列表征与对接证据

外部12条序列记录作为独立证据层分析，不与汇总筛选漏斗进行逐行合并。使用版本控制代码直接依据序列字符串重新计算序列长度、分子质量、名义电荷、疏水残基比例和氨基酸组成。

AChE被选作结构分析背景靶点，是因为已有研究报告该酶可通过外周区域加速淀粉样蛋白β纤维形成[16]。外部记录指定人AChE结构PDB 4EY6，该结构具有配体结合结构信息[17]。Vina均值和标准差按来源报告精确转录。由于受体及配体原始文件、质子化状态、网格定义、构象、日志和逐次运行分数均不可得，本研究未重新运行对接，也不推断接触模式、亲和力或功能。该12条外部序列无法映射到更严格的8条汇总终点集。

### 统计分析与证据解释

所有分析均为描述性分析。保留率以前一个有记录的阶段作为分母。候选序列属于计算记账单位，而不是独立参与者或生物学重复，因此未开展健康—牙周炎假设检验、置信区间估计或肽层面推断模型，也未对缺失的逐行数据进行插补。

Vina分数仅用于来源记录内部排序，不被解释为实验亲和力或结合自由能[18]。当前Vina实现虽改进了搜索和力场选项，但仍无法消除受体准备、搜索空间定义及采样设置的影响[19]。鉴于蛋白质—肽识别可能涉及分散的界面热点片段，单一刚性受体对接排序不被转化为机制结论[20]。

## 结果

### 汇总优选漏斗

来源提供11,269,961条健康标记和11,721,988条牙周炎标记smORF。经蛋白质组匹配和去重后分别保留31,510条和33,786条候选，占各自起始库的0.2796%和0.2882%。后续记录包含3,518条BBB高分候选。219条长度小于7 aa的序列超出所记录的NTxPred2输入范围，NTxPred2对3,299条序列给出预测，其中923条标记为神经毒性阳性。面向Cu/Fe/Zn的mebipred筛选保留111条；AnOxPePred在CHEL≥0.25时保留15条，按记录的组合标准保留12条，最终优选8条。

**表1. 汇总计算筛选漏斗。计数为描述性计算记账单位。**

| 阶段 | 保留数量 | 证据状态 |
| --- | ---: | --- |
| 健康标记smORF | 11,269,961 | 来源汇总计数 |
| 牙周炎标记smORF | 11,721,988 | 来源汇总计数 |
| 蛋白质组支持的健康标记候选 | 31,510 | 来源汇总计数 |
| 蛋白质组支持的牙周炎标记候选 | 33,786 | 来源汇总计数 |
| BBB概率≥0.8 | 3,518 | 来源模型汇总 |
| NTxPred2实际输出 | 3,299 | 来源模型汇总 |
| 神经毒性阳性 | 923 | 来源模型汇总 |
| Cu/Fe/Zn金属结合阳性 | 111 | 来源模型汇总 |
| CHEL≥0.25 | 15 | 来源模型汇总 |
| 组合筛选 | 12 | 来源模型汇总 |
| 最终严格集 | 8 | 成员未知 |

![汇总计算优选漏斗](../figures/prioritization_funnel.png)

**图1.** 汇总计算优选漏斗。该图汇总来源计数，不代表参与者流程或独立生物学重复。

### 外部12条序列记录

外部记录列出12条互不重复的肽。其针对AChE的来源报告Vina均值范围为−9.60至−8.25 kcal/mol。在该记录内部，FLLHTTR排序第一，HVLLLRQCA排序最后。序列组成经独立重算，但对接构象和分数未被独立复现。

**表2. 外部序列记录及来源报告AChE对接汇总。**

| 排名 | 序列 | 长度（aa） | 来源报告均值（kcal/mol） | 来源报告SD |
| ---: | --- | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | −9.60 | 0.08 |
| 2 | KNGIYHLK | 8 | −9.42 | 0.06 |
| 3 | KNAIRLQ | 7 | −9.31 | 0.05 |
| 4 | NRPPHPPY | 8 | −9.18 | 0.09 |
| 5 | QMMKQAQK | 8 | −9.05 | 0.07 |
| 6 | WNMSKYYK | 8 | −8.94 | 0.04 |
| 7 | YPWINHPQ | 8 | −8.83 | 0.10 |
| 8 | WVAHKNY | 7 | −8.71 | 0.06 |
| 9 | YPIVIHPN | 8 | −8.58 | 0.11 |
| 10 | YDRNWNNK | 8 | −8.46 | 0.08 |
| 11 | RKQIKRYL | 8 | −8.34 | 0.05 |
| 12 | HVLLLRQCA | 9 | −8.25 | 0.12 |

## 讨论

本分析把规模很大的来源候选池压缩为两个边界清楚的后续对象：一个成员信息缺失的8条汇总终点集，以及一份独立的12条外部序列记录。其价值在于优选和定位证据缺口，而不是发现已经验证的AD机制。

本研究的生物学动机始于牙周炎—AD界面。*P. gingivalis*感染可合理地关联于系统性炎症信号、LPS和牙龈蛋白酶暴露、囊泡介导的成分运输、BBB扰动及小胶质细胞激活[3–7]。候选流程进一步提出：口腔微生物肽是否可能构成一类尚少研究、并具有BBB、神经毒性、金属/氧化还原或AChE相关预测特征的分子。然而，本研究结果均未证明候选在来源参与者中表达、从口腔生物膜释放、进入循环、跨越BBB、影响神经系统或具有AD特异性。尤其重要的是，汇总来源不能证明任何候选由*P. gingivalis*编码；该菌在本文中是机制研究动机，而不是已确定的序列来源。

经核验的登录号关系也改变了输入数据的表述方式。PRJNA678453是11名健康对照、11名牙周炎患者和66份标本的原始队列；PRJEB65451则是衍生TPA组装资源。参与者、临床标本、配对DNA/RNA测量和组装分析属于不同统计单位，不能混用。由于缺少参与者—序列映射，两组近似的汇总保留率不能支持疾病富集结论。

本研究存在数项决定性局限。第一，逐行模型输出和精确服务器版本缺失，阈值及计数只能在汇总层面审计。第二，8条与12条的成员关系仍未解决。第三，对接记录缺少复现及检查构象所需材料。第四，基于异质数据集训练的预测器可能不适用于极短的微生物组来源肽；多个模型结果一致也不等同于实验独立性。合理的下一步是恢复候选来源链，使用固定版本重新运行预测和对接，继而检验合成质量、稳定性、细胞毒性、BBB转运、金属相互作用、AChE活性以及神经元或胶质细胞表型，之后再讨论疾病机制。

## 结论

汇总证据支持形成一个透明的待验证候选清单，但不支持从牙周炎或*P. gingivalis*到AD的因果链。核正后的来源为：PRJNA678453是包含22名参与者、66份口腔标本的来源队列；PRJEB65451是其衍生的EBI-EMG/MGnify TPA组装项目。12条外部序列及其来源报告AChE分数仍与成员未知的最终8条集合分离。恢复逐行来源并完成独立计算和实验验证，是进行机制解释的前提。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397:1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ. Treatments for Alzheimer’s disease emerge. *Nature*. 2023;616:33–34. doi:10.1038/s41586-023-05769-3.
3. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98:220–227. doi:10.1111/prd.12631.
4. Liu S, Butler CA, Ayton S, Reynolds EC, Dashper SG. *Porphyromonas gingivalis* and the pathogenesis of Alzheimer’s disease. *Crit Rev Microbiol*. 2024;50:127–137. doi:10.1080/1040841X.2022.2163613.
5. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains: evidence for disease causation and treatment with small-molecule inhibitors. *Sci Adv*. 2019;5:eaau3333. doi:10.1126/sciadv.aau3333.
6. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13:e0204941. doi:10.1371/journal.pone.0204941.
7. Gong T, Chen Q, Mao H, et al. Outer membrane vesicles of *Porphyromonas gingivalis* trigger NLRP3 inflammasome and induce neuroinflammation, tau phosphorylation, and memory dysfunction in mice. *Front Cell Infect Microbiol*. 2022;12:925435. doi:10.3389/fcimb.2022.925435.
8. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14:e3486. doi:10.1002/brb3.3486.
9. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178:1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
10. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Nat Microbiol*. 2021;6:564–574. doi:10.1038/s41564-021-00891-0.
11. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *NPJ Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
12. Du Z, Ding X, Xu Y, Li W. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24:bbad135. doi:10.1093/bib/bbad135.
13. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34:e70200. doi:10.1002/pro.70200.
14. Valasatava Y, Rosato A, Banci L, Andreini C. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38:3532–3540. doi:10.1093/bioinformatics/btac358.
15. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
16. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16:881–891. doi:10.1016/S0896-6273(00)80108-7.
17. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55:10282–10286. doi:10.1021/jm300871x.
18. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking. *J Comput Chem*. 2010;31:455–461. doi:10.1002/jcc.21334.
19. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61:3891–3898. doi:10.1021/acs.jcim.1c00203.
20. London N, Raveh B, Schueler-Furman O. Druggable protein–protein interactions—from hot spots to hot segments. *Curr Opin Chem Biol*. 2013;17:952–959. doi:10.1016/j.cbpa.2013.10.011.
