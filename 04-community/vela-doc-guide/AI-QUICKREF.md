# AI开发者Vela应用开发速查

> 聚焦Vela与Web开发的核心差异

---

## ⚠️ 核心差异（必看）

| Web开发 | Vela开发 |
|---------|----------|
| `localStorage` | `@system.storage` |
| `import` 组件 | `<import>` 标签 |
| Vue Router | `manifest.json` + `router.push()` |
| HTTP路径 | `internal://` 协议（仅支持） |
| CSS选择器 | 仅class选择器，不支持`:hover`等 |
| `window` | 无 |
| `document` | 无 |

---

## 生命周期

```javascript
// 页面
onInit() {}    // 数据初始化，接收params
onReady() {}   // DOM渲染完成
onShow() {}    // 显示
onHide() {}    // 隐藏
onDestroy() {} // 销毁

// 应用
onCreate() {}  // 创建
onShow() {}    // 显示
onHide() {}    // 隐藏
onDestroy() {} // 销毁
```

---

## 数据对象

```javascript
export default {
  private: { a: 1 },      // 私有，仅当前页面
  protected: { b: 2 },    // 可被子组件读取
  public: { c: 3 },       // 可被子组件修改
}
```

**接收页面参数**: `this.params.xxx`

---

## 组件通信

```javascript
// 父→子: props
props: ['title']  // 子组件声明

// 子→父: $emit
this.$emit('event', { data: 1 });

// 父→子广播: $broadcast
this.$broadcast('update', { value: 1 });

// 监听: $on
this.$on('event', (data) => {});

// 停止: $off 或 event.$stop()
```

---

## 路由与启动模式

```javascript
router.push({ uri: '/pages/detail', params: { id: 1 } });
router.back();
```

**manifest启动模式**:
```json
"launchMode": "singleTask"  // standard/singleTask/singleTop
```

---

## CSS限制

❌ **不支持**: 后代选择器、子选择器、属性选择器、伪类(`:hover`)、伪元素

✅ **支持**: class选择器、Flexbox、基础属性(width/height/padding/margin/border-radius)

---

## 关键API

| API | 用途 |
|-----|------|
| `@system.router` | 页面跳转 |
| `@system.storage` | 本地存储 |
| `@system.file` | 文件操作（仅internal://） |
| `@system.sensor` | 加速度计、气压计、罗盘 |
| `@system.device` | 获取屏幕形状 |
| `@system.prompt` | 提示对话框 |
| `@system.app` | 应用控制 |
| `@system.vibrator` | 振动 |
| `@system.brightness` | 屏幕亮度 |

---

## 设备适配

```javascript
device.getInfo({ success: (data) => {
  console.log(data.screenShape); // 'circle'/'rect'/'pill-shaped'
}});
```

```html
<div if="{{screenShape === 'circle'}}">圆屏布局</div>
```

| 设备 | designWidth | 屏幕 |
|------|-------------|------|
| 方屏手环 | 336 | 336x480 |
| 胶囊屏 | 192 | 390x312 |
| 圆屏手表 | 480 | 454x454 |

---

## 页面结构（电子书App风格）

```html
<div class="page">
  <img static src="/common/images/hd.png" style="position:absolute;left:0;top:0;width:336px;height:102px;" />
  <img static src="/common/images/back.png" @click="back" style="position:absolute;left:6px;top:6px;width:72px;height:72px;"/>
  <text style="position:absolute;left:78px;top:35px;font-size:32px;font-weight:bold;color:white;">标题</text>
  <list class="list">
    <list-item class="item" for="{{i in items}}">
      <text class="itemtext">{{i.name}}</text>
    </list-item>
  </list>
</div>

<style>
.page { width: 100%; height: 100%; background-color: #000000; position: relative; }
.list { width: 100%; height: 100%; padding: 86px 6px; position: absolute; top: 0; left: 0; }
.item { height: 112px; background: #262626; border-radius: 36px; padding: 14px 20px; margin-bottom: 8px; }
.itemtext { font-size: 32px; font-weight: bold; color: white; }
</style>
```

---

## 快速模板

```javascript
// app.ux
export default {
  onCreate() {},
  onShow() {},
  onHide() {},
  onDestroy() {}
}
```

```json
// manifest.json
{
  "package": "com.example.app",
  "deviceTypeList": ["watch"],
  "features": [
    { "name": "system.router" },
    { "name": "system.storage" }
  ],
  "config": { "designWidth": 336 },
  "router": {
    "entry": "index",
    "pages": { "index": { "component": "index", "path": "/" } }
  }
}
```

---

## 开发要点

1. **内存**: 定期调用 `global.runGC()`
2. **打包**: 需要签名证书
3. **调试**: AIoT-IDE 或真机

---

## 参考文档

- 官方文档: `docs-official/docs/zh/`
- 源码参考: `archive/ebook-app/src/`
- 图标资源: `archive/ebook-app/src/common/images/`
