#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:13
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : union.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



# 获取链接池、ORM表对象
import models

students_name = models.session.query(models.StudentsInfo.name).filter()
students_number = models.session.query(models.StudentsNumberInfo.number)\
    .filter()
class_name = models.session.query(models.ClassesInfo.name).filter()

result = students_name.union_all(students_number).union_all(class_name)

print(result.all())
# [
#      ('Jack',), ('Tom',), ('Mary',), ('Anna',), ('Bobby',),
#      ('160101',), ('160102',), ('160201',), ('160202',), ('160301',), ('160302',),
#      ('one year one class',), ('one year three class',), ('one year two class',)
# ]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()