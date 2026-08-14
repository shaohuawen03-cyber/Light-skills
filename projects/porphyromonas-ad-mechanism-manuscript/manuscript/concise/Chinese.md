# 牙周炎—阿尔茨海默病界面口腔微肽的汇总优选

## 摘要

**背景：** 阿尔茨海默病（Alzheimer’s disease，AD）涉及淀粉样蛋白、tau、神经免疫和血管异常的相互作用。牙周感染，特别是涉及牙龈卟啉单胞菌（*Porphyromonas gingivalis*）的感染，被认为可能参与这一多因素过程，但其在人类中的因果关系和分子链路仍未解决。

**目的：** 在由*P. gingivalis*启发、但不进行菌种来源指认的AD假设框架内，优选可供机制验证的口腔微肽候选。

**方法：** 对健康标记和牙周炎标记的口腔宏基因组候选集汇总记录进行蛋白质组支持、血脑屏障（BBB）、神经毒性、金属结合、抗氧化预测及来源报告乙酰胆碱酯酶（AChE）对接筛选。核查公共登录记录，以区分PRJNA678453来源队列与其衍生的EBI-EMG/MGnify第三方注释（TPA）组装项目PRJEB65451。仅进行描述性计算。

**结果：** 所提供漏斗始于11,269,961条健康标记和11,721,988条牙周炎标记smORF，分别保留31,510条和33,786条经蛋白质组支持的非冗余候选。后续汇总记录包含3,518条BBB高分候选；NTxPred2实际覆盖3,299条，其中923条被判为神经毒性阳性。金属结合和抗氧化筛选依次保留111、15、12和最终8条候选。另一份外部记录列出12条序列，首尾为FLLHTTR和HVLLLRQCA，并报告其针对AChE的Vina均值范围为−9.60至−8.25 kcal/mol。

**结论：** 本分析得到的是用于后续验证的紧凑计算候选集，而非已经证实的牙周炎—AD机制。序列来源链、菌种归属、独立对接复现和实验验证仍不可缺少。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微肽；宏基因组学；机器学习；乙酰胆碱酯酶

## 引言

阿尔茨海默病是一种进行性神经退行性疾病，淀粉样蛋白β积累、tau病理、突触功能障碍、神经炎症和血管异常可在漫长的临床前阶段相互作用[1,2]。这些过程具有明显异质性，不能被简化为单一的感染、炎症或蛋白聚集通路。

牙龈卟啉单胞菌是一种与失调性牙周生物膜相关的革兰阴性厌氧条件致病菌。牙周炎可增加机体反复暴露于口腔微生物、炎症介质和微生物产物的机会。因此，实验研究和死后组织研究提出了多条连接*P. gingivalis*与AD相关病理的可能路径：循环炎症可能影响BBB完整性并激活小胶质细胞；脂多糖和牙龈蛋白酶可能扰动宿主信号与蛋白稳态；外膜囊泡则可能把毒力成分带离牙周生态位[3–7]。这些发现为研究提供了生物学上合理的假设，但不能证明*P. gingivalis*在人类中导致AD。现有证据具有异质性，而且一项双样本孟德尔随机化研究未发现牙周病导致AD的遗传学证据[8]。

另一个尚未解决的机制空白涉及口腔微生物群编码的小蛋白和小肽。微生物组研究表明，小开放阅读框广泛存在，并可能编码此前未知的生物活性分子[9,10]。目前尚不清楚牙周炎标记候选集所代表的口腔微生物肽能否进入循环、跨越BBB、影响神经元或胶质细胞、扰动金属/氧化还原稳态或调节AChE；本研究所考察的候选是否源于*P. gingivalis*同样未知。因此，本研究开展探索性的汇总层面优选，以确定一组可供来源链重建和实验检验的候选，同时不把计算标签视为生物学验证。

## 材料与方法

### 研究设计与数据来源核验

本研究为基于所提供汇总计数的描述性二次分析。来源材料将健康标记和牙周炎标记候选集归于BioProject PRJNA678453及PRJEB65451。登录号核查表明，PRJEB65451并非独立临床队列，而是由PRJNA678453衍生、经metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的TPA宏基因组组装项目。已发表来源队列共22名参与者，包括11名口腔健康对照和11名牙周炎患者；每名参与者采集三个口腔部位标本，共66份标本，包括22份龈下菌斑、22份舌刮取物和22份刺激性唾液标本，并进行了配对宏基因组和宏转录组测量[11]。ENA项目页面目前在PRJEB65451下列出118项序列组装分析；这些是组装记录数，而不是参与者数或临床标本数。

所提供汇总数据不含参与者层面映射、登录号—分组对应表或逐序列模型输出。因此，经核验的11比11队列构成仅用于说明来源，不能作为候选层面推断的分母。来源材料所述24名健康对照、26名牙周炎患者及296个高质量宏基因组组装基因组未予保留，因为这些数字无法由PRJNA678453、PRJEB65451或队列论文证实。

### 汇总筛选与预测算法

所提供流程从按健康状态标记的4–50 aa smORF开始。通过与口腔蛋白质组资源进行精确序列匹配并去重，获得有蛋白质组支持的候选集。UniDL4BioPep预测概率≥0.8定义为高置信度功能预测，BBB概率≥0.8的候选进入下游筛选。NTxPred2仅用于其记录的7–50 aa输入范围；mebipred以0.5为阈值评估Cu/Fe/Zn相关金属结合潜力；AnOxPePred先按CHEL≥0.25筛选，再应用记录中的FRS标准。

这些网站并非采用统一的“深度学习”方法。UniDL4BioPep首先使用预训练ESM-2模型`esm2_t6_8M_UR50D`把肽序列表示为320维嵌入，再输入六层卷积神经网络进行任务特异性二分类[12]。NTxPred2的肽模式微调ESM2-t30进行神经毒性预测，而蛋白模式和混合模式使用ESM-2嵌入与Extra Trees（极端随机树）分类器[13]。mebipred是一种无需序列比对的前馈神经网络方法，以氨基酸组成、理化描述符和金属结合5-mer计数为特征，先预测一般金属结合，再由第二层模型预测特定离子结合[14]。AnOxPePred对肽序列进行one-hot编码，经一维卷积、平均池化和全连接层，分别输出自由基清除和螯合预测[15]。因此，该流程混合了蛋白质语言模型、卷积神经网络、常规集成学习和基于人工特征的神经网络。由于缺少当时服务器快照、提交输入文件和逐行输出，这些说明记录的是文献所述实现，而不是本研究重新运行的模型。

### 外部序列集与对接证据

另一份外部记录包含12条互不重复的7–9 aa序列及AChE对接汇总。序列长度、分子质量、电荷、疏水残基比例和残基组成均由序列字符串重新计算。对接数值按来源报告转录为针对人AChE（PDB 4EY6）的Vina均值和标准差。AChE与胆碱能信号相关，其外周区域可与淀粉样蛋白β发生相互作用[16,17]，但对接本身不能证明亲和力或功能。由于缺少受体和配体原始文件、质子化设置、搜索盒、构象、日志及逐次运行分数，本研究未重新运行对接。该12条外部序列无法逐行连接到汇总漏斗或更严格的8条终点集。

### 统计分析

计数和百分比仅作描述性报告。候选序列是计算记账单位，而非独立参与者或生物学重复，因此未进行肽层面的健康—牙周炎显著性检验。依据既有对接方法学认识，对对接分数作为终点替代指标的局限进行解释[18–20]。

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
