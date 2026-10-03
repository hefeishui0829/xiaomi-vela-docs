# a

## 概述

超链接（默认不带下划线）

## 子组件

仅支持[`<span>`](span.md)

## 属性

支持[通用属性](../general/properties.md)

名称 | 类型 | 默认值 | 必填 | 描述 
---|:---:|---|:---:|--- 
href | `string` |:---:| 否 | 支持的格式参见[页面路由](../../features/basic/router.md)中的 uri 参数。 
额外的： 
href 还可以通过“?param1=value1”的方式添加参数，参数可以在页面中通过`this.param1`的方式使用。使用`this.param1`变量时，需要在目标页面中在 `public`（应用外传参）或 `protected`（应用内传参）下定义 key 名相同的属性 
示例： 
`<a href="/about?param1=value1">关于</a>` 
 
## 样式

支持[text样式](text.md)

支持[通用样式](../general/style.md)

## 事件

支持[通用事件](../general/events.md)

## 示例代码
```html
<template>
 <div>
 <a class="link" href="/home">goHome</a>
 <a href="/home">
 <span class="link">使用span子组件</span>
 </a>
 </div>
</template>
``` 
