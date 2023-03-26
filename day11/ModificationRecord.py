#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 12:25
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : ModificationRecord.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

# 修改的信息：
#  - Jack -> Jack + son
# 在SQLAlchemy中，四则运算符号只能用于数值类型
# 如果是字符串类型需要在原本的基础值上做改变，必须设置
#  - age -> age + 1
# synchronize_session=False

models.session.query(models.UserInfo)\
    .filter_by(name="Jack")\
    .update(
        {
            "name": models.UserInfo.name + "son",
            "age": models.UserInfo.age + 1
        },
        synchronize_session=False
)
# 本次修改具有字符串字段在原值基础上做更改的操作，所以必须添加
# synchronize_session=False
# 如果只修改年龄，则不用添加

# 提交
models.session.commit()
# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()