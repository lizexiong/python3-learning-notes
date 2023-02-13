#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import time


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
    server_ack_msg = sk.recv(100)
    print ("server_response",str(server_ack_msg,'utf8'))
    cmd_res_msg = str(server_ack_msg,'utf8').split('|')
    if cmd_res_msg[0] == "CMD_RESULT_SIZE":
        cmd_res_size = int(cmd_res_msg[1])
        #多发送一个确认代码给服务端，避免一条命令过长有沾包的问题
        sk.send(b"CLIENT_READY_TO_RECV")
    #字符串的总变量,所有接收到的字符串都集中在这里
    res = ""
    #客户端接收的长度
    received_size = 0
    #如果客户端接收的长度小于总长度,那么代表没有接收完成,那么就需要一直接收
    while received_size < cmd_res_size:
        #每次接收500
        data = sk.recv(500)
        #并且更改接收长度
        received_size += len(data)
        #并且把每次接收的字符汇总到res里面
        res += str(data,'utf8')
    else:
        #如果客户端接收的长度不小于总长度，那么代表接收完成，可以打印了
        print (res)
        print ("-----------recv done-----------")

sk.close()
