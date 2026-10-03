# 04 · 社区开发文档

第三方开发者整理的 Vela / 小米手环开发经验文档。**内容原样保留，未做改写**；许可与出处见 [SOURCES.md](../SOURCES.md)。

官方文档告诉你「API 怎么调」，社区文档告诉你「哪些坑会让你白干一天」——两者互补。

---

## [xiaomi-band-dev-guide/](./xiaomi-band-dev-guide/) — 小米手环开发指南 · 避坑手册

> 作者 `KaiTeeDreamChai` · MIT · 专为小米手环（Vela OS / HyperOS）表盘与快应用打造的实战手册
> 上游：<https://github.com/KaiTeeDreamChai/xiaomi-band-dev-guide>

| 文档 | 主题 |
|---|---|
| [01. 平台架构与渲染引擎剖析](./xiaomi-band-dev-guide/docs/01-platform-and-engine.md) | Vela QuickApp 渲染引擎底层原理 |
| [02. 快应用工程搭建与核心 API](./xiaomi-band-dev-guide/docs/02-quickapp-development.md) | 工程结构、生命周期、核心 API 实践 |
| [03. 穿戴式 UI 与交互规范](./xiaomi-band-dev-guide/docs/03-ui-and-interaction.md) | 触控热区、AMOLED 节能、震动反馈 |
| [04. 核心避坑红线速查表](./xiaomi-band-dev-guide/docs/04-pitfalls-and-solutions.md) | Top 10 高频踩坑与解法 |
| [05. 蓝牙侧载与真机部署](./xiaomi-band-dev-guide/docs/05-sideload-and-deployment.md) | 签名体系、AstroBox、侧载流程 |
| [06. 表盘开发全景指南](./xiaomi-band-dev-guide/docs/06-watchface-development.md) | 小米手环 9 / 9 Pro 表盘制作 |

完整入口见其 [README](./xiaomi-band-dev-guide/README.md)。

---

## [vela-doc-guide/](./vela-doc-guide/) — Vela 手表应用开发文档合集

> 作者 `epheiamoe` · CC-BY-SA-4.0 · 整合官方 API 整理、UI 规范、实战教程与 AI 速查
> 上游：<https://github.com/epheiamoe/vela_doc_guide>

| 文档 | 用途 |
|---|---|
| [开发指南](./vela-doc-guide/vela-dev-guide.md) | 官方 API 整理、环境搭建、常见问题（入门 / 进阶） |
| [UI 开发指南](./vela-doc-guide/vela-ui-guide.md) | 通用 UI 设计规范、代码模板、素材 |
| [UI 快速参考](./vela-doc-guide/vela-ui-quickref.md) | 一页式速查表，经典 UI 模式 |
| [Vela vs Web](./vela-doc-guide/vela-vs-web.md) | 与 Web 开发的关键差异（破除「伪 Web 幻觉」） |
| [输入法组件](./vela-doc-guide/input-method-guide.md) | 第三方输入法组件集成 |
| [实战教程：电子书阅读器](./vela-doc-guide/ebook-app-tutorial.md) | 复杂项目完整实现分析 |
| [AI 速查](./vela-doc-guide/AI-QUICKREF.md) | 最小上下文快速入口 |

附带资源：

- `vela-doc-guide/test-app/` — 可直接运行的快应用示例工程（`manifest.json` + 两个页面 `.ux`）
- `vela-doc-guide/vela-dev/SKILL.md` — OpenCode / AI Agent 用的技能定义
- `vela-doc-guide/AGENTS.md.example` — Agent 协作配置模板

完整入口见其 [README](./vela-doc-guide/README.md)。

---

## 官方站点补抓（镜像缺失的 4 篇）

社区镜像 `FangAiden/Vela_Application_Documentation` 缺少 4 个官方页面，已用 `tools/fetch_official_supplement.py` 直接从官方站抓取，补进 `01-official-quickapp-js/` 对应位置：

| 补抓页面 | 落地路径 |
|---|---|
| 蓝牙 bluetooth | `01-official-quickapp-js/features/system/bluetooth.md` |
| 多屏适配 · 模拟器 | `01-official-quickapp-js/guide/multi-screens/simulator.md` |
| AI 自动化生成 | `01-official-quickapp-js/tools/dev/official-site-tutorial.md` |
| AIoT-toolkit 上手 | `01-official-quickapp-js/tools/toolkit/start.md` |

镜像共 143 篇，官方站侧栏可见 107 页；补抓后本地共 147 篇，两相交集无遗漏。
