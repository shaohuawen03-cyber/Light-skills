## 摘要

牙周炎相关口腔菌群失调被认为可能影响阿尔茨海默病（AD）相关炎症，但具体分子链路仍不确定。本研究对口腔小开放阅读框（smORF）汇总数据进行纯计算二次分析，以优选可供验证的微肽。筛选级联整合ESM-2嵌入与任务特异性卷积网络、ESM2-t30神经毒性模型、两级神经网络金属结合预测器和多任务抗氧化卷积网络。序列证据过滤从11,269,961条和11,721,988条smORF起始库中分别保留31,510条和33,786条候选。在牙周炎标记分支中，3,518条候选达到BBB高分；NTxPred2评价3,299条并将923条判为阳性，后续筛选依次保留111、15、12和8条候选。另一张表包含12条7–9 aa序列，其AChE Vina均值范围为−9.60至−8.25 kcal/mol。序列组成和评分排序可以核对，但12条序列与汇总终点的关系、对接执行和分子动力学结果均不可获得。因此，本研究形成的是供独立重现和实验检验的计算候选清单，而不是*Porphyromonas gingivalis*来源、脑暴露、AChE结合或AD机制的证据。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微肽；smORF；深度学习；乙酰胆碱酯酶

## 引言

阿尔茨海默病（AD）的发生发展涉及淀粉样蛋白、tau、突触、免疫和血管过程的相互作用，而非单一分子通路[@scheltens2021alzheimer]。淀粉样蛋白仍具有重要生物学意义，但其与疾病进展的关系必须在这一更广泛网络中解释[@selkoe2016amyloid]。

牙周炎是一种与菌群失调相关的炎症性疾病，可能增加全身炎症负担，并推动了口腔—脑轴研究[@chalmers2025primer]。在牙周生物膜中，牙龈卟啉单胞菌（*Porphyromonas gingivalis*）是一种可参与蛋白水解、免疫调节、组织破坏和群落重塑的条件致病菌[@guo2010gingipain]。死后组织研究曾在AD脑组织中报告*P. gingivalis*相关信号，但不能据此确定方向或因果关系[@dominy2019pgingivalis]。小鼠反复口腔暴露可引起神经炎症和淀粉样蛋白相关改变，支持实验合理性，但不能直接外推到人类[@ilievski2018oral]。囊泡也被提出可运输浓缩微生物货物，但其与人类自然脑暴露的关系仍未解决[@nara2021omv]。一项孟德尔随机化分析未确认牙周病对AD的遗传因果效应，为强因果表述提供了重要限制[@hu2024mendelian]。

微生物组编码的微肽可能是一类尚未充分研究的分子。人类相关微生物组含有大量保守小基因[@sberro2019smallgenes]，专用注释方法能够提高常规流程容易遗漏的smORF检出率[@durrant2021sorf]。然而，预测序列不一定被翻译、从生物膜释放、在循环中保持稳定、跨越血脑屏障（BBB）或在神经组织中发挥作用。

因此，相关机制仍不清楚。本研究旨在采用现代序列模型缩小口腔smORF汇总候选空间，表征现有12条肽，并明确检验AChE、金属/氧化还原、BBB和神经毒性假设所需的后续工作。分析保持探索性，不把任何候选归属于*P. gingivalis*，也不把模型评分视为生物学确认。

## 材料与方法

### 研究设计与数据范围

本研究为纯计算二次分析，使用汇总筛选计数、一张12条序列表和一张AChE对接评分表。本文未开展参与者招募、标本采集、湿实验、新组学处理、预测器再训练、对接重跑或完整MD分析。完整漏斗的逐行序列、受试者/样本映射、登录号与分组对应关系、分类学信息、肽谱匹配、完整模型输出及对接输入均不可获得。

PRJNA678453被视为配对口腔宏基因组和宏转录组数据的来源项目[@belstrom2021periodontitis]。PRJEB65451并非独立临床队列，而是由PRJNA678453衍生、使用metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的第三方注释宏基因组组装项目。由于缺少一致的映射和bin层面清单，本文不报告具体参与者、标本、组装分析或宏基因组组装基因组总数。

### 候选构建与模型级联

所提供分析保留编码4–50 aa肽的smORF。健康标记和牙周炎标记起始库分别含11,269,961条和11,721,988条候选。与指定口腔序列和蛋白质组资源精确匹配并去冗余后，分别保留31,510条和33,786条候选。资源匹配被解释为序列支持信息，而不是分析临床分组中真实表达的证明。

UniDL4BioPep采用预训练ESM-2模型`esm2_t6_8M_UR50D`编码肽序列，产生320维上下文嵌入，再输入六层任务特异性卷积神经网络[@du2023unidl4biopep]。应用阈值为≥0.80，包括BBB优选。NTxPred2随后在文献规定的7–50 aa范围内评价候选，其方法是在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[@rathore2025ntxpred2]。短于7 aa的序列记为模型覆盖范围之外，而不是阴性。

Mebipred把氨基酸组成、理化描述符和金属结合5-mer频率整合到两级人工神经网络框架中，包括一般和离子特异性分类器[@aptekmann2022mebipred]，应用阈值为0.50。AnOxPePred使用包含一维卷积、平均池化和256单元全连接层的多任务深度卷积神经网络，产生自由基清除（FRS）和螯合（CHEL）评分[@olsen2020anoxpepred]。分析终点为CHEL≥0.25、CHEL≥0.25且FRS<0.50，以及CHEL≥0.25且FRS<0.45。本研究未重新训练模型，多模型串行一致不视为独立验证。

### 序列、对接与前瞻性MD分析

对于另一张12条序列表，我们直接依据字符串重算长度，以及组氨酸、半胱氨酸、Arg+Lys和Phe+Tyr+Trp数量。现有对接汇总描述了人AChE PDB 4EY6的AutoDock Vina 1.2.5评分。本研究仅对均值和标准差进行描述性分析。由于缺少制备结构、PDBQT输入、质子化和电荷设置、精确搜索坐标、运行定义、原始分数、日志、构象和相互作用表，未重跑对接，也不把Vina评分解释为亲和力或自由能。

前瞻性100 ns方案用于游离AChE及标记为ALLLHRC、FLLHTTR和YLSLLQR的复合物。计划使用GROMACS[@abraham2015gromacs]、Amber99SB-ILDN[@lindorfflarsen2010amber]、TIP3P水和0.15 mol/L NaCl，依次开展约束NVT、约束NPT和无约束NPT平衡，随后在300 K、1 bar条件下以2 fs步长进行100 ns生产模拟。计划分析RMSD/RMSF、回转半径、溶剂可及表面积、氢键、残基接触、二级结构、径向分布函数和桥连水。由于起始复合物和完整轨迹不可获得，本文不分析任何MD结果。

### 统计分析

所有分析均为描述性分析。保留率以前一有明确记录的阶段为分母。候选序列是嵌套于样本、组装、基因组和同源序列组的计算单位，而非独立生物学重复。因此，未开展健康与牙周炎的汇总假设检验，也未计算置信区间和效应量。

## 结果

### 汇总优选漏斗

序列证据过滤分别保留31,510/11,269,961条健康标记候选（0.2796%）和33,786/11,721,988条牙周炎标记候选（0.2882%）。牙周炎标记分支含3,518条BBB高分输出。NTxPred2评价3,299条，其中923条为模型阳性；另有219条低于规定长度范围。后续筛选得到111条金属结合阳性候选、15条CHEL≥0.25候选、12条CHEL≥0.25且FRS<0.50候选，以及8条CHEL≥0.25且FRS<0.45候选（表1）。由于缺少NTxPred2至mebipred的逐行交接，111/923不被视为已验证转换率。

**表1. 汇总计算优选结果。**

| 阶段 | 操作规则 | n | 分母或限制 |
| --- | --- | ---: | --- |
| 健康标记smORF | 4–50 aa | 11,269,961 | 起始库 |
| 牙周炎标记smORF | 4–50 aa | 11,721,988 | 起始库 |
| 证据过滤后健康标记候选 | 精确匹配与去冗余 | 31,510 | 11,269,961 |
| 证据过滤后牙周炎标记候选 | 精确匹配与去冗余 | 33,786 | 11,721,988 |
| BBB高分 | UniDL4BioPep输出≥0.80 | 3,518 | 牙周炎标记分支 |
| NTxPred2已评估 | 7–50 aa | 3,299 | 3,518 |
| NTxPred2阳性 | 模型阳性标签 | 923 | 3,299 |
| 金属结合阳性 | Mebipred输出≥0.50 | 111 | 逐行交接不可获得 |
| CHEL优先 | CHEL≥0.25 | 15 | 111 |
| 主集合 | CHEL≥0.25且FRS<0.50 | 12 | 111 |
| 严格子集 | CHEL≥0.25且FRS<0.45 | 8 | 成员未知 |

### 12条序列表与对接评分

另一张表包含12条互不重复的7–9 aa肽。其中11条含组氨酸，6条含半胱氨酸，每条均含Arg或Lys。Vina均值范围为−9.60至−8.25 kcal/mol（表2）。在现有评分表内，FLLHTTR排名第一，HVLLLRQCA排名最后。序列组成可以重算，但无法建立对接执行及这些序列与汇总12条或8条集合之间的关系。

**表2. 12条序列及现有AChE对接评分。**

| 排名 | 序列 | 长度（aa） | 平均评分（kcal/mol） | SD |
| ---: | --- | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | −9.60 | 0.08 |
| 2 | YLSLLQR | 7 | −9.49 | 0.05 |
| 3 | ALLLHRC | 7 | −9.29 | 0.11 |
| 4 | FCLHLQLR | 8 | −9.27 | 0.09 |
| 5 | YHHLLCRR | 8 | −9.03 | 0.07 |
| 6 | LLHLPKRTT | 9 | −9.01 | 0.06 |
| 7 | LLHPLRL | 7 | −8.94 | 0.10 |
| 8 | WLLVHLKK | 8 | −8.94 | 0.04 |
| 9 | LLHPLRC | 7 | −8.91 | 0.08 |
| 10 | HLLTLKKHV | 9 | −8.88 | 0.05 |
| 11 | HLPLLHRCC | 9 | −8.35 | 0.12 |
| 12 | HVLLLRQCA | 9 | −8.25 | 0.09 |

## 讨论

本研究在保持“预测不等于机制”这一边界的同时形成紧凑验证集合。深度学习和神经网络模型使大规模搜索可行，但基于异质数据训练的输出可能不适用于极短微生物组肽。完整分析中几乎完全阳性的广义抗菌输出也说明，多个模型标签同时为阳性不能替代生物学重复。

AChE外周区域可影响Aβ组装，因此可提供合理结构背景[@inestrosa1996ache]；PDB 4EY6则提供实验测定的人源结构[@cheung2012ache]。然而，Vina属于筛选方法，排序受受体与配体制备、搜索空间和采样影响[@trott2010vina]。较新Vina实现不能消除这些要求[@eberhardt2021vina]，柔性肽对接还可能需要肽特异性精修[@london2011flexpepdock]。缺少构象和运行定义时，评分范围不能证明AChE结合、位点偏好、抑制、选择性或Aβ调节。

牙周研究背景同样需要严格限定。现有研究支持考察炎症、牙龈蛋白酶、感染和囊泡相关路径，但不能把群落来源肽归属于*P. gingivalis*。只有建立从序列到组装、样本、临床标签、分类学、表达、循环、BBB转运和靶点作用的候选层面链路，才能进一步检验疾病主张。

当前优先事项是恢复漏斗逐行成员，确定严格8/12子集，使用固定版本重跑预测和对接，并在合成后验证肽身份与稳定性。随后应在适当对照下评价BBB转运、细胞毒性、Cu/Fe/Zn相互作用、金属依赖氧化还原效应、AChE/BChE功能、直接结合和Aβ表型。缺少逐行映射、原始对接材料、完整MD输入及实验测量，是本研究的决定性局限。

## 结论

汇总数据支持一条透明计算漏斗，终点为12条主集合和8条严格子集计数。另一张12条肽的表格提供序列组成和AChE评分排序，但无法逐行连接到这些终点，也未独立产生对接或MD结果。该清单适用于分阶段验证，但不能证明*P. gingivalis*来源、疾病特异性、脑暴露、靶点结合、生物活性或因果关系。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
4. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
5. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
6. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
7. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
8. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
9. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
10. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
11. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
12. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
13. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
14. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
15. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
16. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
17. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
18. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
19. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
20. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
21. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
22. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
