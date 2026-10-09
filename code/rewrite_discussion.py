#!/usr/bin/env python3
"""Replace Discussion prose: fact + [n], no 'Author et al. used', no result recap.

Rebuilds English.docx from the pre-Zotero backup (plain [n] for manual import).
Mirrors Chinese discussion in deliverable/Chinese.docx.
"""
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

from lxml import etree

ROOT = Path("/home/user/Light-skills")
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

EN_BACKUP = ROOT / "projects" / "English_backup_pre-zotero.docx"
EN_OUT = ROOT / "projects" / "English.docx"
EN_DELIV = ROOT / "deliverable" / "English.docx"
CN_PATH = ROOT / "deliverable" / "Chinese.docx"

EN_REPLACE = {
    "AChE hydrolyses acetylcholine at cholinergic synapses.": (
        "AChE hydrolyses acetylcholine at cholinergic synapses. In AD tissue the same "
        "enzyme sits on amyloid plaques. AChE accelerates Aβ fibril growth through the "
        "PAS, and AChE–Aβ particles are more toxic than free peptide [4]. Stable "
        "enzyme–peptide complexes change AChE biochemistry and raise fibril "
        "neurotoxicity; the enzyme binds growing fibrils rather than free monomer "
        "alone [38–39]. A short hydrophobic PAS motif is sufficient for that chaperone "
        "effect [5]. A monoclonal antibody to AChE blocks the effect [40], and "
        "PAS-directed small molecules reach the same endpoint [6]. Excess AChE "
        "promotes cortical Aβ plaques in mice [41]. Reviews of AChE in AD place "
        "plaque-associated enzyme in cross-talk with Aβ and phospho-tau, still "
        "sensitive to PAS blockade [42–44]. Hippocampal AChE–Aβ complexes produce "
        "more damage than free fibrils [45]. The PAS maps to Tyr72, Asp74, Tyr124, "
        "Trp286 and Tyr341, about 20 Å from the catalytic triad at the gorge mouth "
        "[46]. Those experiments identify the PAS as a structural hinge between "
        "cholinergic failure and amyloid deposition [2–3]. The present docking and "
        "MD trajectories examine occupancy of that hinge by periodontitis-derived "
        "micropeptides."
    ),
    "An oral exposure path is already documented": (
        "An oral exposure path is already documented at the organism and protease "
        "level. Periodontopathic virulence factors have been detected in short-term "
        "postmortem AD brain [47]. P. gingivalis and gingipains have been reported in "
        "AD brains, and oral infection in mice raises brain Aβ1–42 [14]. AD-like "
        "neurodegeneration occurs in P. gingivalis-infected neurons that keep active "
        "gingipains [48]. Repeated oral application of a periodontal pathogen in "
        "wild-type mice produces neuroinflammation and Aβ-related changes [15]. "
        "P. gingivalis bacteremia increases endothelial permeability through an "
        "Mfsd2a/Caveolin-1 transcytosis path [49]. Gingipains and outer-membrane "
        "vesicles supply vehicles for bacterial cargo beyond the producing cell "
        "[12–13]. Meta-analyses and an AD cohort link periodontitis to later "
        "cognitive decline [9–10]. A two-sample Mendelian randomization analysis did "
        "not support a genetic causal effect [11]. Those reports justify looking at "
        "oral products at the PAS. Assignment of the twelve peptides to P. gingivalis, "
        "or proof that any one string crosses endothelium, lies outside those reports "
        "[7–8,25]. Gingipains, LPS and vesicles already travel, and a 7–9-aa cationic "
        "peptide is smaller than those cargos. Survival of such a peptide in saliva, "
        "serum and endothelium is outside the present calculation."
    ),
    "Deep-learning peptide mining supplies the filter stack used here.": (
        "Deep-learning peptide mining supplies the filter stack used here. Millions of "
        "translated microbiome open reading frames have been scored before experimental "
        "filters [18]. UniDL4BioPep uses the same predict-then-filter logic on ESM-2 "
        "embeddings [19]. NTxPred2, mebipred and AnOxPePred were trained for "
        "neurotoxic, metal-binding and antioxidant endpoints, not for AChE occupancy "
        "[31–33]. Catalogue matches to HOMD, eHOMD and salivary metaproteomes support "
        "prior observation of a string, as in other oral peptide studies [16,26–30], "
        "so the serial scores function as a triage stack. The twelve docking ligands "
        "are 7–9 residues, alkaline, and net-positive at pH 7.4, with leucine-rich "
        "cores. That composition matches the electrostatic character of the PAS. Asp74 "
        "and Trp286 form a common core for peripheral ligands [50], and cationic "
        "substrate first docks on Asp74 [51]. A short cationic peptide is a plausible "
        "PAS occupant on chemical grounds, pending a structure."
    ),
    "Human AChE (PDB 4EY6) gives an experimental frame": (
        "Human AChE (PDB 4EY6) gives an experimental frame for the gorge and PAS [22], "
        "following the aromatic-gorge map on Torpedo AChE [23,52]. The 20-Å gorge "
        "couples a catalytic triad at the base to a peripheral cluster at the rim [53]. "
        "AutoDock Vina is a first-pass ranking engine [34–35]. Recurring contacts fall "
        "on the PAS array (Asp74, Tyr72, Trp286, Tyr341) rather than on a new pocket, "
        "matching the Aβ-binding surface defined previously [4,21,46,54]. Dual "
        "PAS–catalytic geometry of the kind crystallised for donepezil in 4EY6 is not "
        "required for a rim occupant [22]. A strong docking score at Ser203 is not "
        "equivalent to PAS occupancy."
    ),
    "MD studies of AChE–Aβ already treat the enzyme as a nucleation centre.": (
        "MD studies of AChE–Aβ already treat the enzyme as a nucleation centre. "
        "Accelerated sampling pulled Aβ onto the AChE surface [20]. A 1-μs PAS-centred "
        "trajectory remained bound without unfolding the fold [21]. Apo AChE is already "
        "a stiff α/β hydrolase; the deep aromatic gorge does not require large domain "
        "motion for catalysis [52]. PAS binding has been described as a surface event "
        "that need not open the fold [46,54]. On that reading, a complex that stays "
        "compact relative to apo, keeps secondary structure, and remains at the rim is "
        "ligand-induced rigidity at a surface cluster, not peptide-driven unfolding. "
        "The same occupancy pattern is the one reported for surface-bound, "
        "non-dissociating AChE–Aβ complexes [20,21]. PAS-directed ligands suppress "
        "AChE-induced aggregation without requiring catalytic-site occupancy [6]."
    ),
    "Four linked steps then follow from the cited PAS literature.": (
        "Four linked steps then follow from the cited PAS literature. First, PAS "
        "recognition: occupancy of Asp74, Tyr72, Trp286 and Tyr341 places a "
        "heterologous peptide at the gorge mouth that feeds the catalytic triad, the "
        "first step assigned to cationic substrate at this enzyme [3,22,51]. Second, a "
        "lasting enzyme–peptide complex: intermolecular hydrogen bonds persist, as in "
        "AChE–Aβ trajectories and in isolated stable complexes [20,21,38]. Third, "
        "restricted acetylcholine access: physical blockage at the 20-Å gorge entrance "
        "can hinder substrate even while the catalytic core remains folded, the "
        "steric-blockade mode described for PAS ligands [46,53]. Fourth, pathological "
        "chaperone activity: because the PAS is a documented pro-fibrillar site "
        "[4–5,43], a peptide that remains there can lower the nucleation barrier for "
        "endogenous Aβ. Folded AChE would then present a peptide-coated PAS on which "
        "Aβ oligomers can co-assemble, which accounts for the greater hippocampal "
        "damage of AChE–Aβ particles relative to free fibrils [45]."
    ),
    "PAS pharmacology in AChE has mostly been small molecules.": (
        "PAS pharmacology in AChE has mostly been small molecules. PAS ligands reduce "
        "AChE-induced aggregation without requiring catalytic-site occupancy [6]. "
        "Donepezil in 4EY6 spans PAS Trp286 to the catalytic anionic site, a "
        "dual-binding template mapped on Torpedo AChE [22–23]. That surface has been "
        "treated as a design handle for ligands that modulate heterologous protein "
        "associations, including Aβ [46]. Short cationic peptides occupy a larger "
        "surface than those ligands. The present poses place an oral heptapeptide on "
        "the same aromatic cluster. Dual-binding inhibitors were designed to occupy "
        "PAS and the catalytic anionic site at once, with the therapeutic aim of "
        "slowing both acetylcholine hydrolysis and PAS-templated Aβ assembly [44,46]. "
        "An oral heptapeptide that covers only the rim cannot be scored against that "
        "dual-binding template. Occupancy that remains at the rim is the occupancy "
        "treated as the chaperone trigger [4]."
    ),
    "On that literature, short, cationic, leucine-rich oral micropeptides": (
        "On that literature, short, cationic, leucine-rich oral micropeptides "
        "predicted from PRJNA678453 MAGs can occupy the experimentally mapped "
        "Aβ-binding PAS and remain there on a 100-ns timescale. A binding assay and "
        "an Aβ-aggregation experiment are still required."
    ),
}

EN_DELETE_PREFIXES = (
    "Mean RMSF is 0.0778 nm",
    "Hydrogen-bond histories separate the ligands",
)

CN_REPLACE = {
    "AChE 在胆碱能突触水解乙酰胆碱。": (
        "AChE 在胆碱能突触水解乙酰胆碱。AD 组织中，同一酶出现在淀粉样斑块上。"
        "AChE 经 PAS 加速 Aβ 成纤，且 AChE–Aβ 颗粒毒性高于游离肽[4]。稳定的酶–肽复合物改变 "
        "AChE 生化性质并提高纤丝神经毒性；酶结合的是生长中的纤丝而非游离单体[38–39]。"
        "一段疏水 PAS 基序即足以产生伴侣效应[5]。抗 AChE 单抗可阻断该效应[40]，PAS 导向小分子达到同一终点[6]。"
        "小鼠中过量 AChE 促进皮层 Aβ 斑块[41]。关于 AD 中 AChE 的综述把斑块相关酶放进与 Aβ、磷酸化 tau 的交叉对话，"
        "且仍对 PAS 阻断敏感[42–44]。海马区 AChE–Aβ 复合物的损伤强于游离纤丝[45]。"
        "PAS 定位于 Tyr72、Asp74、Tyr124、Trp286 和 Tyr341，距峡部底部催化三联体约 20 Å[46]。"
        "这些实验把 PAS 定为胆碱能衰竭与淀粉样沉积之间的结构铰链[2–3]。"
        "本研究的对接与 MD 轨迹查看牙周炎来源微肽对该铰链的占据。"
    ),
    "口腔暴露路径在菌体和蛋白酶水平已有具体事例。": (
        "口腔暴露路径在菌体和蛋白酶水平已有具体事例。短期死后 AD 脑组织中已检出牙周致病毒力因子[47]。"
        "AD 脑内已报告 P. gingivalis 与牙龈蛋白酶，小鼠口腔感染升高脑内 Aβ1–42[14]。"
        "持续表达活性牙龈蛋白酶的感染神经元出现 AD 样变性[48]。"
        "野生型小鼠反复口腔给予牙周病原后产生神经炎症和 Aβ 相关改变[15]。"
        "P. gingivalis 菌血症经 Mfsd2a/Caveolin-1 转胞吞路径增加内皮通透性[49]。"
        "牙龈蛋白酶与外膜囊泡可把细菌货物送出产生细胞[12–13]。"
        "综合分析与 AD 队列把牙周炎与后续认知下降联系起来[9–10]。"
        "两样本孟德尔随机化并未支持遗传因果效应[11]。这些报告支持在 PAS 上检查口腔产物。"
        "把 12 条肽归于 P. gingivalis，或证明某一字符串穿过内皮，都不在这些报告之内[7–8,25]。"
        "牙龈蛋白酶、脂多糖和囊泡已经在走，7–9 aa 阳离子肽比这些货物更小。"
        "该肽在唾液、血清和内皮中能否存活，不在本次计算范围内。"
    ),
    "深度学习肽挖掘提供了此处的过滤栈。": (
        "深度学习肽挖掘提供了此处的过滤栈。数百万条翻译的微生物组开放阅读框先被打分，再做实验过滤[18]。"
        "UniDL4BioPep 在 ESM-2 嵌入上沿用同一先预测再过滤逻辑[19]。"
        "NTxPred2、mebipred 与 AnOxPePred 分别针对神经毒性、金属结合和抗氧化终点训练，并非针对 AChE 占据[31–33]。"
        "与 HOMD、eHOMD 和唾液宏蛋白质组的目录匹配支持该字符串曾经被观察到，这与其他口腔肽研究中这些资源的角色相同[16,26–30]，"
        "因而串联分数用作分诊栈。12 条对接配体为 7–9 残基、碱性、pH 7.4 净正电，核心偏亮氨酸。"
        "该组成与 PAS 的静电性质相符。Asp74 与 Trp286 构成外周配体的共同核心[50]，阳离子底物首先停在 Asp74[51]。"
        "短阳离子肽在化学上是合理的 PAS 占据者，结构上仍待显示。"
    ),
    "人源 AChE（PDB 4EY6）为峡部与 PAS 提供实验框架": (
        "人源 AChE（PDB 4EY6）为峡部与 PAS 提供实验框架[22]，沿用电鳗 AChE 上的芳香峡部定位[23,52]。"
        "20 Å 峡部把底部催化三联体与 rim 外周簇耦联[53]。AutoDock Vina 是第一轮排序引擎[34–35]。"
        "反复出现的接触落在 PAS 阵列（Asp74、Tyr72、Trp286、Tyr341）上，而不是新口袋，"
        "与先前界定的 Aβ 结合面相符[4,21,46,54]。4EY6 中 donepezil 那样的 PAS–催化双重几何，"
        "并非 rim 占据所必需[22]。Ser203 上的高对接分数不等于 PAS 占据。"
    ),
    "AChE–Aβ 的 MD 已把该酶当作成核中心。": (
        "AChE–Aβ 的 MD 已把该酶当作成核中心。加速采样把 Aβ 拉到 AChE 表面[20]。"
        "1 μs、以 PAS 为中心的轨迹保持结合且不使折叠打开[21]。"
        "apo AChE 本已是刚性 α/β 水解酶；深芳香峡部不需要大结构域运动即可催化[52]。"
        "PAS 结合被写成不必打开折叠的表面事件[46,54]。按该读法，复合物相对 apo 保持紧凑、二级结构保留、停在 rim，"
        "是表面簇上的配体诱导变刚，而不是肽驱动的去折叠。该占据模式与表面结合、不解离的 AChE–Aβ 复合物一致[20,21]。"
        "PAS 导向配体在不要求占据催化位点的情况下抑制 AChE 诱导的聚集[6]。"
    ),
    "四步机制由上述 PAS 文献推出。": (
        "四步机制由上述 PAS 文献推出。第一，PAS 识别：占据 Asp74、Tyr72、Trp286、Tyr341，"
        "把异源肽放在通向催化三联体的峡部入口，即该酶上赋予阳离子底物的第一步[3,22,51]。"
        "第二，持续的酶–肽复合物：分子间氢键持续，与 AChE–Aβ 轨迹以及分离得到的稳定复合物一致[20,21,38]。"
        "第三，乙酰胆碱进入受限：20 Å 峡部入口的物理占据可在催化核心仍折叠时妨碍底物，即 PAS 配体的空间阻断方式[46,53]。"
        "第四，病理性伴侣活性：PAS 是已记录的促纤位点[4–5,43]，停在那里的肽可降低内源 Aβ 的成核壁垒。"
        "折叠的 AChE 于是出示覆肽 PAS，Aβ 寡聚体可在其上共组装，从而解释 AChE–Aβ 颗粒相对游离纤丝更强的海马损伤[45]。"
    ),
    "AChE 的 PAS 药理学此前多为小分子。": (
        "AChE 的 PAS 药理学此前多为小分子。PAS 配体在不要求占据催化位点的情况下降低 AChE 诱导的聚集[6]。"
        "4EY6 中的 donepezil 从 PAS Trp286 跨到催化阴离子位点，即电鳗 AChE 上的双结合模板[22–23]。"
        "该表面被当作调节异源蛋白结合（包括 Aβ）的设计把手[46]。短阳离子肽占据的表面大于这些配体。"
        "此处构象把口腔七肽放在同一芳香簇上。双结合抑制剂被设计成同时占据 PAS 与催化阴离子位点，"
        "治疗意图是同时减慢乙酰胆碱水解和 PAS 模板化的 Aβ 组装[44,46]。"
        "只盖住 rim 的口腔七肽不能按该双结合模板打分。留在 rim 的占据，即被当作伴侣触发的占据[4]。"
    ),
    "按上述文献，从 PRJNA678453 MAG 预测的短、带正电、富亮氨酸口腔微肽": (
        "按上述文献，从 PRJNA678453 MAG 预测的短、带正电、富亮氨酸口腔微肽可以占据实验已定位的 Aβ 结合 PAS，"
        "并在 100 ns 尺度上留在那里。结合测定和 Aβ 聚集实验仍不可少。"
    ),
}

CN_DELETE_PREFIXES = (
    "FLLHTTR 平均 RMSF 为 0.0778 nm",
    "氢键历史比 RMSD 更能分开配体。",
)


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.iter(f"{W}t"))


def set_para_text(p, text: str) -> None:
    pPr = p.find(f"{W}pPr")
    for child in list(p):
        if child is not pPr:
            p.remove(child)
    r = etree.SubElement(p, f"{W}r")
    t = etree.SubElement(r, f"{W}t")
    t.set(XML_SPACE, "preserve")
    t.text = text


def rewrite_xml(xml_bytes: bytes, replace: dict[str, str], delete_prefixes: tuple[str, ...]) -> bytes:
    root = etree.fromstring(xml_bytes)
    body = root.find(f"{W}body")
    if body is None:
        raise SystemExit("no w:body")
    replaced = []
    deleted = []
    unmatched = set(replace)
    for p in list(body.findall(f"{W}p")):
        txt = para_text(p)
        hit_del = next((d for d in delete_prefixes if txt.startswith(d)), None)
        if hit_del:
            parent = p.getparent()
            parent.remove(p)
            deleted.append(hit_del[:40])
            continue
        hit = next((k for k in replace if txt.startswith(k)), None)
        if hit:
            set_para_text(p, replace[hit])
            replaced.append(hit[:40])
            unmatched.discard(hit)
    if unmatched:
        raise SystemExit(f"unmatched prefixes: {sorted(unmatched)}")
    print("  replaced:", len(replaced), replaced)
    print("  deleted:", len(deleted), deleted)
    return etree.tostring(
        root,
        xml_declaration=True,
        encoding="UTF-8",
        standalone=True,
    )


def patch_docx(src: Path, dst: Path, replace: dict[str, str], delete_prefixes: tuple[str, ...]) -> None:
    tmp = dst.with_suffix(".tmp.docx")
    with zipfile.ZipFile(src, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "word/document.xml":
                data = rewrite_xml(data, replace, delete_prefixes)
            zout.writestr(info, data)
    tmp.replace(dst)
    print("wrote", dst, dst.stat().st_size)


def main() -> None:
    print("== English from backup (plain [n], no Zotero fields)")
    shutil.copy2(EN_BACKUP, EN_OUT)
    patch_docx(EN_OUT, EN_OUT, EN_REPLACE, EN_DELETE_PREFIXES)
    shutil.copy2(EN_OUT, EN_DELIV)
    print("copied", EN_DELIV)

    print("== Chinese")
    patch_docx(CN_PATH, CN_PATH, CN_REPLACE, CN_DELETE_PREFIXES)

    def words(text: str) -> int:
        return len(text.split())

    en_body = " ".join(EN_REPLACE.values())
    print("EN discussion body words:", words(en_body))
    print("CN discussion body chars:", sum(len(v) for v in CN_REPLACE.values()))


if __name__ == "__main__":
    main()
