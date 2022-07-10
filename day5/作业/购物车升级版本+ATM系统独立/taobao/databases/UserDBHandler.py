#!/bin/bash




import json,os,sys


def UserInfo(action='read',username="None",parameter="None",parameter_value="None"):
    with open('taobao/databases/UserDB', 'r+') as db_read,open('taobao/databases/user_info_bak','w+') as db_write:
        if action == "read":
            return json.loads(db_read.read())
        elif action == "write":
            ALLDbInfo = json.loads(db_read.read())
            ALLDbInfo[username][parameter] = parameter_value
            db_write.write(json.dumps(ALLDbInfo))
    os.rename('taobao/databases/UserDB','taobao/databases/user_info_tmp')
    os.rename('taobao/databases/user_info_bak', 'taobao/databases/UserDB')
    os.remove('taobao/databases/user_info_tmp')
