#!/usr/bin/env python3
"""Build the wet-lab 2–3 peptide panel memo (CN). Not part of the SCI manuscript."""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path("/home/user/Light-skills")
OUT = ROOT / "deliverable" / "wetlab_ab_pc12_panel"
OUT.mkdir(parents=True, exist_ok=True)

# AGGRESCAN a3v (Conchillo-Sole 2007; used only as a self-amyloid proxy ranker)
A3V = {
    "A": -0.036, "C": 0.662, "D": -1.197, "E": -1.204, "F": 1.754,
    "G": -0.535, "H": -1.003, "I": 1.822, "K": -0.931, "L": 1.380,
    "M": 0.910, "N": -1.302, "P": -0.334, "Q": -1.231, "R": -1.008,
    "S": -0.256, "T": -0.159, "V": 1.594, "W": 1.037, "Y": 1.159,
}

PEPTIDES = [
    # seq, vina_best, vina_mean, pas, contacts, gravy, z, hbonds
    ("FLLHTTR", -9.60, -8.77, "PAS", "Asp74, Tyr72, His287", 0.19, 1.04, 8),
    ("YLSLLQR", -9.49, -9.44, "PAS", "Tyr72, Thr75, Glu202", 0.04, 0.99, 7),
    ("ALLLHRC", -9.29, -9.18, "催化位点", "Ser125, Ser203, Tyr124", 1.14, 0.92, 3),
    ("FCLHLQLR", -9.27, -8.96, "PAS", "Ser203, Thr75, Tyr341", 0.69, 0.92, 7),
    ("YHHLLCRR", -9.03, -8.62, "否", "Trp86, Ser203", -0.95, 1.96, 7),
    ("LLHLPKRTT", -9.01, -8.89, "旁侧", "Ser203, Val340", -0.36, 2.04, 3),
    ("LLHPLRL", -8.94, -8.91, "PAS", "Trp286, Tyr341, His447", 0.84, 1.04, 10),
    ("WLLVHLKK", -8.94, -8.64, "否", "Asn283, Gln279", 0.46, 2.04, 4),
    ("LLHPLRC", -8.91, -8.78, "否", "Ser125, Ser293", 0.66, 0.92, 4),
    ("HLLTLKKHV", -8.88, -8.69, "PAS", "Tyr72, Phe346", 0.08, 2.08, 6),
    ("HLPLLHRCC", -8.35, -8.28, "否", "Ser125, Tyr124, Tyr337", 0.43, 0.85, 4),
    ("HVLLLRQCA", -8.25, -8.07, "PAS", "Thr75", 0.97, 0.92, 4),
]


def a3v_mean(seq: str) -> float:
    return sum(A3V[a] for a in seq) / len(seq)


def hexamers(seq: str) -> list[str]:
    if len(seq) < 6:
        return [seq]
    return [seq[i : i + 6] for i in range(len(seq) - 5)]


def set_run_font(run, name_cn="宋体", name_en="Times New Roman", size=12, bold=False):
    run.bold = bold
    run.font.size = Pt(size)
    run.font.name = name_en
    run.font.color.rgb = RGBColor(0, 0, 0)
    r = run._element.get_or_add_rPr()
    rFonts = r.find(qn("w:rFonts"))
    if rFonts is None:
        from docx.oxml import OxmlElement

        rFonts = OxmlElement("w:rFonts")
        r.append(rFonts)
    rFonts.set(qn("w:ascii"), name_en)
    rFonts.set(qn("w:hAnsi"), name_en)
    rFonts.set(qn("w:eastAsia"), name_cn)


def add_p(doc, text, *, size=12, bold=False, first_line=True, space_after=8, align="left"):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(0)
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    if first_line:
        pf.first_line_indent = Cm(0.74)
    if align == "center":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pf.first_line_indent = Cm(0)
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return p


def add_h(doc, text, size=14):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    run = p.add_run(text)
    set_run_font(run, size=size, bold=True)
    return p


def add_table(doc, header, rows):
    tbl = doc.add_table(rows=1 + len(rows), cols=len(header))
    tbl.style = "Table Grid"
    for j, h in enumerate(header):
        cell = tbl.rows[0].cells[j]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_run_font(run, size=10, bold=True)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = tbl.rows[i + 1].cells[j]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            set_run_font(run, size=10, bold=False)
    doc.add_paragraph()


def build_docx() -> Path:
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Cm(2.54)
    sec.bottom_margin = Cm(2.54)
    sec.left_margin = Cm(2.54)
    sec.right_margin = Cm(2.54)

    add_p(
        doc,
        "从 12 条对接肽筛选 2–3 条用于 Aβ 聚集与 PC12 神经毒性实验",
        size=16,
        bold=True,
        first_line=False,
        align="center",
        space_after=4,
    )
    add_p(
        doc,
        "计算模型检索、对接结果复核与湿实验方案（独立备忘，不写入 SCI 主文）",
        size=12,
        bold=False,
        first_line=False,
        align="center",
        space_after=16,
    )

    add_h(doc, "一、任务与边界")
    add_p(
        doc,
        "导师要求在对接得到的 12 条肽上继续往下筛，选出 2–3 条做湿实验，重点是促进 Aβ 聚集，以及 PC12 细胞神经毒性。"
        "可以结合已有对接和分子动力学，但须先检索有没有现成的预测模型。"
        "本文只做候选指定和实验设计，不改 SCI 主文，也不把计算预测写成已经证实的致病性。",
    )

    add_h(doc, "二、预测模型检索结论")
    add_p(
        doc,
        "先检索“促进 Aβ 聚集”的序列预测模型。目前没有针对“外源短肽是否加速 Aβ40/Aβ42 成纤”训练的专用分类或回归模型。"
        "公开工具分三类，和本任务的对应关系必须分开写。",
    )
    add_p(
        doc,
        "第一类预测肽自身是否形成淀粉样（自聚集），不是预测它是否促进 Aβ。"
        "这一类包括 TANGO、WALTZ、AGGRESCAN、AMYLPRED2、AggBERT（六肽）、PALM、CANYA。"
        "CANYA（Lehner 实验室，Science Advances 2025）在十万级随机肽成核数据上训练，可对短肽给出成核分数，输入上限约 20 aa，适合给 7–9 aa 打自聚集分。"
        "AggBERT 只覆盖六肽。PALM 用 ESM-2 嵌入预测聚集倾向。它们回答的是“这条肽自己会不会成纤”，不能代替 Aβ±肽的 ThT 实验。",
    )
    add_p(
        doc,
        "第二类预测小分子抑制 Aβ 聚集，例如 Amylo-IC50Pred（ACS Chem Neurosci 2025）。训练对象是化合物描述符，不能用于 7–9 aa 肽。",
    )
    add_p(
        doc,
        "第三类是机制替代，而不是序列模型：AChE 经 PAS 加速 Aβ 成纤（Inestrosa 1996 等）。"
        "若短肽占据 PAS，可提出“AChE 介导的促聚集”假说。这正是本研究对接/MD 已经提供的证据类型。"
        "要区分两种实验结局：肽单独加速 Aβ（自种子或共聚集），以及肽+AChE 才加速 Aβ（PAS 伴侣假说）。现有序列模型都做不到这一区分。",
    )
    add_p(
        doc,
        "再检索“PC12 神经毒性肽”预测模型。没有以 PC12 存活率、LDH 或突起长度为标签、专门预测短肽 PC12 毒性的模型。"
        "PC12 是实验读出，不是算法。"
        "序列层面最接近的是 NTxPred2（Rathore 等，Protein Science 2025）：肽/蛋白分模型，肽集 877+877，ESM-2 肽模型独立集 AUC 约 0.98，网页与单机版可用。"
        "主文筛选已经用 NTxPred2 把目录支持名单收到神经毒性阳性，12 条全部来自该阳性集。"
        "ToxinPred/ToxinPred2 预测一般毒性，不是神经元或 PC12 特异。"
        "因此：神经毒性的计算依据用已有 NTxPred2；PC12 必须实测。",
    )

    add_h(doc, "三、12 条肽的对接与已有标签")
    add_p(
        doc,
        "12 条均为 7–9 残基、pH 7.4 净正电、NTxPred2 阳性、目录支持。"
        "对接为人源 AChE（PDB 4EY6）本地三次 AutoDock Vina；MD 只做了最优单次构象中的三条。"
        "表 1 按最优单次亲和力排序。PAS 列为对接最优构象是否接触 PAS 残基，不是实验占据。",
    )

    header = ["肽", "aa", "Vina最优", "三次均值", "PAS", "主要接触", "GRAVY", "a3v均值"]
    rows = []
    ranked = sorted(PEPTIDES, key=lambda x: x[1])
    for seq, best, mean, pas, contacts, gravy, z, hb in ranked:
        rows.append(
            [
                seq,
                str(len(seq)),
                f"{best:.2f}",
                f"{mean:.2f}",
                pas,
                contacts,
                f"{gravy:.2f}",
                f"{a3v_mean(seq):.2f}",
            ]
        )
    add_table(doc, header, rows)
    add_p(
        doc,
        "表 1. 12 条对接肽。Vina 单位 kcal/mol，分数只用于同一流程内排序，不是 Kd。"
        "a3v 均值为 AGGRESCAN 氨基酸聚集标度的简单平均，仅作自聚集相对排序，不是 Aβ 促聚集分数。",
        first_line=False,
        size=10,
        space_after=12,
    )

    add_h(doc, "四、从 12 条收到 3 条的规则")
    add_p(
        doc,
        "因为没有促 Aβ 专用模型，筛选规则用对接几何 + MD 维持 + 已有 NTxPred2，而不是再训练一个模型。",
    )
    add_p(
        doc,
        "规则 1：优先 PAS 接触构象。致病级联假说的第四步是 PAS 上的病理性伴侣，催化位点高分者不能代替 PAS。"
        "规则 2：在 PAS 组内取对接最强且 MD 已做的肽，避免 12 条全部进细胞。"
        "规则 3：另取一条强对接、非外侧 PAS 的催化位点肽作机制对照，用来看促聚集或 PC12 毒性是否依赖 PAS。"
        "规则 4：NTxPred2 在 12 条上没有区分度（全阳性），不能再用来减条数。"
        "规则 5：自聚集 a3v 只作文中注释，不作为入选或淘汰标准，以免把“肽自己成纤”和“促进 Aβ”混为一谈。",
    )
    add_p(
        doc,
        "按上述规则入选三条。FLLHTTR：最优单次 −9.60，PAS 接触 Asp74/Tyr72/His287，氢键最多之一，100 ns 内氢键网维持。"
        "YLSLLQR：三次均值最好（−9.44±0.09），PAS 接触 Tyr72/Thr75，MD 更紧凑、SASA 下降。"
        "ALLLHRC：最优单次第三（−9.29），接触催化 Ser203，不接触外侧 PAS 芳香残基，MD 不维持 PAS 型网络，作为机制对照。"
        "若经费只允许两条，做 FLLHTTR 与 YLSLLQR，对照用 Aβ±AChE 无肽。",
    )

    add_h(doc, "五、推荐湿实验（2–3 条）")
    add_p(
        doc,
        "核心读出两块：Aβ 聚集动力学，PC12 毒性。两条肽加一条对照即可回答导师的问题。"
        "合成：C 端酰胺化、HPLC ≥95%、TFA 置换为醋酸盐、质谱确认。工作液现配，避免反复冻融。",
    )
    add_p(
        doc,
        "实验 A（必须）。Aβ42（或 Aβ40）ThT 成纤动力学，37 °C。"
        "组：Aβ 单独；Aβ+肽（1:1、1:5、1:10，摩尔比预实验）；AChE+Aβ（阳性，文献 PAS 伴侣）；AChE+Aβ+肽；肽单独（自聚集对照）；溶剂对照。"
        "读出：ThT 滞后时间、表观速率、终末荧光。若肽单独 ThT 升高，先解释为自聚集，不能写成促 Aβ。"
        "只有 AChE+Aβ+肽相对 AChE+Aβ 进一步加快，才支持 PAS 伴侣假说；若无 AChE 时肽也加快 Aβ，则是 AChE 非依赖的共聚集或成核。"
        "可选 TEM/AFM 看纤丝形态。",
    )
    add_p(
        doc,
        "实验 B（必须）。PC12 细胞。"
        "未分化或 NGF 分化均可，文中固定一种并写清铺板和血清。"
        "组：肽剂量反应（1–50 μM，24/48 h）；Aβ42 寡聚体或纤丝毒性模型；Aβ+肽；Aβ+AChE±肽（若 A 中看到 AChE 依赖）。"
        "读出：CCK-8 或 MTT 存活，LDH 膜损伤。分化细胞可加突起长度。"
        "NTxPred2 预测的是肽自身神经毒性，故必须有“肽单独”组；Aβ 共孵育才对应“加重 Aβ 神经毒性”。",
    )
    add_p(
        doc,
        "实验 C（建议，一条酶活即可）。Ellman 法测肽对 AChE 水解的影响。"
        "PAS 肽若明显抑制催化，第三步“乙酰胆碱进入受限”才有湿数据；若不抑制，则毒性更可能走伴侣面而不是胆碱能阻断。",
    )

    add_h(doc, "六、不建议做的事")
    add_p(
        doc,
        "不要把 AGGRESCAN/CANYA/AggBERT 的高分写成“预测促进 Aβ 聚集”。"
        "不要把 NTxPred2 阳性写成“已在 PC12 证实神经毒性”。"
        "不要只做对接最好的一条而不做对照：没有 ALLLHRC 或无肽+AChE 对照，PAS 机制无法从一般结合里分开。"
        "不要把这三条的实验方案写进 SCI 主文讨论当已完成工作。",
    )

    add_h(doc, "七、一句话结论")
    add_p(
        doc,
        "没有促进 Aβ 聚集的专用预测模型，也没有 PC12 专用毒性模型。"
        "可用的是：NTxPred2（神经毒性序列，12 条已全阳性）、自聚集预测（与本任务不同）、以及本研究的 AChE-PAS 对接/MD。"
        "湿实验候选指定为 FLLHTTR、YLSLLQR（PAS），ALLLHRC（催化位点对照）。",
    )

    path = OUT / "从12条肽筛选Aβ聚集与PC12实验.docx"
    doc.save(path)
    return path


def build_md() -> Path:
    lines = [
        "# 从 12 条对接肽筛选 2–3 条用于 Aβ 聚集与 PC12 神经毒性实验",
        "",
        "独立备忘，不写入 SCI 主文。",
        "",
        "## 模型检索",
        "",
        "- **没有**“外源短肽促进 Aβ 聚集”的专用序列模型。",
        "- 自聚集模型（TANGO / WALTZ / AGGRESCAN / AggBERT / PALM / CANYA）预测肽自己成纤，不能代替 Aβ±肽实验。",
        "- Amylo-IC50Pred 针对小分子抑制剂，不能用于肽。",
        "- AChE-PAS 对接/MD 是机制替代，不是序列模型。",
        "- **没有** PC12 专用肽毒性模型。NTxPred2 是肽神经毒性序列模型；12 条已全部为阳性。PC12 必须实测。",
        "",
        "## 入选三条",
        "",
        "| 肽 | 角色 | 依据 |",
        "|---|---|---|",
        "| FLLHTTR | PAS 主候选 | Vina 最优 −9.60；PAS Asp74/Tyr72/His287；MD 氢键网维持 |",
        "| YLSLLQR | PAS 主候选 | 三次均值 −9.44；PAS Tyr72/Thr75；MD 更紧凑 |",
        "| ALLLHRC | 催化位点对照 | Vina −9.29；Ser203；MD 不维持 PAS 网络 |",
        "",
        "只做两条时：FLLHTTR + YLSLLQR。",
        "",
        "## 必须实验",
        "",
        "1. Aβ42 ThT：Aβ；Aβ+肽；AChE+Aβ；AChE+Aβ+肽；肽单独。",
        "2. PC12 CCK-8/MTT + LDH：肽单独剂量反应；Aβ±肽；必要时 Aβ+AChE±肽。",
        "3. 建议：Ellman AChE 酶活。",
        "",
    ]
    path = OUT / "README.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    p1 = build_docx()
    p2 = build_md()
    print("wrote", p1, p1.stat().st_size)
    print("wrote", p2, p2.stat().st_size)


if __name__ == "__main__":
    main()
