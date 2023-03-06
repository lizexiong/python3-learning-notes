#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 00:19
# @Author  : 李泽雄
# @Site    : 
# @File    : 简单queue.py
# @Project : python3
# @Software: PyCharm


import queue

#这里只是一个测试类,测试queue可以消费什么类型的数据
class TestClass(object):
    def __init__(self):
        pass

#队列最大长度为三个
q = queue.Queue(maxsize=3)
#可以传输列表类型
q.put([1,2,3])
#可以传输类
q.put(TestClass())
#可以传输字符串
q.put("lizexiong")
#第四个插入，超过列表长度
#q.put("four")

'''
课堂演示
1.列表最大长度为3个
2.q.full查看队列是不是满的
3.q.enpty查看队列是不是空的
4.如果队列只有三个，如果get有4个什么结果
'''
print (q.full())
print (q.get())
print (q.get())
print (q.get())
print (q.get())
print (q.full())
print (q.empty())