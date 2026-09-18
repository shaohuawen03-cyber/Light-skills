# Windows 本机打通安装指南（E:\0github\ 安全克隆版）

> 目标：安装 https://github.com/shaohuawen03-cyber/BrowserSkill/tree/arena/01a0b237-browserskill 的 skills，与本机打通，且克隆目录放在 `E:\0github\`，不覆盖已有目录。

## 一、已完成的工作（本仓库分支 arena/01a0b489-light-skills）

本分支已合并 BrowserSkill 的两个核心 skill：

- `skills/git-sync` (v2.9.2) — 沙箱↔本机双向桥，值守循环、静默推送、产物回传
- `skills/arena-local-bridge` (v2.0) — arena 会话编排 + bsk 浏览器桥 + 11 条实测铁律

同时保留 Light-skills 原有的 23 个 `light-*` 科研技能，总数 25。

根目录已放置 git-sync 的用户侧脚本（`sync.ps1`, `push.ps1`, `watch.ps1`, `bootstrap.ps1`, `auth.ps1`, `doctor.ps1`, `where.cmd` 等），可在任意克隆中直接使用。

新增安全安装器：

- `scripts/install_browser_bridge.ps1` — 安全克隆到 `E:\0github\`，永不覆盖
- `setup_windows.ps1` — 一键入口，调用上者

## 二、Windows 用户一键安装（推荐）

### 前置：Git + Python

```powershell
winget install --id Git.Git -e
winget install --id Python.Python.3.11 -e
# 重开 PowerShell
git --version
python --version
$env:PYTHONUTF8="1"
```

### 步骤 1：安全克隆（不覆盖已有目录）

```powershell
# 方式 A：如果你已经克隆了本仓库到 E:\0github\Light-skills
cd E:\0github\Light-skills
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\install_browser_bridge.ps1 -BaseDir E:\0github\

# 方式 B：全新机器，只有一条命令（会自动创建 E:\0github\）
# 先手动建 E:\0github 并在其中执行：
mkdir E:\0github -Force
cd E:\0github
git clone -b arena/01a0b489-light-skills https://github.com/shaohuawen03-cyber/Light-skills.git
cd Light-skills
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\install_browser_bridge.ps1 -BaseDir E:\0github\ -AutoBootstrap
```

`install_browser_bridge.ps1` 的安全策略：

- 检查 `E:\0github\` 是否存在，不存在则创建
- 对每个目标目录 `E:\0github\Light-skills` 和 `E:\0github\BrowserSkill-01a0b237`：
  - 若已存在 → `[SKIP] 已存在，不覆盖`，仅 `git fetch` 更新远端信息，不改工作区
  - 若不存在 → `git clone --depth 1 -b <分支> <URL> <目录>`

### 步骤 2：启用本机桥（git-sync）

每个仓库独立值守，**默认零后台**，用谁才注册谁。

```powershell
cd E:\0github\BrowserSkill-01a0b237
.\bootstrap.ps1 -Auto          # 首次：执行策略 + git 身份 + 拉分支 + 静默推送 + 注册值守
.\doctor.ps1                   # 体检
.\watch.ps1 -Status            # 看心跳
.\auth.ps1 -Verify             # 验证静默推送

# 同理 Light-skills
cd E:\0github\Light-skills
.\bootstrap.ps1 -Auto
.\doctor.ps1
```

`bootstrap.ps1 -Auto` 会：

1. `Set-ExecutionPolicy RemoteSigned CurrentUser`
2. 设置 repo-local git user（若无）
3. `git fetch + checkout <分支> + pull --ff-only`
4. `auth.ps1 -Setup` 使推送不再弹窗
5. `watch.ps1 -Register` 注册计划任务 `git-sync-watch-<Repo>-<Branch>`，开始轮询

日常：

```powershell
.\sync.ps1                     # 拉沙箱推送
.\where.cmd -Want arena/01a0b237-browserskill  # 定位该用哪个文件夹（[USE] 标记）
.\download.ps1 -Set final      # 产物落地，打印来源仓库/分支/提交/目录
.\push.ps1 "msg"               # 本机提交+推送
.\watch.ps1 -Unregister        # 用完即注销，归零后台
```

多账号（v2.9.0+）：

```powershell
.\auth.ps1 -Accounts           # 列出本机所有 gh 登录 + 能否推本仓库
.\auth.ps1 -Account shaohuawen03-cyber  # 钉住本克隆到指定账号（只改本克隆）
.\auth.ps1 -Verify
```

### 步骤 3：浏览器桥（bsk，可选，若需 arena-local-bridge）

`arena-local-bridge` 技能需要 `bsk` CLI + 扩展来操控 Edge 活标签页。

```powershell
# 安装 bsk CLI
irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex
$env:PATH="$env:USERPROFILE\.local\bin;$env:PATH"
bsk --version

# 安装扩展
# Edge: https://microsoftedge.microsoft.com/addons/detail/browserskill/emacgiaaaiojkkpkddmmdfhmokgmnikg
# Chrome: https://chromewebstore.google.com/detail/hhcmgoofomhgciiibhipgmgkgnoenaoi

# 安装后关闭扩展的“借用标签页前确认”
# 打开扩展 popup → 确认已连接 → bsk doctor 应全绿（仅 extension connected 可能需手动确认）

bsk doctor
bsk install-skill --list --json   # 查看可用 harness
bsk install-skill --harness cursor --json   # 示例：装到 Cursor
```

验证：

```powershell
bsk session start --no-focus --json
# 记下 session id，打开 https://example.com 并截图
bsk session stop <id>
```

### 步骤 4：Light-skills Python 技能发现

```powershell
cd E:\0github\Light-skills
$env:PYTHONUTF8="1"
python scripts\bootstrap_agent_skills.py --targets agents claude opencode --mode auto --force
python scripts\bootstrap_agent_skills.py --check-only
```

会在项目内生成 `.agents/skills`, `.claude/skills`, `.opencode/skills` 的镜像，供 Codex / Claude Code / OpenCode 发现。

## 三、与沙箱联动流程

沙箱侧（Arena）：

```bash
# 修改任务钩子（ASCII！）
$EDITOR code/agent_task.ps1
bash skills/git-sync/scripts/agent-sync.sh "feat: add task"
bash skills/git-sync/scripts/agent-wait.sh --request "执行 agent_task.ps1 并回传判定" --timeout auto
# exit 0 passed / 2 failed / 3 timeout
```

本机侧值守会自动：

- `sync.ps1` 拉任务
- 执行 `code/local_check.ps1`（或 `agent_task.ps1`）
- 推回 `results/status/check_rN_*.txt` 判定 + 产物

沙箱再 `git fetch && git reset --mixed origin/<branch>` 拉回分析。

## 四、紧急停止（两层）

```powershell
# 停本会话的值守
schtasks /End /TN "git-sync-watch-BrowserSkill-01a0b237" 2>$null
schtasks /Delete /TN "git-sync-watch-BrowserSkill-01a0b237" /F 2>$null

# 全量清扫所有 git-sync 家族（15+ 弹窗时用）
Get-ScheduledTask -TaskName 'git-sync-watch-*' -ErrorAction SilentlyContinue |
  ForEach-Object { schtasks /End /TN $_.TaskName 2>$null; schtasks /Delete /TN $_.TaskName /F 2>$null }
Get-CimInstance Win32_Process -Filter "Name='powershell.exe' OR Name='pwsh.exe'" |
  Where-Object { $_.ProcessId -ne $PID -and $_.CommandLine -match 'watch\.ps1|agent_task|local_check|bootstrap|sync\.ps1|agent-handsfree|agent-sync|download\.ps1|upload\.ps1|git-sync' } |
  ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
& "$env:USERPROFILE\.local\bin\bsk.exe" session stop --all 2>$null
```

策略：默认零后台，用哪个会话才注册哪个，任务结束立即 `-Unregister`。

## 五、常见问题

| 症状 | 处置 |
|---|---|
| `where.cmd` 显示多个克隆，哪个可用 | 看 `[USE]` 标记；`where.cmd -Want <分支>` 精确过滤 |
| `auth.ps1 -Verify` 失败 403 | `auth.ps1 -Accounts` 看账号，`auth.ps1 -Account <owner>` 钉住仓库主账号 |
| `watch.ps1 -Status` 心跳过期 | `watch.ps1 -Unregister ; watch.ps1 -Register` 重启值守 |
| `bsk doctor` 报 extension 未连接 | Edge 扩展 popup 确认端口与 daemon 一致，关闭“借用确认”，30 分钟内激活过 arena 标签页 |
| `.ps1` 报中文乱码 | 本仓库 `.ps1` 强制 ASCII，中文只在 `.md/.json`，门禁 `code/check_all.sh` 会拦截 |
| 克隆时提示目录已存在 | 安全策略：永不覆盖，手动 `cd E:\0github\<dir> ; .\sync.ps1` 更新 |

## 六、目录结构（安装后 E:\0github\）

```
E:\0github\
├─ Light-skills\                 # 本仓库（25 skills，含 git-sync + arena-local-bridge）
│  ├─ skills\git-sync\           # 桥
│  ├─ skills\arena-local-bridge\ # 编排
│  ├─ skills\light-*\            # 科研技能 23 个
│  ├─ sync.ps1 / watch.ps1 / ... # 用户侧脚本
│  └─ scripts\install_browser_bridge.ps1
└─ BrowserSkill-01a0b237\         # 上游 BrowserSkill 分支（可选，用于对照最新版）
   ├─ skills\git-sync\
   └─ ...
```

安装器保证：若 `E:\0github\Light-skills` 已存在，不会删除或覆盖，直接跳过。
