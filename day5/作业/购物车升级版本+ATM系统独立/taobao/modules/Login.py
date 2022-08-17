
import sys

from taobao.template.ShoppingList import ShoppingList,ProductListdynamics
from taobao.dbhelper.StoreDBHandler import StoreProductList,StoreUserInfo
from taobao.modules.StoreLogicHandler import Buy,ShoppingTrolley,ExpenseCalendar
from bank.modules.BankLogicHandler import UserMainInterface,UserPay,CloseAnAccount,CreditCardManagerment
from bank.dbhelper.BankDBHandler import BankUserInfo


def Login():
    #密码的计数器,默认0,超过3次会锁定用户
    count_pass = 0
    while True:
        UserName = input("Please input your name")
        # 获取淘宝用户信息
        StoreUserInDb = StoreUserInfo()
        #如果输入的用户名在数据库里面,才开始进行判断
        if UserName in StoreUserInDb.keys():
            #首先判断用户是不是锁定的，如果是锁定的，直接break退出
            userLock = StoreUserInDb[UserName]['lock']
            if userLock == 'True':
                print ("用户已锁定,无法登录")
                break;
            #如果不是锁定的，那么开始接收用户输入的密码
            UserPasswd = StoreUserInDb[UserName]['password']
            #只有输入错误的时候count_pass才回+1,所以只有输入错误小于三次的时候才能在次提示输入密码
            while count_pass < 3:
                password = input("Please input your passwrod")
                if password == UserPasswd:
                    #如果登录成功，才能开始所有的主要逻辑
                    print ("login success")

                    while True:
                        #这里开始,获取所有单个用户的金额信息,已经使用的金额信息,给shoppinglist主页做展示使用
                        BankUserInDb = BankUserInfo()
                        UserWallet = BankUserInDb[UserName]['wallet']
                        Balance = int(UserWallet) - int(BankUserInDb[UserName]['useruseamount'])
                        ShoppingList(UserName,UserWallet,Balance,0)

                        ProductList=StoreProductList()
                        #加载商品信息
                        ProductListdynamics(ProductList)
                        #输入每个信号对应每个操作
                        UserChoice = input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 查看消费记录(f) | 个人信用卡管理(x)| 信用卡后台管理(z) | 退出(q) : ')
                        if UserChoice.isdigit():
                            UserChoice = UserChoice
                            #购买以及退还商品的主函数
                            Buy(UserChoice,UserName,)
                            continue
                        elif UserChoice == 'c':
                            #购物车的朱涵数
                            ShoppingTrolley(UserName)
                            continue
                        elif UserChoice == 'r':
                            #余额充值的主函数
                            UserPay(UserName)
                            continue
                        elif UserChoice == 'b':
                            #结账的主函数
                            CloseAnAccount(UserName)
                        elif UserChoice == 'f':
                            #查看淘宝消费的主函数
                            ExpenseCalendar(UserName)
                        elif UserChoice == 'x':
                            #信用卡管理的主函数
                            UserMainInterface(UserName)
                        elif UserChoice == 'z':
                            #信用卡后台的主函数
                            CreditCardManagerment(UserName)
                        elif UserChoice == 'q':
                            print ("退出系统")
                            sys.exit()
                else:
                    #密码每输错一次,计数器就+1,超过三次直接锁定用户
                    count_pass += 1
            else:
                print ("密码输错3次,用户锁定")
                #密码输错三次直接锁定用户
                StoreUserInfo('write',UserName,'lock','True')
                break;
        else:
            print ("用户不存在,请重新输入用户名")
            continue