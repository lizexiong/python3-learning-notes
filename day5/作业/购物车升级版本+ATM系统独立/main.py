__author__ = 'Administrator'
#!/usr/bin/env python3








import sys,json,os

from taobao.template.ShoppingList import ShoppingList,ProductListdynamics,ProductList
from taobao.databases.UserDBHandler import UserInfo as StroreUserInfo


from bank.databases.BankUserDBHandler import bank_user_info

if __name__ == "__main__":
    count_pass = 0
    while True:
        username = input("Please input your name")
        StoreUserInDb = StroreUserInfo()
        if username in StoreUserInDb.keys():
            userLock = StoreUserInDb[username]['lock']
            if userLock == 'True':
                print ("用户已锁定,无法登录")
                break;
            UserPasswd = StoreUserInDb[username]['password']
            while count_pass < 3:
                password = input("Please input your passwrod")
                if password == UserPasswd:
                    print ("login success")

                    BankUserInDb = bank_user_info()
                    print (BankUserInDb)

                    ShoppingList(username,)
                    ProductListdynamics(ProductList)

                else:
                    count_pass += 1
            else:
                print ("密码输错3次,用户锁定")
                StroreUserInfo('write',username,'lock','True')
                break;
        else:
            print ("用户不存在,请重新输入用户名")
            continue


w7







#
# ShoppingList('lizexiong','15000','15000',0)


