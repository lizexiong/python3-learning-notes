#!/bin/bash




import json,os,sys


def StoreUserInfo(action='read',username="None",parameter="None",parameter_value="None"):
    with open('taobao/databases/StoreUserDB', 'r+') as db_read,open('taobao/databases/StoreUserDBBak','w+') as db_write:
        if action == "read":
            return json.loads(db_read.read())
        elif action == "write":
            ALLDbInfo = json.loads(db_read.read())
            ALLDbInfo[username][parameter] = parameter_value
            db_write.write(json.dumps(ALLDbInfo))
    os.rename('taobao/databases/StoreUserDB','taobao/databases/StoreUserDBTmp')
    os.rename('taobao/databases/StoreUserDBBak', 'taobao/databases/StoreUserDB')
    os.remove('taobao/databases/StoreUserDBTmp')

def StoreProductList(action='read',ProductNum="None",parameter="None",parameter_value="None"):
    with open('taobao/databases/ProductListDB', 'r+') as db_read,open('taobao/databases/ProductListDBBak','w+') as db_write:
        if action == "read":
            return json.loads(db_read.read())
        elif action == "write":
            ALLDbInfo = json.loads(db_read.read())
            ALLDbInfo[ProductNum][parameter] = parameter_value
            db_write.write(json.dumps(ALLDbInfo))
    os.rename('taobao/databases/ProductListDB', 'taobao/databases/ProductListDBTmp')
    os.rename('taobao/databases/ProductListDBBak', 'taobao/databases/ProductListDB')
    os.remove('taobao/databases/ProductListDBTmp')