__author__ = 'Administrator'
#!/usr/bin/env python3








import sys,json

from taobao.template.ShoppingList import ShoppingList





if __name__ == "__main__":
    count_pass = 0
    while count_pass <3:
        username = input("Please input your name")
        db = open('taobao/databases/user_info','r',)
        UserInDb = json.loads(db.read())
        if username in UserInDb.keys():
            UserPasswd = UserInDb[username]['password']
            while True:
                password = input("Please input your passwrod")
                if password == UserPasswd:
                    print ("login success")
                    break
                else:
                    count_pass += 1
        else:
            continue


windows7








    #
    # ShoppingList('lizexiong','15000','15000',0)


