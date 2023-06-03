#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/30 18:53
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : user.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


""" 执行mysql语句 """
import hashlib

from settings import DATABASES
from .mysql_server import MysqlServer

class UserSqlOperation(object):
    @staticmethod
    def check_adm_login(admname):
        db = MysqlServer(DATABASES)
        sql = "select `name`,`password`,`user_group` from user where name='%s'" % admname
        ret = db.run_sql(sql)
        db.close()
        return ret