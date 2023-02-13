












#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket



#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9990)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('请求占领地球','utf8'))          #python3发送给服务端的要转成bytes

server_reply = sk.recv(1024)
print (str(server_reply,'utf8'))                #接收来自服务端的消息转成str

while True:
    user_input = input(">>:").strip()
    sk.send(bytes(user_input,'utf-8'))
    server_reply = sk.recv(1024)
    print ("server_reply:",str(server_reply,'utf8'))

sk.close()

