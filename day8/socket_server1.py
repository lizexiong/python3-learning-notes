#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 23:55
# @Author  : 李泽雄
# @Site    : 
# @File    : socket_server1.py
# @Project : python3
# @Software: PyCharm




# SocketServer实现服务器
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver

class MyServer(socketserver.BaseRequestHandler):

    #这里的handle是固定用法，主要填入服务端的处理
    def handle(self):
        # print self.request,self.client_address,self.server父类方法里面就有
        conn = self.request
        print ("是谁连接过来",self.client_address)
        conn.sendall(bytes("欢迎致电 10086，请输入10000,0转人工服务.", encoding='utf8'))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            if data == 'exit':
                Flag = False
            else:
                print (data)
                conn.sendall(bytes('请重新输入.',encoding='utf8'))


if __name__ == '__main__':
    #就是这里实现多线程,把刚才写的类当作参数传给ThreadingTCPServer这个类
    #简单来说就是来一个客户端连接就实例化一个对象,使用多线程实现多客户端连接
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    #启动这个server,这个server会一直运行，除非CTRL+C停止
    server.serve_forever()


