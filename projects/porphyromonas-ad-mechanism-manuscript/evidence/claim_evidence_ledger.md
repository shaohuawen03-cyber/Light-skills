# Claim–evidence ledger / 主张—证据台账

## Evidence grades / 证据等级

- **A**：主证据源直接给出、内部算术一致的聚合结果。
- **B**：由 A 级聚合计数确定性重新计算的描述性比例。
- **C**：经 DOI/PubMed/出版商页面核验的外部文献，用于背景、工具说明或讨论。
- **E**：用户指定外部v0.4项目中的作者报告汇总；可转录和审计字符串/算术，但未由原始输入与执行产物独立复现。
- **D**：合理但尚未经本研究检验的机制假设，只能在 Discussion/Future work 中明确标为假设。
- **N**：当前无支持，不得作为结果或结论。

| Claim ID | Proposed claim / 拟用主张 | Evidence / 证据 | Grade | Permitted wording / 允许措辞 | Prohibited extension / 禁止外推 |
| --- | --- | --- | --- | --- | --- |
| C01 | 健康和牙周炎原始 sORF 分别为 11,269,961 与 11,721,988 | 主源段落 5、26；表 3-1 | A | “the supplied analysis reported…” | 不得声称已在本轮重新运行 sORF 发现流程 |
| C02 | 证据过滤后候选为 31,510 与 33,786 | 主源段落 9、26；表 3-1 | A | “nonredundant evidence-filtered candidates” | 长肽证据链未澄清前，不把全部称作质谱确证 |
| C03 | 过滤率为 0.2796% 与 0.2882% | 由 C01、C02 重算 | B | 描述性比例 | 不得称显著差异或富集 |
| C04 | 短肽 BBB 高分为 3,359/30,557 与 3,446/32,754 | 主源段落 29、表 3-3 | A/B | “model output ≥0.80” | 不得称真实穿越 BBB |
| C05 | 长肽 BBB 高分为 40/953 与 72/1,032 | 主源段落 29、表 3-2 | A/B | “model output ≥0.80” | 不得称组间显著升高 |
| C06 | 牙周炎分支 BBB 高分候选合计 3,518 | 主源段落 38、表 3-4 | A | “periodontitis-branch candidates” | 不得称牙周炎特异性 |
| C07 | 牙周炎 BBB 高分短肽主要为 8–15 aa（2,893/3,446） | 主源段落 38 | A/B | “83.95% of short candidates” | 不得外推到所有口腔微肽 |
| C08 | NTxPred2 覆盖 3,299，排除 <7 aa 的 219 条 | 主源段落 41、表 3-4 | A/B | “outside this model step’s stated input range” | 不得把未覆盖候选判为阴性 |
| C09 | NTxPred2 阳性 923/3,299，且主源报告均 ≤30 aa | 主源段落 41 | A/B | “predicted neurotoxic” | 不得称已证实神经毒性 |
| C10 | 报告 111 条 Cu/Fe/Zn 结合阳性 | 主源段落 42、表 3-4 | A（交接分母不确定） | 报告计数并注明 denominator/handoff 未独立审核 | 不报告 111/923 百分比为确定结果 |
| C11 | 15 条 CHEL≥0.25；12 条同时 FRS<0.50；8 条同时 FRS<0.45 | 主源段落 43、表 3-4 | A/B | “operational prioritization set” | 不得称促氧化候选已确证 |
| C12 | UniDL4BioPep 是基于预训练生物语言模型嵌入和 CNN 的肽活性预测框架 | Du et al., 2023, DOI 10.1093/bib/bbad135 | C | 工具原理描述 | 不得把输出概率当外部校准的临床概率 |
| C13 | NTxPred2 提供肽/蛋白神经毒性预测模型 | Rathore et al., 2025, DOI 10.1002/pro.70200 | C | 工具用途说明 | 不得替代实验毒理学 |
| C14 | mebipred 从序列估计金属结合潜力 | Aptekmann et al., 2022, DOI 10.1093/bioinformatics/btac358 | C | “metal-binding potential” | 不得称结合常数、位点或配位几何 |
| C15 | AnOxPePred 预测自由基清除和螯合特征 | Olsen et al., 2020, DOI 10.1038/s41598-020-78319-w | C | 工具用途说明 | FRS 低不等于产生自由基；CHEL 高不等于促氧化 |
| C16 | 人体微生物组中存在大量传统流程容易遗漏的小蛋白家族 | Sberro et al., 2019, DOI 10.1016/j.cell.2019.07.016 | C | 引言背景 | 不得据此断言本研究候选均真实表达或有功能 |
| C17 | 牙周炎与认知下降/痴呆存在观察性关联，效应受研究设计等影响 | Larvin et al., 2023；Kaliamoorthy et al., 2022 | C | “associated with” and explicit observational boundary | 不得写成牙周炎导致 AD |
| C18 | 口腔细菌与 AD 的临床研究结果存在异质性 | Liu et al., 2023, DOI 10.3233/JAD-220627 | C | “moderate/inconsistent evidence” | 不得把脑内检出与因果等同 |
| C19 | *P. gingivalis*/gingipain 研究为机制研究提供动机 | Dominy et al., 2019, DOI 10.1126/sciadv.aau3333；Chalmers & Hernandez-Kapila, 2025 | C | 仅作领域背景，并强调本研究无物种归属 | 不得称本研究候选来自 *P. gingivalis* |
| C20 | AChE–Aβ研究提示PAS/峡谷区域可作为结构假设 | AChE/PAS文献 [23–29] | C/D | “motivates a PAS-focused docking question” | 不得据文献断言当前候选结合该区域 |
| C21 | 候选肽可能通过金属稳态、氧化应激、AChE/Aβ 等路径与 AD 相关 | 仅为综合假设；无本研究机制实验 | D | Discussion 中以 “could be tested” 表述 | 不得进入结果性机制结论；不得用 prove/show |
| C22 | 候选肽来源于特定微生物 | 无序列分类学归属 | N | 不写 | 任何属种归因均禁止 |
| C23 | 12 条候选在金属存在时具有促氧化神经毒性 | 无 ROS、脂质过氧化、细胞毒性实验 | N | 仅写为未来验证标准 | 不得作为摘要结果或结论 |
| C24 | 候选肽与 AChE/Aβ/tau 发生经验证的直接结合 | 仅有未复现的外部Vina汇总；无姿势、MD或实验 | N | 仅写“source-reported docking scores” | 不得声称亲和力、接触、功能或机制 |
| C25 | 外部v0.4列出12条互不重复的7–9 aa序列 | 外部提交e28c06d；`external_v04_integration.md` | E | “externally reported twelve-sequence set” | 不得称已与主要来源逐行对应或属于严格8条 |
| C26 | 12条中11条含His、6条含Cys、12条均含Arg/Lys | 当前脚本由序列字符串重算 | E/B | “composition independently recomputed” | 不得由组成推断金属结合、BBB或毒性 |
| C27 | 外部Vina均值范围−9.60至−8.25 kcal/mol，SD 0.04–0.12 | 外部v0.4硬编码汇总；当前脚本核验转录 | E | “source-reported mean±SD; not reproduced” | 不得称结合自由能、亲和力或独立重复 |
| C28 | 外部称使用AChE 4EY6、Vina 1.2.5和40×40×40 Å³ PAS中心盒 | 外部方法叙述；无输入/配置/日志/构象 | E | 可转录方法标签并紧邻缺失声明 | 不得声称对接已复现、PAS接触已验证或MD已完成 |

## Manuscript placement / 稿件放置规则

- C01–C11：Methods/Results；必须带“aggregate supplied record”或同等来源限定。
- C12–C16：Introduction/Methods；引用工具或领域文献。
- C17–C20：Introduction/Discussion；保持观察性、临床前或结构假设边界。
- C21：Discussion/Future work，明确标注假设。
- C22–C24：只允许在limitations中作为“本研究未建立”的否定性边界出现；C24可与C27并列说明外部对接汇总的限制。
- C25–C28：Methods/Results；每次定量使用均须明确“external/source-reported”且不得省略未复现边界。
