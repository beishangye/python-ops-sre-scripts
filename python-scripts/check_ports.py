#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 配置
TARGET_IP = "127.0.0.1"          # 可改为远程 IP
PORT_LIST = [22, 80, 443, 3306, 8080]   # 待检测端口
TIMEOUT = 2   # 连接超时（秒）

def check_port(ip, port, timeout=TIMEOUT):
    """尝试连接目标端口，返回 True 表示开放"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            return result == 0   # 0 表示连接成功
    except Exception:
        return False

def main():
    print(f"========== 端口扫描结果 (目标: {TARGET_IP}) ==========")
    for port in PORT_LIST:
        if check_port(TARGET_IP, port):
            print(f"✅ 端口 {port} 开放")
        else:
            print(f"❌ 端口 {port} 关闭或不可达")
    print("==================================================")

if __name__ == "__main__":
    main()

