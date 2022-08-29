




import json,os


#账单信息的写入和读取模块,和数据库交互
def TransactionRecord(action='read',user=None,type=None,**useroperationrecords):
    with open('bank/databases/BankReportDB', 'r+') as db_read, open('bank/databases/BankReportDBBak', 'w+') as db_write:
        if action == "read":
            try:
                return json.loads(db_read.read())
            except Exception as e:
                return None
        elif action == "write":
            import random,time
            #订单号生成,日期加上随机数来生成一个订单号
            RandomNum = str(random.randint(1000000000,9999999999))
            OrderTimePrefix = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            OrderId = OrderTimePrefix + RandomNum
            OrderTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            try:
                #这里加强了功能,即使数据库里面没有字段和数据也不会报错,整个作业里面,就这个数据库交互模块写的比较完善
                #如果数据库里面没有数据,那么就直接创建一个空字典
                AllDbInfo = json.loads(db_read.read())
            except Exception as e:
                AllDbInfo= dict()

            if AllDbInfo is not None:
                try:
                    #如果数据库不为空,如果用户存在,直接取出数据,如果不存在,那就设置该用户信息为空
                    UserDbInfo = AllDbInfo[user]
                except Exception as e:
                    AllDbInfo[user] = {}
                    UserDbInfo = {}
            else:
                AllDbInfo[user] = {}

            #这里有个计数器是因为,在单个购物订单里面,可能有好几种商品信息,那么就要区分一下编号
            ordernum = 1
            for num,property in useroperationrecords.items():
                if type == "bill":
                    if UserDbInfo.get(OrderId,None):
                        #刚才的技术器就是这里用的
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
            #可以看到,都是取出数据库的所有信息,然后更新之后插入回数据库
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
