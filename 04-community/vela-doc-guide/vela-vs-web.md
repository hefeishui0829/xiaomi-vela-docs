# Vela vs Web 开发 - 关键差异

> 只列Vela与Web开发的不同点，相同的不再说明

---

## 1. 存储

| Web | Vela |
|-----|------|
| `localStorage.getItem()` | `storage.get({ success: (data) => {} })` |
| `localStorage.setItem()` | `storage.set({ key, value })` |

```javascript
// Web
localStorage.setItem('key', 'value');
const val = localStorage.getItem('key');

// Vela
storage.set({ key: 'key', value: 'value' });
storage.get({ key: 'key', success: (data) => { console.log(data); } });
```

---

## 2. 路由

| Web | Vela |
|-----|------|
| `router.push('/page')` | `router.push({ uri: 'pages/index/index' })` |
| `<router-link>` | `<text @click="goBack">` |

**Vela路由必须在manifest.json声明！**

```json
{
  "router": {
    "entry": "index",
    "pages": {
      "index": { "component": "index", "path": "/" },
      "detail": { "component": "detail", "path": "/detail" }
    }
  }
}
```

```javascript
// 跳转
router.push({ uri: 'pages/detail/detail' });
router.push({ uri: 'pages/detail/detail', params: { id: 123 } });

// 返回
router.back();
```

---

## 3. 文件路径

| Web | Vela |
|-----|------|
| `http://...` | `internal://files/...` |
| `/assets/...` | `/common/...` |

```javascript
// 读取应用文件
file.readText({ uri: 'internal://files/data.txt', success: (data) => {} });

// 读取资源文件
<img src="/common/images/icon.png" />
```

---

## 4. 页面生命周期

| Web (Vue) | Vela |
|-----------|------|
| `created` | `onCreate` (App) |
| `mounted` | `onReady` |
| - | `onInit` (页面) |
| `activated` | `onShow` |
| `deactivated` | `onHide` |
| `destroyed` | `onDestroy` |

---

## 5. 组件引入

| Web | Vela |
|-----|------|
| `import MyComp from './comp'` | `<import name="MyComp" src="./comp.ux" />` |

```html
<!-- Vela: 在template中使用 -->
<import name="ListItem" src="../components/listitem.ux" />

<template>
  <ListItem title="Item" />
</template>
```

---

## 6. 组件通信

| Web (Vue) | Vela |
|-----------|------|
| props | props (父传子) |
| $emit | $emit (子传父) |

```javascript
// 子组件触发事件
this.$emit('select', { id: 1 });

// 父组件监听
<ListItem @select="onSelect" />
```

---

## 7. 多设备适配

**Vela特有概念：designWidth**

```json
{
  "config": {
    "designWidth": 336  // 设计稿基准宽度
  }
}
```

| 设备 | designWidth | 屏幕 |
|------|-------------|------|
| 方屏 | 336 | 336×480 |
| 胶囊 | 192 | 390×312 |
| 圆屏 | 480 | 454×454 |

```javascript
// 获取屏幕类型
import device from '@system.device';
device.getInfo({
  success: (data) => {
    console.log(data.screenShape); // 'circle', 'rect', 'pill-shaped'
  }
});
```

```html
<!-- 条件渲染 -->
<div if="{{screenShape === 'circle'}}">圆屏布局</div>
```

---

## 8. 系统API

| 功能 | Vela API |
|------|----------|
| 传感器 | `@system.sensor` |
| 电池 | `@system.battery` |
| 亮度 | `@system.brightness` |
| 振动 | `@system.vibrator` |
| 位置 | `@system.geolocation` |

---

## 9. manifest.json 必须配置项

```json
{
  "package": "com.example.app",    // 必须：包名
  "name": "AppName",               // 必须：应用名
  "deviceTypeList": ["watch"],     // 必须：设备类型
  "features": [                    // 必须：使用的系统API
    { "name": "system.storage" },
    { "name": "system.router" }
  ],
  "config": {
    "designWidth": 336             // 必须：设计宽度
  },
  "router": {                      // 必须：路由配置
    "entry": "index",
    "pages": {}
  }
}
```

---

## 10. 禁止/限制

- ❌ 不支持 `localStorage` → 用 `@system.storage`
- ❌ 不支持 `fetch` URL → 用 `@system.fetch` 或 `internal://`
- ❌ 不支持 `localStorage` 的同步API
- ❌ 内存有限 → 频繁调用 `global.runGC()`
- ⚠️ CSS 不完全支持 → 优先使用 Flex 布局

---

## 快速参考命令

```javascript
// 存储
storage.get({ key, success: (data) => {} });
storage.set({ key, value });

// 路由
router.push({ uri: 'pages/xxx/xxx' });
router.back();

// 文件
file.readText({ uri: 'internal://files/xxx', success: (data) => {} });

// 设备信息
device.getInfo({ success: (data) => { data.screenShape; } });

// 内存
global.runGC();
```

---

*来源: 弦电子书 (ebook-app)*
