---
title: 网络与脚本命令
description: 网络访问、变量脚本、系统控制和压缩归档命令
---

# 网络与脚本命令

## 网络

| 命令 | 用法 |
|------|------|
| `ifconfig` | `ifconfig [interface ...]` |
| `ifup` / `ifdown` | `ifup <interface>` |
| `ping` | `ping [-c <count>] [-i <interval>] [-W <timeout>] [-s <size>] <host>` |
| `nslookup` | `nslookup <hostname>` |
| `wget` | `wget [-o <local-path>] <url>` |
| `arp` | `arp [-i <ifname>] [-a\|-d\|-s <ipaddr> [hwaddr]]` |

## 变量与脚本

| 命令 | 用法 |
|------|------|
| `set` | `set [{+\|-}{e\|x}] [<name> <value>]` |
| `unset` | `unset <name>` |
| `echo` | `echo [-n] [<string\|$name> ...]` |
| `printf` | `printf <string> [args ...]`（格式符不完全生效） |
| `expr` | `expr <expression>` |
| `test` / `[` | `test <expression>` |
| `true` / `false` | 返回 0 / 1 |
| `source` / `.` | `source <file>` |
| `exec` | `exec <cmd>` |
| `alias` / `unalias` | `alias [name[=value]]` |

## 系统控制

| 命令 | 用法 |
|------|------|
| `reboot` | `reboot`，会直接重启设备 |
| `poweroff` | `poweroff`，会直接关机 |
| `timedatectl` | `timedatectl [set-timezone TZ]` |

## 压缩与归档

| 命令 | 用法 |
|------|------|
| `tar` | `tar [-C rootdir] [-g] [-z] <-x\|-t\|-c> filename.tar [...]` |
| `gzip` | `gzip <file>`，无参数运行时可能阻塞 |
| `unzip` | `unzip <file.zip>` |

## 使用建议

- 网络连通性排查可以从 `ifconfig`、`ifup`、`ping`、`nslookup` 这条链路开始。
- 简单脚本优先用 `source` 加 `set/test/expr`，避免使用桌面 shell 常见但这里不支持的语法。
- `reboot` 和 `poweroff` 建议只在确认环境安全时执行。
