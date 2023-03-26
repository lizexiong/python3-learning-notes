#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:19
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : ProsAndConsQuery2.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



# 查询所有班级中的所有学生，学生表中有relationship，并且它的backref为have_student，所以我们可以通过班级.have_student来获取所有学生记录

# 另外，对于班级来说，学生可以有多个，所以have_student应当是一个序列

# 获取链接池、ORM表对象
import models

classes_lst = models.session.query(
    models.ClassesInfo
).all()

for row in classes_lst:
    print("class name :", row.name)
    for student in row.have_student:
        print("student name :", student.name)

# class name : one year one class
#      student name : Jack
#      student name : Anna
# class name : one year two class
#      student name : Tom
# class name : one year three class
#      student name : Mary
#      student name : Bobby

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()



