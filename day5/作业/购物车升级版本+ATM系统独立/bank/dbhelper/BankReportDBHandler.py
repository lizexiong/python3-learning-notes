




import json,os


def TransactionRecord(action='read',user=None,type=None,**useroperationrecords):
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
                AllDbInfo= dict()

            if AllDbInfo is not None:
                try:
                    UserDbInfo = AllDbInfo[user]
                except Exception as e:
                    AllDbInfo[user] = {}
                    UserDbInfo = {}
            else:
                AllDbInfo[user] = {}


            for num,property in useroperationrecords.items():

                if type == "bill":
                    if UserDbInfo.get(OrderId,None):
                        UserDbInfo[OrderId].update({num: {'type': type, 'product': property['name'],
                                                           'price': property['price'], 'buy': property['buy'],
                                                           'time': OrderTime}})
                    else:
                        UserDbInfo[OrderId] = {num: {'type': type, 'product': property['name'], 'price': property['price'],
                                                      'buy': property['buy'], 'time': OrderTime}}
                elif type == "transferaccounts":
                    if UserDbInfo.get(OrderId, None):
                        UserDbInfo[OrderId].update({'type': type, 'transfermoney': useroperationrecords['transfermoney'],'touser':useroperationrecords['touser'],'userbalance':useroperationrecords['userbalance'],'time': OrderTime})
                    else:
                        UserDbInfo[OrderId] = {'type': type, 'transfermoney': useroperationrecords['transfermoney'],'touser':useroperationrecords['touser'],'userbalance':useroperationrecords['userbalance'],'time': OrderTime}
                elif type == "atm":
                    if UserDbInfo.get(OrderId, None):
                        UserDbInfo[OrderId].update({'type': type, 'amount': useroperationrecords['amount'],'userbalance':useroperationrecords['userbalance'],'time': OrderTime})
                    else:
                        UserDbInfo[OrderId] = {'type': type, 'amount': useroperationrecords['amount'],'userbalance':useroperationrecords['userbalance'],'time': OrderTime}

            AllDbInfo[user].update(UserDbInfo)
            db_write.write(json.dumps(AllDbInfo))
    os.rename('bank/databases/BankReportDB', 'bank/databases/BankReportDBTMP')
    os.rename('bank/databases/BankReportDBBak', 'bank/databases/BankReportDB')
    os.remove('bank/databases/BankReportDBTMP')

 