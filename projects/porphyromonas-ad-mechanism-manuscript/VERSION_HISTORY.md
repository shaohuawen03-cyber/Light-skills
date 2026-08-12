# Manuscript version history / 稿件版本记录

> Purpose: maintain one authoritative index of every material manuscript revision, its Git checkpoint, evidence status, deliverables, and recovery method.  
> 用途：以单一权威文件记录每次实质性稿件版本、Git检查点、证据状态、交付物和恢复方法。

## 1. Versioning convention / 版本规则

Tag pattern / 标签格式：

```text
porphyromonas-ad-manuscript-vMAJOR.MINOR.PATCH
```

- **MAJOR / 主版本：** evidence architecture, research question, or manuscript structure changes materially. / 证据架构、研究问题或全文结构发生实质改变。
- **MINOR / 次版本：** new analyses, figures, references, submission documents, or evidence-controlled external integration. / 新增分析、图件、文献、投稿材料或受控外部整合。
- **PATCH / 修订版本：** wording, translation, formatting, metadata, or non-substantive corrections. / 措辞、翻译、格式、元数据或非实质性修正。

Rules / 规则：

1. Update this file before creating a release tag. / 创建标签前先更新本文件。
2. Use annotated tags and push them explicitly. / 使用带说明的annotated tag并显式推送。
3. Never move, overwrite, or reuse an existing release tag. / 不移动、不覆盖、不复用既有版本标签。
4. A tag freezes a recoverable project snapshot; later edits require a new version. / 标签冻结可恢复快照，后续修改必须使用新版本。
5. Manuscript version numbers are independent of the external repository’s “v0.4” label. / 本稿版本号与外部仓库“v0.4”标签相互独立。

## 2. Version ledger / 版本台账

| Manuscript version | Date | Git checkpoint | Release tag | Status | Main content |
| --- | --- | --- | --- | --- | --- |
| **v0.1.0 — source intake** | 2026-08-12 | `f6a020a5c98b243b13963a8de83cd859f52e132d` | Untagged historical checkpoint | Superseded | Initial project materials entered Git management. / 初始研究材料纳入Git管理。 |
| **v0.2.0 — source parsing** | 2026-08-12 | `956210917503cfd2f521c80feeb4eb9aecbf8028` | Untagged historical checkpoint | Superseded | Principal documents parsed and source provenance registered. / 解析主要文档并登记来源。 |
| **v1.0.0 — first bilingual draft** | 2026-08-12 | `1fd8ab3bdf616fd1ab7b0e70d7c71046fb43da58` | Untagged historical checkpoint | Superseded | First English–Chinese SCI draft and initial quality review. / 首版中英文SCI稿与质量检查。 |
| **v2.0.0 — nine-stage aggregate rebuild** | 2026-08-12 | `a31d29466dc8d376d6012abd916152eb82e017f1` | Untagged historical checkpoint | Superseded | Nine-stage reconstruction, 25-reference corpus, aggregate-only evidence boundary, figures, DOCX and submission package. / 九阶段重建、25条文献、汇总证据边界、图件、DOCX及投稿包。 |
| **v3.0.0 — external-v0.4 evidence integration** | 2026-08-12 | Manuscript content commit `2a7573604b6e12bd1d51b897d52c58f0d9ead077`; synchronized history merge `78400a45d65239af0064b24503434413696cd54f`; the annotated tag resolves the final release-management snapshot | `porphyromonas-ad-manuscript-v3.0.0` | **Current tagged release** | Expanded 53-reference parallel manuscript; twelve externally reported sequences; independently recomputed composition; source-reported AChE docking summary; three figures; six supplementary tables; revision-v3 workflow, provenance controls and deterministic audits. / 扩展至53条文献；整合12条外部报告序列、组成审计、来源报告AChE对接汇总、三幅主图、六个补充表、revision-v3工作流及确定性审计。 |

## 3. Scientific status of current release / 当前版本科学状态

**v3.0.0 supports / 可支持：**

- principal-source aggregate funnel and recomputed descriptive percentages;
- twelve externally reported 7–9-aa sequence strings and independently recomputed composition;
- externally reported Vina mean±SD ordering against human AChE PDB 4EY6;
- a provenance-aware, hypothesis-generating validation roadmap.

**v3.0.0 does not support / 不支持：**

- row-level linkage between the twelve strings and the principal screening funnel or stricter eight;
- independently reproduced docking, verified poses/contacts, affinity, free energy, or completed molecular dynamics;
- measured expression, BBB transport, toxicity, metal chemistry, AChE/Aβ function, disease specificity, or AD causality.

## 4. Create and push the current tag / 创建并推送本次标签

The repository includes a guarded cross-platform helper: / 仓库提供带保护检查的跨平台脚本：

```bash
python3 scripts/manage_version_tag.py create \
  --version 3.0.0 \
  --message "v3.0.0: expanded bilingual manuscript with provenance-controlled external-v0.4 integration" \
  --push
```

Equivalent native Git commands / 等价Git命令：

```bash
git status --short
git tag -a porphyromonas-ad-manuscript-v3.0.0 \
  -m "v3.0.0: expanded bilingual manuscript with provenance-controlled external-v0.4 integration"
git push origin refs/tags/porphyromonas-ad-manuscript-v3.0.0
```

The helper refuses to tag a dirty working tree, the wrong branch, or an existing tag. / 脚本会拒绝脏工作区、错误分支或重复标签。

## 5. Verify a tag / 核验标签

```bash
python3 scripts/manage_version_tag.py verify --version 3.0.0
git show --no-patch --decorate porphyromonas-ad-manuscript-v3.0.0
git rev-list -n 1 porphyromonas-ad-manuscript-v3.0.0
```

## 6. Safe recovery / 安全恢复

### 6.1 Inspect the tagged release without changing the active checkout

Recommended: create a separate worktree. / 推荐创建独立worktree，不改变当前工作目录：

```powershell
Set-Location 'E:\0writing\Light-skills'
git fetch origin --tags
git worktree add 'E:\0writing\Light-skills-restore-v3.0.0' porphyromonas-ad-manuscript-v3.0.0
```

Remove it after inspection / 检查后移除：

```powershell
git worktree remove 'E:\0writing\Light-skills-restore-v3.0.0'
```

### 6.2 Restore one file from the tag

```bash
git restore --source=porphyromonas-ad-manuscript-v3.0.0 -- \
  projects/porphyromonas-ad-mechanism-manuscript/manuscript/manuscript_bilingual.docx
```

Review the diff before committing the restored file. / 提交恢复文件前先检查差异。

### 6.3 Compare the current branch with v3.0.0

```bash
git fetch origin --tags
git diff --stat porphyromonas-ad-manuscript-v3.0.0..arena/019ff377-light-skills
git diff porphyromonas-ad-manuscript-v3.0.0..arena/019ff377-light-skills -- \
  projects/porphyromonas-ad-mechanism-manuscript/
```

### 6.4 Recover an older untagged historical version

Use a separate worktree with the exact checkpoint, for example v2.0.0: / 使用精确提交在独立worktree中恢复，例如v2.0.0：

```powershell
git worktree add 'E:\0writing\Light-skills-restore-v2.0.0' a31d29466dc8d376d6012abd916152eb82e017f1
```

Do not use `git reset --hard` for routine recovery; it can discard uncommitted work. / 常规恢复不要使用`git reset --hard`，以免丢失未提交内容。

## 7. Template for the next version / 下一版本记录模板

Copy one row into the ledger and complete: / 在台账中复制一行并补齐：

```text
Version:
Date:
Scientific change:
Evidence added or removed:
Files changed:
Audits and verdicts:
Known limitations:
Content commit:
Release tag:
Push verification:
```
