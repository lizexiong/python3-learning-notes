#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 12:42
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : SingleTableQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

result = models.session.query(models.UserInfo).all()

print(result)
# [<models.UserInfo object at 0x7f4d3d606fd0>, <models.UserInfo object at 0x7f4d3d606f70>]

for row in result:
    print(row)
# object : <id:1 name:Jackson>
# object : <id:2 name:Tom>

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()