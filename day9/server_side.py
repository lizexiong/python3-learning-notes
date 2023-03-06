#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 00:48
# @Author  : 李泽雄
# @Site    : 
# @File    : server_side.py
# @Project : python3
# @Software: PyCharm


import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()
'''
这里主要是monkey的使用，这里是python中的黑魔法，比如很多python不管是读io还是网络接口，
很多都是阻塞的，这个monkey，就自动的把很多变成非阻塞的，具体原理没有研究，有兴趣的小伙伴可以自己研究.
简单来说，这老师啥都没讲，就说这个monkey自动把阻塞的变成非阻塞了。。。
'''

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    while True:
        cli, addr = s.accept()
        #通过spawn调用一个新的协程。调用handler_request传入进去，在把客户端的对象也传入进去
        gevent.spawn(handle_request, cli)

def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as ex:
        print(ex)
    finally:
        conn.close()

if __name__ == '__main__':
    server(8001)