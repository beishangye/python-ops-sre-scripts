#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import datetime

# 阈值设置（可修改）
CPU_THRESHOLD = 80   # 百分比
MEM_THRESHOLD = 90   # 百分比

def check_cpu():
    """获取 CPU 使用率（取 1 秒采样）"""
    return psutil.cpu_percent(interval=1)

def check_memory():
    """获取内存使用率（百分比）"""
    mem = psutil.virtual_memory()
    return mem.percent

def main():
    cpu_usage = check_cpu()
    mem_usage = check_memory()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if cpu_usage > CPU_THRESHOLD:
        print(f"⚠️ [{now}] CPU 使用率过高：{cpu_usage}% (阈值 {CPU_THRESHOLD}%)")
    elif mem_usage > MEM_THRESHOLD:
        print(f"⚠️ [{now}] 内存使用率过高：{mem_usage}% (阈值 {MEM_THRESHOLD}%)")
    else:
        print(f"✅ [{now}] 服务器状态正常 | CPU: {cpu_usage}% | 内存: {mem_usage}%")

if __name__ == "__main__":
    main()