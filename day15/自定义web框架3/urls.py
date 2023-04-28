#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/27 19:40
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from controllers import test

routes = {
    "/index/":test.f1,
    "/news/":test.f2,
}

