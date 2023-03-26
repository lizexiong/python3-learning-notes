#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:09
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : INNERJOIN.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

result = models.session.query(
    models.StudentsInfo.name,
    models.StudentsNumberInfo.number,
    models.ClassesInfo.number
).join(
    models.StudentsNumberInfo,
    models.StudentsInfo.fk_student_id == models.StudentsNumberInfo.id
).join(
    models.ClassesInfo,
    models.StudentsInfo.fk_class_id == models.ClassesInfo.id
).all()

print(result)
# [('Jack', 160201, 1602), ('Tom', 160101, 1601), ('Mary', 160301, 1603), ('Anna', 160102, 1601), ('Bobby', 160202, 1602)]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()