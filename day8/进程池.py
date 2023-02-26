#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 23:37
# @Author  : 李泽雄
# @Site    : 
# @File    : 进程池.py
# @Project : python3
# @Software: PyCharm


from multiprocessing import Process, Pool ,freeze_support
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)



if __name__ == "__main__":
    freeze_support() #windows上必须加，不然进程就回hold住，卡死
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        # pool.apply(func=Foo, args=(i,))  #如果是apply使用同步？那我干嘛还需要多进程？

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。