---
title: 系统属性
description: getprop / setprop 与设备系统属性采样
---

# 系统属性

## 常用命令

| 命令 | 说明 | 用法 |
|------|------|------|
| `getprop` | 读取系统属性 | `getprop [key]`，无参数时列出全部属性 |
| `setprop` | 设置系统属性 | `setprop <key> <value>` |
| `qemuprop` | 模拟器属性同步服务 | 自动启动 |

## getprop 全量属性采样

采样时间：2026-01-30（`adb shell getprop`，`emulator`）

以下“说明 / 值范围”为基于键名与当前值的推测，实际以系统文档和固件实现为准。

| 属性键 | 当前值（观测） | 说明（推测） | 值范围（推测 / 格式） |
|------|------|------|------|
| `persist.bluetooth.log.changed` | `0` | 蓝牙日志变更标记 | 整数 |
| `persist.locale` | `zh_CN` | 系统 locale | locale 字符串，如 `zh_CN` |
| `persist.phone.sco_volume` | `8` | 电话 SCO 音量等级 | 整数 |
| `persist.replace_widget` | `true` | 是否替换小组件 | `true` / `false` |
| `persist.call_mode` | `1` | 通话模式 | 整数枚举 |
| `persist.downkey.pkgname` | `com.xiaomi.miwear.sports` | 下键绑定包名 | 字符串 |
| `persist.selected_local` | `zh_CN` | 当前选择的 locale | locale 字符串 |
| `persist.setup_wizard` | `1` | 首次设置向导完成标记 | `0` / `1` |
| `persist.screen.touch_palm` | `1` | 掌触屏蔽开关 | `0` / `1` |
| `persist.system_novice_guidance` | `false` | 新手引导开关 | `true` / `false` |
| `persist.screen.dimmer_timeout` | `300000` | 屏幕变暗 / 息屏超时 | 毫秒整数 |
| `persist.remind_womenhealth_data` | `false` | 女性健康提醒开关 | `true` / `false` |
| `persist.sms.db_version` | `2` | 短信数据库版本 | 整数 |
| `persist.modem_enabled` | `true` | 基带 / 调制解调器启用开关 | `true` / `false` |
| `persist.priv.com.xiaomi.wear.media` | `true` | 媒体相关私有权限开关 | `true` / `false` |
| `TELEPHONY_TYPE` | `6f7468657273` | 电话类型 / 制式标记 | 十六进制字符串 |
| `is_main_watchface` | `false` | 是否主表盘 | `true` / `false` |
| `miwear_conn_status` | `false` | MiWear 连接状态 | `true` / `false` |
| `bt_conn_status` | `false` | 蓝牙连接状态 | `true` / `false` |
| `activity_service_boot_ready` | `true` | activity_service 启动就绪标记 | `true` / `false` |
| `qemu.timezone` | `Unknown/Unknown` | QEMU 时区 | 时区字符串 |
| `ro.sf.lcd_density` | `320` | 屏幕密度 | 整数（dpi） |
| `qemu.hw.mainkeys` | `0` | 是否有物理主键 | `0` / `1` |
| `dalvik.vm.heapsize` | `256m` | 虚拟机堆大小 | 内存大小字符串 |
| `qemu.sf.fake_camera` | `none` | 模拟相机配置 | 字符串 |
| `ro.opengles.version` | `131072` | OpenGL ES 版本编码 | 整数 |
| `vendor.qemu.dev.bootcomplete` | `1` | QEMU 启动完成标记 | `0` / `1` |
| `ro.product.device.devicetype` | `watch` | 设备类型 | `watch` / `phone` 等 |
| `ro.product.device.screenshape` | `circle` | 屏幕形状 | `circle` / `rect` 等 |
| `ro.build.id` | `202507160414` | 构建 ID | 字符串 |
| `ro.product.board` | `Emulator` | 板卡 / 硬件平台 | 字符串 |
| `ro.product.manufacturer` | `Xiaomi` | 厂商 | 字符串 |
| `ro.product.brand` | `Vela` | 品牌 | 字符串 |
| `ro.product.name` | `Emulator-Vela` | 产品名 | 字符串 |
| `ro.product.device` | `Emulator-Vela` | 设备名 | 字符串 |
| `ro.product.model` | `Emulator-Vela` | 型号 | 字符串 |
| `ro.build.version` | `12.0.0` | 系统版本 | 版本号字符串 |
| `ro.build.version.release` | `12.0.0` | 系统版本（release） | 版本号字符串 |
| `ro.build.codename` | `DEV` | 版本代号 | 字符串 |
