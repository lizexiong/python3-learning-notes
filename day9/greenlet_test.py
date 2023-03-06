#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 00:08
# @Author  : 李泽雄
# @Site    : 
# @File    : greenlet_test.py
# @Project : python3
# @Software: PyCharm


# -*- coding:utf-8 -*-


from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()