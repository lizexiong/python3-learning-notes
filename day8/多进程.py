#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 21:10
# @Author  : 李泽雄
# @Site    : 
# @File    : multiprocessing.py
# @Project : python3
# @Software: PyCharm

#
# from multiprocessing import Process
# import time
#
#
# def f(name):
#     time.sleep(2)
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()