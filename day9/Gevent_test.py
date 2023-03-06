#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 00:12
# @Author  : 李泽雄
# @Site    : 
# @File    : Gevent_test.py
# @Project : python3
# @Software: PyCharm


import gevent


def func1():
    print('\033[31;1m 1 \033[0m')
    gevent.sleep(2)
    print('\033[31;1m 2 \033[0m')


def func2():
    print('\033[32;1m 3 \033[0m')
    gevent.sleep(1)
    print('\033[32;1m 4 \033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    # gevent.spawn(func3),
])