#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.internet import protocol
from twisted.internet import reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):#只要twisted一收到 数据 ，就会调用 此方法
        self.transport.write(data) # 把收到的数据 返回给客户端

def main():
    factory = protocol.ServerFactory() #定义基础工厂类
    factory.protocol = Echo #socketserver 中handle

    reactor.listenTCP(9000,factory)
    reactor.run()

if __name__ == '__main__':
    main()