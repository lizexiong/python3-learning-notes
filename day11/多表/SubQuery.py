#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:14
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : SubQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



# 获取链接池、ORM表对象
import models
from sqlalchemy import func

# 子查询中所有字段的访问都需要加上c的前缀
# 如 sub_query.c.id、 sub_query.c.name等
sub_query = models.session.query(
    # 使用label()来为字段AS一个别名
    # 后续访问需要通过sub_query.c.alias进行访问
    func.min(models.StudentsInfo.age).label("min_age"),
    models.ClassesInfo.id,
    models.ClassesInfo.name
).join(
    models.ClassesInfo,
    models.StudentsInfo.fk_class_id == models.ClassesInfo.id
).group_by(
    models.ClassesInfo.id
).subquery()


result = models.session.query(
    models.StudentsInfo.name,
    sub_query.c.min_age,
    sub_query.c.name
).join(
    sub_query,
    sub_query.c.id == models.StudentsInfo.fk_class_id
).filter(
   sub_query.c.min_age == models.StudentsInfo.age
)

print(result.all())
# [('Jack', 17, 'one year two class'), ('Mary', 16, 'one year three class'), ('Anna', 17, 'one year one class')]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()