#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/27 18:43
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 自定义web框架2.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from wsgiref.simple_server import make_server
import urls





#wsgi内部，也就是make_server调用这个函数的时候会把参数自动传过来，把所有如端口，地址等信息封装起来，传给我们自己的web框架，也就是RunServer
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]
    url = environ['PATH_INFO']
    if url in urls.routes.keys():
        func_name = urls.routes[url]
        ret = func_name()
        return [bytes(ret,encoding='utf-8')]
    else:
        return [bytes("404",encoding='utf-8')]


if __name__ == '__main__':
    #创建socket server对象
    httpd = make_server('', 8001, RunServer)
    print("Serving HTTP on port 8001...")
    #等待用户请求到来
    #只要有请求进来，执行Runserver函数

    httpd.serve_forever()