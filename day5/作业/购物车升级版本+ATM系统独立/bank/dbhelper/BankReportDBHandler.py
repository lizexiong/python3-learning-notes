




import json,os


def TransactionRecord(action=None,user=None,type=None,**usershoppingcart):
    with open('bank/databases/BankReportDB', 'r+') as db_read, open('bank/databases/BankReportDBBak', 'w+') as db_write:
        if action == "read":
            try:
                return json.loads(db_read.read())
            except Exception as e:
                return None
        elif action == "write":
            import random,time
            RandomNum = str(random.randint(1000000000,9999999999))
            OrderTimePrefix = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            OrderId = OrderTimePrefix + RandomNum
            OrderTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            try:
                AllDbInfo = json.loads(db_read.read())
            except Exception as e:
                AllDbInfo = {user:{}}

            # try:
            # UserDbInfo = AllDbInfo[user]

            for num,property in usershoppingcart.items():
                UserDbInfo = AllDbInfo[user]
                print (UserDbInfo)  #这里有问题，怎么让订单在一张里面展示
                if UserDbInfo == '':
                    AllDbInfo[user][OrderId]={'num': num, 'type': type, 'product': property['name'], 'price': property['price'], 'buy': property['buy'], 'time': OrderTime}
                else:
                    TmpOder = {OrderId:{'num': num, 'type': type, 'product': property['name'], 'price': property['price'], 'buy': property['buy'], 'time': OrderTime}}

            AllDbInfo[user].update(TmpOder)
            db_write.write(json.dumps(AllDbInfo))
                # AllDbInfo[user].update({'num': 2, 'type': type, 'product': product, 'price': price, 'buy': buy, 'orderid': OrderId,'time': OrderTime})

            # except Exception as e:
            #     print (e)
            #     AllDbInfo = {user:{'num':num,'type':type,'product':product,'price':price,'buy':buy,'orderid':OrderId,'time':OrderTime}}
            #     # AllDbInfo.update(UserDbInfo)

    os.rename('bank/databases/BankReportDB', 'bank/databases/BankReportDBTMP')
    os.rename('bank/databases/BankReportDBBak', 'bank/databases/BankReportDB')
    os.remove('bank/databases/BankReportDBTMP')

# usershoppingcart={"1": {"name": "huawei", "price": "5000", "buy": 1}}
#
# #TransactionRecord(action='write',user='wuxinzhe',**usershoppingcart)
# TransactionRecord(action='read',user='wuxinzhe',**usershoppingcart)
 