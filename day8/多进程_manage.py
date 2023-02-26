#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 23:10
# @Author  : 李泽雄
# @Site    : 
# @File    : 多进程_manage.py
# @Project : python3
# @Software: PyCharm


from multiprocessing import Process, Manager


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)