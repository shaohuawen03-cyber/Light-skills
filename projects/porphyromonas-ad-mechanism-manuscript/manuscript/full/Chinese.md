## 摘要

牙周炎相关口腔菌群失调被认为可能参与阿尔茨海默病（AD）相关神经炎症过程，但连接口腔微生物组与脑组织的具体分子仍不明确。微生物组小开放阅读框（smORF）编码大量未表征肽，适合计算分流，却不能直接支持机制推断。本研究在明确来源边界的前提下，对口腔smORF汇总优选流程进行纯计算重建，并整合单独归档的乙酰胆碱酯酶（AChE）对接汇总。候选库先经序列/蛋白质组证据过滤，再进入深度学习引导的级联流程，包括ESM-2嵌入与任务特异性卷积网络、微调ESM2-t30神经毒性模型、两级神经网络金属结合预测器和多任务抗氧化CNN。证据过滤后，两条来源分支分别保留31,510和33,786条候选。在牙周炎标注分支中，3,518条候选为BBB高分，3,299条处于NTxPred2肽长度适用域，923条为模型阳性；来源记录随后报告111条金属结合阳性候选、15条CHEL优选候选、12条主集合和8条严格子集。外部记录列出12条互不重复的7–9残基序列，其组成可独立复现，并报告−9.60至−8.25 kcal/mol的AChE Vina均值。由于缺少制备结构、配置、原始运行、日志和构象，上述分数只能排序，不能独立复现或解释为亲和力。本研究还依据版本锁定的外部流程登记了前瞻性100 ns GROMACS方案，但排除尚未完成的轨迹分析，不报告任何分子动力学结果。因此，所得清单仅构成透明、可检验的计算假设集合，不证明翻译、脑暴露、神经毒性、金属依赖化学、AChE结合、牙周炎特异肽组或AD机制。

**关键词：** 深度学习；蛋白质语言模型；口腔微生物组；小开放阅读框；微肽；牙周炎；血脑屏障；神经毒性预测；金属结合预测；乙酰胆碱酯酶；分子对接；分子动力学；来源追踪；假设生成

## 1. 引言

### 1.1 阿尔茨海默病是多层次生物学问题

阿尔茨海默病（Alzheimer’s disease，AD）是一种进行性神经退行性疾病，淀粉样蛋白β（Aβ）沉积、tau病理、突触衰竭、胶质细胞激活、血管功能障碍和系统性共病在漫长的临床前及临床连续体中相互作用[20]。淀粉样蛋白假说仍是解释疾病起始事件的重要框架，但单独的淀粉样蛋白负荷不能解释AD在空间、时间和临床表现上的全部异质性[21]。当前观点因而把淀粉样蛋白和tau置于更广泛的网络中，其中包括先天免疫信号、神经元易损性、脂质和金属稳态、脑血管完整性以及随年龄增长而下降的系统韧性。评价外周暴露时，这种系统视角非常重要：某一具有生物学合理性的因素未必是充分病因，但仍必须通过可追溯的分子和时间证据与疾病相关组织连接起来。

胆碱能系统体现了临床相关性与因果充分性之间的差别。胆碱能功能丧失参与认知症状，乙酰胆碱酯酶（AChE）抑制剂仍是成熟的对症治疗[22]。AChE还与Aβ装配存在非催化相互作用，从而在胆碱能生物学与淀粉样研究之间形成结构联系[23]。但这两点都不意味着每个预测可与AChE相互作用的分子均与AD相关。靶标占据、作用方向、组织暴露、浓度、选择性和下游表型都必须分别建立。这一证据顺序也适用于评价口腔—脑轴中的微生物分子。

慢性外周炎症状态因而被视为可能调节神经退行性易损性的因素。牙周炎尤其受到关注，因为它同时包含持续黏膜炎症、菌群失调的多微生物生物膜、微生物产物间歇进入循环的可能性，以及显著的年龄和共病梯度[43]。但这些特征也使因果解释变得困难。牙周炎可能增加系统炎症负担，也可能与认知下降共享决定因素，而认知下降又会恶化口腔卫生和牙科服务可及性。因此，严格的分子研究必须区分关联、路径合理性、分子身份和已证实功能，不能把它们视为同一层证据。

### 1.2 牙周菌群失调与牙龈卟啉单胞菌

牙周炎是牙支持组织的生态性疾病，而不是单一病原体造成的结果。在易感宿主中，群落结构改变、炎症性营养释放和炎症消退受损可以相互强化，形成具有位点特异性转录活动的失调生态。配对口腔宏基因组和宏转录组数据表明，疾病相关信号随物种和口腔位点变化，分类丰度不能代替功能活性[6]。跨研究宏转录组综合还显示，疾病信号受到队列定义、采样位点、测序深度、标准化、协变量和受试者层面重复的影响[7]。因此，不能把疾病标注分支中恢复的每条序列都称为疾病特异序列。

在这一群落中，牙龈卟啉单胞菌（*Porphyromonas gingivalis*）是研究最充分的革兰阴性厌氧条件致病菌之一。其重要性并不只来自丰度，还来自通过蛋白水解、免疫调节、群落协作和囊泡载荷输送重塑宿主—微生物相互作用的能力。牙龈蛋白酶可依赖具体背景影响宿主蛋白、补体通路、炎症、组织完整性和营养获取[48]。*P. gingivalis*外膜囊泡能够浓缩并运输细菌成分，改变其与宿主组织及邻近微生物的相互作用[47]。这些性质使该菌适合作为口腔—系统假设的生物学背景，但不能据此把无法追溯的群落来源肽归属于该菌。

必须区分微生物种层面的假设与群落肽假设。检出*P. gingivalis* DNA、抗原、牙龈蛋白酶相关信号或囊泡物质，并不意味着某条短肽已经表达、分泌、在血液中稳定、跨越血脑屏障（BBB）或在神经组织中发挥作用。反过来，无法归属于*P. gingivalis*的宏基因组来源肽也可能来自其他口腔分类单元或组装伪影。因此，本文把口腔宏基因组视为群落序列空间，而把*P. gingivalis*作为机制背景而非预设分类标签。

### 1.3 人体、实验和遗传证据具有不同因果权重

牙周炎—AD文献包含回答不同问题的多类证据。观察性综述和荟萃分析通常报告牙周病与认知障碍相关，但效应估计随牙周定义、痴呆判定、随访时间、人群年龄结构和校正策略而变化[35]。临床综合同样发现反复出现的关联，同时强调异质性以及回顾性设计难以确定方向性[36]。聚焦口腔细菌的综述扩展了候选机制，也显示微生物检出、抗体反应、口腔疾病状态和痴呆结局经常来自不同人群[37]。较新的证据评价仍把牙周炎视为潜在风险标志，同时要求更强的纵向和干预设计[38]。

纵向观察提供时间信息，但仍易受混杂和反向因果影响。一项AD队列研究观察到牙周炎与后续认知下降及促炎状态相关[39]。公共数据和文本挖掘分析也提出了共享分子信号[40]。这类研究可用于优选通路，却不能判断牙周暴露是否导致神经退行性改变、早期认知受损是否改变口腔健康，或二者是否共同受年龄、吸烟、糖尿病、药物、虚弱、社会经济条件和医疗可及性影响。

遗传工具研究为单向正面叙事提供了重要制衡。两样本孟德尔随机化分析没有建立牙周病遗传风险对AD的因果效应[41]。更广泛的孟德尔随机化综合同样说明，牙周炎的系统性影响并未在不同结局和工具选择中得到一致支持[42]。这些结果不能排除所有后天炎症或微生物路径，因为遗传易感性与随时间变化的暴露并不相同；但它们削弱了“仅凭流行病学关联即可证明因果”的说法。

机制实验在受控条件下回答更窄的问题。AD相关死后样本中曾报告*P. gingivalis*物质和牙龈蛋白酶相关信号[44]，更早的组织研究也考察了AD脑材料中该菌的存在[45]。野生型小鼠反复口腔暴露可产生脑炎症、神经退行性变化和Aβ相关改变[46]。感染神经元体系中也观察到持续牙龈蛋白酶活性和AD样细胞表型[49]。囊泡研究则为浓缩微生物载荷及宿主信号提供一种合理载体[50]。这些研究的优势是机制分辨率，局限是可迁移性：剂量、暴露途径、模型生物、细胞体系、疾病阶段和终点差异使其不能直接外推至自然发生的人体肽暴露。

综合而言，现有文献支持提出研究问题，却没有建立确定通路。人体关联说明问题具有相关性，实验模型证明部分过程具有可能性，而阴性或不确定的因果分析约束解释。可辩护研究应先识别分子实体、追溯来源、证明暴露，再检验预先指定的功能。本研究仅处理这一证据序列中的前端计算步骤。

### 1.4 从牙周生态位到脑组织的候选路径

牙周菌群失调可能通过多条非互斥路径与神经退行性过程连接。第一条是间接路径：慢性牙周炎症可改变循环细胞因子、急性期反应、内皮激活或免疫细胞状态，从而在不需要活菌进入脑组织的情况下影响神经血管和胶质功能[43]。第二条涉及组织炎症或日常机械扰动期间细菌细胞或可溶性产物的间歇播散。第三条涉及外膜囊泡，其可保护并浓缩脂质、蛋白质、核酸和其他细菌载荷[47]。第四条涉及特定酶或分子片段，包括可能修饰宿主底物的牙龈蛋白酶相关产物[48]。这些路径在人类中的相对贡献仍不确定。

每条路径要求不同证据。炎症路径需要暴露—反应和中介证据；播散路径需要口腔与系统区室中匹配的分子身份；囊泡路径需要载荷表征、生物分布和屏障转运数据；直接肽路径还需要证明smORF被翻译、肽能够耐受加工与蛋白水解，并以足够浓度到达相关组织。BBB预测不能满足这些要求，因为通透性还取决于肽构象、电荷、转运机制、血清结合、降解、外排和实验背景。

微生物编码的小蛋白和小肽在这一框架中仍研究不足。短分子原则上可以是配体、酶调节剂、膜活性物质、免疫信号、金属结合分子或无活性的降解产物。因此，假设空间很广，但广泛合理性不是特定序列的证据。尚未解决的分子空白是：是否存在可追溯的口腔微生物肽，在相关生态背景中表达、离开口腔并产生可重复的神经或血管效应。计算优选只有在缩小候选空间的同时保留这些连续证据要求时才有价值。

### 1.5 微生物组smORF是合理但技术困难的发现空间

smORF长期存在系统性漏注释，因为短编码区难以与随机开放阅读框区分，可提供的系统发育信号有限，而且常低于面向常规基因的识别阈值。对人类相关微生物组的大规模分析仍识别出数千个保守小基因家族，其中许多缺少已知结构域[1]。专用注释方法通过整合谱模型、编码特征、保守性和其他证据，而不是套用常规蛋白长度阈值，提高发现能力[2]。高分辨率多组学则可把预测与转录和蛋白质组观察相连接，从而提高候选可信度[3]。

但证据阶梯依然陡峭。预测smORF不一定被转录；转录本不一定被翻译；肽谱匹配不一定唯一或归属正确；被检出的肽也不一定稳定或具有功能。短ORF生物学综述强调正交验证和谨慎命名[4]。蛋白质基因组研究同样表明，翻译证据必须结合组织、阅读框、错误发现和功能背景解释[5]。在宏基因组中，组装碎片、同源序列、菌株变异和六框翻译会进一步产生数百万短候选。

口腔序列与宏蛋白质组资源提供互补但不等价的证据。HOMD和eHOMD整理口腔及呼吸消化道分类和基因组信息[8]。唾液宏蛋白质组可在自身样本和错误发现框架内支持肽检出[10]。肺癌口腔宏蛋白质组则提供另一种背景特异性观察空间[11]。当代唾液宏蛋白质组流程强调宿主去除、微生物富集、肽和蛋白层面错误控制、分类歧义及公共原始数据保存[12]。与任一资源精确匹配可支持序列存在或曾被观察，但不能单独建立当前疾病标注分支中的表达。

因此，样本层面来源链不可缺少。疾病比较需要把序列连接到contig、组装或bin、标本、参与者、口腔位点、临床分组和处理批次。缺少这条链时，候选计数只是计算记账单位，不是独立生物学重复。当前记录保留汇总分支标签和计数，但缺少估计流行度、富集、分类来源和参与者间不确定性所需的逐行映射。因此，本文使用“牙周炎标注分支”，而不是“牙周炎特异肽组”。

### 1.6 深度学习引导的优选是分流而非验证

smORF搜索空间的规模促使研究使用序列模型，但模型输出继承训练数据的假设和适用域限制。UniDL4BioPep以预训练ESM-2生成上下文嵌入，再通过任务特异性卷积神经网络完成肽活性分类[13]。蛋白质语言模型能够捕获难以人工编码的序列规律，但输出分数仍是模型特异值；除非在可比较的序列和任务域中完成校准，否则不能把它解释为生物学概率。

BBB肽预测可说明这一局限。Augur整合工程化描述符、特征选择、类别平衡和随机森林分类器，并非深度学习模型[14]。B3BPFN则代表不同的模型家族和数据集构建方式[15]。阳性集合定义、去冗余、阴性采样、序列长度、类别平衡和验证设计差异都会实质影响表观性能。极短、富亮氨酸、带正电或组成异常的微生物组肽可能位于模型评估分布之外。因此，“BBB高分”只定义优选阈值，不等于实测转运。

下游工具同样具有异质性。NTxPred2肽模式在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[16]。Mebipred使用工程化序列描述符和两级人工神经网络框架，估计一般及离子相关金属结合潜力[17]。AnOxPePred使用一维卷积和多任务输出预测自由基清除与螯合相关性质[18]。这些工具的串联一致不是正交重复，因为模型重复使用序列组成，训练终点不同，还可能沿漏斗传播相关偏倚。

恰当解释是计算分流。“神经毒性阳性”不是神经元毒性，“金属结合阳性”不是实测解离常数或配位几何，CHEL和FRS输出也不是氧化还原化学。微生物组肽挖掘的有力先例表明，计算候选只有经过合成和受控功能实验后才成为生物学发现[19]。对于纯计算研究，科学贡献应是透明缩小候选空间、准确描述模型、提示适用域风险，并可重复记录仍未检验的内容。

### 1.7 AChE、金属稳态、对接与分子动力学构成结构假设

AChE提供一个具有生物学依据但要求严格的结构随访方向。除水解乙酰胆碱外，AChE可加速Aβ纤维装配[23]。AChE特定基序被认为可促进Aβ纤维形成[24]，PAS定向配体则可在生化体系中抑制AChE诱导的Aβ聚集[25]。结构研究描绘了连接催化区域与外周位点的芳香性峡谷[26]。PDB 4EY6所代表的人AChE结构为配体导向问题提供实验确定的受体框架[27]。这些发现支持提出“候选肽能否稳定占据AChE某一区域”，但不能建立结合、抑制或Aβ效应。

柔性7–9残基肽的对接尤其不确定，因为肽质子化、端基、初始构象、受体柔性、搜索空间位置、评分随机性和对接后精修均可改变排序。AutoDock Vina适合初筛，但其分数不是实验亲和力或结合自由能[51]。后续Vina实现扩展了方法和接口，却没有消除完整制备及执行记录的必要性[52]。FlexPepDock等肽特异精修方法体现了透明初筛后可采用的更高分辨率标准[53]。

分子动力学（MD）可以在规定力场和溶剂模型下检验制备复合物是否停留于某一构象区域，但不能挽救无法追溯或制备不充分的对接构象。已发表AChE–Aβ模拟显示肽的停留位置和接触可随时间改变[28]，加速模拟也说明可以探索AChE表面的替代相互作用[29]。对当前候选而言，有意义的MD需要版本化起始坐标、拓扑和质子化决策、独立种子轨迹、收敛性评价及预先指定分析。在这些要素和完整轨迹可用之前，MD只能作为方案，不能作为结果。

金属生物学构成第二个结构假设。铜、铁和锌稳态失衡与Aβ聚集、氧化还原化学、脂质过氧化和神经元损伤相交[30]。更广义的元素组学视角把这些相互作用置于网络而非单金属机制中[31]。含组氨酸和半胱氨酸的肽可能具有配位基团，但组成不能决定亲和力、选择性、化学计量、几何、氧化态或氧化还原结果。Tau片段实验显示Cu(II)配位可改变肽结构和Aβ聚集[32]；tau26–44进一步说明如何通过专门实验把短动态肽连接到膜和细胞表型[33]。细菌淀粉样蛋白暴露也可改变模型系统中的聚集表型[34]。这些研究提供可检验比较对象，而不是可转移的活性。

### 1.8 知识空白与研究目标

现有文献汇聚出一个边界清楚的空白：牙周炎与AD之间存在异质性观察关联，*P. gingivalis*提供物种特异的机制合理性，口腔微生物组又编码大量未充分表征的小肽。然而，目前缺少的是一条可追溯分子链，把确定的微生物smORF依次连接到翻译、宿主暴露、BBB通过、靶标占据和疾病相关表型。任何单一计算分数都不能跨越这些层次。

因此，本研究处理一个更早且更窄的问题：能否把口腔smORF汇总记录重建为可审计候选漏斗，并在不把不完整来源转化为生物学确定性的前提下整合单独报告的AChE对接汇总？第一项目标是重算所有报告比例、检查分支算术和适用性约束，并按文献架构描述每个预测模型。第二项目标是审计12条序列的唯一性和组成，同时把外部AChE分数排序保留为来源报告。第三项目标是登记可重复的下游MD方案，同时暂不纳入未完成轨迹输出。

本文贡献是一套保留来源边界的计算假设集合，而不是新预测器、临床队列分析、独立复现的对接研究、MD结果或经验证的AD机制。这一定位既保留深度学习引导优选的价值，也明确下一步证据要求。

## 2. 材料与方法

### 2.1 研究设计与证据等级

本研究为纯计算、汇总层面重建，并包含跨仓库结构随访。本稿未实施湿实验、参与者招募、标本采集、新组学处理、对接重跑或已完成的分子动力学分析。写作前将证据划分为四层：

1. **A层——主要来源筛选：** 来自`材料与方法及结果_机制研究版.docx`的计数、阈值和流程描述；其SHA-256为`f4132a02cb9955c808739c3cbf15edd947f6203d577e8586490933a5d2daa4b5`。
2. **B层——外部来源记录汇总：** 来自单独归档的外部来源仓库提交`e28c06db0614512eeb2bca217d2f9a760e804051`的12条序列、组成陈述、对接方法标签和Vina均值±SD。文件哈希和接纳决策记录于`evidence/external_v04_integration.md`。
3. **C层——前瞻性MD方案：** 来自`shaohuawen03-cyber/asd`提交`f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`的版本化GROMACS脚本和100 ns MDP文件。该层只定义后续计算，不提供可接纳结果。
4. **D层——文献背景：** 用于综合AD、牙周炎、*P. gingivalis*、AChE/PAS、金属、口腔微生物组和验证问题的同行评议证据。文献不用于补造缺失结果。

A层始终是筛选漏斗的唯一权威来源；B层不追溯填补主要来源的逐行链路；C层仅限前瞻性方法；D层仅提供解释边界。

### 2.2 队列与登录号来源

主要记录列出PRJNA678453和PRJEB65451。登录号与论文核查表明，PRJNA678453是配对口腔宏基因组/宏转录组的来源项目[6]。PRJEB65451并非独立临床队列，而是由PRJNA678453衍生、使用metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的第三方注释宏基因组组装项目。本完整稿不报告参与者、标本、组装分析或宏基因组组装基因组总数，因为来源包不含能够一致审计这些单位的映射和bin层面清单。

本次重建未招募新参与者、未收集标本，也未重新分析原始组学或临床数据。主要材料中缺少候选核苷酸/氨基酸行、基因组坐标、受试者/样本映射、登录号—分组对应表、MAG-bin清单、bin质量表、分类信息、肽谱匹配、模型输出、运行日志、数据库快照和原始管线。因此，登录号仅用于限定数据来源，不作为候选层面分母，也不构成对分组标签的独立确认。

### 2.3 主要来源smORF构建与证据过滤

据主要记录，研究采用样本特异性映射构建健康和牙周炎smORF库，并保留4–50 aa翻译序列。原始库分别含11,269,961和11,721,988条smORF。随后将候选与指定口腔序列/蛋白质组资源精确匹配并去冗余，获得31,510条健康和33,786条牙周炎分支候选。

过滤集合分为短肽分支（5–30 aa：健康30,557，牙周炎32,754）和长肽分支（31–50 aa：健康953，牙周炎1,032）。初始规则包含4 aa候选，但后续分箱从5 aa开始；4 aa序列去向未被记录。资源匹配被视为过滤证据，而不是当前队列表达或疾病特异性证据。

### 2.4 深度学习序列表征与BBB高分定义

UniDL4BioPep作为第一层功能优选模型。其文献架构使用预训练ESM-2模型`esm2_t6_8M_UR50D`，将每条肽编码为320维上下文嵌入，再输入针对各肽活性任务训练的六层卷积神经网络进行二分类[13]。来源流程采用输出≥0.80作为操作性高分阈值，包括BBB任务。由于缺少精确服务器构建版本、任务特异校准、模型哈希及其在极短肽序列域中的外部验证，本文将输出称为“模型阳性”或“BBB高分”，而不称为实测转运或确认活性。BBB模型文献仅用于说明适用域和校准局限[14] [15]。健康和牙周炎计数仅作描述性分支汇总，不实施候选计数组间检验。

### 2.5 深度学习引导的下游优选

随后使用NTxPred2肽模式评估牙周炎BBB高分集合。该模式采用迁移学习，在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[16]。分析限于其规定的7–50 aa输入范围；更短候选被定义为模型覆盖范围之外，而不是阴性。

其后使用mebipred评估Cu、Fe和Zn相关结合潜力。该无需比对的方法把氨基酸组成、理化描述符和金属结合5-mer频率整合至两级人工神经网络框架，依次通过一般金属结合网络和离子特异性神经分类器[17]。来源流程采用0.50判定阈值。

抗氧化相关性质由多任务深度卷积神经网络AnOxPePred评估。经one-hot编码的肽序列依次通过一维卷积层、平均池化和含256个单元的全连接层，最终分别输出自由基清除（FRS）和螯合（CHEL）分数[18]。保留三个操作性终点：CHEL≥0.25；CHEL≥0.25且FRS<0.50（主集合）；CHEL≥0.25且FRS<0.45（更严格子集）。

本次重建未重新训练任何模型。主要材料不含精确服务器快照、提交输入、模型哈希、随机种子、逐行输出或NTxPred2至mebipred的逐行交接。因此，来源报告的111条被保留为下游结果，但111/923不被解释为经审计转换率。模型间一致仅代表串行计算优选，不构成相互独立的生物学确认。

### 2.6 外部12条序列及组成审计

外部来源稿将12条序列列为CHEL/FRS主集合。由于缺少稳定ID、CHEL/FRS逐行数据和映射文件，无法独立检查其与主要来源12行的对应。采用Python标准库脚本（`scripts/audit_external_docking_summary.py`）重算每条序列的长度、组氨酸数、半胱氨酸数、碱性残基数（Arg+Lys）和芳香残基数（Phe+Tyr+Trp）。审计要求12条标准氨基酸序列互不重复、长度为7–9 aa，并与外部组成汇总一致。

### 2.7 外部对接汇总

外部来源记录称，使用AutoDock Vina 1.2.5将12条肽对接到人AChE PDB 4EY6，并设置40×40×40 Å³的PAS中心盒 [27,51,52]；其提供均值±SD和PAS/峡谷定位叙述。本研究转录12组均值和SD，核验排序及范围并生成描述性图。

本研究未重跑对接。经审核的仓库不含受体或配体制备文件、PDBQT输入、精确盒中心、质子化/电荷设置、配置、exhaustiveness、运行数、种子、原始分数、命令、软件环境、日志、构象或相互作用表。因此，所有数值均标为“来源报告”。在缺失运行定义前，SD没有可解释的实验或计算分母。Vina分数未换算为结合亲和力或自由能 [51,52]。导入的PDF作为来源产物保留；修订后的SVG/PNG在图中直接写明报告边界。

### 2.8 前瞻性GROMACS分子动力学方案

下游MD方案登记自`shaohuawen03-cyber/asd`提交`f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`中的`gromacs_md/`目录（https://github.com/shaohuawen03-cyber/asd/tree/arena/019ff90e-asd/gromacs_md）。控制性文件采用可执行的`mdp/100ns/*.mdp`参数集和`scripts/run_all.sh`，而不采用该仓库其他叙述中关于不同生产时长的表述。计划体系包括游离人AChE，以及标记为ALLLHRC、FLLHTTR和YLSLLQR的AChE复合物。审计时，仓库输入目录中不存在所需复合物PDB，因此该方案按前瞻性方法报告，不表述为已执行分析。

配置流程以GROMACS运行，默认力场为`amber99sb-ildn`，采用TIP3P水拓扑、溶质至边界距离1.0 nm的三斜周期盒，以及中和并加入0.15 mol/L NaCl。能量最小化设置为2,000步最速下降，并对重原子施加1,255 kJ mol⁻¹ nm⁻²位置约束。随后在约束下使用velocity-rescale控温，于1.0 ns NVT过程中从10 K升至300 K；继而在300 K、1 bar下进行1.0 ns约束NPT平衡和1.0 ns无约束NPT平衡。前瞻性生产阶段为100 ns，步长2 fs，使用LINCS约束含氢键，实空间截断1.2 nm，范德华相互作用从1.0 nm开始力切换，长程静电采用PME，温度采用velocity-rescale耦合，压力采用Berendsen耦合。计划每20 ps保存坐标，每条轨迹共5,000帧。

预先指定的轨迹输出包括复合物、AChE和肽层面的RMSD/RMSF、回转半径、溶剂可及表面积、径向分布函数、DSSP二级结构、氢键、残基接触和桥连水分析。任何MD结果被接纳前，必须归档起始坐标、末端和质子化状态、拓扑哈希、精确GROMACS版本、随机种子、重复设计、命令、日志、TPR、轨迹、能量、检查点和最终坐标文件。参考仓库中的未完成分析产物不纳入本稿；本文不报告稳定性、收敛性、接触或体系间MD结论。

### 2.9 描述性统计与审计规则

计数从A层转录；比例按100×n/N并使用明确分母重算。候选序列是嵌套于样本、基因组和同源序列组的计算记账单位，不是独立生物学重复。在缺少受试者/样本—候选行时，对汇总肽计数进行Fisher或卡方检验将造成伪重复并人为缩小不确定性。因此，本研究不报告健康与牙周炎比较的p值、置信区间、效应量、ROC、功效或多重校正。

标准库脚本检查分支加和、分子≤分母、NTxPred2已评估/未评估分区、下游单调性、8/12阈值敏感性、序列组成和分数排序。这些属于算术与来源审计，不是生物学管线或对接的独立复现。

### 2.10 文献与报告完整性

外部文献库未被整库导入。本研究删除重复项、仅对应更正说明的错误标识符、与既往排除文件相关的材料以及未被修订论证使用的参考文献。最终53条文献在英文、中文、核验记录和BibTeX之间进行DOI清单一致性检查。整理后的DOI清单作为本研究的参考文献控制记录予以保留。

## 3. 结果

### 3.1 证据过滤使两个原始smORF库均缩减99.7%以上

健康和牙周炎分支分别以11,269,961和11,721,988条smORF起始。证据过滤和去冗余后保留31,510条健康候选（0.2796%）和33,786条牙周炎分支候选（0.2882%）。短肽和长肽分支之和与每个过滤后总数完全一致。这些比例描述计算保留，不代表参与者患病率或疾病富集。

**表1. 汇总候选库与BBB高分输出**

| 分支 | 原始smORF | 证据过滤后 | 短肽背景（5–30 aa） | 短肽BBB高分，n（%） | 长肽背景（31–50 aa） | 长肽BBB高分，n（%） |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 健康 | 11,269,961 | 31,510 | 30,557 | 3,359（10.99） | 953 | 40（4.20） |
| 牙周炎队列 | 11,721,988 | 33,786 | 32,754 | 3,446（10.52） | 1,032 | 72（6.98） |

### 3.2 BBB高分率随长度分支呈描述性差异

健康与牙周炎的短肽BBB高分率分别为10.99%和10.52%，长肽分支分别为4.20%和6.98%。牙周炎分支有3,446条短肽和72条长肽BBB高分，总计3,518条。短肽占3,446/3,518（97.95%），长肽占72/3,518（2.05%）。由于候选层面的独立性未被建立，未对上述并列比例进行推断检验。

主要记录的短肽长度汇总包括5–7 aa 547条、8–15 aa 2,893条和16–30 aa 6条；另有72条长肽为31–50 aa。因此牙周炎BBB高分集合以短序列为主，但缺少逐行身份，无法分析重叠、分类归属和参与者分布。

### 3.3 多活性输出出现饱和警示

完整UniDL4BioPep类别汇总保留在补充材料中。一个分布对解释尤其重要：健康短肽中30,537/30,557（99.93%）、牙周炎短肽中32,721/32,754（99.90%）被广义抗菌标签判为阳性。在统一0.80阈值下接近普遍阳性，不能视为实验活性口腔抗生素的合理估计。这提示序列域偏移、任务校准局限或标签特异阈值问题，也反对将跨模型一致性视作独立验证。

### 3.4 牙周炎分支从3,518条BBB高分候选缩至来源报告的12/8个终点

NTxPred2评估3,299/3,518条候选（93.77%）；219/3,518（6.23%）低于声明模型范围，属于未评估。已评估候选中，923/3,299（27.98%）被预测为阳性。主要记录随后报告111条mebipred阳性候选，其中15/111（13.51%）满足CHEL≥0.25，12/111（10.81%）进一步满足FRS<0.50，8/111（7.21%）满足FRS<0.45。收紧FRS阈值后保留主集合的8/12（66.67%）。

**表2. 牙周炎分支汇总优选记录**

| 阶段 | 操作规则 | n | 可审计分母/状态 |
| --- | --- | ---: | --- |
| 短肽BBB高分 | UniDL4BioPep BBB输出≥0.80；5–30 aa | 3,446 | 32,754条短肽候选 |
| 长肽BBB高分 | UniDL4BioPep BBB输出≥0.80；31–50 aa | 72 | 1,032条长肽候选 |
| BBB高分总计 | 短肽+长肽 | 3,518 | 算术和 |
| NTxPred2已评估 | 声明范围7–50 aa | 3,299 | 3,518条BBB高分候选 |
| NTxPred2未评估 | 低于声明范围 | 219 | 3,518条BBB高分候选 |
| NTxPred2阳性 | 来源模型标签 | 923 | 3,299条已评估候选 |
| 金属结合阳性 | mebipred输出≥0.50 | 111 | 来源报告下游计数；逐行交接缺失 |
| CHEL优选 | CHEL≥0.25 | 15 | 111条报告金属阳性候选 |
| 主集合 | CHEL≥0.25且FRS<0.50 | 12 | 111条报告金属阳性候选 |
| 更严格子集 | CHEL≥0.25且FRS<0.45 | 8 | 111条报告金属阳性候选；成员未知 |

![图1. 保留证据边界的汇总优选漏斗](../figures/prioritization_funnel.png)

**图1.** 汇总筛选漏斗。实线转换可由算术重建。因缺少逐行链路，NTxPred2至mebipred转换保持虚线。主要来源缺少候选身份；外部来源记录提供12条序列，但未提供其逐行筛选链路。

### 3.5 外部序列清单可进行组成审计

外部来源记录列出12条互不重复的序列，均由标准氨基酸组成，长度7–9个残基（表3）。11条含组氨酸，6条含半胱氨酸，每条都至少含一个Arg/Lys。这些组成陈述可直接由字符串复现，有助于合成和假设设计，但不能验证金属结合、BBB转运、毒性、分类归属或其与主要来源12行的对应。

**表3. 外部报告12条序列及独立重算组成**

| 按报告Vina均值排序 | 序列 | 长度 | His | Cys | Arg+Lys | Phe+Tyr+Trp |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | 1 | 0 | 1 | 1 |
| 2 | YLSLLQR | 7 | 0 | 0 | 1 | 1 |
| 3 | ALLLHRC | 7 | 1 | 1 | 1 | 0 |
| 4 | FCLHLQLR | 8 | 1 | 1 | 1 | 1 |
| 5 | YHHLLCRR | 8 | 2 | 1 | 2 | 1 |
| 6 | LLHLPKRTT | 9 | 1 | 0 | 2 | 0 |
| 7 | LLHPLRL | 7 | 1 | 0 | 1 | 0 |
| 8 | WLLVHLKK | 8 | 1 | 0 | 2 | 1 |
| 9 | LLHPLRC | 7 | 1 | 1 | 1 | 0 |
| 10 | HLLTLKKHV | 9 | 2 | 0 | 2 | 0 |
| 11 | HLPLLHRCC | 9 | 1 | 2 | 1 | 0 |
| 12 | HVLLLRQCA | 9 | 1 | 1 | 1 | 0 |

更严格8/12子集的成员仍未知，因为两个证据层均未提供序列层面的FRS标签。

### 3.6 来源报告Vina汇总可对12条序列排序，但不构成对接复现

外部记录提供的Vina均值为−9.60至−8.25 kcal/mol，SD为0.04至0.12（表4，图2）。排序、唯一性和数值范围均通过确定性检查。前三条报告均值依次为FLLHTTR −9.60、YLSLLQR −9.49和ALLLHRC −9.29 kcal/mol；末两条为HLPLLHRCC −8.35和HVLLLRQCA −8.25 kcal/mol。

**表4. 针对人AChE PDB 4EY6的来源报告AutoDock Vina汇总**

| 排名 | 序列 | 报告均值（kcal/mol） | 报告SD | 当前证据状态 |
| ---: | --- | ---: | ---: | --- |
| 1 | FLLHTTR | −9.60 | 0.08 | 已转录汇总；原始运行/构象缺失 |
| 2 | YLSLLQR | −9.49 | 0.05 | 同上 |
| 3 | ALLLHRC | −9.29 | 0.11 | 同上 |
| 4 | FCLHLQLR | −9.27 | 0.09 | 同上 |
| 5 | YHHLLCRR | −9.03 | 0.07 | 同上 |
| 6 | LLHLPKRTT | −9.01 | 0.06 | 同上 |
| 7 | LLHPLRL | −8.94 | 0.10 | 同上 |
| 8 | WLLVHLKK | −8.94 | 0.04 | 同上 |
| 9 | LLHPLRC | −8.91 | 0.08 | 同上 |
| 10 | HLLTLKKHV | −8.88 | 0.05 | 同上 |
| 11 | HLPLLHRCC | −8.35 | 0.12 | 同上 |
| 12 | HVLLLRQCA | −8.25 | 0.09 | 同上 |

![图2. 来源报告PAS中心对接分数汇总](../figures/fig5_docking_scores.png)

**图2.** 针对PDB 4EY6的来源报告Vina均值±SD描述性可视化。数值转录自外部来源记录，未被独立复现。缺失运行定义使SD无法对应已知数量的独立重复；Vina分数不是结合自由能 [51,52]。

外部叙述还描述了PAS/峡谷接触，但不存在构象或相互作用文件，因此残基层面的接触陈述未被提升为经审计观察。可辩护的结构结果仅限来源不完整的集合内报告排序。

### 3.7 证据阶梯仅部分前移

外部序列清单解决了“没有可合成分子”的实际问题，但未解决链路问题：没有稳定标识将每条序列连接到受试者、组装、证据匹配、预测器行、CHEL/FRS行或更严格子集。对接汇总同样不能替代可复现对接产物。翻译/表达、BBB转运、细胞毒性、金属依赖化学和疾病相关性仍未被检验。

![图3. 证据阶梯](../figures/evidence_ladder.png)

**图3.** 整合外部来源记录和前瞻性MD流程后的证据阶梯。汇总筛选已达到；12条序列和对接分数属于部分可用的来源报告信息；MD阶段仅有登记方法，不含可接纳轨迹结果。原始链路和对接产物、表达、暴露、表型、机制和因果关系仍未解决或未测试。

## 4. 讨论

### 4.1 扩展重建的主要贡献

本次重建具有足够的科学深度，可同时呈现生物学理由与证据瓶颈。主要筛选记录描述了剧烈收缩：牙周炎分支超过1,170万条smORF变为33,786条证据过滤候选、3,518条BBB高分输出、3,299条已评估序列中的923条NTxPred2阳性，最终形成来源报告的12条和8条CHEL/FRS终点计数。外部来源记录整合增加了12条明确的7–9 aa序列及其AChE对接报告排序，使匿名终点计数转化为具体、可合成的假设集合。

但扩展不能支持更强因果语言。12条序列尚不能逐行追溯至主要漏斗，对接也不能从现有项目复现。因此，核心进展是**保留来源边界的可操作性**：研究者能看到应合成哪些序列、应尝试复现哪一外部排序、缺少哪些信息以及哪些陈述仍被禁止。

### 4.2 与当前smORF和肽发现标准的比较

当前smORF研究把预测与翻译或蛋白质组证据结合 [1–5]；当代口腔宏蛋白质组采用明确错误控制、分类和谱图保存 [10–12]；有说服力的肽挖掘研究会合成候选并测量功能 [19]。本研究记录与上述标准有三项差距：第一，无法在序列/谱图层面检查证据匹配；第二，缺少参与者和样本映射；第三，两个来源均未提供带锁定版本和数据库的可执行筛选流程。

外部12条序列仍具有实用价值。确认来源后，可开展精确重复搜索、分类归属、模型适用域评估、合成可行性审查和预测器直接重跑。该集合还呈现短、阳离子、富亮氨酸且组氨酸/半胱氨酸富集的组成模式。这可能反映预期金属结合筛选，也可能反映序列域偏倚、膜活性基序或相关预测器特征。赋予生物学意义之前，需要组成匹配的诱饵序列和替代预测器。

### 4.3 AChE/PAS对接随访的解释

AChE PAS是AD导向假设的合理靶点，因为AChE可加速Aβ装配，PAS定向配体可调节该过程 [23–29]。PDB 4EY6提供具药理学配体的人AChE结构 [27]。因此，来源报告的PAS中心Vina筛选可作为初步结构分流 [51,52]。外部分数范围显示，在所选评分流程下12条均被保留，极端均值相差约1.35 kcal/mol。

但多项因素阻止将该范围视为结合证据。7–9 aa柔性肽具有大量构象；受体刚性、质子化、端基、肽初始构象、盒位置、exhaustiveness和评分随机性均可改变排序。外部项目没有提供这些细节或任何构象。未说明SD代表模式、种子、重复制备还是其他单位，故不能解释。单一靶标/流程的分数不能证明选择性、PAS相对于其他位点的偏好、催化抑制、Aβ调节或细胞内活性。可复现随访应保存受体和配体制备文件、精确命令、种子、所有分数与构象，以及容器/环境。随后可采用FlexPepDock等柔性精修或肽特异流程检验排序稳定性 [53]。

### 4.4 金属结合与短神经活性肽假设

11条含组氨酸、6条含半胱氨酸，为配位提供了可能基团，但组成或mebipred不能给出结合常数、化学计量、选择性、氧化态、几何或氧化还原行为。Tau片段研究展示了测量路径：Cu(II)配位可与结构变化及Aβ聚集效应联系 [32]，tau26–44则提供短神经活性肽的细胞和生物物理证据 [33]。Curli实验显示细菌淀粉样暴露可改变模型生物中的聚集表型 [34]。这些是实验模板，而不是类比证明。

最低限度的金属验证应以光谱和量热比较Cu(II)、Fe(II/III)和Zn(II)，估计化学计量和亲和力，并在肽单独、金属单独、打乱序列、组成匹配以及阳性/阴性对照下测量金属依赖ROS和脂质过氧化。效应需在独立合成批次中重复并呈浓度依赖。“促氧化”标签应要求在明确定义的金属条件下氧化增加，而不是仅依赖CHEL高/FRS低预测。

### 4.5 牙周炎–AD解释仍属于假设生成

流行病学记录可提供动机，但不能证明该通路 [35–43]。牙周炎可能与年龄、吸烟、糖尿病、社会经济状况、口腔护理、药物、虚弱和认知下降导致的反向因果相关。近期遗传因果分析是对强机制叙事的重要制衡 [41,42]。特定牙龈卟啉单胞菌研究支持牙龈蛋白酶、炎症、囊泡或感染路径的合理性 [44–50]，但不能转移给未归属的群落序列。

因此，本研究不声称12条肽是牙周炎特异、牙龈卟啉单胞菌来源、存在于血液或脑，或与AD存在因果关系。唯一队列相关陈述是：主要流程通过标注为牙周炎的分支对它们进行优选。分类归属和队列流行度需要序列—组装—样本映射及合适的受试者层面统计。

### 4.6 为什么汇总候选计数不支持推断性组间检验

外部来源记录草稿使用了肽层面的2×2检验，本研究未保留。来自同一参与者的数百万smORF、跨参与者同源序列、同一组装的候选以及重复精确匹配彼此相关。把每条序列当作独立单位会夸大有效样本量，并可能为微小差异生成很小的p值。适当单位应是参与者或样本，并在处理聚类、重复序列、测序深度、口腔位点和协变量后汇总或建模候选结果。

有效的健康—牙周炎比较需要参与者×候选或参与者×特征矩阵、预先指定终点、一致分母、重复/同源处理，以及在参与者层面运行的混合模型或置换模型。目前不存在这些行，因此描述性比例是可辩护分析的上限。

### 4.7 可重复性优先事项

最高优先级是重建统一的候选层面表格，包含：序列；稳定ID；基因组坐标；组装；参与者/样本；分组；分类；序列/蛋白质组证据及谱图层面统计；每个预测器的版本、分数、阈值决策和适用性标记；CHEL/FRS值；主集合/严格集合成员；以及与每个对接配体的链接。筛选流程应包含数据库快照、精确命令、锁定环境和校验和。

对接发布应增加受体登录号和链、缺失残基处理、质子化、端基、电荷、水/辅因子、配体构象、PDBQT、盒中心与大小、exhaustiveness、mode数、energy range、种子、原始日志、所有构象、聚类和相互作用分析代码。现已登记的GROMACS流程记录了100 ns方案，但审计快照不含起始复合物结构和完整模拟包。本稿不使用任何局部轨迹指标。后续MD报告必须版本化最终参数集，前瞻性解决生产期控压以及种子/重复设计，归档全部原始轨迹与日志，并在不根据结果修改流程的前提下实施预先指定分析。

### 4.8 实验验证路线与停止规则

分阶段计划可降低成本，并防止下游叙事弥补上游不确定性：

1. **链路与计算复现：** 核实12行，恢复8/12子集，重跑预测器和对接，并测试替代肽构象/流程。
2. **翻译/表达：** 采用队列匹配宏转录组、可行时核糖体测序，或具有肽层面错误发现率控制和分类唯一性的靶向宏蛋白质组。
3. **化学身份与稳定性：** 合成肽并确认纯度/质量；测量血清/蛋白酶稳定性、溶解度、聚集和非特异膜破坏。
4. **BBB与毒理：** 使用通透/转运模型，再实施神经元与非神经元存活、膜完整性及剂量—反应测定；分别评估预测BBB和NTx标签。
5. **金属化学：** 定量Cu/Fe/Zn结合，并在受控化学计量和氧化态下测量金属依赖ROS/脂质过氧化。
6. **AChE/Aβ测试：** 测量AChE/BChE活性、必要时直接结合，以及肽单独和金属条件下Aβ聚集。对接只能指导实验，不能替代实验。
7. **疾病相关性：** 只有身份、暴露、可重复生化活性和生物学重复表型均得到验证的候选，才能进入复杂疾病模型。

停止规则不可缺少。无法追溯的序列不应进入机制解释；缺少表达证据的肽可保留为合成假设，但不能作为队列生物标志物；无论对接分数如何，未通过可复现金属依赖或毒理学实验的肽均不应被描述为神经毒机制。

### 4.9 优势与局限

优势包括明确分离的证据架构、完整汇总算术、显式分母、拒绝伪重复推断检验、整合具体序列清单、独立序列组成审计、透明对接来源、前瞻性版本化MD方案、基于证据综合的机制背景，以及可复现SVG和文档构建。本稿还保留负面边界，而不隐藏材料缺失。

局限仍具有决定性。主要来源缺少逐行数据和代码；外部序列清单无法审计连接到主要来源12行或更严格8条；对接汇总缺少原始产物且未复现；MD起始结构和完整原始模拟包不可用，轨迹分析尚未完成，本文不报告MD结果；候选分类、翻译、队列表达、BBB转运、毒性、金属化学、AChE结合/功能、Aβ效应和疾病关联均未测量；登录号关系已解决，但候选—样本、登录号—分组和MAG-bin映射仍不可得。增加文字或文献不能消除这些局限。

## 5. 结论

保留来源边界的重建可在不夸大的前提下提高汇总研究的科学用途。主要记录支持一条可审计算术漏斗，终点为12条主集合和8条严格集合计数。单独归档的外部来源记录增加了12条明确的7–9 aa序列及其AChE Vina报告排序；序列组成和分数排序可复现，但筛选链路与对接执行不可复现。因此，当前结果是一套扩展、可操作的假设包，而不是经验证的肽机制。

下一步计算工作是发布或重建逐行筛选和对接产物，并以版本化输入、完整轨迹、日志、重复定义和预先指定分析完成已登记MD流程。其后仍需实验评价表达、转运、毒理、金属化学和AChE/Aβ效应。在此之前，不应提出疾病特异性、靶标结合、动态稳定性或因果结论。

## 声明

### 伦理批准与参与同意

现有材料描述公共数据衍生序列的汇总二次计算分析，不含可识别参与者信息。本次重建未进行新招募、干预或标本采集。因此，本文不报告新的人类参与者活动，也不指定伦理批准编号。

### 出版同意

不适用；本文不含可识别个体材料。

### 数据可用性

主要记录列出PRJNA678453、PRJEB65451、PXD003151、PXD004319、PXD026727及HOMD/eHOMD。PRJEB65451是与PRJNA678453关联的衍生EBI-EMG/MGnify TPA组装项目；因缺少可重算映射和bin清单，正文不报告队列或MAG总数。外部来源记录提供表3的12条序列，但不含稳定ID、受试者/样本映射、谱图、分类、预测器逐行输出、严格子集标签或主要来源链路。PDB 4EY6为公共结构[27]。原始对接输入、运行、日志和构象不可用。前瞻性MD脚本版本化于`shaohuawen03-cyber/asd`提交`f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`；本次分析无法获得完整起始结构和原始生产轨迹。

### 代码可用性

本仓库含文档提取、汇总算术、序列组成检查、可编辑文字SVG图件、DOCX打包和质量审计代码；不含原始smORF发现/预测管线，也不含外部对接的可执行复现。参考MD仓库含前瞻性流程，但缺少接纳结果所需的完整输入和原始轨迹。因此，现有代码可复现报告算术和文档层审计，但不能复现缺少输入和执行产物的分析。

### 经费

来源材料中无可用经费信息。

### 利益冲突

来源材料中无可用利益冲突声明。

### 作者贡献

来源材料中无可用作者身份和CRediT贡献信息；作者资格不从文件来源推断。

### 生成式人工智能使用

生成式AI助手用于来源组织、双语起草、确定性检查、图件脚本和语言编辑；未生成新生物学观察，也未独立复现缺失的筛选/对接分析。科学主张被限定于有引文支持的文献和可审计来源记录。

## 参考文献

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
3. Davin ME, Ortís Sunyer J, Delgado LF, et al. High-resolution multi-omics enhances prediction and detection of smORF-encoded proteins in the human gut microbiome. *Nat Commun*. 2026. doi:10.1038/s41467-026-72762-5.
4. Couso JP, Patra P. Short ORFs: finding gems in hidden places. *Curr Opin Genet Dev*. 2017;45:14–21. doi:10.1016/j.gde.2017.04.002.
5. van Heesch S, Wit F, Botter J, et al. The translational landscape of the human heart. *Cell*. 2019;178(1):236–251.e24. doi:10.1016/j.cell.2019.05.010.
6. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
7. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
8. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
9. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
10. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
11. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
12. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
13. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
14. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
15. Liu X, Zhao Z, Guan J, et al. Prediction of blood-brain barrier-penetrating peptides using B3BPFN. *Front Mol Biosci*. 2026;13:1858506. doi:10.3389/fmolb.2026.1858506.
16. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
17. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
18. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
19. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
20. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
21. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
22. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
23. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
24. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
25. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
26. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept). *Structure*. 1999;7(3):297–307. doi:10.1016/s0969-2126(99)80040-9.
27. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
28. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
29. Lushchekina SV, Kots ED, Novichkova DA, et al. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7:396–402. doi:10.1007/s12668-016-0375-x.
30. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
31. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer’s disease. *J Biol Chem*. 2021;296:100105. doi:10.1074/jbc.REV120.008207.
32. Di Natale G, Bellia F, Sciacca MFM, et al. Tau-peptide fragments and their copper(II) complexes: effects on amyloid-β aggregation. *Inorg Chim Acta*. 2018;472:82–92. doi:10.1016/j.ica.2017.09.061.
33. Perini G, Ciasca G, Minelli E, et al. Dynamic structural determinants underlie the neurotoxicity of the N-terminal tau 26–44 peptide. *Int J Biol Macromol*. 2019;141:278–289. doi:10.1016/j.ijbiomac.2019.08.220.
34. Chen SG, Stribinskis V, Rane MJ, et al. Exposure to the functional bacterial amyloid protein curli enhances alpha-synuclein aggregation. *Sci Rep*. 2016;6:34477. doi:10.1038/srep34477.
35. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
36. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
37. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
38. Kim J, Han DH. Periodontitis as a risk factor for dementia. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
39. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
40. Jiang Z, Shi Y, Zhao W, et al. Association between chronic periodontitis and the risk of Alzheimer’s disease. *BMC Oral Health*. 2021;21:466. doi:10.1186/s12903-021-01827-2.
41. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
42. Zhao Y, Zhang C, Chang X, et al. Causal association between periodontitis and systemic diseases: a systematic review and meta-analysis of Mendelian randomization studies. *BMC Oral Health*. 2026;26:383. doi:10.1186/s12903-026-07725-9.
43. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
44. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
45. Poole S, Singhrao SK, Kesavalu L, et al. Determining the presence of *Porphyromonas gingivalis* in Alzheimer’s disease brain. *J Alzheimers Dis*. 2013;33(3):665–678. doi:10.3233/JAD-2012-121149.
46. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
47. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
48. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
49. Haditsch U, Roth T, Rodriguez L, et al. Alzheimer’s disease-like neurodegeneration in *Porphyromonas gingivalis* infected neurons with persistent expression of active gingipains. *J Alzheimers Dis*. 2020;75(4):1361–1376. doi:10.3233/JAD-200393.
50. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
51. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
52. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
53. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
