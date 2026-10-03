# 小米Vela手表JS开发指南

> 文档基于小米官方Vela JS应用开发文档整理
> 源仓库: [VelaDocs](https://github.com/CheongSzesuen/VelaDocs) (GPL-3.0)
> 本文档采用 CC BY-SA 4.0 许可证

---

## 目录

1. [文档索引/目录](#文档索引目录)
2. [开发环境搭建](#开发环境搭建)
3. [核心概念](#核心概念)
4. [API速查表](#api速查表)
5. [常见问题/排错指南](#常见问题排错指南)
6. [多设备适配要点](#多设备适配要点)

---

## 文档索引/目录

### 官方文档路径索引

| 类别 | 文档路径 | 说明 |
|------|----------|------|
| **入门指南** | `docs-official/docs/zh/guide/index.md` | 应用概述、特点、应用场景 |
| **快速开始** | `docs-official/docs/zh/guide/start/use-ide.md` | IDE安装、项目创建、运行调试 |
| **项目结构** | `docs-official/docs/zh/guide/start/project-overview.md` | 目录结构、配置文件 |
| **框架文档** | `docs-official/docs/zh/guide/framework/index.md` | 框架简介、路由管理、数据绑定 |
| **生命周期** | `docs-official/docs/zh/guide/framework/script/lifecycle.md` | 页面/应用生命周期 |
| **组件开发** | `docs-official/docs/zh/guide/framework/template/component.md` | 自定义组件、父子通信 |
| **项目配置** | `docs-official/docs/zh/guide/framework/manifest.md` | manifest.json配置 |
| **多屏适配** | `docs-official/docs/zh/guide/multi-screens/index.md` | 多设备适配指南 |
| **适配规范** | `docs-official/docs/zh/guide/multi-screens/specs.md` | 适配技术规范 |
| **系统API** | `docs-official/docs/zh/features/system/index.md` | 系统能力接口 |
| **网络API** | `docs-official/docs/zh/features/network/index.md` | 网络请求接口 |
| **调试工具** | `docs-official/docs/zh/tools/debug/debug.md` | 调试运行指南 |
| **常见问题** | `docs-official/docs/zh/guide/other/faq.md` | FAQ |

---

## 开发环境搭建

### 1. 系统要求

| 操作系统 | 最低版本要求 |
|----------|--------------|
| macOS | 14（Sonoma）及以上 |
| Windows | 10 或更高版本 |
| Ubuntu | 20.04 LTS 或更高版本 |

### 2. 安装 AIoT-IDE

AIoT-IDE 是开发 Xiaomi Vela JS 应用的官方集成开发环境，基于 VS Code 构建。

**下载与安装：**

1. 下载 AIoT-IDE 安装包
2. macOS 安装可能需要执行：
   ```bash
   sudo xattr -r -d com.apple.quarantine /path/to/AIoT-IDE.app
   ```

**历史版本：** [点击查看](https://kpan.mioffice.cn/webfolder/ext/j6SfQsarf8I%40?n=0.18700074913007825) (密码：99E6)

### 3. 创建项目

1. 点击左上角「文件」>「新建项目」
2. 点击卡片左侧边栏的 Vela，点击「创建」
3. 选择一个项目模版，点击「下一步」
4. 输入项目名称和项目保存路径，点击「创建」

### 4. 模拟器环境管理

```bash
# 模拟器环境说明
- 点击「检查模拟器环境，创建模拟器实例」按钮
- 选择「自动安装」，插件自动安装模拟器依赖
- 推荐使用 Vela 正式版（4.0）版本的镜像
```

### 5. 运行与调试

```javascript
// 运行项目
点击 banner 栏的「运行」按钮

// 调试项目
点击 banner 栏的「调试」按钮
// 调试面板支持：DOM树查看、Console、断点调试
```

### 6. 打包项目

**开发模式打包：**
```bash
点击 banner 栏的「打包」按钮
# 生成 dist/.debug.rpk 和 build 目录
```

**生产模式打包：**
```bash
# 需要先配置签名证书
# 点击「发布」按钮 > 填写信息 > 点击「完成」
# 插件会在 sign 目录下生成 private.pem 和 certificate.pem
```

---

## 核心概念

### 1. 项目结构

```
├── manifest.json      # 项目配置文件
├── app.ux             # 应用级生命周期、全局数据
├── pages/             # 页面目录
│   ├── index/
│   │   └── index.ux   # 页面文件
│   └── detail/
│       └── detail.ux
├── i18n/              # 多语言配置
│   ├── defaults.json
│   ├── zh-CN.json
│   └── en-US.json
└── common/            # 公共资源
    ├── style.css
    ├── utils.js
    └── logo.png
```

### 2. UX文件结构

一个页面由三部分组成：`template`（模板）、`style`（样式）、`script`（脚本）

```html
<template>
  <div class="page">
    <text class="title">欢迎打开{{title}}</text>
    <input class="btn" type="button" value="跳转到详情页" onclick="routeDetail">
  </div>
</template>

<style>
  .btn {
    width: 400px;
    height: 60px;
    background-color: #09ba07;
    color: #ffffff;
  }
</style>

<script>
  import router from '@system.router'
  
  export default {
    // 页面数据对象
    private: {
      title: '示例页面'
    },
    // 按钮点击回调
    routeDetail() {
      router.push({ uri: '/pages/detail' })
    }
  }
</script>
```

### 3. 页面数据对象

```javascript
export default {
  // private: 私有数据，外部不可覆盖
  private: {
    a: 1,
    b: 'hello'
  },
  // protected: 受保护数据
  protected: {
    c: 2
  },
  // public: 公共数据（可从外部传入）
  public: {
    d: 3
  }
}
```

### 4. 生命周期

#### 页面生命周期

| 生命周期 | 说明 |
|----------|------|
| `onInit()` | ViewModel数据已准备好 |
| `onReady()` | 模板已编译完成，可获取DOM节点 |
| `onShow()` | 页面显示 |
| `onHide()` | 页面隐藏 |
| `onDestroy()` | 页面销毁 |
| `onBackPress()` | 返回按钮按下 |
| `onRefresh(query)` | 页面重新打开（singleTask模式） |
| `onConfigurationChanged(event)` | 配置变更（如语言改变） |

#### APP生命周期

| 生命周期 | 说明 |
|----------|------|
| `onCreate()` | 应用创建 |
| `onShow()` | 应用显示 |
| `onHide()` | 应用隐藏 |
| `onDestroy()` | 应用销毁 |
| `onError(e)` | 捕获异常 |

### 5. 组件系统

#### 自定义组件

```html
<!-- 子组件 part1.ux -->
<template>
  <div class="part1">
    <text>{{message}}</text>
  </div>
</template>

<script>
  export default {
    props: ['message'],
    onInit() {
      console.log('组件初始化')
    }
  }
</script>
```

#### 引入组件

```html
<import name="comp-part1" src="./part1"></import>

<template>
  <div>
    <comp-part1 message="Hello"></comp-part1>
  </div>
</template>
```

#### 父子组件通信

**父传子：** 通过 props
```javascript
// 子组件
props: ['title'],
onInit() {
  console.log(this.title)  // 获取父组件传入的值
}
```

**子传父：** 通过 $emit
```javascript
// 子组件
this.$emit('customEvent', { data: 'value' })

// 父组件
<comp oncustom-event="handleEvent"></comp>

handleEvent(evt) {
  console.log(evt.detail.data)
}
```

**父传子广播：** 通过 $broadcast
```javascript
// 父组件
this.$broadcast('update', { value: 'new data' })

// 子组件
this.$on('update', (data) => {
  console.log(data.value)
})
```

**任意组件通信：** 通过 $on/$dispatch
```javascript
// 监听事件
this.$on('customEvent', (data) => {
  console.log(data)
})

// 停止监听
this.$off('customEvent')
// 或
event.$stop()
```

---

## API速查表

### 1. 页面路由 router

> 无需在manifest中声明

```javascript
import router from '@system.router'

// 跳转到应用内页面
router.push({ uri: '/pages/detail', params: { id: '1' } })

// 替换当前页面
router.replace({ uri: '/pages/detail' })

// 返回上一页
router.back()

// 返回指定页面
router.back({ path: '/home' })

// 清空页面栈
router.clear()

// 获取页面栈长度
var length = router.getLength()

// 获取当前页面状态
var state = router.getState()
// state.index, state.name, state.path
```

### 2. 数据请求 fetch

> 需在manifest中声明: `{ "name": "system.fetch" }`

```javascript
import fetch from '@system.fetch'

// 基础请求
fetch.fetch({
  url: 'https://api.example.com/data',
  method: 'GET',
  success: function(res) {
    console.log(res.data)
  },
  fail: function(data, code) {
    console.log(code)
  }
})

// Promise方式
fetch.fetch({
  url: 'https://api.example.com/data',
  responseType: 'json'
}).then(res => {
  console.log(res.data)
}).catch(error => {
  console.log(error)
})
```

### 3. 本地存储 storage

> 需在manifest中声明: `{ "name": "system.storage" }`

```javascript
import storage from '@system.storage'

// 存储数据
storage.set({
  key: 'username',
  value: 'John',
  success: function() {
    console.log('存储成功')
  }
})

// 读取数据
storage.get({
  key: 'username',
  success: function(data) {
    console.log(data)
  }
})

// 删除数据
storage.delete({
  key: 'username'
})

// 清空所有数据
storage.clear()
```

### 4. 网络状态 network

> 需在manifest中声明: `{ "name": "system.network" }`

```javascript
import network from '@system.network'

// 获取网络类型
network.getType({
  success: function(data) {
    // data.type: 'wifi', '4g', '5g', 'none' 等
    console.log(data.type)
  }
})

// 监听网络变化
network.subscribe({
  callback: function(data) {
    console.log('网络类型变化:', data.type)
  }
})

// 取消监听
network.unsubscribe()
```

### 5. 地理位置 geolocation

> 需在manifest中声明: `{ "name": "system.geolocation" }`

```javascript
import geolocation from '@system.geolocation'

// 获取位置
geolocation.getLocation({
  success: function(data) {
    console.log(data.latitude, data.longitude)
  }
})

// 监听位置变化
geolocation.subscribe({
  callback: function(data) {
    console.log(data.latitude, data.longitude)
  }
})

// 取消监听
geolocation.unsubscribe()
```

### 6. 文件存储 file

> 需在manifest中声明: `{ "name": "system.file" }`
> **注意**: 仅支持 `internal://` 协议路径

```javascript
import file from '@system.file'

// 读取文本文件
file.readText({
  uri: 'internal://files/book.txt',
  success: function(data) {
    console.log(data.text)
  }
})

// 读取二进制文件
file.readArrayBuffer({
  uri: 'internal://files/book.txt',
  position: 0,
  length: 1000,
  success: function(data) {
    console.log(data.buffer)
  }
})

// 写入文本文件
file.writeText({
  uri: 'internal://files/output.txt',
  text: 'Hello Vela',
  success: function() {
    console.log('写入成功')
  }
})

// 写入二进制数据
file.writeArrayBuffer({
  uri: 'internal://files/data.bin',
  buffer: uint8Array,
  success: function() {
    console.log('写入成功')
  }
})

// 列出目录文件
file.list({
  uri: 'internal://files/books/',
  success: function(data) {
    console.log(data.fileList)
  }
})

// 获取文件信息
file.get({
  uri: 'internal://files/book.txt',
  success: function(data) {
    console.log(data.length, data.lastModifiedTime)
  }
})

// 删除文件
file.delete({
  uri: 'internal://files/book.txt'
})

// 移动文件
file.move({
  srcUri: 'internal://cache/book.txt',
  dstUri: 'internal://files/book.txt'
})

// 复制文件
file.copy({
  srcUri: 'internal://files/book.txt',
  dstUri: 'internal://files/book_copy.txt'
})
```

**URI协议说明**:
- `internal://files/` - 应用私有文件目录
- `internal://cache/` - 缓存目录（可被清理）
- `/Common/` - 应用资源目录（只读）

### 7. 传感器 sensor

> 需在manifest中声明: `{ "name": "system.sensor" }`

#### 加速度计 (Accelerometer)

```javascript
import sensor from '@system.sensor'

// 订阅加速度计数据
sensor.subscribeAccelerometer({
  interval: 'normal',  // 'game' | 'ui' | 'normal'
  callback: function(data) {
    console.log(data.x, data.y, data.z)
  }
})

// 取消订阅
sensor.unsubscribeAccelerometer()
```

#### 气压计 (Pressure)

```javascript
// 订阅气压计数据
sensor.subscribePressure({
  callback: function(data) {
    console.log(data.pressure)  // 单位: hPa
  }
})

// 取消订阅
sensor.unsubscribePressure()
```

#### 罗盘 (Compass)

```javascript
// 订阅罗盘数据
sensor.subscribeCompass({
  callback: function(data) {
    console.log(data.direction)  // 0-360度
    console.log(data.accuracy)    // 精度: 3高/2中/1低/-1不可信
  }
})

// 取消订阅
sensor.unsubscribeCompass()
```

**注意**: 不同传感器支持的设备不同，请参考官方文档确认设备兼容性。

### 7. 振动 vibrator

> 需在manifest中声明: `{ "name": "system.vibrator" }`

```javascript
import vibrator from '@system.vibrator'

// 振动
vibrator.vibrate({
  duration: 200
})

// 短振动
vibrator.vibrateShort({})
```

### 8. 屏幕亮度 brightness

> 需在manifest中声明: `{ "name": "system.brightness" }`

```javascript
import brightness from '@system.brightness'

// 设置屏幕亮度 (0-1)
brightness.set({
  brightness: 0.5
})

// 获取屏幕亮度
brightness.get({
  success: function(data) {
    console.log(data.brightness)
  }
})
```

### 9. 电量 battery

> 需在manifest中声明: `{ "name": "system.battery" }`

```javascript
import battery from '@system.battery'

// 获取电量信息
battery.getLevel({
  success: function(data) {
    console.log(data.level)  // 0-100
    console.log(data.charging)  // true/false
  }
})
```

### 10. 录音 record

> 需在manifest中声明: `{ "name": "system.record" }`

```javascript
import record from '@system.record'

// 开始录音
record.start({
  filename: '/record/test.amr',
  success: function() {
    console.log('录音开始')
 

// 停止录音
record.stop({
  success: function(data) {
    console.log('录音文件:', data.filePath)
  }
})
```

---

## 常见问题/排错指南

### Q1: 如何适配不同尺寸的屏幕？

框架默认屏幕分辨率是480*480，Vela三方应用会自动适配。

```json
// manifest.json
{
  "config": {
    "designWidth": 466
  }
}
```

CSS中的尺寸数值与设计稿保持一致即可。

### Q2: 模拟器怎么跟手表通信？

模拟器跟手机通讯需要外接蓝牙适配器，配置复杂，建议使用**真机调试**。

### Q3: 如何解决签名不正确的问题？

手表和手机通信前会检查应用签名，调试时需要手机app和手表rpk使用**配套的证书**打包。

### Q4: 如何排查通信(interconnect)问题？

1. 检查手表端发送的数据结构是否正确
2. 排查手机端打印的日志（使用adb logcat工具）

### Q5: 如何解决列表数据更新闪烁？

通过for循环渲染的列表，可以增加`tid`属性来解决：

```html
<text for="{{item in list}}" tid="id">{{item.name}}</text>
```

### Q6: 如何将rpk上传到手表真机运行？

1. 手机安装小米运动健康（联系商务获取）
2. 点击【小米运动健康】-->【我的】-->【关于】-->【Debug】
3. 点击【第三方应用】> 【Install third app】
4. 选择本地rpk文件安装

### Q7: 如何查看手表真机日志？

1. 小米运动健康与手表同步
2. 在手表上复现问题
3. 【小米运动健康】-->【我的】-->【关于】-->【Debug】-->【拉取固件日志】
4. 日志保存在: `/sdcard/Android/data/com.mi.health/files/log`

### Q8: npm安装依赖失败？

```bash
# 创建 .npmrc 文件，内容如下：
registry="https://registry.npmmirror.com/"

# 然后重新运行
npm i
```

### Q9: Windows下openssl缺失？

1. 安装openssl并配置系统环境变量
2. 重启电脑
3. 验证安装: 在终端输入 `openssl`

---

## 多设备适配要点

### 1. 设备屏幕参数

| 设备类型 | 设备型号 | 屏幕形状 | 分辨率 | 屏幕宽度DP | 长宽比 |
|----------|----------|----------|--------|------------|--------|
| 手表 | Xiaomi Watch S1 Pro | 圆形 | 480x480 | 240 | 1 |
| 手表 | Xiaomi Watch H1 | 圆形 | 466x466 | 233 | 1 |
| 手表 | Xiaomi Watch S3 | 圆形 | 466x466 | 233 | 1 |
| 手表 | Xiaomi Watch S4 | 圆形 | 466x466 | 233 | 1 |
| 手表 | REDMI Watch 5 | 矩形 | 432x514 | 216 | 0.8 |
| 手环 | 小米手环8 Pro | 矩形 | 336x480 | 168 | 0.7 |
| 手环 | 小米手环9 | 胶囊形 | 192x490 | 96 | 0.4 |
| 手环 | 小米手环10 | 胶囊形 | 212x520 | 106 | 0.4 |

### 2. 自适应布局

使用Flex弹性布局实现屏幕自适应：

```html
<div>
  <text style="flex-grow: 1; background-color: aqua;">1</text>
  <text style="flex-grow: 1; background-color: yellow;">2</text>
  <text style="flex-grow: 1; background-color: red;">3</text>
</div>
```

### 3. CSS 限制

Vela 不支持以下 CSS 特性：

| 不支持 | 说明 | 替代方案 |
|--------|------|----------|
| 后代选择器 `.a .b {}` | 无法使用 | 直接使用 class |
| 子选择器 `.a > .b {}` | 无法使用 | 直接使用 class |
| 兄弟选择器 `.a + .b {}` | 无法使用 | 直接使用 class |
| 属性选择器 `[attr] {}` | 无法使用 | 直接使用 class |
| 通用选择器 `* {}` | 无法使用 | 逐个指定 class |
| 伪类 `:hover` `:active` `:focus` | 不支持 | 使用点击事件替代 |
| 伪元素 `::before` `::after` | 不支持 | 使用实际元素 |

**支持的 CSS 特性：**
- class 选择器
- Flexbox 布局 (display: flex)
- 基础属性 (width, height, padding, margin, border-radius)
- 文字样式 (font-size, font-weight, color, text-align)
- 背景 (background-color)
- 定位 (position: absolute/relative)

### 4. 自适应单位

#### px 单位

在manifest中配置designWidth，系统自动按比例缩放：

```json
{
  "config": {
    "designWidth": 336
  }
}
```

#### 百分比 %

```html
<text style="width: 20%">20%</text>
<text style="width: 40%">40%</text>
```

### 4. 固定单位 dp

保持元素在不同屏幕上物理尺寸一致：

```html
<text style="width: 116dp; height: 30dp">固定尺寸</text>
```

### 5. 媒体查询

根据屏幕形状应用不同样式：

```css
/* 圆形屏幕 */
@media screen and (shape: circle) {
  .container {
    padding-left: 80px;
    flex-direction: row;
  }
}

/* 矩形屏幕 */
@media screen and (shape: rect) {
  .container {
    padding-top: 50px;
    flex-direction: column;
  }
}
```

### 6. 获取屏幕信息

```javascript
import device from '@system.device'

device.getInfo({
  success: function(ret) {
    console.log(ret.screenShape)  // 'circle', 'rect', 'pill-shaped'
    console.log(ret.screenWidth)  // 屏幕宽度
    console.log(ret.screenHeight) // 屏幕高度
  }
})
```

### 7. 多屏适配最佳实践

1. **使用designWidth配置设计稿基准宽度**
2. **优先使用Flex布局和百分比**
3. **关键元素使用dp固定尺寸**
4. **使用媒体查询适配不同屏幕形状**
5. **使用IDE的多屏模拟器预览效果**

---

## 附录

### manifest.json 完整配置示例

```json
{
  "package": "com.example.demo",
  "name": "示例应用",
  "icon": "/Common/icon.png",
  "versionName": "1.0",
  "versionCode": 1,
  "minAPILevel": 1,
  "deviceTypeList": ["watch"],
  "features": [
    { "name": "system.fetch" },
    { "name": "system.storage" },
    { "name": "system.network" }
  ],
  "config": {
    "logLevel": "log",
    "designWidth": 466
  },
  "router": {
    "entry": "index",
    "pages": {
      "index": {
        "component": "index",
        "path": "/"
      },
      "detail": {
        "component": "detail"
      }
    }
  },
  "display": {
    "backgroundColor": "#ffffff"
  }
}
```

### API Level 参考

| API Level | 版本说明 |
|-----------|----------|
| API Level 1 | 基础版本 |
| API Level 2 | 新增特性 |
| API Level 3 | 新增特性 |
| API Level 4 | 新增特性 |

---

**文档版本**: 1.0  
**更新时间**: 2026-03-16  
**官方文档**: https://iot.mi.com/vela/quickapp/zh/
