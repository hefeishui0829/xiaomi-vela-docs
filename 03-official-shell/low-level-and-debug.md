---
title: 底层与调试命令
description: 内存、模块、RPMsg 与底层诊断相关命令
---

# 底层与调试命令

| 命令 | 用法 |
|------|------|
| `xd` | `xd <hex-address> <byte-count>`，内存十六进制转储 |
| `mw` | `mw <hex-address>[=<hex-value>] [<byte-count>]`，内存读写 |
| `memdump` | `memdump [pid\|used\|free\|on\|off]` |
| `insmod` | `insmod <file-path> <module-name>` |
| `rmmod` | `rmmod <module-name>` |
| `lsmod` | `lsmod` |
| `losetup` | `losetup [-d <dev>] \| [[-o <offset>] [-r] [-b <sect-size>] <dev> <file>]` |
| `mkrd` | `mkrd [-m <minor>] [-s <sect-size>] <nsectors>`，创建 RAM 磁盘 |
| `mkfifo` | `mkfifo <path>` |
| `rpmsg` | `rpmsg <panic\|dump\|ping> <path\|all> [value\|times length ack sleep]` |
| `rptun` | `rptun <start\|stop\|reset\|panic\|dump\|ping\|test> <path\|all>` |
| `watch` | `watch [-n interval] [-c count] <command>` |

## 适用场景

- 内存排查：`xd`、`mw`、`memdump`
- 模块装载：`insmod`、`rmmod`、`lsmod`
- 虚拟块设备与镜像：`losetup`、`mkrd`
- 多核/跨端通信：`rpmsg`、`rptun`

## 注意事项

- `mw`、`xd` 这类命令直接面向地址空间，执行前需要确认地址和长度。
- `rpmsg` / `rptun` 常用于联调底层链路，建议配合平台日志一起看。
