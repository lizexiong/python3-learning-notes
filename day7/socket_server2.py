












#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1',9990)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print ('server waiting...')
    conn,addr = sk.accept()

    client_data = conn.recv(1024)
    print (str(client_data,'utf8'))         #接收到客户端的东西要转成str
    conn.sendall(bytes('不要回答,不要回答,不要回答','utf8'))    #这里发送的时候要转成bytes

    while True:
        try:
            client_data = conn.recv(1024)
            print ("client_data:",str(client_data,'utf8'))
            if not client_data:break;
        except Exception:
            print ('test')
            break
        conn.send(client_data)
    conn.close()