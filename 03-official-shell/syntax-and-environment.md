---
title: 语法与运行环境
description: nsh 的基本命令格式、语法差异、文件系统和环境变量
---

# 语法与运行环境

## 命令格式

```text
[nice [-d <niceness>]] <cmd> [> <file>|>> <file>] [&]
```

## 支持的语法

| 特性 | 语法 |
|------|------|
| 分号链 | `cmd1; cmd2` |
| 管道 | `cmd1 \| cmd2` |
| 输出重定向 | `cmd > file`、`cmd >> file` |
| 变量赋值 | `set name value` |
| 变量引用 | `echo $name` |
| 后台执行 | `cmd &` |
| 条件测试 | `test -f path`、`[ -f path ]` |
| 算术 | `expr 1 + 2` |
| 脚本 | `source file.sh` |
| 子 shell | `sh -c 'cmd'` |

## 控制流

```sh
if test -f /tmp/file.txt
then
  echo exists
else
  echo not found
fi
```

```sh
while test $i -lt 3
do
  echo $i
  set i $(expr $i + 1)
done
```

`until/do/done` 同样可用。

## 不支持的能力

| 特性 | 说明 |
|------|------|
| `$(cmd)` | 命令替换不可用 |
| `&&` / `\|\|` | 逻辑链不可用，用 `;` 替代 |
| `2>&1` / `2>file` | stderr 重定向不可用 |
| 通配符 `*` `?` | 不支持 glob 展开 |
| `grep` / `sed` / `awk` | 默认不存在 |

## 文件系统

| 挂载点 | 类型 | 读写 |
|--------|------|------|
| `/data` | fatfs | 可读写 |
| `/tmp` | tmpfs | 可读写，重启后清空 |
| 其余系统目录 | romfs | 只读 |

## 环境变量

```sh
env
```

| 变量 | 示例值 |
|------|--------|
| `PWD` | `/` |
| `TZ` | `Asia/Shanghai` |

## 使用建议

- 涉及脚本时优先使用 `set`、`test`、`expr` 这一套内建能力。
- 写临时文件建议放在 `/tmp`，持久数据放到 `/data`。
- 需要复杂文本处理时，通常要转到宿主机脚本或更高层工具完成。
