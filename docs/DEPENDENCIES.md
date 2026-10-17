# 配套模块

`lyplunwen` 是总控入口，会在对应阶段按需调用其他技能。仅安装本仓库不会自动安装配套模块。

| 用途 | 模块 |
| --- | --- |
| 材料盘点、研究问题、文献、设计、证据、引用、初稿和审计 | research-architect-intake、research-architect-brainstorm、research-architect-literature、research-architect-design、research-architect-evidence、research-architect-citation、research-architect-draft、research-architect-audit |
| 选定论文精读与题录核验 | nature-reader、nature-paper-card、nature-ref-verifier；同时检查各模块所需的共享资源 |
| 引用支持核查与审稿返修 | ARS 的 citation-check、reviewer、revision-coach、revision、rebuttal-audit |
| 语言清理 | anti-defensive-writing、humanizer-zh（中文）、humanizer（英文） |
| Word/PDF 生成和版面核查 | documents、pdf，以及各自需要的生成、转换与渲染工具 |

以 `skills/lyplunwen/references/integrated-routing.md` 为详细路由依据。各模块按其可信来源分别安装；本仓库未复制这些模块的源代码，也未附带任何账号登录状态。

安装主技能后，可以先让 Codex 检查环境：

```text
检查 lyplunwen 的配套模块和工具环境。列出已具备、待安装和可直接替代的步骤，先不要启动论文项目。
```

需要联网文献、全文、外部数据或文档渲染时，实际可用能力取决于接收者的工具和服务权限。完整论文流程按真实材料及适用关卡推进。
