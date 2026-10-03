# 01 · 官方 JS 快应用文档（Xiaomi Vela）

> 小米官方 `Xiaomi Vela JS 应用` 文档站 <https://iot.mi.com/vela/quickapp/zh/> 的完整 Markdown 副本。
> 这是**小米手环 / 手表快应用开发的主文档**，内容原样保留，未做改写。

## 分区导航

| 分区 | 篇数 | 说明 |
|---|---:|---|
| [components/](./components/) | 27 | 内置 UI 组件参考: 基础 / 容器 / 表单 / 通用样式与事件 |
| [features/](./features/) | 25 | 运行时 API: 基础 / 数据 / 网络 / 系统能力 / 安全 / 其他 |
| [guide/](./guide/) | 42 | 从零上手: 环境搭建、项目结构、UX 语法、框架机制、多屏适配、发布上架 |
| [samples/](./samples/) | 0 | 官方示例代码与设计模式参考 |
| [tools/](./tools/) | 24 | AIoT-IDE、调试器、模拟器、项目模板、打包发布 |
| [images/](./images/) | — | 文档配图 207 张 |

---

## components/ — 组件

内置 UI 组件参考: 基础 / 容器 / 表单 / 通用样式与事件

- [a](./components/basic/a.md)
- [barcode2+](./components/basic/barcode.md)
- [chart](./components/basic/chart.md)
- [image-animator2+](./components/basic/image-animator.md)
- [image](./components/basic/image.md)
- [marquee](./components/basic/marquee.md)
- [progress](./components/basic/progress.md)
- [qrcode2+](./components/basic/qrcode.md)
- [span](./components/basic/span.md)
- [text](./components/basic/text.md)
- [div](./components/container/div.md)
- [list-item](./components/container/list-item.md)
- [list](./components/container/list.md)
- [scroll2+](./components/container/scroll.md)
- [stack](./components/container/stack.md)
- [swiper](./components/container/swiper.md)
- [input](./components/form/input.md)
- [picker](./components/form/picker.md)
- [slider](./components/form/slider.md)
- [switch](./components/form/switch.md)
- [动画样式](./components/general/animation-style.md)
- [背景图样式](./components/general/background-img-styles.md)
- [颜色配置](./components/general/color.md)
- [通用事件](./components/general/events.md)
- [通用方法](./components/general/methods.md)
- [通用属性](./components/general/properties.md)
- [通用样式](./components/general/style.md)

## features/ — JS 接口

运行时 API: 基础 / 数据 / 网络 / 系统能力 / 安全 / 其他

- [应用上下文 app](./features/basic/app.md)
- [应用配置 configuration](./features/basic/configuration.md)
- [设备信息 device](./features/basic/device.md)
- [页面路由 router](./features/basic/router.md)
- [文件存储 file](./features/data/file.md)
- [数据存储 storage](./features/data/storage.md)
- [通用语法](./features/grammar.md)
- [数据请求 fetch](./features/network/fetch.md)
- [设备通信 interconnect](./features/network/interconnect.md)
- [下载 request](./features/network/request.md)
- [上传 uploadtask3+](./features/network/uploadtask.md)
- [音频 audio](./features/other/audio.md)
- [弹窗 prompt](./features/other/prompt.md)
- [密码算法 crypto](./features/security/crypto.md)
- [电量信息 battery](./features/system/battery.md)
- [蓝牙 bluetooth](./features/system/bluetooth.md)
- [屏幕亮度 brightness](./features/system/brightness.md)
- [事件 event4+](./features/system/event.md)
- [地理位置 geolocation](./features/system/geolocation.md)
- [网络信息 network](./features/system/network.md)
- [录音 record](./features/system/record.md)
- [传感器 sensor](./features/system/sensor.md)
- [振动 vibrator](./features/system/vibrator.md)
- [系统音量 volume](./features/system/volume.md)
- [解压缩 zip](./features/system/zip.md)

## guide/ — 教程

从零上手: 环境搭建、项目结构、UX 语法、框架机制、多屏适配、发布上架

- [常用业务优化](./guide/best-practice/business.md)
- [内存优化](./guide/best-practice/memory.md)
- [启动时延优化](./guide/best-practice/start.md)
- [多屏设计](./guide/design/multi-screens.md)
- [拓展组件](./guide/developer-materials/extension-components.md)
- [项目配置](./guide/framework/manifest.md)
- [后台运行](./guide/framework/other/background-running.md)
- [动态组件](./guide/framework/other/dynamic-component.md)
- [hap 链接](./guide/framework/other/hap-schema.md)
- [多语言覆盖](./guide/framework/other/i18n.md)
- [language-list](./guide/framework/other/language-list.md)
- [页面启动模式](./guide/framework/other/launch-mode.md)
- [页面切换](./guide/framework/page-switch.md)
- [项目结构](./guide/framework/project-structure.md)
- [全局属性和方法](./guide/framework/script/global-data-method.md)
- [生命周期](./guide/framework/script/lifecycle.md)
- [页面数据对象](./guide/framework/script/page-data.md)
- [媒体查询2+](./guide/framework/style/media-query.md)
- [页面样式与布局](./guide/framework/style/page-style-and-layout.md)
- [组件](./guide/framework/template/component.md)
- [计算属性](./guide/framework/template/computed.md)
- [事件绑定](./guide/framework/template/event.md)
- [循环指令](./guide/framework/template/for.md)
- [条件指令](./guide/framework/template/if.md)
- [组件属性](./guide/framework/template/props.md)
- [UX 文件](./guide/framework/ux.md)
- [条件编译](./guide/multi-screens/conditional-compilation.md)
- [代码示例](./guide/multi-screens/samples.md)
- [概述](./guide/multi-screens/simulator.md)
- [适配规范](./guide/multi-screens/specs.md)
- [常见问题](./guide/other/faq.md)
- [注意事项](./guide/other/tips.md)
- [验收标准](./guide/publish/acceptance-criteria.md)
- [添加交互](./guide/start/add-interactivity.md)
- [数据获取](./guide/start/data-fetch.md)
- [项目结构](./guide/start/project-overview.md)
- [编译参数](./guide/start/toolkit-params.md)
- [安装环境](./guide/start/use-ide.md)
- [编写页面UI](./guide/start/user-interface.md)
- [APILevel2](./guide/version/APILevel2.md)
- [APILevel3](./guide/version/APILevel3.md)
- [APILevel4](./guide/version/APILevel4.md)

## samples/ — 编程示例

官方示例代码与设计模式参考


## tools/ — 工具

AIoT-IDE、调试器、模拟器、项目模板、打包发布

- [优化评分](./tools/debug/audit.md)
- [编译设置](./tools/debug/build-setting.md)
- [调试运行](./tools/debug/debug.md)
- [内存分析](./tools/debug/memory.md)
- [多屏适配](./tools/debug/multi-screens.md)
- [编译预览](./tools/debug/start.md)
- [功能按钮](./tools/debug/toolbar.md)
- [日志查看](./tools/debug/watch-log.md)
- [应用热更新](./tools/dev/build.md)
- [代码美化](./tools/dev/format.md)
- [可视化编辑](./tools/dev/manifest.md)
- [AI 自动化生成](./tools/dev/official-site-tutorial.md)
- [代码补全](./tools/dev/start.md)
- [功能介绍](./tools/devicedebug/start.md)
- [设备管理](./tools/emulator/create-emulator.md)
- [运行模拟器](./tools/emulator/emulator-run.md)
- [新建项目](./tools/project/create-project.md)
- [管理项目](./tools/project/project.md)
- [项目类型](./tools/project/template.md)
- [发布应用](./tools/release/release.md)
- [打包应用](./tools/release/start.md)
- [了解界面](./tools/start/project.md)
- [AIoT-toolkit](./tools/toolkit/start.md)
- [升级迁移](./tools/toolkit/update.md)
