# lyplunwen · LYP 论文 0→1

一个面向中文学术研究的 Codex skill：从选题和材料盘点开始，推进研究设计、真实证据整理、论文写作、实质审稿、语言清理与 Word/PDF 交付。

它以证据和研究主线组织写作，保留原稿与阶段版本；真实研究结果尚未产生时，先完成执行计划，不编造结果。

## 从 GitHub 安装

本仓库的技能目录为 `skills/lyplunwen`。

在 Codex 中发送：

```text
使用 $skill-installer 安装这个 GitHub skill：
https://github.com/li5109881719-bot/lyplunwen/tree/main/skills/lyplunwen
安装后检查 SKILL.md、agents、references 和 scripts 是否齐全，并列出缺失的配套模块。
```

仓库公开，接收者可通过上面的链接获取主技能。

技能未出现在列表中时，重启 Codex 后再查看。

## 手动安装

从 GitHub 下载仓库 ZIP 并解压，将 `skills/lyplunwen` 整个文件夹放入个人技能目录。当前官方文档列出的目录是 `~/.agents/skills/`；最终应存在：

```text
~/.agents/skills/lyplunwen/SKILL.md
```

也可安装到论文项目内的 `.agents/skills/lyplunwen/`。不同版本客户端的实际目录可让 Codex 检查确认；已安装同名技能时先保留备份，避免重复安装。

## 使用

新建论文项目时，告诉 Codex 项目文件夹位置并发送：

```text
使用 $lyplunwen 启动这个论文项目，先盘点材料，不要直接写全文。
```

继续已有项目时：

```text
使用 $lyplunwen 继续当前论文项目，读取 paper_output，判断已完成阶段和下一步。
```

主流程：材料盘点 → 问题与可行性 → 文献与缺口 → 确认研究主线 → 研究设计 → 执行真实研究 → 证据和引用 → 论文蓝图 → 初稿 → 实质审稿返修 → 语言清理 → 文档交付。

项目产物在使用者自己的论文目录内保存，不写入技能安装目录。

## 配套模块

仓库包含 `lyplunwen` 主技能及其自身脚本、参考规则和界面元数据。Research Architect、Nature 系列、ARS、语言清理、文档生成等配套模块需要按需另行安装或启用，详见 [配套模块说明](docs/DEPENDENCIES.md)。

缺少配套技能时，主技能允许在安全可行的范围内直接完成相应任务，并记录替代处理；这不等于配套模块已经安装，也不保证所有能力都能由当前环境替代。

内置的 `project_state.py` 使用 Python 3 标准库，运行环境须支持 `pathlib.Path.is_relative_to`（Python 3.9 起提供）。文档生成、渲染和外部服务可能需要另外的运行环境或服务连接。

## 仓库结构

```text
skills/lyplunwen/
├── SKILL.md
├── agents/openai.yaml
├── scripts/project_state.py
└── references/
    ├── artifacts-and-gates.md
    ├── historical-evidence.md
    ├── integrated-routing.md
    ├── state-and-versions.md
    └── venue-and-delivery.md
docs/DEPENDENCIES.md
SHA256SUMS.txt
```

本仓库中的 8 个技能源文件来自 2026-10-17 的已安装版本，按原样复制；`SHA256SUMS.txt` 记录这些文件的校验值。本次整理没有在接收者环境中执行完整论文流程。

## 官方参考

- [创建技能、安装目录及 GitHub 安装方式](https://learn.chatgpt.com/docs/build-skills)

长期分发也可另行封装为插件；本仓库采用独立 skill 形式。
