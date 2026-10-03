---
title: 运行时与媒体工具
description: Lua / QuickJS / WASM、网络工具、媒体能力与应用管理
---

# 运行时与媒体工具

## 脚本运行时

| 命令 | 说明 | 用法 |
|------|------|------|
| `lua` | Lua 5.4.0 解释器 | `lua [options] [file [args]]` |
| `qjs` | QuickJS 解释器，全局仅提供 `console` | `qjs -e 'code'` / `qjs file.js` |
| `iwasm` | WebAssembly Micro Runtime | `iwasm [-f <func>] [--stack-size=n] [--heap-size=n] <file.wasm>` |
| `vapp` | AIoT JS 应用引擎 | `vapp [options] [file]`，同 `aiot` |
| `aiotjsc` | AIoT JS 字节码编译器 | `aiotjsc [-o output] [-e] [-m] <file\|appdir>` |

## 网络工具

| 命令 | 说明 | 用法 |
|------|------|------|
| `curl` | HTTP/HTTPS/FTP/MQTT 客户端 | `curl [-X METHOD] [-d data] [-H header] [-o file] <url>` |
| `iperf` | 网络性能测试 | `iperf -s` / `iperf -c <ip> [-u] [-p port] [-t time] [-i interval]` |
| `ping` | ICMP Ping | `ping [-c <count>] [-i <interval>] [-W <timeout>] [-s <size>] <host>` |
| `wget` | HTTP 文件下载 | `wget [-o <local-path>] <url>` |
| `ftpd_start` | 启动 FTP 服务器 | `ftpd_start [-4\|-6]` |
| `ftpd_stop` | 停止 FTP 服务器 | `ftpd_stop` |
| `telnetd` | Telnet 服务守护进程 | `telnetd` |
| `renew` | DHCP 续租 | `renew` |

## 媒体

| 命令 | 说明 | 用法 |
|------|------|------|
| `ffmpeg` | 多媒体转码处理 | `ffmpeg [options] -i <input> [options] <output>` |
| `ffprobe` | 媒体文件信息查看 | `ffprobe <file>` |
| `nxplayer` | 交互式音频播放器（NxPlayer 1.05） | `nxplayer`，交互式环境可用 `h` 查看命令 |
| `nxrecorder` | 音频录制 | `nxrecorder` |
| `nxlooper` | 音频回环测试 | `nxlooper` |
| `mediad` | 媒体服务守护进程 | 自动启动 |
| `mediatool` | 媒体服务交互式调试 | `mediatool` |

### ffmpeg 能力概览

| 类别 | 编解码器 / 能力 |
|------|-----------------|
| 音频解码 | AAC (libhelix), AC3, FLAC, MP3, OPUS (libopus), Vorbis, AMR-NB/WB, ADPCM, SBC, LDAC, LC3 |
| 音频编码 | AAC, OPUS (libopus), AMR-NB, SBC, PCM, WavPack |
| 视频解码 | H.264, VP8, rawvideo |
| 视频编码 | MJPEG, MPEG4, rawvideo |
| 容器格式 | MP4, MP3, OGG, WAV, HLS, FLAC, AAC, AMR, MPEG-TS, SBC |
| 网络协议 | HTTP/HTTPS, FTP, TCP, UDP, RTP, TLS, HLS, Unix socket, rpmsg |
| 设备 | bluelet, fbdev, nuttx, V4L2 |

## 应用管理

| 命令 | 说明 | 用法 |
|------|------|------|
| `am` | Activity Manager | `am <start\|stop> <packagename>` |
| `pm` | 包管理器 | `pm <install\|uninstall> [packagename\|rpkfile]` |
| `vappmonitor` | 虚拟应用监控 | `vappmonitor <arg1> <arg2>` |
