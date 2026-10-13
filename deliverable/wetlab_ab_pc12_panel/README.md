# 从 12 条对接肽筛选 2–3 条用于 Aβ 聚集与 PC12 神经毒性实验

独立备忘，不写入 SCI 主文。

## 模型检索

- **没有**“外源短肽促进 Aβ 聚集”的专用序列模型。
- 自聚集模型（TANGO / WALTZ / AGGRESCAN / AggBERT / PALM / CANYA）预测肽自己成纤，不能代替 Aβ±肽实验。
- Amylo-IC50Pred 针对小分子抑制剂，不能用于肽。
- AChE-PAS 对接/MD 是机制替代，不是序列模型。
- **没有** PC12 专用肽毒性模型。NTxPred2 是肽神经毒性序列模型；12 条已全部为阳性。PC12 必须实测。

## 入选三条

| 肽 | 角色 | 依据 |
|---|---|---|
| FLLHTTR | PAS 主候选 | Vina 最优 −9.60；PAS Asp74/Tyr72/His287；MD 氢键网维持 |
| YLSLLQR | PAS 主候选 | 三次均值 −9.44；PAS Tyr72/Thr75；MD 更紧凑 |
| ALLLHRC | 催化位点对照 | Vina −9.29；Ser203；MD 不维持 PAS 网络 |

只做两条时：FLLHTTR + YLSLLQR。

## 必须实验

1. Aβ42 ThT：Aβ；Aβ+肽；AChE+Aβ；AChE+Aβ+肽；肽单独。
2. PC12 CCK-8/MTT + LDH：肽单独剂量反应；Aβ±肽；必要时 Aβ+AChE±肽。
3. 建议：Ellman AChE 酶活。
