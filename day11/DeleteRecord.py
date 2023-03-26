#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 12:28
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : DeleteRecord.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm

# 获取链接池、ORM表对象
import models

models.session.query(models.UserInfo).filter_by(name="Mary").delete()

# 提交
models.session.commit()
# 关闭链接，亦可使用session.remove()，它将回收该链接
models.session.close()
