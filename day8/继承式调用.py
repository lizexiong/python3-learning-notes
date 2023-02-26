#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 23:12
# @Author  : 李泽雄
# @Site    : 
# @File    : 继承式调用.py
# @Project : python3
# @Software: PyCharm


import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        print("running on number:%s" % self.num)

        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()