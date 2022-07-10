











#!/bin/bash


import json,os,sys


def BankUserInfo(action='read',username="None",parameter="None",parameter_value="None"):
    with open('bank/databases/BankUserInfo', 'r+') as db_read,open('bank/databases/bank_user_info_bak','w+') as db_write:
        if action == "read":
            return json.loads(db_read.read())
        elif action == "write":
            ALLDbInfo = json.loads(db_read.read())
            ALLDbInfo[username][parameter] = parameter_value
            db_write.write(json.dumps(ALLDbInfo))
    os.rename('bank/databases/BankUserInfo','bank/databases/bank_user_info_tmp')
    os.rename('bank/databases/bank_user_info_bak', 'bank/databases/BankUserInfo')
    os.remove('bank/databases/bank_user_info_tmp')
