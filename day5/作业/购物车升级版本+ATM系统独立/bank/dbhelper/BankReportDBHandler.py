




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

            ordernum = 1
            for num,property in useroperationrecords.items():
                if type == "bill":
                    if UserDbInfo.get(OrderId,None):
                        UserDbInfo[OrderId].update({ordernum: {'num':num,'type': type, 'product': property['name'],
                                                           'price': property['price'], 'buy': property['buy'],
                                                           'time': OrderTime}})
                    else:
                        UserDbInfo[OrderId] = {ordernum: {'num':num,'type': type, 'product': property['name'], 'price': property['price'],
                                                      'buy': property['buy'], 'time': OrderTime}}
                elif type == "transferaccounts":
                    if UserDbInfo.get(OrderId, None):
                        UserDbInfo[OrderId].update({ordernum: {'type': type, 'transfermoney': property['transfermoney'],
                                                               'touser':property['touser'],'userbalance':property['userbalance'],
                                                               'time': OrderTime}})
                    else:
                        UserDbInfo[OrderId] = {ordernum:{'type': type, 'transfermoney': property['transfermoney'],
                                                         'touser':property['touser'],'userbalance':property['userbalance'],
                                                         'time': OrderTime}}
                elif type == "atm":
                    if UserDbInfo.get(OrderId, None):
                        UserDbInfo[OrderId].update({ordernum:{'type': type, 'usercash':property['usercash'] ,
                                                              'userbalance':property['userbalance'],'time': OrderTime}})
                    else:
                        UserDbInfo[OrderId] = {ordernum:{'type': type, 'usercash':property['usercash'] ,
                                                         'userbalance':property['userbalance'],'time': OrderTime}}
                ordernum += 1

            AllDbInfo[user].update(UserDbInfo)
            db_write.write(json.dumps(AllDbInfo))
    os.rename('bank/databases/BankReportDB', 'bank/databases/BankReportDBTMP')
    os.rename('bank/databases/BankReportDBBak', 'bank/databases/BankReportDB')
    os.remove('bank/databases/BankReportDBTMP')


# def AllBills(action="read",user=None,**userbill):
#     with open('bank/databases/BankBillDB', 'r+') as db_read, open('bank/databases/BankBillDBBak', 'w+') as db_write:
#         if action == "read":
#             try:
#                 return json.loads(db_read.read())
#             except Exception as e:
#                 return None
#         elif action == "write":
#             import random,time
#             RandomNum = str(random.randint(1000000000,9999999999))
#             OrderTimePrefix = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
#             OrderId = OrderTimePrefix + RandomNum
#             OrderTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
#             try:
#                 AllDbInfo = json.loads(db_read.read())
#             except Exception as e:
#                 AllDbInfo= dict()
#
#             if AllDbInfo is not None:
#                 try:
#                     UserDbInfo = AllDbInfo[user]
#                 except Exception as e:
#                     AllDbInfo[user] = {}
#                     UserDbInfo = {}
#             else:
#                 AllDbInfo[user] = {}
#
#             for num, property in userbill.items():
#                 if UserDbInfo.get(OrderId, None):
#                     print ("账单系统出错,不能有重复的账单")
#                 else:
#                     UserDbInfo[OrderId] = {
#                          'type': type, 'ordernum':order'product': property['name'], 'price': property['price'], 'time': OrderTime}
#
#
#             # ALLDbInfo = json.loads(db_read.read())
#             # ALLDbInfo[user][parameter] = parameter_value
#             # db_write.write(json.dumps(ALLDbInfo))
#         os.rename('bank/databases/BankUserDB', 'bank/databases/BankUserDBTMP')
#         os.rename('bank/databases/BankUserDBBak', 'bank/databases/BankUserDB')
#         os.remove('bank/databases/BankUserDBTMP')
