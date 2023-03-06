#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 00:39
# @Author  : 李泽雄
# @Site    : 
# @File    : gevent_spawn.py
# @Project : python3
# @Software: PyCharm


from gevent import monkey;

monkey.patch_all()
import gevent
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])