# Vela复杂应用开发实战教程 - 小米手环电子书阅读器

> 本教程基于 [com.bandbbs.ebook](https://github.com/youshen2/com.bandbbs.ebook) (AGPL-3.0) 编写
> 本文档采用 CC BY-SA 4.0 许可证

## 目录

1. [项目架构概览](#1-项目架构概览)
2. [与传统Web app的关键区别](#2-与传统web-app的关键区别)
3. [核心功能实现思路](#3-核心功能实现思路)
4. [关键代码片段和模式](#4-关键代码片段和模式)
5. [性能优化技巧](#5-性能优化技巧)
6. [常见问题和注意事项](#6-常见问题和注意事项)
7. [开发注意事项/教训](#7-开发注意事项)

---

## 1. 项目架构概览

### 1.1 目录结构

```
com.bandbbs.ebook/
├── src/
│   ├── pages/                    # 页面目录
│   │   ├── index/index.ux         # 书架主页
│   │   ├── detail/detail.ux       # 阅读器核心页面
│   │   ├── textReader/            # 纯文本阅读器
│   │   ├── swipe/                 # 翻页设置
│   │   ├── bookmarks/             # 书签管理
│   │   ├── push/                  # 书籍推送
│   │   └── ...                    # 30+页面
│   ├── utils/                     # 工具类
│   │   ├── storage.js             # 配置存储
│   │   ├── bookStorage.js         # 书架数据管理
│   │   ├── chapterManager.js      # 章节管理
│   │   ├── interconn.js           # 手机-手环互联
│   │   └── ...
│   ├── components/                # 组件
│   ├── i18n/                      # 国际化
│   ├── common/                    # 公共资源
│   │   └── style.css              # 全局样式
│   └── manifest.json              # 应用配置
├── package.json
└── README.md
```

### 1.2 页面架构特点

Vela应用的页面由.ux文件组成，每个文件包含三个部分：

1. template - 视图层
2. script - 逻辑层
3. style - 样式层

### 1.3 核心模块说明

| 模块 | 职责 |
|------|------|
| storage.js | 应用配置存储（字体大小、翻页方式等） |
| bookStorage.js | 书架数据持久化（书籍列表、阅读进度） |
| chapterManager.js | 章节索引管理、缓存 |
| interconn.js | 手机与手环双向通信 |

---

## 2. 与传统Web app的关键区别

> 这是AI开发Vela应用最关键的知识！

### 2.1 文件结构差异

| 特性 | 传统Web | Vela快应用 |
|------|---------|------------|
| 单文件组件 | .vue | .ux |
| 路由配置 | Vue Router | manifest.json |
| 状态管理 | Vuex/Redux | global对象 |
| 打包 | Webpack/Vite | 专用IDE |

### 2.2 关键API差异

#### 2.2.1 存储系统

```javascript
// 传统Web
localStorage.setItem('key', 'value');

// Vela
import storage from '@system.storage';
storage.get({ key: 'EBOOK_FONT', success: (data) => { } });
storage.set({ key: 'EBOOK_FONT', value: '30' });
```

#### 2.2.2 路由系统

```javascript
import router from '@system.router';
router.push({ uri: '/pages/detail', params: { name: 'book1' } });
router.back();
```

#### 2.2.3 文件系统（Vela独有）

```javascript
import file from '@system.file';
file.readText({ uri: 'internal://files/book.txt', success: ... });
file.readArrayBuffer({ uri: 'internal://files/book.txt', position: 0, length: 1000 });
file.writeText({ uri: 'internal://files/output.txt', text: 'content' });
file.list({ uri: 'internal://files/books/', success: ... });
```

### 2.3 数据绑定

Vela使用private/public/protected定义数据：

```javascript
private: { message: 'Hello' }
```

直接修改即可触发更新：

```javascript
this.message = 'World';
```

### 2.4 生命周期

| Vue | Vela | 说明 |
|-----|------|------|
| onLoad | onInit | 初始化 |
| onShow | onShow | 显示 |
| onHide | onHide | 隐藏 |
| onUnload | onDestroy | 销毁 |
| - | onBackPress | 返回键 |

### 2.5 手环特有限制

1. 屏幕尺寸：336x480像素
2. 内存有限：需频繁调用global.runGC()
3. 无DOM：虚拟化组件系统
4. 文件系统：使用internal://files/路径

---

## 3. 核心功能实现思路

### 3.1 电子书解析和分页

#### 3.1.1 文件结构

```
internal://files/books/{bookDir}/
├── lindex.txt        # 索引文件
├── indexes/          # 章节索引
│   └── 1.txt        # 1-100章索引
├── content/         # 章节内容
│   └── 0.txt       # UTF-16 LE编码
└── cover.jpg
```

#### 3.1.2 核心分页逻辑

```javascript
readFileText(readOffset, cb) {
  let length = this.txtSizePage * 2;  // UTF-16每字符2字节
  const maxLength = this.allSize - readOffset;
  if (length > maxLength) length = maxLength;

  file.readArrayBuffer({
    uri: self.cPath,
    position: readOffset,
    length: length,
    success: (data) => {
      const buffer = new Uint8Array(data.buffer);
      let str = '';
      // UTF-16 LE解码
      for (let i = 0; i < buffer.length; i += 2) {
        str += String.fromCharCode(buffer[i + 1] * 256 + buffer[i]);
      }
      cb(str, buffer.length);
    }
  });
}
```

### 3.2 滑动翻页实现

三种模式：
- swipe: column - 上下滑动
- swipe: row - 左右滑动切换章节  
- swipe: off - 点击翻页

```javascript
onTouchEnd(e) {
  if (this.overscrollDistance > this.chapterSwitchSensitivity) {
    if (this.isAtChapterStart) this.changeChapter(-1);
    else if (this.isAtChapterEnd) this.changeChapter(1);
  }
}
```

### 3.3 进度保存与同步

```javascript
// 进度数据结构
{
  chapterIndex: 5,
  offsetInChapter: 1024,
  scrollOffset: 150,
  fontSize: 30,
  lastReadTimestamp: Date.now()
}

// 自动保存
setupAutoSave() {
  if (this.saveMode === 'periodic') {
    this.periodicSaveTimer = setInterval(() => {
      this._performSave();
    }, this.saveIntervalValue * 1000);
  }
}
```

### 3.4 手机-手环互联

```javascript
import interconnect from '@system.interconnect';

export default class Interconn {
  constructor() {
    this.conn = interconnect.instance();
    this.conn.onmessage = ({data}) => {
      const { tag, ...payload } = JSON.parse(data);
      this.callbacks[tag](payload);
    }
  }

  send(tag, payload) {
    return new Promise((resolve, reject) => {
      this.conn.send({ data: { ...payload, tag }, success: resolve, fail: reject });
    });
  }
}
```

---

## 4. 关键代码片段和模式

### 4.1 缓存模式

```javascript
// 文件缓存
if (typeof global.__storage_cache__ === 'undefined') {
  global.__storage_cache__ = null;
}

// 章节缓存 - 带过期时间
const chapterCache = new Map();
const CACHE_EXPIRY = 5 * 60 * 1000;

async function getCachedChapter(bookName, chapterIndex) {
  const key = bookName + '_' + chapterIndex;
  const cached = chapterCache.get(key);
  if (cached && (Date.now() - cached.timestamp < CACHE_EXPIRY)) {
    return cached.data;
  }
  const chapter = await loadChapter(bookName, chapterIndex);
  chapterCache.set(key, { data: chapter, timestamp: Date.now() });
  return chapter;
}
```

### 4.2 Promise化回调API

```javascript
// utils/runAsyncFunc.js
export default function runAsyncFunc(func, params) {
  return new Promise((resolve, reject) => {
    func({
      success: resolve,
      fail: (data, code) => reject({ data, code }),
      ...params
    });
  });
}

// 使用
const data = await runAsyncFunc(file.readText, { uri: '...' });
```

### 4.3 深拷贝

```javascript
function clone(obj) {
  return JSON.parse(JSON.stringify(obj));
}
```

### 4.4 内存管理

```javascript
onDestroy() {
  this.timer && clearInterval(this.timer);
  this.page1 = null;
  this.page2 = null;
  global.runGC();  // 重要!
}

changeChapter(offset) {
  global.runGC();  // 切换章节时主动GC
  this.loadChapter(nextIndex, () => {...});
}
```

---

## 5. 性能优化技巧

### 5.1 懒加载章节内容

```javascript
loadInitialSegments() {
  this.readFileText(this.currentFileOffset, (str, bytesRead) => {
    this.page1 = { text: str, offset: this.currentFileOffset };
    this.loadNextSegmentNoScroll();  // 预加载下一页
  });
}
```

### 5.2 页面分页

```javascript
loadPage(page) {
  const start = page * this.pageSize;
  this.visibleBooks = this.allBooks.slice(start, start + this.pageSize);
  this.currentPage = page;
}
```

### 5.3 减少重绘

```javascript
onScroll(e) {
  if (this.wait) return;  // 加载中不处理
  this.currentScrollTop = e.scrollY;
}
```

---

## 6. 常见问题和注意事项

### 6.1 文件路径问题

```javascript
// 正确
const uri = 'internal://files/books/book1/content/0.txt';

// 错误
const uri = './files/book1/content/0.txt';
```

### 6.2 UTF-16编码

```javascript
let str = '';
for (let i = 0; i < buffer.length; i += 2) {
  str += String.fromCharCode(buffer[i + 1] * 256 + buffer[i]);
}
```

### 6.3 异步API

```javascript
// 错误：连续await
const book1 = await bookStorage.get('book1');
const book2 = await bookStorage.get('book2');

// 正确：并行请求
const [b1, b2] = await Promise.all([
  bookStorage.get('book1'),
  bookStorage.get('book2')
]);
```

---

## 7. 开发注意事项

### 7.1 调试技巧

1. console.log支持
2. 真机调试
3. try-catch包裹关键API

```javascript
try {
  const data = await runAsyncFunc(file.readText, { uri: path });
} catch (e) {
  console.error('读取失败:', e);
}
```

### 7.2 发布检查清单

- manifest.json配置正确
- 所有页面路由已注册
- 权限features已申请
- 测试内存占用

### 7.3 学习资源

- 小米Vela文档: https://iot.mi.com/vela/quickapp/zh/guide/
- 项目配套安卓同步器: https://github.com/youshen2/com.bandbbs.ebook-android

---

## 附录：常用API速查

| API | 用途 |
|-----|------|
| @system.router | 路由跳转 |
| @system.storage | Key-Value存储 |
| @system.file | 文件操作 |
| @system.prompt | 提示信息 |
| @system.device | 设备信息 |
| @system.brightness | 屏幕亮度 |
| @system.interconnect | 手机手环互联 |
| @system.app | 应用管理 |

---

> 本教程基于开源项目 com.bandbbs.ebook 编写  
> 项目采用 AGPL-3.0 协议开源
