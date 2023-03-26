#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 14:15
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : AggregateQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models
# 导入聚合函数
from sqlalchemy import func

result = models.session.query(
    func.sum(models.UserInfo.age)
).group_by(
    models.UserInfo.gender
).having(
    func.sum(models.UserInfo.id > 1)
).all()

# 过滤成功的结果数量
print(len(result))
# 1

# 过滤成功的结果
print(result)
# [(Decimal('38'),)]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()