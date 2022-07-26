




import json


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
            try:
                ALLDbInfo = json.loads(db_read.read())[user]
            except:
                ALLDbInfo = {user:{'num':num,'type':type,'product':product,'price':price,'buy':buy}}
            print (ALLDbInfo)
            #ALLDbInfo[user][num] = num
            db_write.write(json.dumps(ALLDbInfo))


TransactionRecord(action='write',user='lizexiong')
 