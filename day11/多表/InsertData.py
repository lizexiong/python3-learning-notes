#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:06
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : InsertData.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models
import datetime


models.session.add_all(
    (
        # 插入学号表数据
        models.StudentsNumberInfo(
            number=160201,
            admission=datetime.datetime.date(datetime.datetime(2016, 9, 1)),
            graduation=datetime.datetime.date(datetime.datetime(2021, 6, 15))
        ),
        models.StudentsNumberInfo(
            number=160101,
            admission=datetime.datetime.date(datetime.datetime(2016, 9, 1)),
            graduation=datetime.datetime.date(datetime.datetime(2021, 6, 15))
        ),
        models.StudentsNumberInfo(
            number=160301,
            admission=datetime.datetime.date(datetime.datetime(2016, 9, 1)),
            graduation=datetime.datetime.date(datetime.datetime(2021, 6, 15))
        ),
        models.StudentsNumberInfo(
            number=160102,
            admission=datetime.datetime.date(datetime.datetime(2016, 9, 1)),
            graduation=datetime.datetime.date(datetime.datetime(2021, 6, 15))
        ),
        models.StudentsNumberInfo(
            number=160302,
            admission=datetime.datetime.date(datetime.datetime(2016, 9, 1)),
            graduation=datetime.datetime.date(datetime.datetime(2021, 6, 15))
        ),
        models.StudentsNumberInfo(
            number=160202,
            admission=datetime.datetime.date(datetime.datetime(2016, 9, 1)),
            graduation=datetime.datetime.date(datetime.datetime(2021, 6, 15))
        ),
        # 插入教师表数据
        models.TeachersInfo(
            number=3341, name="David", gender="male", age=32,
        ),
        models.TeachersInfo(
            number=3342, name="Jason", gender="male", age=30,
        ),
        models.TeachersInfo(
            number=3343, name="Lisa", gender="female", age=28,
        ),
        # 插入班级表数据
        models.ClassesInfo(
            number=1601, name="one year one class", fk_teacher_id=1
        ),
        models.ClassesInfo(
            number=1602, name="one year two class", fk_teacher_id=2
        ),
        models.ClassesInfo(
            number=1603, name="one year three class", fk_teacher_id=3
        ),
        # 插入中间表数据
        models.ClassesAndTeachersRelationship(
            fk_class_id=1, fk_teacher_id=1
        ),
        models.ClassesAndTeachersRelationship(
            fk_class_id=2, fk_teacher_id=1
        ),
        models.ClassesAndTeachersRelationship(
            fk_class_id=3, fk_teacher_id=1
        ),
        models.ClassesAndTeachersRelationship(
            fk_class_id=1, fk_teacher_id=2
        ),
        models.ClassesAndTeachersRelationship(
            fk_class_id=3, fk_teacher_id=3
        ),
        # 插入学生表数据
        models.StudentsInfo(
            name="Jack", gender="male", age=17, fk_student_id=1, fk_class_id=2
        ),
        models.StudentsInfo(
            name="Tom", gender="male", age=18, fk_student_id=2, fk_class_id=1
        ),
        models.StudentsInfo(
            name="Mary", gender="female", age=16, fk_student_id=3,
            fk_class_id=3
        ),
        models.StudentsInfo(
            name="Anna", gender="female", age=17, fk_student_id=4,
            fk_class_id=1
        ),
        models.StudentsInfo(
            name="Bobby", gender="male", age=18, fk_student_id=6, fk_class_id=2
        ),
    )
)

models.session.commit()

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()