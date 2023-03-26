#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:23
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : JoinQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

from sqlalchemy import func

result = models.session.query(
    models.ClassesInfo.name,
    func.count(models.StudentsInfo.id)
).join(
    models.StudentsInfo,
    models.ClassesInfo.id == models.StudentsInfo.fk_class_id
).group_by(
    models.ClassesInfo.id
).all()

print(result)
# [('one year one class', 2), ('one year two class', 2), ('one year three class', 1)]


# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()