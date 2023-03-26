#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 12:20
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : BatchAddition.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models


user_instance1 = models.UserInfo(
    name="Tom",
    age=19,
    phone=330624,
    address="Shanghai",
    gender="male"
)

user_instance2 = models.UserInfo(
    name="Mary",
    age=20,
    phone=330623,
    address="Chongqing",
    gender="female"
)


models.session.add_all(
    (
        user_instance1,
        user_instance2
    )
)

# 提交
models.session.commit()
# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()