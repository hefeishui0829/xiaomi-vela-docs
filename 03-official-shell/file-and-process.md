---
title: 文件与进程命令
description: 文件系统、路径、进程与系统信息类常用命令
---

# 文件与进程命令

## 文件操作

| 命令 | 用法 |
|------|------|
| `ls` | `ls [-lRsh] <dir>` |
| `cat` | `cat <path> [<path> ...]` |
| `cp` | `cp [-r] <src> <dest>` |
| `mv` | `mv <old> <new>` |
| `rm` | `rm [-rf] <path>` |
| `mkdir` | `mkdir [-p] <path>` |
| `rmdir` | `rmdir <path>` |
| `ln` | `ln [-s] <target> <link>` |
| `readlink` | `readlink <link>` |
| `truncate` | `truncate -s <length> <path>` |
| `cmp` | `cmp <path1> <path2>` |
| `md5` | `md5 <path>` |
| `dd` | `dd if=<in> of=<out> [bs=<size>] [count=<n>] [skip=<n>] [seek=<n>]` |
| `hexdump` | `hexdump <path>` |
| `mount` | `mount [-t <fstype> [-o <opts>] [<dev>] <mount-point>]` |
| `umount` | `umount <dir>` |

## 路径工具

| 命令 | 用法 |
|------|------|
| `basename` | `basename <path> [<suffix>]` |
| `dirname` | `dirname <path>` |
| `pwd` | `pwd` |
| `cd` | `cd <path>` |

## 进程管理

| 命令 | 用法 |
|------|------|
| `ps` | `ps [-heap] [pid ...]` |
| `kill` | `kill [-<signal>] <pid>` |
| `pkill` | `pkill [-<signal>] <name>` |
| `pidof` | `pidof <name>` |
| `wait` | `wait pid1 [pid2 ...]` |
| `nice` | `nice [-d <niceness>] <cmd>` |
| `sleep` | `sleep <sec>` |
| `usleep` | `usleep <usec>` |

## 系统信息

| 命令 | 用法 |
|------|------|
| `uname` | `uname [-a]` |
| `uptime` | `uptime` |
| `date` | `date [-s "MMM DD HH:MM:SS YYYY"]` |
| `df` | `df` |
| `free` | `free` |
| `dmesg` | `dmesg` |
| `env` | `env` |
| `resetcause` | `resetcause` |
| `fdinfo` | `fdinfo [pid]` |
| `time` | `time "<command>"` |

## 常见场景

- 看挂载和空间：先 `mount`，再 `df`
- 查进程和句柄：先 `ps`，再 `fdinfo [pid]`
- 对比文件或做快速校验：`cmp` / `md5`
