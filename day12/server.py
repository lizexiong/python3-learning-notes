#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/27 0:19
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : server.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm




import socket

def handler_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK \r\n\r\n","UTF-8"))
    f = open('template.html','r',encoding='utf8')
    data = f.read()
    f.close()
    client.send(bytes(data,'UTF-8'))
    #client.send(bytes("<h1 style='color:red'> LiZeXiong </h1>","UTF-8"))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8003))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handler_request(connection)

if __name__ == "__main__":
    main()