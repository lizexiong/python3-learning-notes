











#!/bin/bash


import json,os,sys

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


