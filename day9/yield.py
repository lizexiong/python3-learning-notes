#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 23:56
# @Author  : 李泽雄
# @Site    :
# @File    : yield.py
# @Project : python3
# @Software: PyCharm


import time
import queue
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield   #2.yield给了new_baozi
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)

def producer():
    r = con.__next__()    #碰到yield的时候，需要手动__next__才能走下一步
    r = con2.__next__()
    n = 0
    while n < 3:
        n += 1
        con.send(n)   #1.send给了yield
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)

if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()