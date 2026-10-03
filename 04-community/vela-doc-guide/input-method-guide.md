# Vela 输入法组件开发指南

> 基于 [Vela_input_method](https://github.com/NEORUAA/Vela_input_method) (MIT License)
> 本文档采用 CC BY-SA 4.0 许可证

## 目录

1. [组件概述](#1-组件概述)
2. [实现原理](#2-实现原理)
3. [安装使用方法](#3-安装使用方法)
4. [API参考](#4-api参考)
5. [使用示例](#5-使用示例)
6. [注意事项](#6-注意事项)
7. [常见问题](#7-常见问题)

---

## 1. 组件概述

### 1.1 基本信息

| 项目 | 说明 |
|------|------|
| 组件名称 | `input-method` |
| 源码位置 | `components/InputMethod/InputMethod.ux` |
| 适用平台 | Vela（小米穿戴应用） |

### 1.2 功能特性

- 多语言支持：中文（拼音输入）、英文、数字符号输入
- 多种键盘布局：`QWERTY` 全键盘布局、`T9` 九键布局
- 多屏幕适配：`circle`（圆屏）、`rect`（方屏）、`pill-shaped`（胶囊屏）
- 智能候选词：基于 6763 个常用汉字的拼音匹配
- 震动反馈：支持长振动、短振动模式
- 大小写切换：英文输入时支持大小写切换

### 1.3 适用设备

| 设备类型 | `screentype` | `designWidth` |
|----------|--------------|---------------|
| 圆屏 | `circle` | 480 |
| 方屏 | `rect` | ≥336 |
| 胶囊屏 | `pill-shaped` | ≥192 |

---

## 2. 实现原理

### 2.1 整体架构

组件由以下部分组成：

```
InputMethod/
├── InputMethod.ux      # 主组件文件
└── assets/
    ├── dic.js          # 词典文件
    ├── dicUtil.js      # 拼音匹配工具
    ├── full/           # 圆屏全键盘图片
    ├── t9/            # 圆屏九键图片
    ├── horizontal/    # 方屏图片
    └── arc/           # 胶囊屏图片
```

### 2.2 词典机制

#### `dic.js`

词典文件收录了 6763 个常用汉字，按使用频率排序，支持多音字。

#### `dicUtil.js`

提供 `SimpleInputMethod` 模块进行拼音匹配：

```javascript
// 初始化词典
SimpleInputMethod.initDict(dicData);

// 获取汉字候选列表
SimpleInputMethod.getHanzi('ni'); // 返回: ['你', '尼', '拟', ...]
```

采用**最长前缀匹配策略**：从最长 6 个字符开始递减尝试匹配。

### 2.3 UI 渲染机制

| 屏幕类型 | 尺寸 | 布局特点 |
|---------|------|----------|
| `circle` | 480x321px | 圆屏专用布局 |
| `rect` | 100%x255px | 方屏横向滚动 |
| `pill-shaped` | 100%x305px | 胶囊屏弧形指示器 |

### 2.4 状态管理

核心状态变量：

| 状态 | 说明 |
|------|------|
| `cval` | 当前输入的拼音串 |
| `resultList` | 候选词列表 |
| `lang` | 当前语言模式 |
| `numFlag` | 是否为数字模式 |
| `upperFlag` | 是否为大写模式 |

---

## 3. 安装使用方法

### 3.1 手动安装

```bash
# 1. 下载项目
git clone https://github.com/NEORUAA/Vela_input_method.git

# 2. 拷贝 components 文件夹到目标项目的 src 目录
cp -r Vela_input_method/components /your-project/src/
```

### 3.2 在页面中引用

```html
<import name="input-method" src="../../components/InputMethod/InputMethod.ux"></import>
```

### 3.3 项目集成示例

参见第 5 节使用示例

---

## 4. API 参考

### 4.1 属性（Props）

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
|--------|------|--------|------|------|
| `hide` | `boolean` | `true` | 是 | 控制键盘显示/隐藏 |
| `keyboardtype` | `string` | `"QWERTY"` | 否 | 键盘布局类型 |
| `maxlength` | `number` | `5` | 否 | 候选词数量 |
| `vibratemode` | `string` | `""` | 否 | 震动模式 |
| `screentype` | `string` | `"circle"` | 否 | 屏幕类型 |

#### `keyboardtype` 取值

| 值 | 说明 |
|----|------|
| `QWERTY` | 全键盘布局 |
| `T9` | 九键布局（胶囊屏不支持） |

#### `vibratemode` 取值

| 值 | 说明 |
|----|------|
| `""` | 不震动 |
| `"long"` | 长振动 |
| `"short"` | 短振动 |

#### `screentype` 取值

| 值 | 说明 |
|----|------|
| `circle` | 圆屏 |
| `rect` | 方屏 |
| `pill-shaped` | 胶囊屏 |

### 4.2 事件（Events）

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `complete` | `{ detail: { content: string } }` | 选中候选词时触发 |
| `delete` | - | 删除字符时触发 |
| `keyDown` | `{ detail: { content: string } }` | 按键时触发 |
| `visibilityChange` | `{ detail: { visible: boolean } }` | 显示状态变化时触发 |

---

## 5. 使用示例

### 5.1 基础用法

```html
<import name="input-method" src="../../components/InputMethod/InputMethod.ux"></import>

<template>
  <div class="container">
    <text>{{inputText}}</text>
    <input-method
      hide="{{keyboardVisible}}"
      keyboardtype="QWERTY"
      maxlength="5"
      vibratemode="short"
      screentype="circle"
      @complete="onComplete"
      @delete="onDelete"
    ></input-method>
  </div>
</template>

<script>
export default {
  private: {
    inputText: "",
    keyboardVisible: false
  },

  onComplete(evt) {
    this.inputText += evt.detail.content;
  },

  onDelete() {
    this.inputText = this.inputText.slice(0, -1);
  }
};
</script>
```

### 5.2 方屏九键

```html
<input-method
  hide="{{hide}}"
  keyboardtype="T9"
  screentype="rect"
  maxlength="6"
></input-method>
```

### 5.3 不同屏幕配置

| 设备类型 | 配置 |
|----------|------|
| 圆屏 | `{ screentype: 'circle', keyboardtype: 'QWERTY', maxlength: 5 }` |
| 方屏 | `{ screentype: 'rect', keyboardtype: 'T9', maxlength: 6 }` |
| 胶囊屏 | `{ screentype: 'pill-shaped', keyboardtype: 'QWERTY', maxlength: 4 }` |

---

## 6. 注意事项

### 6.1 屏幕适配

确保根据实际设备设置正确的 `screentype` 属性。**胶囊屏仅支持 `QWERTY` 全键盘布局**。

### 6.2 性能优化

组件使用 `if` 条件渲染处理大量候选词列表，**避免使用 `show`**。

```html
<!-- 推荐 -->
<input if="{{showKeyboard}}" ...></input>

<!-- 不推荐 -->
<input show="{{showKeyboard}}" ...></input>
```

### 6.3 使用限制

- 胶囊屏不支持 `T9` 九键布局
- 仅支持 6763 个常用汉字
- 不支持声调

### 6.4 资源文件结构

```
assets/
├── full/           # 圆屏全键盘图片 (QWERTY)
├── t9/             # 圆屏九键图片 (T9)
├── horizontal/     # 方屏图片
└── arc/            # 胶囊屏图片
```

---

## 7. 常见问题

**Q1: 如何隐藏/显示键盘？**

```javascript
// 隐藏
this.hide = true;

// 显示
this.hide = false;
```

**Q2: 如何获取用户输入的字符？**

```javascript
onComplete(evt) {
  // evt.detail.content 为用户选中的字符
  this.inputText += evt.detail.content;
}
```

**Q3: 候选词数量太少？**

调整 `maxlength` 属性：

```html
<input-method maxlength="10"></input-method>
```

**Q4: 胶囊屏无法使用九键？**

这是设计限制，胶囊屏仅支持 `QWERTY` 全键盘。

**Q5: 输入拼音后没有候选词？**

1. 确认使用内置词典中的汉字（6763 个常用汉字）
2. 检查 `lang` 属性是否为 `cn`
3. 确认 `numFlag` 为 `false`

**Q6: 如何实现自定义候选词？**

需要修改 `dic.js` 词典文件，添加自定义词汇。

---

## 附录

### A. 词典覆盖范围

6763 个常用汉字，涵盖 GB2312 一二级汉字及常用异体字和多音字。

### B. 键盘布局

**圆屏全键盘：**
```
W E R T Y U I O
S D F G H J K
X C V B N M
```

**圆屏九键：**
```
abc  def  ghi
jkl  mno  pqrs
tuv  wxyz
```

**方屏全键盘：**
```
Q W E R T Y U I O P
A S D F G H J K L
Z X C V B N M
```

---

> 文档版本: 1.0  
> 最后更新: 2024年  
> 组件来源: [Vela_input_method](https://github.com/NEORUAA/Vela_input_method)
