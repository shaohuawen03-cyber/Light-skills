# Discussion replacements. Keys = prefixes in the a9 English backup
# (or current Chinese body). Fact + [n]; overview of THIS study; no et al. used;
# no RMSD/SASA tables. First-appearance numbers 38-54 stay in order.

EN_REPLACE = {
    "AChE hydrolyses acetylcholine at cholinergic synapses.": (
        "Twelve 7–9-aa cationic peptides from the periodontitis MAG library dock to "
        "human AChE, and three remain on the surface for 100 ns without unfolding the "
        "enzyme. Recurring contacts sit on the PAS (Asp74, Tyr72, Trp286, Tyr341), the "
        "peripheral site that templates Aβ assembly [4–6]. AChE–Aβ particles are more "
        "toxic than free peptide, and stable enzyme–peptide complexes raise fibril "
        "neurotoxicity [4,38–39]. A short hydrophobic PAS motif is sufficient for that "
        "chaperone effect [5]; antibody blockade and PAS-directed ligands reach the "
        "same endpoint [6,40]. Excess AChE promotes cortical plaques in mice [41], and "
        "plaque-associated enzyme remains PAS-sensitive [42–44]. Hippocampal AChE–Aβ "
        "complexes out-damage free fibrils [45]. The PAS maps to Tyr72, Asp74, Tyr124, "
        "Trp286 and Tyr341, about 20 Å from the catalytic triad [46]. The trajectories "
        "below ask whether an oral micropeptide can occupy that hinge [2–3]."
    ),
    "An oral exposure path is already documented": (
        "An oral path to brain AChE is a hypothesis, not a demonstrated traffic route. "
        "Periodontopathic cargo has been reported in AD brain, and oral infection can "
        "raise brain Aβ in mice [14,15,47–49]. Gingipains and outer-membrane vesicles "
        "already leave the producing cell [12–13]. Epidemiology links periodontitis to "
        "later cognitive decline [9–10]; Mendelian randomization did not support a "
        "genetic causal effect [11]. Those reports justify looking at oral products at "
        "the PAS. They do not assign the twelve peptides to P. gingivalis, or prove "
        "that any string crosses endothelium [7–8,25]. Survival in saliva, serum and "
        "endothelium is outside this calculation."
    ),
    "Deep-learning peptide mining supplies the filter stack used here.": (
        "The twelve docking ligands are 7–9 residues, alkaline, and net-positive at "
        "pH 7.4, with leucine-rich cores. That composition matches the electrostatic "
        "character of the PAS: Asp74 and Trp286 form a common core for peripheral "
        "ligands [50], and cationic substrate first docks on Asp74 [51]. A short "
        "cationic peptide is a plausible PAS occupant on chemical grounds, pending a "
        "structure. Deep-learning scores in this work are a triage stack, not a "
        "replication of the original predictors."
    ),
    "Human AChE (PDB 4EY6) gives an experimental frame": (
        "Human AChE (PDB 4EY6) frames the gorge and PAS [22], following the "
        "aromatic-gorge map on Torpedo AChE [23,52]. The 20-Å gorge couples a "
        "catalytic triad at the base to a peripheral cluster at the rim [53]. AutoDock "
        "Vina is a first-pass ranking engine [34–35]. Recurring contacts fall on the "
        "PAS array rather than a new pocket. FLLHTTR meets Asp74, Tyr72 and His287; "
        "YLSLLQR bridges Tyr72 and Thr75 at the gorge mouth; LLHPLRL spans Trp286 and "
        "Tyr341, the pair occupied by crystallised PAS ligands [54] and by donepezil "
        "in 4EY6 [22]. HLLTLKKHV reaches Phe346 in the 344–361 zone occupied by Aβ on "
        "a microsecond trajectory [21]. ALLLHRC is the exception: it binds catalytic "
        "Ser203 and misses the outer PAS aromatics. About half of the twelve best "
        "poses meet PAS residues. The three MD ligands were the strongest scorers, two "
        "of them PAS-positive. Docking scores put all twelve strings in a favourable "
        "window; they are ranks, not binding constants, and they do not by themselves "
        "separate a PAS occupant from a catalytic-site occupant. That distinction is "
        "the contact list."
    ),
    "MD studies of AChE–Aβ already treat the enzyme as a nucleation centre.": (
        "MD studies of AChE–Aβ already treat the enzyme as a nucleation centre "
        "[20,21]. The same occupancy pattern appears here. Apo AChE stays a compact "
        "hydrolase. ALLLHRC tracks that control. FLLHTTR and YLSLLQR sit tighter than "
        "apo after the first half of the run. A complex that is more compact than apo, "
        "with helix and sheet retained, is read as local rigidity after binding, not "
        "as unfolding [21,52]. YLSLLQR is the most compact ligand on the enzyme; "
        "ALLLHRC, which missed the PAS, is the most mobile. Rim loops fluctuate more "
        "than the triad, as expected for a surface cluster rather than a buried pocket "
        "[46,54]. Radius of gyration barely shifts, and secondary structure overlays "
        "the apo trace."
    ),
    "Mean RMSF is 0.0778 nm": (
        "Fluctuations at the catalytic core stay low in all four systems. FLLHTTR and "
        "YLSLLQR sit below apo in mean fluctuation; ALLLHRC sits slightly above. That "
        "pattern matches PAS binding as a surface event that need not open the fold "
        "[46,54]."
    ),
    "Hydrogen-bond histories separate the ligands": (
        "Intermolecular hydrogen bonds separate the ligands more clearly than "
        "compactness alone. FLLHTTR holds a dense net for the whole window; YLSLLQR a "
        "thinner net; ALLLHRC decays after early occupancy. Persistent contacts remain "
        "at the surface rather than in bulk solvent. Solvent-accessible surface rises "
        "for ALLLHRC, stays near apo for FLLHTTR, and falls only for YLSLLQR. FLLHTTR "
        "therefore reads as a hydrogen-bond-rich PAS occupant that rigidifies the "
        "protein without burying extra surface; YLSLLQR as a compact PAS occupant that "
        "does bury surface; ALLLHRC as a catalytic-site scorer that does not leave a "
        "lasting PAS-type network. PAS-directed ligands already separate from "
        "catalytic-site ligands on aggregation assays [6]. A microsecond Aβ trajectory "
        "and the present peptide trajectories differ in ligand length and window; both "
        "still show a ligand remaining at the PAS with the fold closed [21]."
    ),
    "Four linked steps then follow from the cited PAS literature.": (
        "Four linked steps then follow. First, PAS recognition: occupancy of Asp74, "
        "Tyr72, Trp286 and Tyr341 places a heterologous peptide at the gorge mouth "
        "that feeds the catalytic triad [3,22,51]. Second, a lasting enzyme–peptide "
        "complex: intermolecular hydrogen bonds persist, as in AChE–Aβ trajectories "
        "and in isolated stable complexes [20,21,38]. Third, restricted acetylcholine "
        "access: physical blockage at the 20-Å gorge entrance can hinder substrate "
        "even while the catalytic core remains folded [46,53]. Fourth, pathological "
        "chaperone activity: because the PAS is a documented pro-fibrillar site "
        "[4–5,43], a peptide that remains there can lower the nucleation barrier for "
        "endogenous Aβ. Folded AChE would then present a peptide-coated PAS on which "
        "Aβ oligomers can co-assemble, which accounts for the greater hippocampal "
        "damage of AChE–Aβ particles relative to free fibrils [45]."
    ),
    "PAS pharmacology in AChE has mostly been small molecules.": (
        "PAS pharmacology in AChE has mostly been small molecules. PAS ligands reduce "
        "AChE-induced aggregation without requiring catalytic-site occupancy [6]. "
        "Donepezil in 4EY6 spans PAS Trp286 to the catalytic anionic site [22–23]. "
        "That surface has been treated as a design handle for ligands that modulate "
        "heterologous protein associations, including Aβ [46]. Short cationic peptides "
        "occupy a larger surface than those ligands. Dual-binding inhibitors were "
        "designed to occupy PAS and the catalytic anionic site at once [44,46]. An "
        "oral heptapeptide that covers only the rim cannot be scored against that "
        "template. Occupancy that remains at the rim is the occupancy treated as the "
        "chaperone trigger [4]. FLLHTTR and YLSLLQR remain at that rim; ALLLHRC does "
        "not."
    ),
    "On that literature, short, cationic, leucine-rich oral micropeptides": (
        "Taken together, short, cationic, leucine-rich oral micropeptides predicted "
        "from PRJNA678453 MAGs can occupy the experimentally mapped Aβ-binding PAS and "
        "remain there on a 100-ns timescale. A binding assay and an Aβ-aggregation "
        "experiment are still required."
    ),
}

EN_DELETE_PREFIXES: tuple[str, ...] = ()

CN_REPLACE = {
    "AChE 在胆碱能突触水解乙酰胆碱。": (
        "牙周炎 MAG 文库筛出的十二条 7–9 aa 阳离子肽对接到人源 AChE，其中三条在 100 ns 内留在表面且不使酶去折叠。"
        "反复出现的接触落在 PAS（Asp74、Tyr72、Trp286、Tyr341），即模板化 Aβ 组装的外周位点[4–6]。"
        "AChE–Aβ 颗粒毒性高于游离肽，稳定的酶–肽复合物提高纤丝神经毒性[4,38–39]。"
        "一段疏水 PAS 基序即足以产生伴侣效应[5]；抗体阻断与 PAS 导向配体达到同一终点[6,40]。"
        "小鼠中过量 AChE 促进皮层斑块[41]，斑块相关酶仍对 PAS 阻断敏感[42–44]。"
        "海马区 AChE–Aβ 复合物的损伤强于游离纤丝[45]。"
        "PAS 定位于 Tyr72、Asp74、Tyr124、Trp286 和 Tyr341，距催化三联体约 20 Å[46]。"
        "下文轨迹问的是口腔微肽能否占据这一铰链[2–3]。"
    ),
    "口腔暴露路径在菌体和蛋白酶水平已有具体事例。": (
        "口腔产物到达脑内 AChE 仍是假说，不是已经证明的转运路径。"
        "AD 脑内已有牙周病原货物的报告，小鼠口腔感染可升高脑内 Aβ[14,15,47–49]。"
        "牙龈蛋白酶与外膜囊泡已能把货物送出产生细胞[12–13]。"
        "流行病学把牙周炎与后续认知下降联系起来[9–10]；孟德尔随机化未支持遗传因果[11]。"
        "这些报告支持在 PAS 上检查口腔产物，并不把十二条肽归于 P. gingivalis，也不证明任一字符串穿过内皮[7–8,25]。"
        "唾液、血清和内皮中的存活不在本次计算范围内。"
    ),
    "深度学习肽挖掘提供了此处的过滤栈。": (
        "十二条对接配体为 7–9 残基、碱性、pH 7.4 净正电，核心偏亮氨酸，与 PAS 的静电性质相符。"
        "Asp74 与 Trp286 构成外周配体的共同核心[50]，阳离子底物首先停在 Asp74[51]。"
        "短阳离子肽在化学上是合理的 PAS 占据者，结构上仍待显示。"
        "本文深度学习分数只作分诊栈，不是对原预测器的湿实验重复。"
    ),
    "人源 AChE（PDB 4EY6）为峡部与 PAS 提供实验框架": (
        "人源 AChE（PDB 4EY6）给出峡部与 PAS 的实验框架[22]，沿用电鳗 AChE 的芳香峡部定位[23,52]。"
        "20 Å 峡部把底部催化三联体与 rim 外周簇耦联[53]。AutoDock Vina 是第一轮排序引擎[34–35]。"
        "反复出现的接触落在 PAS 阵列上，而不是新口袋。"
        "FLLHTTR 碰到 Asp74、Tyr72 与 His287；YLSLLQR 在峡部入口桥接 Tyr72 与 Thr75；"
        "LLHPLRL 跨越 Trp286 与 Tyr341，即晶体 PAS 配体与 4EY6 中 donepezil 占据的同一对残基[22,54]。"
        "HLLTLKKHV 到达微秒轨迹中 Aβ 所在的 344–361 区 Phe346[21]。"
        "ALLLHRC 是例外：它结合催化 Ser203，不接触外侧 PAS 芳香残基。"
        "约半数最优构象碰到 PAS 残基。三条 MD 配体是打分最强者，其中两条 PAS 阳性。"
        "对接分数把十二条串放进有利窗口；它们是排序，不是结合常数，本身不能把 PAS 占据者与催化位点占据者分开。分开来自接触名单。"
    ),
    "AChE–Aβ 的 MD 已把该酶当作成核中心。": (
        "AChE–Aβ 的 MD 已把该酶当作成核中心[20,21]。同一占据模式在此出现。"
        "apo AChE 保持紧凑水解酶。ALLLHRC 跟随该对照。FLLHTTR 与 YLSLLQR 在轨迹后半段比 apo 更紧。"
        "复合物比 apo 更紧凑、螺旋与片层保留，读作结合后局部变刚，而不是去折叠[21,52]。"
        "YLSLLQR 是酶上最紧凑的配体；未碰到 PAS 的 ALLLHRC 最活动。"
        "rim loop 比三联体更活动，符合 PAS 是表面簇而非埋藏口袋[46,54]。"
        "回转半径几乎不动，二级结构与 apo 轨迹重叠。"
        "四个体系中催化核心涨落都低。FLLHTTR 与 YLSLLQR 的平均涨落低于 apo，ALLLHRC 略高。"
        "分子间氢键比紧凑程度更能分开配体：FLLHTTR 全程维持密网，YLSLLQR 网较薄，ALLLHRC 在早期占据后衰减。"
        "持续接触留在表面而非体相溶剂。溶剂可及表面在 ALLLHRC 上升，FLLHTTR 接近 apo，仅 YLSLLQR 下降。"
        "因此 FLLHTTR 读作富氢键的 PAS 占据者，使蛋白变刚但不额外埋藏表面；YLSLLQR 读作紧凑并埋藏表面的 PAS 占据者；"
        "ALLLHRC 读作随后失去 PAS 型网络的催化位点高分者。"
        "PAS 导向配体与催化位点配体在聚集测定上本已分开[6]。"
        "微秒 Aβ 轨迹与此处肽轨迹在配体长度和窗口上不同，两者都显示配体留在 PAS 上且折叠未打开[21]。"
    ),
    "四步机制由上述 PAS 文献推出。": (
        "由此推出四步。第一，PAS 识别：占据 Asp74、Tyr72、Trp286、Tyr341，把异源肽放在通向催化三联体的峡部入口[3,22,51]。"
        "第二，持续的酶–肽复合物：分子间氢键持续，与 AChE–Aβ 轨迹及分离得到的稳定复合物一致[20,21,38]。"
        "第三，乙酰胆碱进入受限：20 Å 峡部入口的物理占据可在催化核心仍折叠时妨碍底物[46,53]。"
        "第四，病理性伴侣活性：PAS 是已记录的促纤位点[4–5,43]，停在那里的肽可降低内源 Aβ 的成核壁垒。"
        "折叠的 AChE 于是出示覆肽 PAS，Aβ 寡聚体可在其上共组装，从而解释 AChE–Aβ 颗粒相对游离纤丝更强的海马损伤[45]。"
    ),
    "AChE 的 PAS 药理学此前多为小分子。": (
        "AChE 的 PAS 药理学此前多为小分子。PAS 配体在不要求占据催化位点的情况下降低 AChE 诱导的聚集[6]。"
        "4EY6 中的 donepezil 从 PAS Trp286 跨到催化阴离子位点[22–23]。"
        "该表面被当作调节异源蛋白结合（包括 Aβ）的设计把手[46]。短阳离子肽占据的表面大于这些配体。"
        "双结合抑制剂被设计成同时占据 PAS 与催化阴离子位点[44,46]。只盖住 rim 的口腔七肽不能按该模板打分。"
        "留在 rim 的占据，即被当作伴侣触发的占据[4]。FLLHTTR 与 YLSLLQR 留在 rim；ALLLHRC 不在。"
    ),
    "按上述文献，从 PRJNA678453 MAG 预测的短、带正电、富亮氨酸口腔微肽": (
        "综上，从 PRJNA678453 MAG 预测的短、带正电、富亮氨酸口腔微肽可以占据实验已定位的 Aβ 结合 PAS，"
        "并在 100 ns 尺度上留在那里。结合测定和 Aβ 聚集实验仍不可少。"
    ),
}

CN_DELETE_PREFIXES: tuple[str, ...] = ()
