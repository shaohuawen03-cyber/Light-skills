## 摘要

牙周炎相关口腔菌群失调可能参与阿尔茨海默病（AD）相关炎症，但尚未建立明确的分子连接。微生物组小开放阅读框（smORF）构成规模庞大的候选肽空间，可用于计算优选。本研究旨在重建口腔smORF汇总筛选级联，并形成可供机制随访的适量肽候选集。本研究为纯计算二次分析，整合序列/蛋白质组过滤、ESM-2嵌入与任务特异性卷积网络、ESM2-t30神经毒性模型、两级神经网络金属结合预测器、多任务抗氧化卷积网络、序列组成分析及独立乙酰胆碱酯酶（AChE）对接汇总。从11,269,961条和11,721,988条smORF起始库中分别保留31,510条和33,786条候选。牙周炎标记分支中3,518条候选达到BBB高分；NTxPred2评价3,299条，其中923条为模型阳性；后续筛选依次保留111、15、12和8条候选。另一张表包含12条互不重复的7–9 aa序列，其AChE Vina均值范围为−9.60至−8.25 kcal/mol。序列组成和评分排序可以复核，但逐行对应关系和对接执行仍未解决。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微肽；smORF；深度学习；乙酰胆碱酯酶；分子动力学

## 引言

阿尔茨海默病（AD）是一种进行性神经退行性疾病，其病理涉及淀粉样蛋白β（Aβ）、tau、突触、免疫、血管和代谢异常的相互作用[@scheltens2021alzheimer]。淀粉样蛋白仍是疾病生物学的核心组成，但其负荷本身不能解释AD在时间过程和临床表现上的异质性[@selkoe2016amyloid]。因此，外周炎症状态更适合被理解为多层次疾病过程中的潜在修饰因素，而不是单一充分病因。

胆碱能系统体现了临床相关性与因果充分性之间的区别。胆碱能功能丧失参与认知症状，乙酰胆碱酯酶（AChE）抑制剂仍是既定的AD对症治疗药物[@hampel2018cholinergic]。AChE还可通过非催化相互作用加速Aβ纤维组装[@inestrosa1996ache]。这些发现使AChE成为具有生物学依据的结构靶点，但并不意味着每个获得计算评分的AChE配体都与AD有关。靶点结合、作用方向、组织暴露、选择性、浓度和下游表型需要分别建立。

牙周炎是由失调性多微生物生物膜与易感宿主反应共同驱动的慢性炎症性疾病。它可能造成持续炎症负担和微生物产物的间歇性系统暴露，由此推动口腔—脑轴研究[@chalmers2025primer]。配对口腔宏基因组和宏转录组观察显示，疾病相关活动随物种和口腔位点而变化，因此分类学丰度不能替代功能证据[@belstrom2021periodontitis]。跨研究宏转录组综合进一步提示，队列定义、采样、测序深度、标准化、协变量和参与者层面重复都会影响牙周特征[@ovsepian2024periodontal]。

在该生态系统中，牙龈卟啉单胞菌（*Porphyromonas gingivalis*）是研究较充分的革兰阴性厌氧条件致病菌。牙龈蛋白酶、免疫调节、组织降解、营养获取和群落协作使该菌即使在丰度不占优势时也可能重塑牙周生态位[@guo2010gingipain]。外膜囊泡能够浓缩和运输细菌组分，并改变细菌与宿主细胞及邻近微生物之间的相互作用[@ho2015omv]。这些特征提供机制背景，但不能把缺少来源链的群落肽直接归属于*P. gingivalis*。在把菌种层面证据转移至某条肽之前，必须建立该序列与组装、样本、分类单元、翻译事件和暴露路径之间的联系。

多类证据支持继续探索，同时也显示出现有缺口。观察性综合通常报告牙周病与认知障碍相关，但效应估计受到牙周定义、痴呆判定、随访、年龄结构和校正策略影响[@larvin2023periodontalcognition]。一项AD队列研究发现牙周炎与后续认知下降及促炎状态相关，提供了时间信息，但不能排除混杂与反向因果[@ide2016periodontitis]。

机制研究回答的是更窄的问题。AD相关死后组织中曾检出*P. gingivalis*相关DNA或蛋白信号，但疾病组织中的检出不能确定暴露方向、时间或因果作用[@dominy2019pgingivalis]。小鼠反复口腔暴露可产生神经炎症、神经退行性和Aβ相关改变，说明特定模型下具有生物学合理性，但不能直接外推至人类[@ilievski2018oral]。囊泡研究为浓缩细菌货物和宿主细胞信号提供可能载体，但其在人类自然暴露中的生物分布和有效剂量仍不确定[@nara2021omv]。相反，孟德尔随机化分析未确认牙周病对AD的遗传因果效应，为强因果表述提供必要限制[@hu2024mendelian]。人体关联、实验合理性和遗传证据回答不同问题，尚未形成确定的因果通路。

微生物组编码的小蛋白和微肽可能构成尚未充分研究的分子中介。人类微生物组大规模分析发现许多保守的小基因家族，其中多数缺少已知结构域或功能[@sberro2019smallgenes]。专用smORF注释通过整合编码特征等信息提高检出灵敏度，而不是沿用常规蛋白长度阈值[@durrant2021sorf]。短ORF研究仍需谨慎命名和正交验证，因为编码预测本身不能证明翻译[@couso2017sorfs]。蛋白质基因组研究进一步表明，翻译证据必须结合阅读框、组织背景、错误发现控制和肽唯一性进行解释[@vanheesch2019heart]。即使检测到肽，也不代表它必然从生物膜释放、在血液中稳定、跨越血脑屏障（BBB）或在神经组织中发挥作用。

因此，相关分子机制仍不清楚。本研究定位于早期计算优选，而不是机制检验。我们重建汇总候选漏斗，按照实际算法描述各模型架构，表征一份12条序列清单，并限定现有AChE对接评分表的解释范围。研究目标是在不夸大模型输出的前提下缩小候选空间，并形成从序列追溯、独立计算、分子动力学（MD）到实验验证的科学顺序。

## 材料与方法

### 研究设计与数据来源

本研究为纯计算二次分析，使用汇总筛选计数、模型汇总、一张12条序列表及相应AChE对接评分表。本文未开展参与者招募、标本采集、湿实验、新组学处理、预测器再训练或对接重跑；MD轨迹分析作为预设扩展正在进行。所提供的健康与牙周炎标签仅作为分支标签保留，不视为已经核实的候选层面疾病归属。

我们核查公共登录号背景，以区分来源项目与衍生组装。PRJNA678453是配对口腔宏基因组和宏转录组测量的来源项目[@belstrom2021periodontitis]。PRJEB65451并非独立临床队列，而是由PRJNA678453衍生、使用metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的第三方注释宏基因组组装项目。由于现有材料不含一致的登录号—分组表、样本—组装映射和bin层面清单，本文省略具体参与者、标本、组装分析和宏基因组组装基因组总数。

序列支持步骤使用了证据含义不同的口腔基因组和宏蛋白质组资源。HOMD/eHOMD提供人类口腔与呼吸消化道的分类学和基因组背景[@chen2010homd]。唾液宏蛋白质组数据可在其自身采样和错误发现框架内支持肽观察[@belstrom2016metaproteomics]。其他口腔宏蛋白质组数据集提供情境特异的序列观察，但不能证明当前疾病标记分支中的表达[@jiang2022oralmetaproteomics]。近期唾液宏蛋白质组工作还强调宿主去除、微生物富集、肽层面错误控制、分类学歧义和原始数据保存[@yuan2025osample]。因此，对任何资源的精确匹配都被视为序列支持，而不是队列特异表达证据。

现有数据不含完整漏斗的候选核苷酸行、完整肽序列行、基因组坐标、样本映射、分类学归属、肽谱匹配、完整预测器输出或原始发现管线。因此，无法估计参与者层面患病率，不能进行分类学归属和疾病富集检验，也不能重建所有模型阶段之间的精确候选交接。

### smORF候选定义与序列证据过滤

所提供分析保留编码4–50 aa肽的翻译smORF。健康标记和牙周炎标记起始库分别包含11,269,961条和11,721,988条候选。候选序列与指定口腔序列和蛋白质组资源进行精确匹配并去冗余，最终保留31,510条健康标记候选和33,786条牙周炎标记候选。精确匹配仅解释为序列存在或曾在相关资源中被观察的支持信息，而不是分析疾病标记分支中真实表达的证明。

过滤后候选分为短肽（5–30 aa）和长肽（31–50 aa）分支。健康标记分支含30,557条短肽和953条长肽；牙周炎标记分支含32,754条短肽和1,032条长肽。虽然初始定义包括4 aa肽，但下游分箱从5 aa开始，因此无法根据汇总表确定4 aa序列的去向。

### 深度学习引导的多模型优选

第一层功能优选采用UniDL4BioPep。该架构使用预训练ESM-2模型`esm2_t6_8M_UR50D`把每条肽编码为320维上下文表示，随后输入用于二分类肽活性任务的六层任务特异性卷积神经网络[@du2023unidl4biopep]。包括BBB任务在内均使用≥0.80阈值。由于该极短微生物组肽域缺少校准和实验转运信息，本文把输出称为“BBB高分”，而不是BBB可透过。

已发表BBB肽预测器在阳性集定义、阴性采样、序列范围、特征、架构和验证设计方面存在异质性。例如，Augur组合工程描述符、特征选择、类别平衡和随机森林，而不是采用深度学习[@gu2024bbb]。这种差异意味着阈值输出具有模型特异性，不能视为体内转运的校准概率。极短、富亮氨酸且带正电的候选尤其可能受到分布偏移影响。

主源还分别保留了短肽与长肽分支中22项UniDL4BioPep功能输出的高置信度计数，包括ACE抑制、TTCA、BBB、抗寄生虫、NeuroPred、抗细菌、抗真菌、抗病毒、毒性、抗氧化FRS、致敏性、DPP-IV抑制、细胞穿透、苦味、鲜味、广谱抗菌、两项抗疟输出、群体感应、两项抗癌输出和Anti-MRSA。所有任务均采用所提供的≥0.80阈值。计数和比例按分支特异背景转录（长肽：健康标记953条、牙周炎标记1,032条；短肽：30,557条和32,754条）；这些输出是可重叠的任务标签，不作为独立生物学重复或组间富集证据。

牙周炎标记BBB高分集合随后进入NTxPred2肽模式。该模型在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[@rathore2025ntxpred2]。仅将处于文献规定7–50 aa输入范围的肽视为已评估；更短候选记为超出模型覆盖，而不是阴性。

Mebipred评价Cu、Fe和Zn相关结合潜力。与ESM模型不同，mebipred把氨基酸组成、理化描述符和金属结合5-mer频率整合到两级人工神经网络框架中：一般金属结合网络之后连接离子特异性分类器[@aptekmann2022mebipred]，判定阈值为0.50。

抗氧化相关性质采用多任务深度卷积神经网络AnOxPePred评价。经one-hot编码的肽序列依次通过一维卷积、平均池化和256单元全连接层，产生自由基清除（FRS）和螯合（CHEL）输出[@olsen2020anoxpepred]。保留三个操作终点：CHEL≥0.25；CHEL≥0.25且FRS<0.50；CHEL≥0.25且FRS<0.45。由于多个模型重复利用序列组成且训练终点异质，串行模型一致仅作为计算分流，不视为相互独立的生物学确认。

### 序列表征与对接评分分析

另一张表包含12条被描述为CHEL/FRS主集合的肽序列。因缺少稳定标识符和序列层面CHEL/FRS输出，无法确认其是否对应汇总终点。我们直接依据字符串重算长度，以及组氨酸、半胱氨酸、碱性残基（Arg+Lys）和芳香残基（Phe+Tyr+Trp）数量，并检查序列唯一性及标准氨基酸组成。

选择AChE作为结构背景，是因为其外周区域与加速Aβ组装有关[@inestrosa1996ache]。一个明确的AChE结构基序被认为可促进Aβ纤维形成[@deferrari2001motif]。生化体系中的PAS定向配体能够抑制AChE诱导的Aβ聚集，这使该位点成为合理的结构假设，但不能证明当前肽具有活性[@bartolini2003pas]。PDB 4EY6提供具有配体结合信息的实验测定人AChE结构[@cheung2012ache]。现有对接表描述12条肽的AutoDock Vina 1.2.5评分。Vina适用于初步筛选，但评分受受体制备、配体质子化、初始构象、搜索空间位置、exhaustiveness和随机采样影响[@trott2010vina]。较新Vina实现扩展了方法，但不能消除这些依赖[@eberhardt2021vina]。因此，本文仅对均值和标准差进行描述性分析，不把评分换算为亲和力或自由能。制备结构、精确网格中心、运行定义、原始分数、日志、构象和相互作用表均不可获得。

### 正在进行的分子动力学扩展

预设的100 ns MD扩展包括游离人AChE以及标记为ALLLHRC、FLLHTTR和YLSLLQR的AChE复合物。计划使用GROMACS[@abraham2015gromacs]、Amber99SB-ILDN力场[@lindorfflarsen2010amber]、TIP3P水模型、溶质至盒边界1.0 nm的三斜周期盒，并在中和后加入0.15 mol/L NaCl。能量最小化包括2,000步最速下降及重原子位置约束。平衡过程包括1.0 ns约束NVT升温（10至300 K）、1.0 ns约束NPT平衡和300 K、1 bar条件下1.0 ns无约束NPT平衡。

生产阶段设定为100 ns，步长2 fs；含氢键采用LINCS约束，静电相互作用采用粒子网格Ewald法，温度耦合采用velocity-rescale方法，压力耦合采用Berendsen方法。坐标每20 ps保存一次，即每条轨迹计划得到5,000帧。预设输出包括复合物、AChE和肽层面的RMSD/RMSF、回转半径、溶剂可及表面积、二级结构、径向分布函数、氢键、残基接触及桥连水。已发表AChE–Aβ模拟表明，受体骨架相对稳定可与肽表面迁移和接触改变同时发生，因此解释时需结合多个指标，而不能只依赖RMSD[@atanasova2020md]。比较性轨迹处理与质量控制仍在进行；稳定性、收敛性、接触和体系间测量将在预设分析完成后补充。

## 结果

### 序列证据过滤与BBB高分输出

序列证据过滤分别保留31,510/11,269,961条健康标记候选（0.2796%）和33,786/11,721,988条牙周炎标记候选（0.2882%）（表1）。健康标记分支中，3,359/30,557条短肽（10.99%）和40/953条长肽（4.20%）为BBB高分。牙周炎标记分支中，3,446/32,754条短肽（10.52%）和72/1,032条长肽（6.98%）为BBB高分，总计3,518条；其中短肽占97.95%。

**表1. 候选库与BBB高分输出汇总。**

| 分支 | 原始smORF | 证据过滤后 | 短肽背景 | 短肽BBB高分，n（%） | 长肽背景 | 长肽BBB高分，n（%） |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 健康标记 | 11,269,961 | 31,510 | 30,557 | 3,359 (10.99%) | 953 | 40 (4.20%) |
| 牙周炎标记 | 11,721,988 | 33,786 | 32,754 | 3,446 (10.52%) | 1,032 | 72 (6.98%) |

所提供牙周炎标记长度汇总包括5–7 aa 547条、8–15 aa 2,893条、16–30 aa 6条以及31–50 aa 72条。因此，优选集合以短序列为主。由于缺少逐行身份，无法评价序列重叠、分类学分布或参与者层面患病率。

广义抗菌输出接近饱和：健康标记短肽中30,537/30,557条（99.93%）、牙周炎标记短肽中32,721/32,754条（99.90%）超过共同0.80阈值。这种近乎普遍的阳性不太可能代表具有实验活性的口腔抗菌肽比例，更可能提示序列域偏移、校准限制或该标签不适合采用共同阈值。

### 长肽与短肽多维功能预测结果

主源中的多维功能汇总以紧凑形式保留（表2）。长肽比例使用健康标记953条和牙周炎标记1,032条为背景；短肽比例使用30,557条和32,754条为背景。长肽输出以Bitter（66.63%；62.11%）、Anti-parasitic（30.22%；27.13%）和Antimicrobial（21.62%；23.06%）为主。短肽Antimicrobial_activity接近饱和（99.93%；99.90%），APP_Anti-parasitic、Quorum_sensing和ACP_Anticancer_main输出也较大。牙周炎标记短肽分支包含3,446条BBB、4,019条NeuroPred和4,728条Anti-MRSA高置信度输出。主源在两个分支汇总中使用了略有差异的模型标签后缀；表1按对应功能类别并列，不把它们视为已经校准或实验等价的测量。

**表2. UniDL4BioPep评分≥0.80的长肽与短肽多维功能预测结果。**

| 功能输出 | 长肽健康 n（%） | 长肽牙周炎 n（%） | 短肽健康 n（%） | 短肽牙周炎 n（%） |
| --- | ---: | ---: | ---: | ---: |
| 抗癌（替代模型） | 91 (9.55%) | 121 (11.72%) | 7,878 (25.78%) | 8,380 (25.58%) |
| BBB | 40 (4.20%) | 72 (6.98%) | 3,359 (10.99%) | 3,446 (10.52%) |
| 群体感应 | 173 (18.15%) | 190 (18.41%) | 11,834 (38.73%) | 12,674 (38.69%) |
| 广谱抗菌 | 206 (21.62%) | 238 (23.06%) | 30,537 (99.93%) | 32,721 (99.90%) |
| 抗细菌 | 111 (11.65%) | 153 (14.83%) | 9,269 (30.33%) | 9,273 (28.31%) |
| 抗MRSA | 47 (4.93%) | 62 (6.01%) | 4,315 (14.12%) | 4,728 (14.43%) |
| 细胞穿透肽 | 15 (1.57%) | 29 (2.81%) | 4,435 (14.51%) | 4,133 (12.62%) |
| 抗真菌 | 73 (7.66%) | 96 (9.30%) | 8,732 (28.58%) | 8,475 (25.87%) |
| 毒性 | 13 (1.36%) | 18 (1.74%) | 2,770 (9.07%) | 2,751 (8.40%) |
| 鲜味 | 17 (1.78%) | 15 (1.45%) | 6,095 (19.95%) | 6,094 (18.61%) |
| 抗疟（替代模型） | 12 (1.26%) | 14 (1.36%) | 1,724 (5.64%) | 1,695 (5.17%) |
| TTCA | 1 (0.10%) | 1 (0.10%) | 9,123 (29.86%) | 9,161 (27.97%) |
| 抗氧化FRS | 43 (4.51%) | 41 (3.97%) | 4,171 (13.65%) | 4,093 (12.50%) |
| DPP-IV抑制 | 0 (0.00%) | 0 (0.00%) | 207 (0.68%) | 266 (0.81%) |
| 抗疟（主模型） | 0 (0.00%) | 0 (0.00%) | 6,496 (21.26%) | 6,586 (20.11%) |
| 抗寄生虫 | 288 (30.22%) | 280 (27.13%) | 21,185 (69.33%) | 22,010 (67.20%) |
| NeuroPred | 82 (8.60%) | 77 (7.46%) | 3,876 (12.68%) | 4,019 (12.27%) |
| 抗癌（主模型） | 37 (3.88%) | 31 (3.00%) | 11,370 (37.21%) | 12,023 (36.71%) |
| ACE抑制 | 20 (2.10%) | 14 (1.36%) | 2,781 (9.10%) | 2,856 (8.72%) |
| 致敏性 | 16 (1.68%) | 11 (1.07%) | 8,599 (28.14%) | 9,422 (28.77%) |
| 抗病毒 | 55 (5.77%) | 52 (5.04%) | 7,501 (24.55%) | 7,221 (22.05%) |
| 苦味 | 635 (66.63%) | 641 (62.11%) | 5,037 (16.48%) | 4,986 (15.22%) |


### 串行模型优选

NTxPred2评价3,299/3,518条牙周炎标记BBB高分候选（93.77%）；219/3,518条（6.23%）超出规定长度范围。在已评估候选中，923/3,299条（27.98%）为模型阳性。后续汇总筛选依次保留111条mebipred阳性、15条CHEL≥0.25、12条CHEL≥0.25且FRS<0.50，以及8条CHEL≥0.25且FRS<0.45候选（表3）。收紧FRS阈值后保留主集合的8/12（66.67%）。由于缺少候选层面交接数据，111/923不解释为已验证转换率。

主源报告923条NTxPred2阳性候选全部≤30 aa。因此，宏蛋白质组支持并去重后的72条牙周炎标记31–50 aa BBB高分长肽均未保留在进入后续mebipred和AnOxPePred金属结合/CHEL/FRS筛选的神经毒性阳性集合中，汇总的12条终点因而只包含短肽。由于缺少逐行输出，无法重建每条长肽被排除的具体原因。

**表3. 汇总计算优选结果。**

| 阶段 | 操作规则 | n | 分母或限制 |
| --- | --- | ---: | --- |
| 健康标记smORF | 4–50 aa | 11,269,961 | 起始库 |
| 牙周炎标记smORF | 4–50 aa | 11,721,988 | 起始库 |
| 证据过滤后健康标记候选 | 精确匹配与去冗余 | 31,510 | 11,269,961 |
| 证据过滤后牙周炎标记候选 | 精确匹配与去冗余 | 33,786 | 11,721,988 |
| 短肽BBB高分 | UniDL4BioPep输出≥0.80；5–30 aa | 3,446 | 32,754 |
| 长肽BBB高分 | UniDL4BioPep输出≥0.80；31–50 aa | 72 | 1,032 |
| BBB高分总计 | 短肽+长肽 | 3,518 | 算术和 |
| NTxPred2已评估 | 7–50 aa | 3,299 | 3,518 |
| NTxPred2阳性 | 模型阳性标签 | 923 | 3,299 |
| 金属结合阳性 | Mebipred输出≥0.50 | 111 | 逐行交接不可获得 |
| CHEL优先 | CHEL≥0.25 | 15 | 111 |
| 主集合 | CHEL≥0.25且FRS<0.50 | 12 | 111 |
| 严格子集 | CHEL≥0.25且FRS<0.45 | 8 | 序列成员未知 |

### 12条序列的组成与对接评分排序

另一张表包含12条互不重复、仅由标准氨基酸组成的肽，长度为7–9个残基（表4）。其中11条含组氨酸，6条含半胱氨酸，每条均至少含一个Arg或Lys。这些特征可提出合成和金属配位假设，但序列组成不能确定金属亲和力、选择性、化学计量、配位几何、氧化态、BBB转运、毒性、分类学归属或与汇总终点的对应关系。

Vina均值范围为−9.60至−8.25 kcal/mol，标准差范围为0.04至0.12。FLLHTTR、YLSLLQR和ALLLHRC的均值最低，HLPLLHRCC和HVLLLRQCA的均值最高。1.35 kcal/mol的跨度仅描述该评分表。标准差的逐次运行分母不可获得；缺少构象时也无法评价残基层面相互作用。因此，组氨酸/半胱氨酸组成和评分顺序应用于设计后续实验，而不是推断结合或机制。

**表4. 12条序列的组成及现有AChE对接评分。**

| 排名 | 序列 | 长度 | His | Cys | Arg+Lys | 平均评分（kcal/mol） | SD |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | 1 | 0 | 1 | −9.60 | 0.08 |
| 2 | YLSLLQR | 7 | 0 | 0 | 1 | −9.49 | 0.05 |
| 3 | ALLLHRC | 7 | 1 | 1 | 1 | −9.29 | 0.11 |
| 4 | FCLHLQLR | 8 | 1 | 1 | 1 | −9.27 | 0.09 |
| 5 | YHHLLCRR | 8 | 2 | 1 | 2 | −9.03 | 0.07 |
| 6 | LLHLPKRTT | 9 | 1 | 0 | 2 | −9.01 | 0.06 |
| 7 | LLHPLRL | 7 | 1 | 0 | 1 | −8.94 | 0.10 |
| 8 | WLLVHLKK | 8 | 1 | 0 | 2 | −8.94 | 0.04 |
| 9 | LLHPLRC | 7 | 1 | 1 | 1 | −8.91 | 0.08 |
| 10 | HLLTLKKHV | 9 | 2 | 0 | 2 | −8.88 | 0.05 |
| 11 | HLPLLHRCC | 9 | 1 | 2 | 1 | −8.35 | 0.12 |
| 12 | HVLLLRQCA | 9 | 1 | 1 | 1 | −8.25 | 0.09 |

## 讨论

### 主要发现

本研究重建一条计算漏斗，把数百万条smORF候选缩减为12条主集合和8条严格子集的汇总终点，同时表征另一份12条明确序列并保留现有AChE对接表的评分顺序。主要科学贡献不是验证牙周炎—AD机制，而是形成边界清楚的候选集、明确模型适用性限制，并为恢复缺失的序列层面和实验依据提供有序路径。

### 模型级联的解释

该级联整合现代神经网络架构，但不能视为多次独立确认。UniDL4BioPep和NTxPred2均使用蛋白质语言模型表示，而mebipred和AnOxPePred包含组成衍生信息，相关序列特征可能沿连续筛选传播。不同训练集在终点定义、序列长度、去冗余、类别平衡和阴性集构建上也存在差异。对于富亮氨酸、带正电且仅7–9 aa的微生物组肽，这些问题尤为重要，因为候选可能偏离训练分布。

接近饱和的抗菌输出提供内部校准警示。它不否定所有排序，但表明共同概率阈值在不同任务中可能具有完全不同的意义。因此，“BBB高分”“神经毒性阳性”“金属结合阳性”、CHEL和FRS都只是操作性模型标签，并不等同于转运、神经元损伤、结合常数、配位几何或氧化还原活性。

这一界定符合当前微生物组肽发现标准。计算挖掘能够有效缩小序列空间，但只有经过候选合成和受控功能实验后，计算候选才能转化为生物学发现[@torres2024peptideantibiotics]。可靠的候选矩阵应把每条序列连接到基因组坐标、组装、样本、临床标签、分类学归属、肽谱证据、每项预测评分与适用性标记以及最终集合成员。没有这种结构，就不能把两个库相近的汇总保留率解释为富集或减少，也不能把牙周炎标签赋予单条肽。

### AChE、金属与肽结构假设

AChE外周区域可影响Aβ组装，因此具有生物学相关性，但这一背景不能把对接评分转化为靶点结合。柔性肽具有多种可达构象，质子化、末端状态、受体柔性、初始结构和搜索设置均可能改变排序。独立重现应包含制备后的受体和配体文件、多种起始构象、明确随机种子、全部原始分数与构象，以及FlexPepDock等肽特异性柔性精修[@london2011flexpepdock]。正在进行的比较性MD扩展可从记录完整的起始复合物评价接触持续性和构象行为，而不能替代不确定的对接制备。MD应分别报告受体拟合和肽自拟合运动，明确周期性边界处理，保存起始结构与拓扑，采用独立种子，并评价重复间收敛。已发表AChE–Aβ轨迹可作为方法学参照，但其中的肽驻留区域和接触不能迁移到本研究的7–9残基候选[@atanasova2020md]。

组氨酸和半胱氨酸富集提供潜在金属配位基团。金属稳态失衡与Aβ聚集、氧化还原化学、脂质过氧化和神经元损伤相交，但这些通路构成网络，而不是单一笼统的“金属结合”终点[@bush2013metal]。元素组学视角也强调金属种类、区室、氧化态、配体环境和浓度[@lei2021elements]。序列组成不能确定亲和力、化学计量、离子选择性、配位几何、氧化态或氧化还原后果。直接测量应在受控pH和化学计量下比较Cu(II)、Fe(II/III)和Zn(II)，并包括光谱、热力学、活性氧及脂质过氧化终点。需要设置仅肽、仅金属、打乱序列、组成匹配及明确阳性和阴性对照。

### 牙周与AD解释

牙周背景仍属于假设生成。人体关联可能受到年龄、吸烟、糖尿病、用药、衰弱、社会经济因素、口腔护理可及性和反向因果影响。*P. gingivalis*实验系统在规定剂量和暴露路径下证明若干可能性，但不能转移到缺少追溯关系的群落肽。当前标签不能证明任何序列具有牙周炎特异性、由*P. gingivalis*编码、在来源口腔群落中表达、进入循环或到达脑组织。

可信的分子链需要序列到contig或组装的映射、样本和临床分组、分类学解析、队列匹配的转录或翻译证据、系统暴露、BBB转运以及可重复的靶点或细胞表型。每一步回答不同问题，不能通过累积更多计算评分来替代。

### 验证优先级与局限

首要任务是恢复候选层面数据表，将序列、稳定标识符、基因组坐标、组装、样本、分组、分类学、肽谱证据、每个预测器评分与适用性标记、CHEL/FRS值、主/严格集合成员及对接配体身份连接起来。这将解决12条明确序列是否对应汇总终点，并确定严格8条子集。

固定版本计算重现后，合成肽应依次接受身份、纯度、溶解性、聚集和血清/蛋白酶稳定性检验。BBB转运与细胞毒性应分别采用浓度—反应设计和非神经元对照。随后在预设条件下评价金属化学、AChE/BChE活性、直接结合及Aβ聚集。正在进行的MD扩展将在质量控制后提供轨迹稳定性和接触指标；只有分子身份、暴露、可重复生化活性和生物学重复表型均成立时，才适合进入疾病模型。

另一项关键流程局限是BBB优选后的长度依赖性流失。尽管牙周炎标记分支中有72条经宏蛋白质组支持并去重的长肽达到BBB高分，但923条NTxPred2阳性序列全部≤30 aa；因此，后续金属结合及CHEL/FRS网页预测级联没有保留任何长肽，最终汇总的12条候选只包含短肽。这一结果不能证明长肽在生物学上缺乏神经毒性或金属相关活性；它可能反映串行阈值、模型适用性或校准以及网页预测器实现方式。缺少候选层面评分时，无法区分这些解释。

决定性局限包括缺少漏斗逐行数据、12与8终点成员未解决、缺少原始对接输入和构象、MD轨迹分析仍在进行，以及缺少生物学测量。健康标记与牙周炎标记库相近的汇总保留率不能支持疾病富集，因为适当推断单位应是参与者或样本。这些限制将当前研究限定为计算优选与验证规划。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
4. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
5. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
6. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
7. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
8. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
9. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
10. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
11. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
12. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
13. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
14. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
15. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
16. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
17. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
18. Couso JP, Patra P. Short ORFs: finding gems in hidden places. *Curr Opin Genet Dev*. 2017;45:14–21. doi:10.1016/j.gde.2017.04.002.
19. van Heesch S, Wit F, Botter J, et al. The translational landscape of the human heart. *Cell*. 2019;178(1):236–251.e24. doi:10.1016/j.cell.2019.05.010.
20. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
21. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
22. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
23. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
24. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
25. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
26. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
27. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
28. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
29. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
30. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
31. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
32. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
33. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
34. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
35. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
36. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
37. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
38. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
39. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
40. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer’s disease. *J Biol Chem*. 2021;296:100105. doi:10.1074/jbc.REV120.008207.
