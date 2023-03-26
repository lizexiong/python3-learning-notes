#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 14:02
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : ConditionQueryOr.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models
# 导入OR
from sqlalchemy import or_

result = models.session.query(
    models.UserInfo,
).filter(
    or_(
        models.UserInfo.name == "Jackson",
        models.UserInfo.gender == "male"
    )
).all()

# 过滤成功的结果数量
print(len(result))
# 1

# 过滤成功的结果
print(result)
# [<models.UserInfo object at 0x7f11391ea2b0>]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()