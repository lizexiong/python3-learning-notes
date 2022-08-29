











#!/bin/bash


import json,os,sys

#银行用户信息写入查询模块,直接调用数据库交互
#这里的交互也不太智能,数据库所需要的用户信息以及字段必须存在,否则就会报错,该问题在银行的账单处理模块得到解决
def BankUserInfo(action='read',username="None",parameter="None",parameter_value="None"):
    with open('bank/databases/BankUserDB', 'r+') as db_read,open('bank/databases/BankUserDBBak','w+') as db_write:
        if action == "read":
            return json.loads(db_read.read())
        elif action == "write":
            ALLDbInfo = json.loads(db_read.read())
            ALLDbInfo[username][parameter] = parameter_value
            db_write.write(json.dumps(ALLDbInfo))
    os.rename('bank/databases/BankUserDB','bank/databases/BankUserDBTMP')
    os.rename('bank/databases/BankUserDBBak', 'bank/databases/BankUserDB')
    os.remove('bank/databases/BankUserDBTMP')


