#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:26
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 正反查询.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

david = models.session.query(
    models.TeachersInfo
).filter(
    models.TeachersInfo.name == "David"
).first()

student_lst = []

# 反向查询拿到任教班级，反向是一个列表，所以直接for
for row in david.mid:
    cls = row.mid_to_class
    # 通过任教班级，反向拿到其下的所有学生
    cls_students = cls.have_student
    # 遍历学生
    for student in cls_students:
        student_lst.append(
            (
                david.name,
                student.name,
                student.age,
                cls.name
            )
        )

# 筛选出年龄最小的
min_age_student_lst = sorted(
    student_lst, key=lambda tpl: tpl[2])[0]

print(min_age_student_lst)
# ('David', 'Mary', 16, 'one year three class')

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()