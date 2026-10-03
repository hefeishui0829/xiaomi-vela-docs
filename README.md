# Xiaomi Vela 文档库（手环 / 手表 JS 快应用）

> 小米 Vela JS 快应用官方文档的**完整离线副本**，外加两份社区实战文档。
> **245 篇 · 正文 694 KB · 配图 207 张**
> 原始内容一律未做改写，仅按主题分类归置并补了导航索引。

官方在线文档：<https://iot.mi.com/vela/quickapp/zh/>

---

## 目录地图

| 目录 | 篇数 | 内容 | 什么时候看 |
|---|---:|---|---|
| **[01-official-quickapp-js/](./01-official-quickapp-js/)** | 148 | **官方 JS 快应用文档**（教程 / 组件 / JS 接口 / 工具 / 示例） | ★ 手环快应用开发的主文档，从这开始 |
| [02-official-lua/](./02-official-lua/) | 71 | 官方 Lua 应用文档 | 写 Lua 形态应用时 |
| [03-official-shell/](./03-official-shell/) | 9 | 官方 Shell 文档 | 调试 / 命令行环境时 |
| [04-community/](./04-community/) | 17 | 社区实战文档（手环避坑手册、UI 规范、示例工程） | 官方文档没讲清的坑在这 |
| [SOURCES.md](./SOURCES.md) | — | 来源、许可、抓取方式、免责声明 | 二次分发前必读 |
| [tools/](./tools/) | — | 补抓脚本与索引生成器 | 想重新生成时 |

---

## 手环开发推荐阅读顺序

第一次上手小米手环快应用，按这个顺序读最省时间：

1. `01-official-quickapp-js/guide/start/` — 环境搭建与第一个应用
   - [项目概览](./01-official-quickapp-js/guide/start/project-overview.md) → [使用 AIoT-IDE](./01-official-quickapp-js/guide/start/use-ide.md) → [添加交互](./01-official-quickapp-js/guide/start/add-interactivity.md)
2. `01-official-quickapp-js/guide/multi-screens/` — **手环屏幕适配是头号坑**
   - [设备规格表](./01-official-quickapp-js/guide/multi-screens/specs.md)（手环 9 = 192×490，手环 10 = 212×520，手环 8/9 Pro = 336×480）
3. `01-official-quickapp-js/guide/framework/` — UX 文件结构、模板语法、样式、生命周期
4. `01-official-quickapp-js/components/` + `features/` — 写功能时按需查
5. `04-community/xiaomi-band-dev-guide/docs/` — **上线前读一遍避坑清单**
   - [04. 核心避坑红线速查表](./04-community/xiaomi-band-dev-guide/docs/04-pitfalls-and-solutions.md)
   - [05. 蓝牙侧载与真机部署](./04-community/xiaomi-band-dev-guide/docs/05-sideload-and-deployment.md)

---

## 各分区速览（01-official-quickapp-js）

| 分区 | 篇数 | 说明 |
|---|---:|---|
| [guide/](./01-official-quickapp-js/guide/) | 42 | 入门、框架机制、UX 语法、样式、多屏适配、多语言、后台运行、最佳实践、发布验收、API Level 变更 |
| [components/](./01-official-quickapp-js/components/) | 27 | text / image / list / div / swiper / input / picker / slider / switch / chart / qrcode 等 |
| [features/](./01-official-quickapp-js/features/) | 25 | router / storage / file / fetch / request / sensor / vibrator / battery / **bluetooth** / geolocation / crypto 等 |
| [tools/](./01-official-quickapp-js/tools/) | 24 | AIoT-IDE、调试器、内存分析、模拟器、项目模板、打包发布 |
| [samples/](./01-official-quickapp-js/samples/) | 1 | 官方编程示例索引 |
| [images/](./01-official-quickapp-js/images/) | — | 207 张配图（101 MB） |

完整篇目列表见 [01-official-quickapp-js/README.md](./01-official-quickapp-js/README.md)。

---

## 与其他文档的关系

- 官方文档讲「API 怎么用」，社区文档讲「哪些坑会白干一天」——两者都收了，建议配合看
- 本库只做归档与分类，不保证与官方站实时同步；抓取时间见 [SOURCES.md](./SOURCES.md)

## 许可

**官方文档版权归小米所有**，此处仅为离线查阅与归档副本。社区文档各自遵循其上游许可（MIT / CC-BY-SA-4.0）。二次分发前请务必阅读 [SOURCES.md](./SOURCES.md)。
