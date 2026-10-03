# Vela UI 快速参考

> 基于弦电子书App的经典UI设计规范

---

## 页面结构
```
┌─────────────────────────────┐
│  [hd.png: 336x102]         │  ← 顶部状态栏
│  [←]     标题      [更多]  │  ← 按钮72x72, 位置(6,6)和(258,6)
├─────────────────────────────┤
│                             │
│       内容区域               │  ← list, padding: 86px 6px
│       (列表/滚动)           │
│                             │
├─────────────────────────────┤
│  [bt.png: 336x102]          │  ← 底部操作栏(可选)
│  [亮度]   进度     [书签]  │
└─────────────────────────────┘
```

## 颜色
| 用途 | 色值 |
|------|------|
| 背景 | `#000000` |
| 卡片/列表项 | `#262626` |
| 强调/选中 | `#0D6EFF` |
| 警告 | `#ad0000` |
| 主文字 | `#FFFFFF` |
| 次级文字 | `rgba(255,255,255,0.6)` |
| 辅助文字 | `rgba(255,255,255,0.4)` |

## 字体
| 元素 | 字号 | 字重 |
|------|------|------|
| 页面标题 | 32px | bold |
| 副标题/时间 | 24px | bold |
| 列表主标题 | 32px | bold |
| 列表副标题 | 28px | bold |
| 阅读器正文 | 30px | bold |

**行高计算**: `lineHeight = -0.01 * fontSize² + 1.62 * fontSize - 3.23`
- fontSize=30 → lineHeight=34
- fontSize=32 → lineHeight=36

## 间距
| 元素 | 值 |
|------|-----|
| 状态栏/底部栏 | 102px高 |
| 左右边距 | 6px |
| 列表区内边距 | 86px 6px |

## 列表项
```css
.item {
  height: 112px;
  background: #262626;
  border-radius: 36px;
  padding: 14px 20px;
  margin-bottom: 8px;
}

.itemtext { font-size: 32px; font-weight: bold; color: white; }
.itemtext2 { font-size: 28px; font-weight: bold; color: rgba(255,255,255,0.6); }
```

## 封面列表
```css
.cover-item { flex-direction: row; align-items: center; }
.cover-img { width: 64px; height: 84px; border-radius: 8px; margin-right: 16px; }
```

## 组件尺寸
| 组件 | 尺寸 |
|------|------|
| 按钮图标 | 72x72px |
| 小开关 | 60x42px |
| 大开关 | 102x72px |
| 封面图 | 64x84px |
| 箭头 | 48x48px |
| 勾选 | 40x40px |
| 分页按钮 | 72x72px |

## 开关按钮
```html
<img src="{{isOn ? '/common/images/Switch_ON.png' : '/common/images/Switch_OFF.png'}}" />
```

## 多设备适配
| 设备 | designWidth | 屏幕 | 类型 |
|------|-------------|------|------|
| 方屏手环 | 336 | 336x480 | rect |
| 胶囊屏 | 192 | 390x312 | pill-shaped |
| 圆屏手表 | 480 | 454x454 | circle |

```javascript
import device from '@system.device';
device.getInfo({
  success: (data) => {
    this.screenShape = data.screenShape; // 'circle', 'rect', 'pill-shaped'
  }
});
```

```html
<!-- 条件渲染适配 -->
<div if="{{screenShape === 'circle'}}">圆屏布局</div>
<div else>方屏/胶囊屏布局</div>
```

## 图标资源
```
hd.png    - 336x102  顶部状态栏
bt.png    - 336x102  底部操作栏
back.png  - 72x72    返回
more.png  - 72x72    更多
enter.png - 48x48    进入箭头
check.png - 40x40    选中勾选
Switch_ON.png  - 60x42  开关开
Switch_OFF.png - 60x42  开关关
pre.png   - 72x72    上一页
next.png  - 72x72    下一页
search.png - 72x72   搜索
empty.png - 128x128  空状态
```

## 标准列表页面模板
```html
<template>
  <div class="page">
    <img static src="/common/images/hd.png" style="position:absolute;left:0;top:0;width:336px;height:102px;" />
    <img static src="/common/images/back.png" @click="back" style="position:absolute;left:6px;top:6px;width:72px;height:72px;"/>
    <text style="position:absolute;left:78px;top:35px;width:180px;font-size:32px;font-weight:bold;color:white;text-align:center;">{{title}}</text>
    <list class="list">
      <list-item class="item" for="{{item in items}}" @click="onItemClick($item)">
        <text class="itemtext">{{item.name}}</text>
        <text class="itemtext2">{{item.subtitle}}</text>
      </list-item>
    </list>
  </div>
</template>

<style>
.page { width: 100%; height: 100%; background-color: #000000; position: relative; }
.list { width: 100%; height: 100%; padding: 86px 6px; position: absolute; top: 0; left: 0; }
.item { width: 100%; height: 112px; padding: 14px 20px; margin-bottom: 8px; background-color: #262626; border-radius: 36px; justify-content: center; }
.itemtext { font-size: 32px; font-weight: bold; color: white; }
.itemtext2 { font-size: 28px; font-weight: bold; color: rgba(255,255,255,0.6); }
</style>

<script>
import router from '@system.router';
export default {
  private: { title: '标题', items: [] },
  onItemClick(item) { console.log(item); },
  back() { router.back(); }
}
</script>
```

---

*来源: 弦电子书 (ebook-app)*
