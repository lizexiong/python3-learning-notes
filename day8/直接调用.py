#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 23:09
# @Author  : 李泽雄
# @Site    : 
# @File    : 直接调用.py
# @Project : python3
# @Software: PyCharm


import threading
import time


def sayhi(num):  # 定义每个线程要运行的函数

    print("running on number:%s" % num)

    time.sleep(3)


if __name__ == '__main__':

    #2.所以这里有一个列表，我们把实例添加到列表里面，然后在用一个for循环执行出去，那么就是即使加了join还是可以实现多线程，这样就可以实现并发执行所有子线程，并且所有子线程执行完成后才退出程序
    t_list = []
    for i in range(10):
        t = threading.Thread(target=sayhi,args=[i,])
        t.start()
        #1.如果这里t.join,那么还是会阻塞，因为循环一次完成后才会循环到下次
        #3.添加实例到列表
        t_list.append(t)

    #4循环刚才的实例,循环刚才的线程实例
    for i in t_list:
        print (i)
        i.join()


    '''
        t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
    t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例

    t1.start()  # 启动线程
    t2.start()  # 启动另一个线程


    print(t1.name)  # 获取线程名
    print(t2.name)
    t2.join()   #t2.wait()
    print ("---main---")
    '''
