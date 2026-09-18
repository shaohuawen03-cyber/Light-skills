# 鲜味肽机器学习筛选自循环任务 - 本机执行指南

> 任务已推送到分支 `arena/01a0b489-light-skills`，提交 `d15453c`，包含：
> - `code/generate_umami_docx.py` - 生成毕业论文 docx
> - `code/agent_task.ps1` - 本机值守执行的任务钩子（ASCII-only）
> - `results/status/success_criteria.json` - 成功判据
> - `deliverable/机器学习筛选鲜味肽_毕业论文.docx` - 预生成示例

## 1. 修复 403 权限问题（必须）

你机器上有两个 gh 登录：

- `mqgg5630-cyber` (active, 机器默认)
- `shaohuawen03-cyber` (可推本仓库)

`Light-skills` 仓库 owner 是 `shaohuawen03-cyber`，所以 active 账号推会 403。按 v2.9.0 多账号策略，**只钉住本克隆**：

```powershell
cd E:\0github\Light-skills
.\auth.ps1 -Accounts
.\auth.ps1 -Account shaohuawen03-cyber
.\auth.ps1 -Verify
```

`Verify` 应显示 `push --dry-run : passed`。此操作只改本克隆的 local git config，不影响其他克隆的默认账号。

## 2. 重新注册值守（你之前 Unregister 了）

```powershell
cd E:\0github\Light-skills
.\watch.ps1 -Register
.\watch.ps1 -Status
```

若出现 `%1 不是有效的 Win32 应用程序`，是杀毒软件拦截了 `C:\ProgramData\git-sync\watchhost-*.exe`。两种方案：

- **方案 A（推荐，无需管理员）**：接受 `flash` 模式，每次登录闪一下黑窗，不影响功能。当前已是 flash 模式，`self-test PASSED` 即成功。
- **方案 B（零闪，管理员）**：
  ```powershell
  # 管理员 PowerShell
  .\watch.ps1 -Unregister
  .\watch.ps1 -Register -Headless
  ```
  需先 `.\auth.ps1 -GhLogin` 确保 gh token 在 session 0 可用。

心跳新鲜（<2 分钟）即正常。

## 3. 拉取最新任务并执行自循环

```powershell
cd E:\0github\Light-skills
.\sync.ps1
# 应看到 d15453c 提交
dir code\agent_task.ps1
dir code\generate_umami_docx.py

# 手动测试任务（不经过值守）
powershell -NoProfile -ExecutionPolicy Bypass -File code\agent_task.ps1

# 或等待值守自动执行（hands-free）
# 沙箱已推送任务，值守每 2 分钟轮询一次，检测到 handshake 后执行 local_check.ps1 -> agent_task.ps1
.\watch.ps1 -Status
# 看 heartbeat 的 last_action / last_run
```

`agent_task.ps1` 会：

1. 自动修复 auth pin
2. 列出 `conda env list` 和 `E:\0mcp-agv\agents\cnki_agent`
3. `pip install python-docx lark` 并运行 `code\generate_umami_docx.py`
4. 尝试调用 `E:\0mcp-agv\agents\cnki_agent\main.py --help`（若存在）
5. 验证 `deliverable\*.docx` 并写入 `results\status\success_criteria.json`

## 4. 检查产物并回传

```powershell
dir deliverable\
# 应有：
# 机器学习筛选鲜味肽_毕业论文.docx (41KB+)
# ML_Umami_Peptide_Screening_Thesis.docx

.\download.ps1 -Set final
# 产物会镜像到 E:\0github\Light-skills_out，并打印来源仓库/分支/提交

# 手动推送判定（若 auto_push 未开启）
.\push.ps1 "local: umami thesis generated"
```

沙箱侧会通过 `agent-wait.sh` 检测到 `passed` 并自动 `accept`。

## 5. Conda 环境与 CNKI Agent 对接

- **Lark**：`code\generate_umami_docx.py` 会尝试 `import lark`，若 base 没有，脚本会尝试 `conda run -n lark`。建议：
  ```powershell
  conda env list
  conda run -n lark python -c "import lark; print(lark.__version__)"
  conda run -n lark python -m pip install python-docx scikit-learn
  ```

- **毕业论文模板**：若你 conda 环境中有自定义模板生成器，请将其路径告诉 agent，或直接修改 `code\generate_umami_docx.py` 的 `Document()` 部分，对接你的模板。

- **CNKI Agent**：`E:\0mcp-agv\agents\cnki_agent` 若存在，`agent_task.ps1` 会列出其文件并尝试 `main.py --help`。你可以：
  ```powershell
  dir E:\0mcp-agv\agents\cnki_agent
  cat E:\0mcp-agv\agents\cnki_agent\README.md
  ```
  然后告知 agent 如何调用它生成 CNKI 格式，agent 可更新 `generate_umami_docx.py` 对接。

## 6. bsk 浏览器桥（可选）

你已安装 `bsk 0.3.0`，请运行：

```powershell
bsk doctor
bsk browsers
```

若 `doctor` 报 `extension connected` 失败，需在 Edge 中打开扩展 popup，确认端口与 daemon 一致，并关闭“借用标签页前确认”。`bsk doctor` 全绿后，`arena-local-bridge` 技能才能操控 arena.ai 会话。

## 7. 当前分支状态

- `where.cmd -Want arena/01a0b489-light-skills` 已显示 `[USE] E:\0github\Light-skills`，正确。
- `BrowserSkill-01a0b237` 未克隆是正常的，因为 `Install-Safe.ps1` 在你机器上无输出（可能被拦截）。如需对照，可手动：
  ```powershell
  cd E:\0github\
  git clone -b arena/01a0b237-browserskill https://github.com/shaohuawen03-cyber/BrowserSkill.git BrowserSkill-01a0b237
  ```

## 8. 紧急停止

```powershell
.\watch.ps1 -Unregister
# 或全量清扫
Get-ScheduledTask -TaskName 'git-sync-watch-*' -ErrorAction SilentlyContinue | ForEach-Object { schtasks /End /TN $_.TaskName 2>$null; schtasks /Delete /TN $_.TaskName /F 2>$null }
```

完成后请运行 `.\doctor.ps1` 和 `dir deliverable\` 并贴出结果，agent 将继续优化 docx 内容或对接你的 cnki_agent。
