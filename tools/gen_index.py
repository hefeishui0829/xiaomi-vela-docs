#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为各分类目录自动生成 README.md 导航索引。

只读原始文档, 提取标题生成链接表, 不改动任何原始 md 文件。
标题优先级: frontmatter 的 sidebar_label > 正文首个 # 标题 > 文件名

用法:
    python3 tools/gen_index.py
"""

import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 分区中文名与说明
SECTION_DESC = {
    "guide": ("教程", "从零上手: 环境搭建、项目结构、UX 语法、框架机制、多屏适配、发布上架"),
    "components": ("组件", "内置 UI 组件参考: 基础 / 容器 / 表单 / 通用样式与事件"),
    "features": ("JS 接口", "运行时 API: 基础 / 数据 / 网络 / 系统能力 / 安全 / 其他"),
    "tools": ("工具", "AIoT-IDE、调试器、模拟器、项目模板、打包发布"),
    "samples": ("编程示例", "官方示例代码与设计模式参考"),
    "images": ("配图", "文档引用的截图与示意图"),
}


def read_frontmatter_label(path):
    try:
        with open(path, encoding="utf-8") as f:
            head = f.read(400)
    except Exception:
        return None
    if not head.startswith("---"):
        return None
    m = re.search(r"^sidebar_label:\s*['\"]?(.*?)['\"]?\s*$", head, re.M)
    if m:
        t = m.group(1).strip()
        return t or None
    return None


def read_h1(path):
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
                if line and not line.startswith("---"):
                    break
    except Exception:
        pass
    return None


def title_of(path):
    name = os.path.basename(path)[:-3]
    if name == "index":
        return None
    t = read_frontmatter_label(path) or read_h1(path) or name
    return t.replace("|", "\\|").strip()


def build_tree(base, exclude=("images",)):
    """返回 [(分区名, [(相对路径, 标题)]), ...]"""
    out = []
    for sub in sorted(os.listdir(base)):
        d = os.path.join(base, sub)
        if not os.path.isdir(d) or sub in exclude:
            continue
        items = []
        for p in sorted(glob.glob(os.path.join(d, "**", "*.md"), recursive=True)):
            rel = os.path.relpath(p, base).replace("\\", "/")
            t = title_of(p)
            if t is None:
                continue
            items.append((rel, t))
        # index.md 排最前
        items.sort(key=lambda x: (not x[0].endswith("/index.md"), x[0]))
        out.append((sub, items))
    return out


def gen_official_quickapp():
    base = os.path.join(ROOT, "01-official-quickapp-js")
    tree = build_tree(base)
    lines = ["# 01 · 官方 JS 快应用文档（Xiaomi Vela）",
             "",
             "> 小米官方 `Xiaomi Vela JS 应用` 文档站 <https://iot.mi.com/vela/quickapp/zh/> 的完整 Markdown 副本。",
             "> 这是**小米手环 / 手表快应用开发的主文档**，内容原样保留，未做改写。",
             "",
             "## 分区导航",
             "",
             "| 分区 | 篇数 | 说明 |",
             "|---|---:|---|"]
    for sub, items in tree:
        cn, desc = SECTION_DESC.get(sub, (sub, ""))
        lines.append(f"| [{sub}/](./{sub}/) | {len(items)} | {desc} |")
    lines.append("| [images/](./images/) | — | 文档配图 207 张 |")
    lines.append("")
    lines.append("---")
    lines.append("")

    for sub, items in tree:
        cn, desc = SECTION_DESC.get(sub, (sub, ""))
        lines.append(f"## {sub}/ — {cn}")
        lines.append("")
        lines.append(f"{desc}")
        lines.append("")
        idx = [i for i in items if i[0].endswith("/index.md")]
        for rel, t in idx:
            lines.append(f"- [分区首页 · {t}](./{rel})")
        rest = [i for i in items if not i[0].endswith("/index.md")]
        if rest:
            if idx:
                lines.append("")
            for rel, t in rest:
                lines.append(f"- [{t}](./{rel})")
        lines.append("")

    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"01-official-quickapp-js/README.md  分区 {len(tree)}  篇目 {sum(len(i) for _, i in tree)}")


def gen_simple(folder, title, intro, exclude=()):
    base = os.path.join(ROOT, folder)
    tree = build_tree(base, exclude=exclude)
    lines = [f"# {title}", "", "> " + intro, ""]
    total = 0
    for sub, items in tree:
        cn, desc = SECTION_DESC.get(sub, (sub, ""))
        lines.append(f"## {sub}/ — {cn}")
        lines.append("")
        if desc:
            lines.append(desc)
            lines.append("")
        for rel, t in items:
            lines.append(f"- [{t}](./{rel})")
            total += 1
        lines.append("")
    # 散落在根目录的 md
    top = []
    for p in sorted(glob.glob(os.path.join(base, "*.md"))):
        name = os.path.basename(p)[:-3]
        if name in ("README", "index"):
            continue
        t = title_of(p) or name
        top.append((name + ".md", t))
    if top:
        lines.append("## 根目录文档")
        lines.append("")
        for rel, t in top:
            lines.append(f"- [{t}](./{rel})")
            total += 1
        lines.append("")
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"{folder}/README.md  篇目 {total}")


def main():
    gen_official_quickapp()
    gen_simple("02-official-lua", "02 · 官方 Lua 应用文档",
               "Vela 平台另一种应用形态（Lua 脚本应用）的官方文档副本，内容原样保留。")
    gen_simple("03-official-shell", "03 · 官方 Shell 文档",
               "Vela Shell 相关官方文档副本，内容原样保留。")


if __name__ == "__main__":
    main()
