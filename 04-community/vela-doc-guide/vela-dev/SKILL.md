# Vela 应用开发 Skill

> 开发小米 Vela 手表应用的 AI 助手

## 概述

这个 Skill 帮助 AI 开发小米 Vela 手表应用（快应用）。适用于小米手环 8Pro/9Pro、REDMI Watch 等设备。

## 安装

```bash
# 1. 创建 skill 目录
mkdir -p ~/.claude/skills/vela-dev

# 2. 复制本文件到该目录
cp SKILL.md ~/.claude/skills/vela-dev/

# 3. 重启 Claude Code
```

## 快速入口

| 任务 | 参考文档 |
|------|----------|
| 新建项目 | 参考 AGENTS.md.example |
| UI 开发 | 使用 vela-ui-guide.md |
| API 查找 | 使用 vela-dev-guide.md |
| 参考示例 | archive/ 目录 |

## 核心知识

### 项目结构

```
src/
├── pages/           # 页面
│   └── index/
│       └── index.ux
├── components/      # 组件
├── utils/          # 工具
├── i18n/           # 国际化
├── common/         # 资源
├── manifest.json   # 配置
└── config-watch.json
```

### 关键差异 (vs Web)

| Web | Vela |
|-----|------|
| `localStorage` | `@system.storage` |
| Vue Router | `manifest.json` + `router.push()` |
| `import` | `<import>` 标签 |
| HTTP 路径 | `internal://` 协议 |

### manifest.json 基础

```json
{
  "package": "com.example.app",
  "name": "AppName",
  "versionName": "1.0.0",
  "versionCode": 1,
  "pages": [
    { "src": "pages/index/index.ux" }
  ],
  "config": {
    "designWidth": 336
  }
}
```

### 屏幕适配

| 设备 | designWidth | 屏幕 |
|------|-------------|------|
| 圆屏 | 480 | 454x454 |
| 方屏 | 336 | 336x336 |
| 胶囊 | 192 | 390x312 |

### UI 规范

```
背景: #000000
卡片: #262626
强调: #0D6EFF
文字: #FFFFFF
次级: rgba(255,255,255,0.6)

大标题: 32px
标题: 24px
正文: 28-30px
```

### 常用 API

```javascript
// 路由
import router from '@system.router';
router.push({ uri: 'pages/detail/detail' });
router.back();

// 存储
import storage from '@system.storage';
storage.get({ key: 'xxx' });
storage.set({ key: 'xxx', value: 'xxx' });

// 文件
import file from '@system.file';
file.readText({ uri: 'internal://files/xxx.txt' });

// 传感器
import sensor from '@system.sensor';
sensor.subscribeAccelerometer({ callback: (data) => {} });
```

### 页面生命周期

| Vela | 说明 |
|------|------|
| `onInit` | 初始化 |
| `onShow` | 显示 |
| `onHide` | 隐藏 |
| `onDestroy` | 销毁 |

## 注意事项

1. **内存限制**：手环内存有限，频繁调用 `global.runGC()`
2. **屏幕适配**：使用 `rpx` 或根据 designWidth 计算
3. **调试**：使用 AIot-IDE 模拟器或真机
4. **打包**：需配置证书才能安装到真机

## 参考资源

- 官方文档: https://iot.mi.com/vela/quickapp/zh/guide/
- IDE下载: https://iot.mi.com/vela/quickapp/zh/guide/start/use-ide.html

---

*此 Skill 基于 vela_doc_guide 项目整理*
