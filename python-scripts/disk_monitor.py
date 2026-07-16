#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运维脚本：磁盘使用率监控
功能：执行 df -h 命令，过滤出根目录(/)的使用率，并输出告警信息
作者：beishangye
创建日期：2026-07-04
"""

import subprocess
import re

def get_disk_usage():
    """
    执行系统命令并提取关键信息
    """
    try:
        # 执行 df -h 命令并获取输出
        result = subprocess.run(['df', '-h'], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # 按行分割
        lines = output.strip().split('\n')
        
        print("=== 磁盘使用情况 ===")
        for line in lines[1:]:  # 跳过表头
            # 使用正则表达式或 split 分割空白字符
            parts = re.split(r'\s+', line)
            if len(parts) >= 5:
                filesystem = parts[0]
                size = parts[1]
                used = parts[2]
                avail = parts[3]
                use_percent = parts[4]
                mount_point = parts[5] if len(parts) > 5 else ""
                
                # 过滤无用字符（去掉 % 符号，只保留数字）
                use_num = int(use_percent.replace('%', ''))
                
                # 如果挂载点是根目录，且使用率超过 80%，发出警告
                if mount_point == '/' and use_num > 80:
                    print(f"⚠️ [告警] 根目录使用率: {use_percent} (已超过80%)")
                else:
                    print(f"{mount_point or filesystem}: {use_percent}")
    
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
    except Exception as e:
        print(f"脚本运行异常: {e}")

if __name__ == "__main__":
    get_disk_usage()