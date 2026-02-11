#!/usr/bin/env python3
"""Simple FTP Server"""
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

def main():
    # 创建授权器
    authorizer = DummyAuthorizer()

    # 添加匿名用户，根目录为当前目录，有读取权限
    current_dir = os.getcwd()
    authorizer.add_anonymous(current_dir, perm='elradfmw')

    # 创建FTP处理器
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "Welcome to Python FTP Server."

    # 设置服务器地址和端口
    address = ('0.0.0.0', 2121)
    server = FTPServer(address, handler)

    # 设置最大连接数
    server.max_cons = 256
    server.max_cons_per_ip = 5

    print(f"FTP服务器已启动！")
    print(f"地址: ftp://localhost:2121")
    print(f"根目录: {current_dir}")
    print(f"访问方式: ftp://anonymous@localhost:2121")
    print("按 Ctrl+C 停止服务器")

    # 启动服务器
    server.serve_forever()

if __name__ == '__main__':
    main()
