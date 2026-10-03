#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从官方文档站 (iot.mi.com) 补抓镜像仓库缺失的页面, 转成与镜像同风格的 Markdown。

风格对齐点(与 01-official-quickapp-js 现有文件保持一致):
  - frontmatter 仅写 sidebar_label
  - 图片下载到 images/, 正文用相对路径 ../../images/xxx.png 引用
  - 表格用标准 GFM
  - 不改动正文内容, 只做 HTML -> Markdown 的结构化转换

用法:
    python3 tools/fetch_official_supplement.py            # 抓 PAGES 里列出的页面
    python3 tools/fetch_official_supplement.py --check    # 只核对本地是否已存在
"""

import os
import re
import sys
import ssl
import time
import urllib.request
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag

BASE = "https://iot.mi.com"
PREFIX = "/vela/quickapp/zh/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_ROOT = os.path.join(ROOT, "01-official-quickapp-js")
IMG_DIR = os.path.join(DOC_ROOT, "images")

# 镜像(FangAiden/Vela_Application_Documentation)缺失、需从官方站直接补抓的页面
# 左侧 = 官方 URL 路径, 右侧 = 落地 md 相对 DOC_ROOT 的路径
PAGES = [
    ("/vela/quickapp/zh/features/system/bluetooth.html", "features/system/bluetooth.md"),
    ("/vela/quickapp/zh/guide/multi-screens/simulator.html", "guide/multi-screens/simulator.md"),
    ("/vela/quickapp/zh/tools/dev/official-site-tutorial.html", "tools/dev/official-site-tutorial.md"),
    ("/vela/quickapp/zh/tools/toolkit/start.html", "tools/toolkit/start.md"),
]

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def ctx():
    c = ssl.create_default_context()
    c.check_hostname = False
    c.verify_mode = ssl.CERT_NONE
    return c


def get(url, timeout=30, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=timeout, context=ctx()).read()
        except Exception as e:
            if i == retries - 1:
                raise
            print(f"    重试 {i+1}/{retries}: {e}")
            time.sleep(2)
    return None


# ---------------------------------------------------------------- HTML -> MD

def esc(t):
    """正文文本转义: 只转义会破坏 Markdown 结构的字符, 尽量少动。"""
    if t is None:
        return ""
    return t.replace("\\", "\\\\").replace("`", "\\`")


def inline(node):
    """递归渲染行内内容。"""
    if isinstance(node, NavigableString):
        return esc(str(node))
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    kids = "".join(inline(c) for c in node.children)

    if name in ("strong", "b"):
        return f"**{kids.strip()}**" if kids.strip() else kids
    if name in ("em", "i"):
        return f"*{kids.strip()}*" if kids.strip() else kids
    if name == "code":
        return f"`{node.get_text()}`"
    if name == "br":
        return "  \n"
    if name == "a":
        href = node.get("href", "")
        text = kids.strip() or node.get_text().strip()
        if not text:
            return ""
        if href.startswith("http"):
            return f"[{text}]({href})"
        return f"[{text}]({urljoin(PREFIX, href)})"
    if name == "img":
        src = node.get("src", "")
        alt = node.get("alt", "")
        src = rewrite_image(src)
        return f"![{alt}]({src})" if src else ""
    return kids


def rewrite_image(src):
    """站内图片统一改成 images/ 下的相对引用路径(图片本体由 fetch_page 预先下载)。"""
    if not src:
        return ""
    if src.startswith("http"):
        return src
    fname = os.path.basename(urlparse(urljoin(BASE, src)).path)
    return "../../images/" + fname if fname else src


def block_list(node, ordered, depth=0):
    out = []
    for li in node.find_all("li", recursive=False):
        text = render_children(li, in_list=True).strip()
        indent = "  " * depth
        marker = "1. " if ordered else "- "
        out.append(f"{indent}{marker}{text}")
    return "\n".join(out)


def render_table(table):
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        rows.append([inline(c).strip().replace("\n", " ") for c in cells])
    if not rows:
        return ""
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    head, body = rows[0], rows[1:]
    out = ["| " + " | ".join(head) + " |",
           "|" + "|".join(["---"] * ncol) + "|"]
    for r in body:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def render_children(node, in_list=False):
    """渲染一个容器节点的所有直接子节点为 Markdown 块。"""
    parts = []
    for child in node.children:
        if isinstance(child, NavigableString):
            t = str(child).strip()
            if t:
                parts.append(esc(t))
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name.lower()

        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            parts.append("#" * level + " " + inline(child).strip())
        elif name == "p":
            t = inline(child).strip()
            if t:
                parts.append(t)
        elif name == "pre":
            code = child.get_text()
            # 丢弃 VuePress 的代码行号列
            code = re.sub(r"^\s*\d+\s*(?=[|│])", "", code, flags=re.M)
            lang = ""
            for c in child.find_all("code"):
                for cls in (c.get("class") or []):
                    if cls.startswith("language-"):
                        lang = cls[9:]
            parts.append(f"```{lang}\n{code.rstrip()}\n```")
        elif name == "blockquote":
            inner = render_children(child).strip()
            parts.append("\n".join("> " + l for l in inner.split("\n")))
        elif name in ("ul", "ol"):
            parts.append(block_list(child, name == "ol"))
        elif name == "table":
            parts.append(render_table(child))
        elif name == "hr":
            parts.append("* * *")
        elif name in ("div", "section", "main", "article", "span"):
            parts.append(render_children(child, in_list))
        elif name == "img":
            src = child.get("src", "")
            alt = child.get("alt", "")
            r = rewrite_image(src)
            if r:
                parts.append(f"![{alt}]({r})")
        else:
            parts.append(render_children(child, in_list))
    return "\n\n".join(p for p in parts if p and p.strip())


def html_to_md(html, sidebar_label):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one("div.theme-default-content.content__default")
    if body is None:
        body = soup.select_one("main.page") or soup
    # 去掉标题锚点链接
    for a in body.select("a.header-anchor"):
        a.decompose()
    md = render_children(body).strip()
    md = re.sub(r"\n{3,}", "\n\n", md)
    return f"---\nsidebar_label: '{sidebar_label}'\n---\n\n{md}\n"


# ---------------------------------------------------------------- 主流程

def fetch_page(url_path, rel_md):
    url = urljoin(BASE, url_path)
    print(f"  抓取 {url}")
    html = get(url).decode("utf-8", "ignore")

    soup = BeautifulSoup(html, "html.parser")
    for a in soup.select("a.header-anchor"):
        a.decompose()
    h1 = soup.select_one("div.theme-default-content h1")
    title = h1.get_text().strip() if h1 else os.path.basename(rel_md)[:-3]

    # 先下载正文引用的图片
    for img in soup.select("div.theme-default-content img"):
        src = img.get("src", "")
        if not src:
            continue
        abs_url = urljoin(BASE, src)
        fname = os.path.basename(urlparse(abs_url).path)
        if not fname:
            continue
        dest = os.path.join(IMG_DIR, fname)
        if os.path.exists(dest):
            continue
        try:
            os.makedirs(IMG_DIR, exist_ok=True)
            with open(dest, "wb") as f:
                f.write(get(abs_url))
            print(f"    图片 {fname}")
        except Exception as e:
            print(f"    图片失败 {fname}: {e}")

    md = html_to_md(html, title)
    out = os.path.join(DOC_ROOT, rel_md)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"    -> {rel_md}  ({len(md)} 字符)")
    return True


def main():
    check = "--check" in sys.argv
    os.makedirs(IMG_DIR, exist_ok=True)

    if check:
        print("核对补抓页面是否已存在:")
        for url_path, rel_md in PAGES:
            p = os.path.join(DOC_ROOT, rel_md)
            print(f"  {'OK  ' if os.path.exists(p) else '缺失'} {rel_md}")
        return

    print("补抓镜像缺失的官方页面")
    print("-" * 60)
    ok = 0
    for url_path, rel_md in PAGES:
        try:
            if fetch_page(url_path, rel_md):
                ok += 1
        except Exception as e:
            print(f"  失败 {rel_md}: {e}")
    print("-" * 60)
    print(f"完成 {ok}/{len(PAGES)}")


if __name__ == "__main__":
    main()
