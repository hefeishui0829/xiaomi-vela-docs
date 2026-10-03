---
title: 设备服务与测试工具
description: 蓝牙、DBus、电话、日志、uORB、安全与测试演示工具
---

# 设备服务与测试工具

## 蓝牙

| 命令 | 说明 | 用法 |
|------|------|------|
| `bluetoothd` | 蓝牙协议栈守护进程 | 自动启动 |
| `bttool` | 蓝牙调试工具 | `bttool <command> [args]` |
| `miconnect` | 小米设备连接服务 | 自动启动 |

### bttool 子命令

| 子命令 | 说明 |
|--------|------|
| `enable` / `disable` | 启用 / 禁用蓝牙 |
| `state` | 获取适配器状态 |
| `inquiry start <timeout>` / `inquiry stop` | 搜索设备 |
| `pair` | 响应配对请求 |
| `connect <addr>` / `disconnect <addr>` | 经典蓝牙连接 |
| `leconnect` / `ledisconnect <addr>` | BLE 连接 |
| `createbond <addr> <transport>` | 创建绑定，`0` 为 BLE，`1` 为 BREDR |
| `removebond <addr> <transport>` | 移除绑定 |
| `setalias <addr>` | 设置设备别名 |
| `device <addr>` | 查看设备信息 |
| `setphy <addr> <txphy> <rxphy>` | 设置 LE PHY |
| `adv` | 广播管理 |
| `scan` | BLE 扫描 |
| `a2dpsrc` | A2DP Source 控制 |
| `avrcpct` | AVRCP 控制 |
| `hf` | 免提模式 |
| `ag` | 音频网关 |
| `spp` | 串口通信 |
| `hidd` | HID 设备 |
| `gattc` | GATT Client |
| `gatts` | GATT Server |
| `dump` | 转储适配器状态 |
| `log` | 日志控制 |

## DBus

| 命令 | 说明 | 用法 |
|------|------|------|
| `dbusdaemon` | DBus 系统总线守护进程 | `dbusdaemon --system --nopidfile --nofork` |
| `dbussend` | 发送 DBus 消息 | `dbussend [--system] [--print-reply] --dest=<name> --type=<type> <path> <method> [args]` |
| `dbusmonitor` | 监控 DBus 消息 | `dbusmonitor [--system\|--session\|--address ADDR] [--monitor\|--profile\|--pcap]` |

## 通信与电话

| 命令 | 说明 | 用法 |
|------|------|------|
| `ofonod` | oFono 电话服务守护进程 | 自动启动 |
| `rild` | RIL 守护进程 | 自动启动 |
| `telephonytool` | 电话调试工具 | `telephonytool` |

## 日志与调试

| 命令 | 说明 | 用法 |
|------|------|------|
| `setlogmask` | 设置日志掩码级别 | `setlogmask <d\|i\|n\|w\|e\|c\|a\|r>` |
| `offline_log` | 离线日志管理 | `offline_log <start[-d\|-w]\|stop\|clear>` |
| `dumpstack` | 转储所有线程栈 | `dumpstack` |
| `log_service` | 日志服务守护进程 | 自动启动 |

## uORB 传感器

| 命令 | 说明 | 用法 |
|------|------|------|
| `uorb_listener` | 监听 uORB 主题数据 | `uorb_listener [topics] [-n <count>] [-r <rate>] [-t <sec>] [-T] [-l]` |

### uorb_listener 参数

| 参数 | 说明 |
|------|------|
| `<topics>` | 主题名，多个使用 `,` 分隔 |
| `-n <count>` | 接收消息数量，`0` 表示不限 |
| `-r <rate>` | 订阅频率，`0` 表示不限 |
| `-t <sec>` | 监听时长，默认 `5s` |
| `-T` | 持续打印更新的主题 |
| `-l` | 仅执行一次快照 |
| `-f` | 记录到文件 |

## 安全

| 命令 | 说明 | 用法 |
|------|------|------|
| `opteed` | OP-TEE 安全守护进程 | 自动启动 |
| `ca_triad_tool` | TEE 设备三元组管理 | `ca_triad_tool <set\|get> <did\|key> [value]` |

## 系统服务

| 命令 | 说明 |
|------|------|
| `miwear` | 主系统服务，负责 UI 框架和表盘等能力 |
| `miwear_activity_service` | Activity 生命周期管理 |
| `miwear_bluetooth` | 蓝牙管理服务 |
| `miwear_rtc_checker` | RTC 时钟校验 |
| `vibratord` | 振动马达服务 |
| `kvdbd` | 键值数据库服务（UnQLite） |
| `servicemanager` | 系统服务注册管理器 |
| `adbd` | ADB 守护进程 |

## 测试与演示

| 命令 | 说明 | 用法 |
|------|------|------|
| `hello` | Hello World 测试 | `hello` |
| `lvgldemo` | LVGL 演示 | `lvgldemo` |
| `uikit_demo` | UIKit 演示 | `uikit_demo` |
| `feature_test_cli` | 特性测试 | `feature_test_cli` |
| `adapter_test` | 适配器测试 | `adapter_test` |
| `pipe` | 管道测试 | `pipe` |
| `sb` / `rb` | XMODEM 发送 / 接收 | `sb <file>` / `rb <file>` |
| `rpsock_client` / `rpsock_server` | RPMsg socket 测试 | 按程序参数运行 |
| `lyra_lite_sdk_tools` | Lyra SDK 工具 | 交互式使用 |
