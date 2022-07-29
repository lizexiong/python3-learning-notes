




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
                AllDbInfo = {"user":}

            try:
                UserDbInfo = json.loads(db_read.read())[user]
            except Exception as e:
                UserDbInfo[user] = None


            TmpUserInfo={}
            for num,property in usershoppingcart.items():
                if TmpUserInfo.get(OrderId,None):
                    TmpUserInfo[OrderId].update({num: {'type': type, 'product': property['name'],
                                                       'price': property['price'], 'buy': property['buy'],
                                                       'time': OrderTime}})
                else:
                    TmpUserInfo[OrderId] = {num: {'type': type, 'product': property['name'], 'price': property['price'],
                                                  'buy': property['buy'], 'time': OrderTime}}
            LastUserDbInfo = UserDbInfo.update(TmpUserInfo)
            print (LastUserDbInfo)
            AllDbInfo[user].update(LastUserDbInfo)
            db_write.write(json.dumps(AllDbInfo))
    os.rename('bank/databases/BankReportDB', 'bank/databases/BankReportDBTMP')
    os.rename('bank/databases/BankReportDBBak', 'bank/databases/BankReportDB')
    os.remove('bank/databases/BankReportDBTMP')

 