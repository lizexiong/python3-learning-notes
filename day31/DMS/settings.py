#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/30 18:47
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : settings.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



template_variables = dict(
    title=u'Docker管理平台',
    name =u'Docker管理平台',
    username="",
)

DATABASES = dict(
    DB='DMS',
    USERNAME='root',
    PASSWORD='huawei',
    HOST='127.0.0.1',
    PORT=3306,
)

NODE_LIST = ['node_ip', 'port']

COOKIE_NAME  = "user_id"