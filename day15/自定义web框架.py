#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/27 17:43
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 自定义web框架.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from wsgiref.simple_server import make_server

def f1():
    f = open('f1.html',encoding='utf-8')
    data = f.read()
    f.close()
    import time
    db_str = str(time.time())
    data = data.replace('F1',db_str)
    return data

def f2():
    from jinja2 import  Template
    f = open('f2.html',encoding='utf-8')
    result = f.read()
    template = Template(result)
    #接收值，进行特殊的替换
    data = template.render(name='lizexiong',user_list=['wuxinzhe','liuwen'])
    return data

routes = {
    "/index/":f1,
    "/news/":f2,
}

#wsgi内部，也就是make_server调用这个函数的时候会把参数自动传过来，把所有如端口，地址等信息封装起来，传给我们自己的web框架，也就是RunServer
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]
    url = environ['PATH_INFO']
    if url in routes.keys():
        func_name = routes[url]
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