#!/bin/bash




import json,os,sys

#淘宝商城的用户信息写入查询模块,直接调用数据库交互
#淘宝的数据库交互模块不太智能,数据库所需要的用户信息以及字段必须存在,否则就会报错,该问题在银行的账单处理模块得到解决
def StoreUserInfo(action='read',username="None",parameter="None",parameter_value="None"):
    with open('taobao/databases/StoreUserDB', 'r+') as db_read,open('taobao/databases/StoreUserDBBak','w+') as db_write:
        if action == "read":
            #默认就是read,就是读取淘宝商品的用户信息
            return json.loads(db_read.read())
        elif action == "write":
            #因为数据库是文件,这里拿出所有数据库信息,所有用户的所有信息,然后将单用户的单个字段更新重新写回数据库即可,所以该函数目前只接受一个数据字段信息的修改
            #如果需要多个参数修改,那就得在代码逻辑层面多次调用了
            ALLDbInfo = json.loads(db_read.read())
            ALLDbInfo[username][parameter] = parameter_value
            db_write.write(json.dumps(ALLDbInfo))
    #这里就是一个新增文件和删除文件的操作了,不做过多解释
    os.rename('taobao/databases/StoreUserDB','taobao/databases/StoreUserDBTmp')
    os.rename('taobao/databases/StoreUserDBBak', 'taobao/databases/StoreUserDB')
    os.remove('taobao/databases/StoreUserDBTmp')


#所有商品的数据库信息,代码和上面用户信息一模一样,这里就不做过多解释
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