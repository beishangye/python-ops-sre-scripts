#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运维脚本：内存使用率监控
功能：执行 free -m 命令，计算并输出内存使用率
"""

import subprocess
import re

# 执行 free -m 命令并获取输出
result = subprocess.run(['free', '-m'], capture_output=True, text=True)

# 按行切割输出
lines = result.stdout.strip().split('\n')

# 遍历每一行，找到以 "Mem:" 开头的那一行
for line in lines:
    if line.startswith('Mem:'):
        # 按空白字符切割这一行
        parts = re.split(r'\s+', line)
        
        # 提取关键数据
        total = int(parts[1])   # 总内存 (MB)
        used = int(parts[2])    # 已用内存 (MB)
        avail = int(parts[6])   # 可用内存 (MB)
        
        # 计算使用率
        percent = (used / total) * 100
        
        # 输出结果
        print(f"内存使用率: {percent:.1f}%")
        
        # 找到后不再继续循环
        break