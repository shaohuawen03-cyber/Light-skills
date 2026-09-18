# Windows 本机打通（E:\0github\ 安全版）

> 安装 https://github.com/shaohuawen03-cyber/BrowserSkill/tree/arena/01a0b237-browserskill 的 skills，与本机打通，克隆目录放 `E:\0github\`，不要覆盖已有目录。

## 一键安装

```powershell
# 方式 1：已在 E:\0github\Light-skills 中
cd E:\0github\Light-skills
powershell -NoProfile -ExecutionPolicy Bypass -File Install-Safe.ps1

# 方式 2：全新机器
mkdir E:\0github -Force
cd E:\0github
git clone -b arena/01a0b489-light-skills https://github.com/shaohuawen03-cyber/Light-skills.git
cd Light-skills
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\install_browser_bridge.ps1 -BaseDir E:\0github\ -AutoBootstrap
```

**安全策略**：

- `E:\0github\` 不存在则创建，存在则复用
- `E:\0github\Light-skills` 和 `E:\0github\BrowserSkill-01a0b237` 若已存在，显示 `[SKIP] 已存在，不覆盖`，仅 `git fetch`，不改工作区
- 克隆用 `--depth 1` 加速

## 启用本机桥

```powershell
cd E:\0github\Light-skills
.\bootstrap.ps1 -Auto
.\doctor.ps1
.\watch.ps1 -Status
.\auth.ps1 -Verify

# 用完注销，归零后台
.\watch.ps1 -Unregister
```

多账号：

```powershell
.\auth.ps1 -Accounts
.\auth.ps1 -Account shaohuawen03-cyber
```

日常：

```powershell
.\sync.ps1
.\where.cmd -Want arena/01a0b489-light-skills
.\download.ps1 -Set final
```

## 浏览器桥（可选）

```powershell
irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex
bsk --version
bsk doctor
```

扩展：Edge Add-ons / Chrome Web Store 搜 BrowserSkill，关闭“借用标签页前确认”。

## 文档

- 完整指南：`docs/windows_browser_bridge_setup.md`
- 技能总目录：`SKILLS.md`
- 科研技能：`README.md`
