__author__ = 'Administrator'
#!/usr/bin/env python3



import sys,json,os

from taobao.template.ShoppingList import ShoppingList,ProductListdynamics,ProductList,ProductListNum
from taobao.databases.StoreUserDBHandler import StoreUserInfo
from taobao.modules.buy import Buy
from taobao.modules.shoppingtrolley import ShoppingTrolley

from bank.databases.BankUserDBHandler import BankUserInfo

if __name__ == "__main__":
    count_pass = 0
    while True:
        UserName = input("Please input your name")
        StoreUserInDb = StoreUserInfo()
        if UserName in StoreUserInDb.keys():
            userLock = StoreUserInDb[UserName]['lock']
            if userLock == 'True':
                print ("用户已锁定,无法登录")
                break;
            UserPasswd = StoreUserInDb[UserName]['password']
            while count_pass < 3:
                password = input("Please input your passwrod")
                if password == UserPasswd:
                    print ("login success")

                    while True:
                        BankUserInDb = BankUserInfo()
                        UserWallet = BankUserInDb[UserName]['wallet']
                        Balance = int(UserWallet) - int(BankUserInDb[UserName]['useamount'])
                        ShoppingList(UserName,UserWallet,Balance,0)
                        ProductListdynamics(ProductList)
                        UserChoice = input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 信用卡管理(x)| 退出(q) : ')
                        if UserChoice.isdigit():
                            UserChoice = int(UserChoice)
                            Buy(UserChoice,UserName,)
                            continue
                        elif UserChoice == 'c':
                            ShoppingTrolley(UserName)
                            continue
                        elif UserChoice == 'r':
                            #UserPayment()
                            continue
                        elif UserChoice == 'b':
                            pass
                            #CloseAnAccount()
                        elif UserChoice == 'x':
                            pass
                        elif UserChoice == 'q':
                            print ("退出系统")
                            sys.exit()
                else:
                    count_pass += 1
            else:
                print ("密码输错3次,用户锁定")
                StoreUserInfo('write',UserName,'lock','True')
                break;
        else:
            print ("用户不存在,请重新输入用户名")
            continue









#
# ShoppingList('lizexiong','15000','15000',0)


