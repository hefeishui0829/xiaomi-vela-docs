import { tool } from '@opencode-ai/plugin';

export const velaApi = tool({
  description: '查询 Vela 特有 API（与Web不同的部分）',
  args: {
    api: tool.schema.string().describe('API名称'),
  },
  async execute({ api }) {
    const apiMap = {
      router: 'import router from "@system.router";\nrouter.push({ uri: "pages/detail/detail", params: { id: 1 } });\nrouter.replace({ uri: "pages/home/home" });\nrouter.back();\nrouter.clear();',
      
      storage: 'import storage from "@system.storage";\nstorage.get({ key: "key", success: (data) => {} });\nstorage.set({ key: "key", value: "value" });\nstorage.delete({ key: "key" });\nstorage.clear();',
      
      file: 'import file from "@system.file";\nfile.readText({ uri: "internal://files/data.txt", success: (data) => {} });\nfile.writeText({ uri: "internal://files/data.txt", text: "content" });\nfile.list({ uri: "internal://files/", success: (data) => {} });',
      
      sensor: 'import sensor from "@system.sensor";\nsensor.subscribeAccelerometer({ interval: "normal", callback: (data) => {} });\nsensor.unsubscribeAccelerometer();',
      
      app: 'import app from "@system.app";\napp.terminate(); // 退出应用\napp.getInfo({ success: (data) => {} });',
      
      prompt: 'import prompt from "@system.prompt";\nprompt.showToast({ message: "提示文字" });\nprompt.showDialog({ title: "标题", message: "内容", buttons: [{ text: "确定", color: "#0D6EFF" }] });',
      
      device: 'import device from "@system.device";\ndevice.getInfo({ success: (data) => { console.log(data.screenShape); } });\ndevice.getTotalStorage({ success: (data) => {} });\ndevice.getAvailableStorage({ success: (data) => {} });',
      
      lifecycle: '页面生命周期:\nonInit() - 数据初始化，页面参数在此获取\nonReady() - DOM渲染完成\nonShow() - 页面显示\nonHide() - 页面隐藏\nonDestroy() - 页面销毁\n\n应用生命周期:\nonCreate() → onShow() → onHide() → onDestroy()',
      
      data: 'export default {\n  private: { a: 1 },     // 私有，仅当前页面可用\n  protected: { b: 2 },    // 保护，可被子组件访问\n  public: { c: 3 },        // 公开，可被子组件修改\n  onInit() {\n    // 通过 this.params.xxx 获取页面参数\n  }\n}',
      
      component: '// 子组件通信\n// 父→子: 通过 props 传递\n// 子→父: this.$emit("event", data)\n// 父→子: this.$broadcast("event", data)\n// 任意: this.$on("event", callback)\n// 停止: this.$off("event") 或 event.$stop()'
    };
    
    const result = apiMap[api.toLowerCase()];
    if (!result) {
      return '未知API。可用:\nrouter-路由\nstorage-存储\nfile-文件(仅internal://)\nsensor-传感器\napp-应用控制\nprompt-提示对话框\ndevice-设备信息\nlifecycle-生命周期\ndata-数据对象\ncomponent-组件通信';
    }
    return result;
  }
});

export const velaTemplate = tool({
  description: '获取 Vela 项目模板代码',
  args: {
    type: tool.schema.string().describe('模板类型'),
  },
  async execute({ type }) {
    const templates = {
      page: '// 最小页面\n<template>\n  <div class="page">\n    <text>{{message}}</text>\n  </div>\n</template>\n\n<script>\nexport default {\n  private: { message: "Hello" },\n  onInit() { console.log("Page initialized"); }\n}\n</script>\n\n<style>\n.page { width: 100%; height: 100%; background-color: #000000; }\n</style>',
      
      settings: '// 设置页面\n<template>\n  <div class="page">\n    <img static src="/common/images/hd.png" style="position:absolute;left:0;top:0;width:336px;height:102px;" />\n    <img static src="/common/images/back.png" @click="back" style="position:absolute;left:6px;top:6px;width:72px;height:72px;"/>\n    <text style="position:absolute;left:78px;top:35px;width:180px;font-size:32px;font-weight:bold;color:white;text-align:center;">设置</text>\n    <list class="list">\n      <list-item class="item" @click="toggle">\n        <text class="itemtext">{{settingName}}</text>\n        <img src="{{isOn ? \'/common/images/Switch_ON.png\' : \'/common/images/Switch_OFF.png\'}}" style="width:60px;height:42px;" static />\n      </list-item>\n    </list>\n  </div>\n</template>\n\n<script>\nimport router from "@system.router";\nexport default {\n  private: { settingName: "开关设置", isOn: false },\n  toggle() { this.isOn = !this.isOn; },\n  back() { router.back(); }\n}\n</script>\n\n<style>\n.page { width: 100%; height: 100%; background-color: #000000; position: relative; }\n.list { width: 100%; height: 100%; padding: 86px 6px; position: absolute; top: 0; left: 0; }\n.item { width: 100%; height: 112px; padding: 14px 20px; margin-bottom: 8px; background-color: #262626; border-radius: 36px; justify-content: space-between; align-items: center; }\n.itemtext { font-size: 32px; font-weight: bold; color: white; }\n</style>',
      
      list: '// 列表页面\n<template>\n  <div class="page">\n    <img static src="/common/images/hd.png" style="position:absolute;left:0;top:0;width:336px;height:102px;" />\n    <img static src="/common/images/back.png" @click="back" style="position:absolute;left:6px;top:6px;width:72px;height:72px;"/>\n    <text style="position:absolute;left:78px;top:35px;width:180px;font-size:32px;font-weight:bold;color:white;text-align:center;">{{title}}</text>\n    <list class="list">\n      <list-item type="item" class="item" for="{{item in items}}" @click="onItemClick($item)">\n        <text class="itemtext">{{item.name}}</text>\n        <text class="itemtext2">{{item.subtitle}}</text>\n      </list-item>\n    </list>\n  </div>\n</template>\n\n<script>\nimport router from "@system.router";\nexport default {\n  private: { title: "列表", items: [] },\n  onItemClick(item) { console.log(item); },\n  back() { router.back(); }\n}\n</script>\n\n<style>\n.page { width: 100%; height: 100%; background-color: #000000; position: relative; }\n.list { width: 100%; height: 100%; padding: 86px 6px; position: absolute; top: 0; left: 0; }\n.item { width: 100%; height: 112px; padding: 14px 20px; margin-bottom: 8px; background-color: #262626; border-radius: 36px; justify-content: center; }\n.itemtext { font-size: 32px; font-weight: bold; color: white; }\n.itemtext2 { font-size: 28px; font-weight: bold; color: rgba(255,255,255,0.6); }\n</style>',
      
      manifest: '{\n  "package": "com.example.app",\n  "name": "MyApp",\n  "deviceTypeList": ["watch"],\n  "features": [\n    { "name": "system.router" },\n    { "name": "system.storage" },\n    { "name": "system.file" },\n    { "name": "system.prompt" },\n    { "name": "system.app" }\n  ],\n  "config": {\n    "designWidth": 336\n  },\n  "router": {\n    "entry": "index",\n    "pages": {\n      "index": { "component": "index", "path": "/", "launchMode": "singleTask" },\n      "detail": { "component": "detail", "path": "/detail" }\n    }\n  },\n  "display": {\n    "backgroundColor": "#000000"\n  }\n}',
      
      multi: '// 多设备适配页面\n<template>\n  <div class="page">\n    <!-- 圆屏布局 -->\n    <div if="{{screenShape === \'circle\'}}">\n      <img static src="/common/images/hd_circle.png" style="..." />\n    </div>\n    <!-- 方屏/胶囊屏 -->\n    <div else>\n      <img static src="/common/images/hd.png" style="..." />\n    </div>\n  </div>\n</template>\n\n<script>\nimport device from "@system.device";\nexport default {\n  private: { screenShape: "rect" },\n  onInit() {\n    device.getInfo({\n      success: (data) => { this.screenShape = data.screenShape; }\n    });\n  }\n}\n</script>',
      
      csslimits: '// Vela不支持的CSS:\n// ❌ 后代选择器: .a .b { }\n// ❌ 子选择器: .a > .b { }\n// ❌ 兄弟选择器: .a + .b { }\n// ❌ 属性选择器: [attr] { }\n// ❌ 通用选择器: * { }\n// ❌ 伪类: :hover, :active, :focus { }\n\n// ✅ 支持的:\n// - class选择器: .item { }\n// - Flexbox: display:flex; flex-direction:row; justify-content:center;\n// - 基础属性: width, height, padding, margin, border-radius\n// - 文字: font-size, font-weight, color, text-align'
    };
    
    const result = templates[type];
    if (!result) {
      return '未知模板。可用:\npage-最小页面\nsettings-设置页\nlist-列表页\nmanifest-应用配置\nmulti-多设备适配\ncsslimits-CSS限制';
    }
    return result;
  }
});

export const velaUi = tool({
  description: '获取 Vela UI 规范（关注特有布局和组件）',
  args: {
    item: tool.schema.string().describe('查询项'),
  },
  async execute({ item }) {
    const ui = {
      layout: '// 标准页面布局\n背景:#000\n顶部:hd.png(336x102)\n返回:back.png(72x72,left:6,top:6)\n标题:text(32px bold,left:78,top:35)\n内容:list(padding:86px 6px)\n底部:bt.png(top:378,可选)\n\n列表项:\n.item{height:112px;background:#262626;border-radius:36px;padding:14px 20px;margin-bottom:8px}\n.itemtext{font-size:32px;bold;white}\n.itemtext2{font-size:28px;bold;rgba(255,255,255,0.6)}',
      
      colors: '颜色:\n背景:#000000\n卡片:#262626\n强调:#0D6EFF\n警告:#ad0000\n主文字:#FFFFFF\n次级:rgba(255,255,255,0.6)\n辅助:rgba(255,255,255,0.4)',
      
      fonts: '字体:\n标题:32px bold\n副标题:24px bold\n正文:30px\n行高:lineHeight = -0.01*fontSize² + 1.62*fontSize - 3.23',
      
      components: '组件尺寸:\n按钮:72x72px\n开关:60x42px\n封面:64x84px\n图标:48x48px\n列表项:112px高,36px圆角',
      
      multi: '多设备:\n方屏:designWidth=336,336x480,rect\n胶囊:designWidth=192,390x312,pill-shaped\n圆屏:designWidth=480,454x454,circle\n\n条件渲染:\n<div if="{{screenShape===\'circle\'}}">圆屏</div>\n<div else>方屏</div>',
      
      images: '图标(/common/images/):\nhd.png-336x102状态栏\nbt.png-336x102底部栏\nback.png-72x72返回\nmore.png-72x72菜单\nenter.png-48x48进入\ncheck.png-40x40选中\nSwitch_ON/OFF.png-60x42开关\npre/next.png-72x72翻页\nsearch.png-72x72搜索\nempty.png-128x128空状态'
    };
    
    const result = ui[item];
    if (!result) {
      return '未知项。可用:\nlayout-页面布局\ncolors-颜色\nfonts-字体\ncomponents-组件尺寸\nmulti-多设备适配\nimages-图标资源';
    }
    return result;
  }
});

export const velaQuickRef = tool({
  description: '获取 Vela 开发要点（与Web不同的核心差异）',
  args: {
    topic: tool.schema.string().describe('主题'),
  },
  async execute({ topic }) {
    const ref = {
      diff: '【核心差异】\n1.存储:localStorage→@system.storage\n2.路由:Vue Router→manifest.json+router.push()\n3.组件:import→<import>标签\n4.文件:HTTP路径→internal://协议(仅读)\n5.样式:CSS→Flexbox为主，不支持:hover/:active等',
      
      lifecycle: '【生命周期】\n页面:\nonInit()-数据初始化，接收params\nonReady()-DOM渲染完成\nonShow()-显示\nonHide()-隐藏\nonDestroy()-销毁\n\n应用:\nonCreate→onShow→onHide→onDestroy',
      
      data: '【数据对象】\nprivate:{}-私有，仅当前页面\nprotected:{}-保护，可被子组件读取\npublic:{}-公开，可被子组件修改\n\n接收页面参数:this.params.xxx',
      
      component: '【组件通信】\n父→子: props传递\n子→父: this.$emit("event", data)\n父→子: this.$broadcast("event", data)\n监听: this.$on("event", callback)\n停止: event.$stop()',
      
      launchmode: '【启动模式】\nstandard-每次创建新实例\nsingleTask-复用当前实例\nsingleTop-栈顶复用\n\nmanifest配置:\n"launchMode": "singleTask"',
      
      css: '【CSS限制】\n❌不支持:\n- 后代/子/兄弟选择器\n- 属性选择器\n- 伪类(:hover等)\n- 通用选择器(*)\n\n✅支持:\n- class选择器\n- Flexbox\n- 基础属性(width/height/padding/margin/border-radius)\n- 文字样式',
      
      devices: '【设备适配】\n方屏:336x480,designWidth=336,rect\n胶囊:390x312,designWidth=192,pill-shaped\n圆屏:454x454,designWidth=480,circle\n\n获取:device.getInfo→screenShape\n条件:<div if="{{screenShape===\'xxx\'}}">',
      
      tips: '【开发要点】\n1.内存:global.runGC()定期清理\n2.图片:internal://协议\n3.状态栏:hd.png(102px)\n4.底部栏:bt.png(102px)\n5.列表项:112px高,36px圆角\n6.打包:需签名证书\n7.调试:AIoT-IDE模拟器或真机'
    };
    
    const result = ref[topic];
    if (!result) {
      return '未知主题。可用:\ndiff-核心差异\nlifecycle-生命周期\ndata-数据对象\ncomponent-组件通信\nlaunchmode-启动模式\ncss-CSS限制\ndevices-设备适配\ntips-开发要点';
    }
    return result;
  }
});
