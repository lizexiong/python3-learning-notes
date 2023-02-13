


#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
改代码只能在linux系统下测试
'''


import socket,subprocess

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print ('server waiting...')
    conn,addr = sk.accept()

    while True:
        #接收来自客户端的命令并打印出来（不管是发送还是接收的都是bytes格式）
        client_data = conn.recv(1024)
        print ("client_cmd:",str(client_data,'utf8'))
        #如果客户端没有数据，直接跳出这次循环,一般是客户端断开后防止死循环
        if not client_data:break;
        #将客户端的命令转成成为str用subprocess执行
        cmd = str(client_data,'utf8').strip()
        cmd_call = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        cmd_result = cmd_call.stdout.read()
        #如果客户端返回的结果==0，那么代表执行的就是如cd,或者命令执行出错了，那么就返回我们自定义的提示
        if len(cmd_result) == 0:
            cmd_result = b'cmd executio has no output' #（不管是发送还是接收的都是bytes格式）
        print (cmd_result,type(cmd_result),str(cmd_result,'utf8'))
        conn.send(cmd_result)
    conn.close()







