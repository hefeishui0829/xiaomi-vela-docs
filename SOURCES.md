# 来源、许可与免责声明

本仓库是**归档与分类整理**，不生产内容。所有原始文档均原样复制，未做正文改写；
新增的只有导航索引（各目录 `README.md`）与两个工具脚本。

---

## 一、官方 JS 快应用文档 — `01-official-quickapp-js/`

| 项 | 内容 |
|---|---|
| 原始出处 | 小米官方文档站 <https://iot.mi.com/vela/quickapp/zh/> |
| 版权 | **© 小米科技有限责任公司，版权所有** |
| 获取方式 | ① 主体 143 篇来自社区镜像 `FangAiden/Vela_Application_Documentation`（该镜像系用其 `scripts/import_quickapp_docs.py` 从官方站抓取转录）；② 镜像缺失的 4 篇由本仓库 `tools/fetch_official_supplement.py` 直接从官方站抓取 |
| 抓取时间 | 2026-10-03 |
| 落地篇数 | 147 篇正文 + 207 张配图 |

补抓的 4 篇（其余 143 篇来自镜像）：

- `features/system/bluetooth.md`
- `guide/multi-screens/simulator.md`
- `tools/dev/official-site-tutorial.md`
- `tools/toolkit/start.md`

> 官方站侧栏可见 107 个页面，镜像含 143 篇（镜像比侧栏更全，多出 APILevel4、`guide/framework/script/*` 等），补抓后无遗漏。

**性质说明**：官方文档以网页形式公开发布，此处转为 Markdown 仅为便于离线检索与版本归档。
如小米提出异议或文档更新，请以上游官方站为准，本仓库可随时撤下。

## 二、官方 Lua 应用文档 — `02-official-lua/`

- 出处：同上，Vela 平台 Lua 形态应用的官方文档
- 版权：**© 小米科技有限责任公司**
- 篇数：70 篇

## 三、官方 Shell 文档 — `03-official-shell/`

- 出处：同上
- 版权：**© 小米科技有限责任公司**
- 篇数：8 篇

## 四、社区文档 — `04-community/`

### 4.1 `xiaomi-band-dev-guide/`

| 项 | 内容 |
|---|---|
| 上游 | <https://github.com/KaiTeeDreamChai/xiaomi-band-dev-guide> |
| 作者 | KaiTeeDreamChai |
| 许可 | **MIT** |
| 上游 commit | `905d2ef`（2026-10-01） |
| 内容 | 小米手环表盘与快应用开发指南、避坑手册、真机部署，6 篇正文 |

### 4.2 `vela-doc-guide/`

| 项 | 内容 |
|---|---|
| 上游 | <https://github.com/epheiamoe/vela_doc_guide> |
| 作者 | epheiamoe |
| 许可 | **CC BY-SA 4.0**（署名-相同方式共享） |
| 上游 commit | `cb38464`（2026-03-18） |
| 内容 | Vela 开发指南、UI 规范、速查表、输入法组件、电子书阅读器实战教程、示例工程 |

> **CC BY-SA 4.0 注意**：转载或改编这部分内容时，须署名原作者并以**相同许可**共享衍生作品。
> 本仓库将其作为独立整体原样收录（集合作品），未做改编，故不影响同仓内其他独立内容的许可。

---

## 五、本仓库自有内容

| 文件 | 许可 |
|---|---|
| `README.md`、`SOURCES.md`、各目录 `README.md` | 可自由使用 |
| `tools/fetch_official_supplement.py` | 可自由使用 |
| `tools/gen_index.py` | 可自由使用 |

---

## 六、免责

- 本仓库**不是**小米官方项目，与小米公司无隶属或授权关系
- 文档内容可能存在时效性偏差，开发请以官方站与真机实测为准
- 涉及设备规格（屏幕分辨率、API Level）的数据来自官方文档，实际机型可能存在差异
- 若你是上述内容的权利人且不希望被收录，请提 issue，将在 24 小时内移除

## 七、如何重新生成

```bash
# 补抓官方站缺失页面 -> 01-official-quickapp-js/
python3 tools/fetch_official_supplement.py

# 核对补抓结果
python3 tools/fetch_official_supplement.py --check

# 重新生成各目录导航索引
python3 tools/gen_index.py
```

依赖：`beautifulsoup4`。
