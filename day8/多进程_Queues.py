#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 21:52
# @Author  : 李泽雄
# @Site    : 
# @File    : 多进程_Queues.py
# @Project : python3
# @Software: PyCharm


from multiprocessing import Process, Queue  #这里的queue是多进程模块里面的，具体的下一章在进行讲解


def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()