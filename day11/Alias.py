#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 12:51
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : Alias.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

result = models.session.query(
    models.UserInfo.name.label("s_name"),
    models.UserInfo.age.label("s_age")
).all()

for row in result:
    print(row.s_name)
    print(row.s_age)


# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()