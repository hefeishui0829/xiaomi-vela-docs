# Vela 手表应用开发文档指南

> 整合小米官方文档、第三方组件、实战项目，助力开发者快速上手 Vela 应用开发
> 
> 适用设备：小米手环 8Pro/9Pro、REDMI Watch 5/6 等 Vela OS 手表设备

---

## 项目简介

本项目为 **Vela 手表应用开发文档合集**，旨在为开发者提供：

- **官方文档整理** - 小米 Vela JS API 文档的 Markdown 版本
- **组件使用指南** - 第三方输入法等组件的集成文档
- **UI 设计规范** - 从实际项目提取的通用 UI 开发指南
- **实战教程** - 复杂应用的完整实现分析

---

## 快速导航

| 文档 | 说明 | 目标 |
|------|------|------|
| [开发指南](./vela-dev-guide.md) | 官方API整理、环境搭建、常见问题 | 入门/进阶 |
| [UI开发指南](./vela-ui-guide.md) | 通用UI设计规范、代码模板、素材 | 全阶段 |
| [UI快速参考](./vela-ui-quickref.md) | 一页式速查表，经典UI模式 | 快速开发 |
| [输入法组件](./input-method-guide.md) | 第三方输入法组件使用 | 需要输入功能 |
| [实战教程](./ebook-app-tutorial.md) | 复杂项目完整分析 | 进阶学习 |
| [AI速查](./AI-QUICKREF.md) | 最小上下文快速入口 | AI/人类 |

---

## OpenCode 集成

本项目提供 **OpenCode 自定义工具**，可在任何目录的 OpenCode 中直接调用。

### 全局安装（推荐）

```bash
# 工具已安装到 ~/.config/opencode/tools/vela.ts
# OpenCode 重启后自动加载
```

### 工具列表

| 工具 | 功能 | 示例 |
|------|------|------|
| `velaApi` | 查询 API 参考 | router, storage, file, sensor, device |
| `velaTemplate` | 获取项目模板 | page, settings, list, cover, manifest |
| `velaUi` | 查询 UI 规范 | colors, fonts, spacing, listitem, switch, cover, multi, reader |
| `velaQuickRef` | 快速参考 | diff, lifecycle, devices, tips, patterns |

### 使用示例

```
用户: "查询 storage API"
AI调用: velaApi({ api: "storage" })

用户: "给我一个 settings 模板"
AI调用: velaTemplate({ type: "settings" })

用户: "查询 listitem"
AI调用: velaUi({ item: "listitem" })

用户: "查询 patterns"
AI调用: velaQuickRef({ topic: "patterns" })
```

---

## 技术概览

| 维度 | 说明 |
|------|------|
| **开发语言** | JavaScript |
| **页面文件** | `.ux` (类Vue单文件组件) |
| **样式** | CSS (Flex布局) |
| **存储** | `@system.storage` |
| **文件系统** | `@system.file` (仅 `internal://` 协议) |
| **IDE** | AIoT-IDE (基于VS Code) |

---

## 项目结构

```
vela_doc_guide/
├── docs-official/            # 小米官方文档 (GPL-3.0)
│   └── docs/zh/             # 完整API文档目录
│
├── archive/                  # 源码示例
│   ├── ebook-app/           # 电子书阅读器 (AGPL-3.0)
│   │   └── src/
│   └── input-method/        # 输入法组件 (MIT)
│
├── 文档 (根目录)
    ├── LICENSE              # CC BY-SA 4.0
    ├── README.md            # 本文件
    ├── AGENTS.md.example   # AI开发模板
    ├── AI-QUICKREF.md      # AI速查表
    ├── vela-dev-guide.md    # 开发指南
    ├── vela-ui-guide.md    # UI开发指南
    ├── input-method-guide.md # 组件指南
    └── ebook-app-tutorial.md # 实战教程
```

---

## 设备适配速查

| 设备 | designWidth | 屏幕尺寸 | 类型 |
|------|-------------|----------|------|
| 小米手环 8Pro/9Pro | 336 | 336×336 | 方屏 |
| REDMI Watch 5/6 | 192 | 390×312 | 胶囊屏 |
| 圆形表盘 | 480 | 454×454 | 圆屏 |

---

## 许可证

- **文档**: CC BY-SA 4.0
- **官方源码**: GPL-3.0
- **输入法组件**: MIT
- **电子书App**: AGPL-3.0

详见 [LICENSE](LICENSE) 文件。

---

## 参考来源

| 项目 | 原许可证 | 用途 |
|------|---------|------|
| [VelaDocs](https://github.com/CheongSzesuen/VelaDocs) | GPL-3.0 | 官方API文档 |
| [Vela_input_method](https://github.com/NEORUAA/Vela_input_method) | MIT | 输入法组件 |
| [com.bandbbs.ebook](https://github.com/youshen2/com.bandbbs.ebook) | AGPL-3.0 | 电子书阅读器 |

---

## 资源链接

| 资源 | 地址 |
|------|------|
| 官方文档 | https://iot.mi.com/vela/quickapp/zh/guide/ |
| IDE下载 | https://iot.mi.com/vela/quickapp/zh/guide/start/use-ide.html |
| 米坛社区 | https://www.bandbbs.cn/ |

---

## 如何使用本项目

### 人类开发者
1. 新手：从 [开发指南](./vela-dev-guide.md) 开始
2. 需要UI：参考 [UI开发指南](./vela-ui-guide.md)
3. 参考实际项目：查看 [archive](./archive/) 目录下的源码

### AI 开发者
1. 快速上手：查看 [AI速查](./AI-QUICKREF.md)
2. 新项目：复制 `AGENTS.md.example` 为 `AGENTS.md` 并按模板开发
3. 深入理解：参考 [实战教程](./ebook-app-tutorial.md)
