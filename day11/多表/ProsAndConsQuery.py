#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 15:16
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : ProsAndConsQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



# 查询所有学生的所在班级，我们可以通过学生的from_class字段拿到其所在班级
# 另外，对于学生来说，班级只能有一个，所以have_student应当是一个对象

# 获取链接池、ORM表对象
import models

students_lst = models.session.query(
    models.StudentsInfo
).all()

for row in students_lst:
    print(f"""
            student name : {row.name}
            from : {row.from_class.name}
          """)

# student name : Mary
# from : one year three class

# student name : Anna
# from : one year one class

# student name : Bobby
# from : one year two class

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()