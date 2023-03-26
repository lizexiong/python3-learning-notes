#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 13:58
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : ConditionQuery.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 获取链接池、ORM表对象
import models

result = models.session.query(
    models.UserInfo,
).filter(
    models.UserInfo.name == "Jackson"
).all()

# 上面是Python语句形式的过滤条件，由filter方法调用
# 亦可以使用ORM的形式进行过滤，通过filter_by方法调用
# 如下所示
# .filter_by(name="Jackson").all()
# 个人更推荐使用filter过滤，它看起来更直观，更简单，可以支持 == != > < >= <=等常见符号

# 过滤成功的结果数量
print(len(result))
# 1

# 过滤成功的结果
print(result)
# [<models.UserInfo object at 0x7f11391ea2b0>]

# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()