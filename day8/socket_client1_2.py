#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 00:23
# @Author  : 李泽雄
# @Site    : 
# @File    : socket_client1_2.py
# @Project : python3
# @Software: PyCharm



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 00:07
# @Author  : 李泽雄
# @Site    :
# @File    : socket_client1.py
# @Project : python3
# @Software: PyCharm




import socket

ip_port = ("127.0.0.1",9999)

sk = socket.socket()

sk.connect(ip_port)
sk.settimeout(500)


while True:
    data = sk.recv(1024)
    print ("服务端返回:",data)
    l = input("请输入值:")
    sk.sendall(bytes(l,encoding='utf8'))
    if l == "exit":
        break

sk.close()