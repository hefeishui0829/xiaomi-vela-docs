---
title: NuttX Shell（nsh）
description: NuttX nsh 的语法差异、命令分类与设备侧服务速查
tags: ["type:ref"]
---

# NuttX Shell（nsh）

设备侧使用的 `nsh` 与常见 POSIX `sh` 差异较大，适合单独作为一套运行时环境来理解。本分区把原来混在一页里的内容拆成了按主题浏览的结构，方便开发、联调和排障时快速定位。

## 分区导航

| 主题 | 说明 |
|------|------|
| [语法与运行环境](syntax-and-environment.md) | 命令格式、支持/不支持的语法、文件系统和环境变量 |
| [文件与进程命令](file-and-process.md) | 文件操作、路径工具、进程管理与系统信息 |
| [网络与脚本命令](network-and-scripting.md) | 网络访问、变量/脚本、系统控制与压缩归档 |
| [底层与调试命令](low-level-and-debug.md) | 内存、模块、RPMsg、RAM 磁盘与底层调试 |
| [运行时与媒体工具](runtimes-and-media.md) | Lua / QuickJS / WASM、网络工具、媒体处理和应用管理 |
| [系统属性](system-properties.md) | `getprop` / `setprop` 与设备属性采样 |
| [设备服务与测试工具](services-and-testing.md) | 蓝牙、DBus、电话、日志、uORB、安全与演示工具 |

## 使用建议

- 优先把 `nsh` 当作“设备命令执行环境”来理解，而不是完整的桌面 shell。
- 命令是否可用与参数范围可能随具体固件配置变化，本分区记录的是当前项目中的常见集合。
- 像 `getprop` 采样、媒体编解码能力和设备服务，更适合在真机或模拟器环境里结合实际输出验证。
