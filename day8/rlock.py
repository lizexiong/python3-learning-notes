#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 14:10
# @Author  : 李泽雄
# @Site    : 
# @File    : rlock.py
# @Project : python3
# @Software: PyCharm


import threading, time

def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)


if __name__ == '__main__':

    num, num2 = 0, 0
    '''
    如果不加入Rock，那么这么多锁，锁就混乱了，不知道谁是谁的锁，输出的结果一定是一个死循环
    rlock可以理解成为一个锁关系的记录表,让每一层知道谁是谁的锁。
    '''
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)