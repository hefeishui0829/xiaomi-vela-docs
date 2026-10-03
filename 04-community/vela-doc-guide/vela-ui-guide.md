# Vela 应用 UI 开发指南

> 基于实际项目（弦电子书）提取的通用UI设计规范，适用于各类Vela手表应用开发

---

## ⚡ 快速参考（AI开发必读）

### 标准页面结构
```
背景:#000000
├── hd.png (336x102, 顶部状态栏)
├── back.png (72x72, 6,6, 返回按钮)
├── 标题 (32px bold white, 78,35)
├── list (padding: 86px 6px)
└── bt.png (336x102, 底部操作栏, 可选)
```

### 列表项样式
```
.item {
  height: 112px;
  background: #262626;
  border-radius: 36px;
  padding: 14px 20px;
  margin-bottom: 8px;
}
```

### 文字样式
```
主标题: font-size: 32px; font-weight: bold; color: white;
副标题: font-size: 28px; font-weight: bold; color: rgba(255,255,255,0.6);
```

### 颜色
```
背景: #000000 | 卡片: #262626 | 强调: #0D6EFF | 文字: #FFFFFF
```

---

## 1. 设计规范速查表

### 1.1 屏幕与布局基础

| 属性 | 值 | 说明 |
|------|-----|------|
| 屏幕宽度 | 336px | 应用固定宽度 |
| 屏幕高度 | 480px | 应用固定高度 |
| 状态栏区域 | 102px (hd.png) | 顶部固定高度 |
| 底部操作栏 | 102px (bt.png) | 底部固定高度 |
| 侧边距 | 6px | 左右安全边距 |
| 列表区域内边距 | 86px 6px | 避开顶部状态栏 |

### 1.2 颜色系统

```
主色板:
├── 纯黑背景      #000000
├── 深灰卡片      #262626  
├── 强调蓝色      #0D6EFF (选中状态)
└── 警告红色      #ad0000 (存储不足提示)

文字颜色:
├── 纯白          #FFFFFF
├── 次级白        rgba(255,255,255,0.6)  (60%)
├── 辅助灰        rgba(255,255,255,0.4)  (40%)
└── 禁用灰        rgba(255,255,255,0.5)  (50%)

特殊颜色:
└── 章节标题灰    #aaa / #666
```

### 1.3 字体层级

```css
/* 页面主标题 - 时间上方 */
font-size: 24px;
line-height: 32px;
font-weight: bold;
color: rgba(255,255,255,0.6);

/* 页面大标题 - 状态栏下方 */
font-size: 32px;
line-height: 42px;
font-weight: bold;
color: white;

/* 列表项主标题 */
font-size: 32px;
font-weight: bold;
color: white;

/* 列表项副标题 */
font-size: 28px;
font-weight: bold;
color: rgba(255,255,255,0.6);

/* 阅读内容 - 默认 */
font-size: 30px;
line-height: 34px;
font-weight: bold;

/* 辅助说明文字 */
font-size: 20-24px;
line-height: 28px;
color: rgba(255,255,255,0.5);
```

### 1.4 间距系统 (px)

```
间距命名   值    用途
─────────────────────────────────────
xs        2-4   极小间距
s         6     基础边距
m         10-14 组件内边距
l         20    列表项内边距
xl        24    区块间距
xxl       36-48 大间距/圆角
─────────────────────────────────────
```

### 1.5 组件尺寸

```
组件              宽      高     圆角
────────────────────────────────────
页面容器         336     480     -
列表项           100%    112     36px
按钮图标         72      72      -
开关(小)         60      42      -
开关(大)         102     72      -
输入框           324     182     36px
数字选择器       324     72      -
封面图           64      84      8px
────────────────────────────────────
```

### 1.6 行高计算公式

```javascript
// 根据字号动态计算行高
lineHeight = parseInt(-0.01 * (fontSize ** 2) + 1.62 * fontSize - 3.23);

// 示例值:
// fontSize=20 → lineHeight=28
// fontSize=26 → lineHeight=30  
// fontSize=30 → lineHeight=34
// fontSize=40 → lineHeight=38
// fontSize=50 → lineHeight=40
```

---

## 2. 完整代码模板

### 2.1 基础页面骨架

```html
<!-- 标准页面模板 (336x480) -->
<template>
  <div class="page" style="flex-direction: column;">
    
    <!-- 列表内容区域 -->
    <list class="list">
      <list-item class="item" @click="handleClick" type="item">
        <div class="item-content">
          <text class="itemtext">主标题</text>
          <text class="itemtext2">副标题</text>
        </div>
        <img src="/common/images/enter.png" class="arrow" static/>
      </list-item>
    </list>

    <!-- 顶部状态栏 -->
    <img static src="/common/images/hd.png" 
         style="position: absolute;left: 0px;top: 0px;width: 336px;height: 102px;" />
    
    <!-- 顶部按钮 -->
    <img static src="/common/images/back.png" @click="back" 
         style="position: absolute;left: 6px;top: 6px;width: 72px;height: 72px;"/>
    <img static src="/common/images/more.png" @click="openMenu" 
         style="position: absolute;left: 258px;top: 6px;width: 72px;height: 72px;"/>
    
    <!-- 顶部标题 -->
    <text style="position: absolute;left: 78px;top: 7px;width: 180px;
                 line-height: 32px;font-weight:bold;font-size:24px;
                 color:rgba(255,255,255,0.6);text-align:center;">
      {{nowTime}}
    </text>
    <text static style="position: absolute;left: 78px;top: 35px;width: 180px;
                 line-height: 42px;font-weight:bold;font-size:32px;
                 color:white;text-align:center;">
      页面标题
    </text>
  </div>
</template>

<script>
import router from '@system.router'
import storage from '../../utils/storage.js'

export default {
  private: {
    nowTime: "00:00",
    timer: null,
    timeFormat: '24h'
  },

  onInit() {
    this.loadSettings();
    this.timer = setInterval(() => { this.updateTime(); }, 60000);
  },

  onDestroy() {
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
  },

  loadSettings() {
    storage.get({
      key: 'EBOOK_TIME_FORMAT',
      success: (data) => {
        if (data) this.timeFormat = data;
        this.updateTime();
      },
      fail: () => this.updateTime()
    });
  },

  updateTime() {
    const date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    if (this.timeFormat === '12h') {
      let ampm = hours >= 12 ? '下午' : '上午';
      hours = hours % 12;
      hours = hours ? hours : 12;
      minutes = minutes < 10 ? '0' + minutes : minutes;
      this.nowTime = `${ampm} ${hours}:${minutes}`;
    } else {
      hours = hours < 10 ? '0' + hours : hours;
      minutes = minutes < 10 ? '0' + minutes : minutes;
      this.nowTime = `${hours}:${minutes}`;
    }
  },

  back() { router.back(); }
}
</script>

<style>
@import '../../common/style.css';
</style>
```

### 2.2 公共样式文件 (style.css)

```css
/* 页面容器 */
.page {
  width: 336px;
  height: 480px;
  background-color: #000000;
}

/* 列表容器 */
.list {
  width: 336px;
  height: 480px;
  position: absolute;
  top: 0px;
  left: 0px;
  padding: 86px 6px;
}

/* 列表项 */
.item {
  width: 100%;
  height: 112px;
  padding: 14px 20px;
  margin-bottom: 8px;
  background-color: #262626;
  border-radius: 36px;
  justify-content: space-around;
  align-items: center;
}

/* 选中状态 */
.item2 {
  background-color: #0D6EFF !important;
}

/* 列表项内容容器 */
.item-content {
  width: 100%;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  flex: 1;
  height: 100%;
  overflow: hidden;
}

/* 主标题 */
.itemtext {
  font-size: 32px;
  width: 100%;
  font-weight: bold;
  color: white;
  text-overflow: ellipsis;
  lines: 1;
}

/* 副标题 */
.itemtext2 {
  font-size: 28px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.6);
  text-overflow: ellipsis;
  lines: 1;
}

/* 图标尺寸 */
.arrow {
  width: 48px;
  height: 48px;
}

.switch {
  width: 60px;
  height: 42px;
}

.switch2 {
  width: 102px;
  height: 72px;
}

/* 预览区域 */
.preview-item {
  position: absolute;
  left: 6px;
  top: 86px;
  width: 324px;
  height: 308px;
  padding: 24px 18px;
  border: #262626 4px;
  border-radius: 36px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

### 2.3 列表项选中状态切换

```html
<!-- 模板中使用 -->
<list-item class="item {{isSelected ? 'item2' : ''}}" @click="selectItem">
  <div class="item-content">
    <text class="itemtext">选项名称</text>
    <text class="itemtext2">选项描述</text>
  </div>
  <img if="{{isSelected}}" src="/common/images/check.png" 
       style="width:40px;height: 40px;" static />
</list-item>
```

### 2.4 开关按钮模板

```html
<list-item class="item" @click="toggleSetting">
  <div class="item-content">
    <text class="itemtext">设置名称</text>
    <text class="itemtext2">设置描述</text>
  </div>
  <img src="{{isEnabled ? '/common/images/Switch_ON.png' : '/common/images/Switch_OFF.png'}}" 
       class="switch"/>
</list-item>
```

### 2.5 带底部数字选择器的页面

```html
<template>
  <div class="page" style="flex-direction: column;">
    <list class="list">
      <!-- 设置项列表 -->
    </list>
    
    <img src="/common/images/bt.png" 
         style="position: absolute;left: 0px;top: 378px;width: 336px;height: 102px;" />
    <number style="position: absolute;bottom:6px" 
            max.static="100" min.static="1" step.static="1" 
            value="{{currentValue}}" @change="onChange" 
            name.static="设置名称"></number>
  </div>
</template>
```

---

## 3. 素材资源清单

### 3.1 通用图标 (src/common/images/)

| 文件名 | 尺寸 | 用途 |
|--------|------|------|
| hd.png | 336x102 | 顶部状态栏背景 |
| bt.png | 336x102 | 底部操作栏背景 |
| back.png | 72x72 | 返回按钮 |
| more.png | 72x72 | 更多/菜单按钮 |
| enter.png | 48x48 | 进入/箭头图标 |
| check.png | 40x40 | 选中勾选 |
| Switch_ON.png | 60x42 | 开关开 |
| Switch_OFF.png | 60x42 | 开关关 |
| plus.png | 72x72 | 加号/增加 |
| minis.png | 72x72 | 减号/减少 |
| search.png | 72x72 | 搜索按钮 |
| search_shadow.png | - | 搜索按钮阴影 |
| reset.png | 72x72 | 重置按钮 |
| pre.png | 72x72 | 上一页 |
| next.png | 72x72 | 下一页 |
| add_bookmark.png | 72x72 | 添加书签 |
| brightness.png | 72x72 | 亮度图标(开) |
| brightness_off.png | 72x72 | 亮度图标(关) |
| empty.png | 128x128 | 空状态图标 |
| push.png | 72x72 | 推送/同步按钮 |
| about_bg.png | - | 关于页面背景 |
| delete.png | - | 删除图标 |
| edit.png | - | 编辑图标 |
| info.png | - | 信息图标 |
| bin.png | - | 垃圾桶图标 |

### 3.2 输入法组件 (src/components/InputMethod/assets/)

```
InputMethod/
├── full/     全键盘 (26字母+数字+符号)
├── t9/       T9键盘
├── horizontal/  横屏键盘
└── arc/      弧形键盘
```

### 3.3 数字键盘 (src/common/images/num_pad/)

```
num_pad/
├── 0.png ~ 9.png  数字按键
└── del.png        删除按键
```

---

## 4. 关键实现技巧

### 4.1 时间显示 (支持12/24小时制)

```javascript
updateTime() {
  const date = new Date();
  let hours = date.getHours();
  let minutes = date.getMinutes();
  
  if (this.timeFormat === '12h') {
    let ampm = hours >= 12 ? '下午' : '上午';
    hours = hours % 12;
    hours = hours ? hours : 12;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    this.nowTime = `${ampm} ${hours}:${minutes}`;
  } else {
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    this.nowTime = `${hours}:${minutes}`;
  }
}
```

### 4.2 文字过长滚动效果 (Marquee)

```html
<!-- 启用跑马灯效果 -->
<marquee scrollamount="22" class="itemtext" text-offset="25">
  {{longText}}
</marquee>

<!-- 禁用时使用普通文本 -->
<text else class="itemtext">{{shortText}}</text>
```

### 4.3 数字选择器组件使用

```html
<!-- 引入组件 -->
<import name="number" src="../../components/number_choose/number_choose"></import>

<!-- 使用 -->
<number style="position: absolute;bottom:6px" 
        max.static="50" min.static="20" step.static="1" 
        value="{{fontSize}}" @change="onFontSizeChange" 
        name.static="当前字号"></number>
```

### 4.4 分页列表实现

```javascript
// 数据
visibleItems: [],
currentPage: 0,
pageSize: 6,
allItems: [],

// 加载分页
loadPage(page) {
  const start = page * this.pageSize;
  this.visibleItems = this.allItems.slice(start, start + this.pageSize);
  this.currentPage = page;
},

// 计算总页数
get totalPages() {
  return Math.ceil(this.allItems.length / this.pageSize) || 1;
}
```

```html
<!-- 分页控件 -->
<list-item type="pagination" class="pagination-container" if="{{totalPages > 1}}">
  <div class="pagination-controls">
    <img src="/common/images/pre.png" if="{{currentPage > 0}}" 
         @click="prevPage" class="pagination-button"/>
    <text class="pagination-text">{{currentPage + 1}} / {{totalPages}}</text>
    <img src="/common/images/next.png" if="{{currentPage < totalPages - 1}}" 
         @click="nextPage" class="pagination-button"/>
  </div>
</list-item>
```

```css
.pagination-container {
  width: 100%;
  height: 80px;
  background-color: transparent;
  justify-content: center;
  align-items: center;
}

.pagination-controls {
  width: 100%;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  padding: 0 8px;
}

.pagination-button {
  width: 72px;
  height: 72px;
}

.pagination-text {
  font-size: 28px;
  font-weight: bold;
  color: white;
}
```

### 4.5 设置存储与读取

```javascript
// 存储设置
storage.set({
  key: 'SETTING_KEY',
  value: this.settingValue.toString()
});

// 读取设置
storage.get({
  key: 'SETTING_KEY',
  success: (data) => {
    if (data) this.settingValue = data;
  },
  fail: () => {
    this.settingValue = 'default';
  }
});
```

### 4.6 页面间参数传递

```javascript
// 跳转时传递参数
router.push({
  uri: '/pages/detail',
  params: { name: bookDirName }
});

// 目标页面接收
export default {
  protected: {
    name: ''  // 通过 protected 接收
  },
  
  onInit() {
    console.log(this.name); // 获取传递的参数
  }
}
```

---

## 5. AI开发代码片段库

### 5.1 设置页面快速生成

```javascript
// 生成设置项的通用模式
const settingItems = [
  { key: 'SETTING_KEY', title: '设置名称', subtitle: '设置描述', default: 'default' },
  // 添加更多...
];

// 批量加载
loadSettings() {
  settingItems.forEach(item => {
    storage.get({
      key: item.key,
      success: (data) => {
        this[item.key] = data || item.default;
      }
    });
  });
}
```

### 5.2 列表项组件模板

```html
<!-- 标准列表项 -->
<list-item class="item {{isActive ? 'item2' : ''}}" 
           @click="onItemClick($item)" type="item">
  <div class="item-content">
    <text class="itemtext">{{$item.title}}</text>
    <text class="itemtext2">{{$item.subtitle}}</text>
  </div>
  <img if="{{isActive}}" src="/common/images/check.png" 
       style="width:40px;height: 40px;" static />
</list-item>
```

### 5.3 阅读器内容区域模板

```html
<scroll scroll-y="{{true}}" 
        style="position: absolute;width: 336px;
               height: {{480 - verticalMargin * 2}}px;
               top: {{verticalMargin}}px;">
  <div style="width: 336px; flex-direction: column;">
    <text style="width: 336px; 
                 text-align: left; 
                 color: rgba(255,255,255,{{opacity/100}}); 
                 font-size: {{fontSize}}px; 
                 font-weight: {{boldEnabled ? 'bold' : 'normal'}}; 
                 line-height: {{lineHeight}}px;">
      {{content}}
    </text>
  </div>
</scroll>
```

### 5.4 警告/提示条

```html
<list-item type="tip" class="item warning-item">
  <text class="itemtext" style="lines: 2;font-size: 24px;line-height:32px;">
    警告提示内容
  </text>
</list-item>

<!-- 样式 -->
.warning-item {
  background-color: #ad0000;
  padding: 2px 20px;
}
```

### 5.5 封面列表项 (书架模式)

```html
<list-item type="book" class="item cover-item">
  <img if="{{hasCover}}" class="cover-image" 
       src="internal://files/books/{{dirName}}/{{coverFileName}}" />
  <div class="text-content">
    <marquee if="{{marqueeEnabled}}" scrollamount="22" 
             class="itemtext" text-offset="25">{{bookName}}</marquee>
    <text else class="itemtext">{{bookName}}</text>
    <text class="itemtext2">{{progressText}}</text>
  </div>
</list-item>

<style>
.cover-item {
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
}
.cover-image {
  width: 64px;
  height: 84px;
  background-color: #333;
  margin-right: 16px;
  border-radius: 8px;
  flex-shrink: 0;
}
.text-content {
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  flex: 1;
  height: 100%;
  overflow: hidden;
}
</style>
```

---

## 6. 与系统Vela组件的差异

### 6.1 自定义组件封装

| 组件 | 自定义实现 | 说明 |
|------|-----------|------|
| 数字选择器 | number_choose | 替代系统picker，支持加减按钮 |
| 输入法 | InputMethod | 自定义T9/全键盘/横屏键盘 |
| 进度条 | 自定义progress | 底部进度条组件 |

### 6.2 特殊布局模式

1. **双层状态栏**: 使用hd.png作为顶部背景，配合实际内容实现状态栏效果
2. **底部固定栏**: 使用bt.png实现底部操作区域
3. **全屏列表**: list组件配合absolute定位实现内容滚动区

### 6.3 交互差异

- 使用`onlongpress`替代原生长按事件
- 使用`@click`处理点击，`@touchstart/move/end`处理手势
- 自定义翻页逻辑（章节切换、滑动等）

---

## 7. 动画与交互分析

### 7.1 翻页动画

阅读器支持多种翻页模式:

```javascript
// 章节切换样式
chapterSwitchStyle: 'button' | 'boundary' | 'swipe'

// 按钮模式 - 章节首尾显示"上一章/下一章"按钮
// 越界模式 - 滚动到章节首尾后继续滑动触发换章
// 滑动模式 - 左右滑动触发换章 (需设置swipeSensitivity)
```

### 7.2 点击反馈

- 列表项: 通过`item2` class切换背景色(#0D6EFF)提供选中反馈
- 开关: 切换Switch_ON.png/Switch_OFF.png图片
- 图标按钮: 无额外动画，依靠页面切换提供反馈

### 7.3 跑马灯效果

```html
<marquee scrollamount="22" text-offset="25">长文本内容</marquee>
<!-- scrollamount: 滚动速度 -->
<!-- text-offset: 滚动留白 -->
```

---

## 8. 多设备适配详解

> 本节基于电子书阅读器项目，分析其多设备适配方案

### 8.1 设备类型与屏幕参数

| 设备类型 | deviceType | designWidth | 屏幕分辨率 | 屏幕形状 | 典型设备 |
|----------|------------|-------------|------------|----------|----------|
| 方屏手环 | watch | 336 | 336×480 | rect | 小米手环8Pro/9Pro |
| 胶囊屏手表 | watch | 192 | 390×312 | pill-shaped | REDMI Watch 5/6 |
| 圆形表盘 | watch | 480 | 454×454 | circle | 圆形手表 |

### 8.2 manifest.json 配置

```json
{
  "package": "com.example.app",
  "name": "AppName",
  "deviceTypeList": ["watch"],
  "config": {
    "designWidth": 336
  },
  "features": [
    { "name": "system.device" }
  ]
}
```

### 8.3 获取设备信息

```javascript
import device from '@system.device'

export default {
  private: {
    screenShape: 'rect',
    screenWidth: 336,
    screenHeight: 480
  },
  
  onInit() {
    device.getInfo({
      success: (ret) => {
        this.screenShape = ret.screenShape  // 'circle', 'rect', 'pill-shaped'
        this.screenWidth = ret.screenWidth
        this.screenHeight = ret.screenHeight
      }
    })
  }
}
```

### 8.4 条件渲染适配

使用 `if` 条件渲染不同屏幕的UI：

```html
<template>
  <div class="page">
    <!-- 圆屏布局 -->
    <div if="{{screenShape === 'circle'}}">
      <text>圆屏专用内容</text>
    </div>
    
    <!-- 方屏/胶囊屏布局 -->
    <div else>
      <text>方屏/胶囊屏内容</text>
    </div>
  </div>
</template>
```

### 8.5 媒体查询适配

```css
/* 圆屏 */
@media screen and (shape: circle) {
  .container {
    padding-left: 80px;
  }
}

/* 方屏 */
@media screen and (shape: rect) {
  .container {
    padding-top: 50px;
  }
}

/* 胶囊屏 */
@media screen and (shape: pill-shaped) {
  .container {
    padding-top: 30px;
  }
}
```

### 8.6 设计宽度 (designWidth) 适配

```json
// manifest.json - 针对不同基准设计
{
  "config": {
    "designWidth": 336  // 方屏基准
  }
}
```

系统会自动将 CSS 中的尺寸数值按比例转换到目标设备。

### 8.7 百分比与 Flex 适配

```html
<!-- 推荐：使用百分比和 flex-grow 自动适应 -->
<div style="width: 100%; flex-direction: column;">
  <div style="flex-grow: 1;">
    自适应内容区
  </div>
</div>

<!-- 不推荐：固定像素值 -->
<div style="width: 336px;">
```

### 8.8 电子书 App 适配示例

```html
<template>
  <div class="page">
    <!-- 顶部状态栏 - 圆屏调整位置 -->
    <img if="{{screenShape === 'circle'}}" 
          static src="/common/images/hd.png" 
          style="position: absolute; left: 13px; top: 0px; width: 454px; height: 116px;" />
    <img else static src="/common/images/hd.png" 
          style="position: absolute; left: 0px; top: 0px; width: 336px; height: 102px;" />
    
    <!-- 返回按钮 - 圆屏调整 -->
    <img if="{{screenShape === 'circle'}}"
          static src="/common/images/back.png" 
          @click="back" 
          style="position: absolute; left: 19px; top: 6px; width: 72px; height: 72px;"/>
    <img else static src="/common/images/back.png" 
          @click="back" 
          style="position: absolute; left: 6px; top: 6px; width: 72px; height: 72px;"/>
  </div>
</template>
```

### 8.9 适配检查清单

- [ ] manifest.json 配置正确的 designWidth
- [ ] 申请 system.device 权限
- [ ] 使用 device.getInfo() 获取屏幕信息
- [ ] 使用条件渲染 if="{{screenShape === 'xxx'}}" 适配不同屏幕
- [ ] 使用百分比和 Flex 布局而非固定像素
- [ ] 测试方屏、圆屏、胶囊屏三种设备

---

## 9. 完整样式模板

### 9.1 style.css (电子书阅读器风格)

```css
/* 页面容器 */
.page {
  width: 336px;
  height: 480px;
  background-color: #000000;
  position: relative;
}

/* 列表容器 */
.list {
  width: 336px;
  height: 480px;
  position: absolute;
  top: 0px;
  left: 0px;
  padding: 86px 6px;
}

/* 列表项 */
.item {
  width: 100%;
  height: 112px;
  padding: 14px 20px;
  margin-bottom: 8px;
  background-color: #262626;
  border-radius: 36px;
  justify-content: space-around;
  align-items: center;
}

/* 选中状态 */
.item2 {
  background-color: #0D6EFF !important;
}

/* 列表项内容 */
.item-content {
  width: 100%;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  flex: 1;
  height: 100%;
  overflow: hidden;
}

/* 主标题 */
.itemtext {
  font-size: 32px;
  width: 100%;
  font-weight: bold;
  color: white;
  text-overflow: ellipsis;
  lines: 1;
}

/* 副标题 */
.itemtext2 {
  font-size: 28px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.6);
  text-overflow: ellipsis;
  lines: 1;
}

/* 封面列表项 */
.cover-item {
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
}

.cover-image {
  width: 64px;
  height: 84px;
  background-color: #333;
  margin-right: 16px;
  border-radius: 8px;
  flex-shrink: 0;
}

/* 警告项 */
.warning-item {
  background-color: #ad0000;
  padding: 2px 20px;
}

/* 分页控件 */
.pagination-container {
  width: 100%;
  height: 80px;
  background-color: transparent;
  justify-content: center;
  align-items: center;
}

.pagination-controls {
  width: 100%;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  padding: 0 8px;
}

.pagination-button {
  width: 72px;
  height: 72px;
}

.pagination-text {
  font-size: 28px;
  font-weight: bold;
  color: white;
}

/* 搜索浮窗 */
.search-fab-container {
  position: absolute;
  right: 24px;
  bottom: 24px;
  width: 72px;
  height: 72px;
}
```

---

## 附录: 完整颜色变量速查

```css
:root {
  /* 背景色 */
  --bg-primary: #000000;
  --bg-secondary: #262626;
  --bg-accent: #0D6EFF;
  --bg-warning: #ad0000;
  
  /* 文字色 */
  --text-primary: #FFFFFF;
  --text-secondary: rgba(255,255,255,0.6);
  --text-tertiary: rgba(255,255,255,0.4);
  --text-disabled: rgba(255,255,255,0.5);
  
  /* 章节特殊色 */
  --text-chapter-primary: #aaa;
  --text-chapter-secondary: #666;
}
```

---

*文档来源: 弦电子书 (ebook-app)*
*生成时间: 2024年*
