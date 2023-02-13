







#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket



#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)


while True:
    user_input = input("cmd>>:").strip()
    #如果用户输入为0,跳出这次循环,进入下一次循环,这个空格不会到服务端
    if len(user_input) == 0:continue
    #如果用户输入q直接退出整个shell客户端
    if user_input == 'q':break
    #把用户输入的命令发送给服务端(发送给服务端的格式只能是bytes)
    sk.send(bytes(user_input,'utf-8'))
    #接收来自服务器命令执行之后的结果
    server_reply = sk.recv(1024)
    #将结果转成str打印出来
    print ("server_reply:",str(server_reply,'utf8'))

sk.close()

