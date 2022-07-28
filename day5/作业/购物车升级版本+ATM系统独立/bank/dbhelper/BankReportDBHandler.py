




import json,os


def TransactionRecord(action=None,time='None',user=None,type=None,**usershoppingcart):
    with open('../databases/BankReportDB', 'r+') as db_read, open('../databases/BankReportDBBak', 'w+') as db_write:
        if action == "read":
            if type == None:
                pass
            elif type == "bill":
                pass
            elif type == "atm":
                pass
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
            UserDbInfo = AllDbInfo[user]

            for i in usershoppingcart.values():
                print (i)
                #AllDbInfo[user][OrderId]={'num': 2, 'type': type, 'product': i[product], 'price': price, 'buy': buy, 'time': OrderTime}
                # AllDbInfo[user].update({'num': 2, 'type': type, 'product': product, 'price': price, 'buy': buy, 'orderid': OrderId,'time': OrderTime})

            # except Exception as e:
            #     print (e)
            #     AllDbInfo = {user:{'num':num,'type':type,'product':product,'price':price,'buy':buy,'orderid':OrderId,'time':OrderTime}}
            #     # AllDbInfo.update(UserDbInfo)
            db_write.write(json.dumps(AllDbInfo))
    os.rename('../databases/BankReportDB', '../databases/BankReportDBTMP')
    os.rename('../databases/BankReportDBBak', '../databases/BankReportDB')
    os.remove('../databases/BankReportDBTMP')


TransactionRecord(action='write',user='wuxinzhe',**usershoppingcart=)
 