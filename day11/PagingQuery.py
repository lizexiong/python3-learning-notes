#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 14:12
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : PagingQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



# 获取链接池、ORM表对象
import models

result = models.session.query(
    models.UserInfo,
).all()[0:1]

# 过滤成功的结果数量
print(len(result))
# 1

# 过滤成功的结果
print(result)
# [<models.UserInfo object at 0x7fee1614f4f0>]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()