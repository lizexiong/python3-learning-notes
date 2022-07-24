__author__ = 'Administrator'
#!/usr/bin/env python3



import sys

from taobao.template.ShoppingList import ShoppingList,ProductListdynamics
from taobao.dbhelper.StoreDBHandler import StoreProductList,StoreUserInfo
from taobao.modules.StoreLogicHandler import Buy,ShoppingTrolley
from bank.modules.BankLogicHandler import UserMainInterface,UserPay,CloseAnAccount,CreditCardManagerment
from bank.dbhelper.BankDBHandler import BankUserInfo

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
                        Balance = int(UserWallet) - int(BankUserInDb[UserName]['useruseamount'])
                        ShoppingList(UserName,UserWallet,Balance,0)

                        ProductList=StoreProductList()
                        ProductListdynamics(ProductList)
                        UserChoice = input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 查看消费记录(f) | 个人信用卡管理(x)| 信用卡后台管理(z) | 退出(q) : ')
                        if UserChoice.isdigit():
                            UserChoice = UserChoice
                            Buy(UserChoice,UserName,)
                            continue
                        elif UserChoice == 'c':
                            ShoppingTrolley(UserName)
                            continue
                        elif UserChoice == 'r':
                            UserPay(UserName)
                            continue
                        elif UserChoice == 'b':
                            CloseAnAccount(UserName)
                        elif UserChoice == 'f':
                            pass
                        elif UserChoice == 'x':
                            UserMainInterface(UserName)
                        elif UserChoice == 'z':
                            CreditCardManagerment()
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


