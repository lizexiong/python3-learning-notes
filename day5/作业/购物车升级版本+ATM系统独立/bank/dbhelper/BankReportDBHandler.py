




import json,os


def TransactionRecord(action=None,time=None,user=None,num=None,type=None,product=None,price=None,buy=None):
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
            except:
                AllDbInfo = {}

            try:
                UserDbInfo = AllDbInfo[user]
                print (UserDbInfo)
                UserDbInfo[user] = {
                    {'num': 1, 'type': type, 'product': product, 'price': price, 'buy': buy, 'orderid': OrderId,
                           'time': OrderTime}}
            except Exception as e:
                print (e)
                UserDbInfo = {user:{'num':num,'type':type,'product':product,'price':price,'buy':buy,'orderid':OrderId,'time':OrderTime}}
            AllDbInfo.update(UserDbInfo)
            db_write.write(json.dumps(AllDbInfo))
    os.rename('../databases/BankReportDB', '../databases/BankReportDBTMP')
    os.rename('../databases/BankReportDBBak', '../databases/BankReportDB')
    os.remove('../databases/BankReportDBTMP')


TransactionRecord(action='write',user='lizexiong')
 