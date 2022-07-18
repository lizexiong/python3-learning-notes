








import os,sys
from bank.databases.BankUserDBHandler import BankUserInfo

#from taobao.modules.StoreHandler import ShoppingTrolley         #这里不能导入了,因为StoreHandler也会调用这里的模块，就造成了循环，导入就会报错,具体原因见
from taobao.template.ShoppingList import UserShoppingTrolley



def UserMainInterface(user):
    os.system('cls')
    FromBankUserInfo = BankUserInfo()
    print ("*" * 121)
    while True:
        print("欢迎进入银行系统".center(117, '*'))
        print ("用户:",user,"信用额度:",FromBankUserInfo[user]['wallet'],"已使用:",FromBankUserInfo[user]['useruseamount'])
        print ('请选择菜单 ：输入选择  | 余额充值(1) | 结帐(2) | 提现(3) |转账(4) | 查看账单(5)| 查看消费记录(6) | 还款(7) | ATM操作日志(8)| 退出(q) : ')
        try:
            UserChoice = input("请输入需要的操作")
        except:
            print ("输入错误,请重新选择")
        if UserChoice == "1":
            UserPay(user)
        elif UserChoice == "2":
            CloseAnAccount(user)
        elif UserChoice == "q":
            sys.exit()


#用户充值模块，这个不多做解释
def UserPay(user):
    FromBankUserInfo = BankUserInfo()
    UserWallet = int(FromBankUserInfo[user]['wallet'])
    print ("当前可用额度：",int(FromBankUserInfo[user]['wallet'])-int(FromBankUserInfo[user]['useruseamount']))
    while True:
        UserChoice = input("是否需要充值,y/n")
        if UserChoice == 'y':
            UserInBalance=int(input("输入要充值的金额"))
            BankUserInfo('write',user,'wallet',UserWallet+UserInBalance)
            break
        elif UserChoice == 'n':
            break
        else:
            print ("请输入正确的选项")

#用户结算模块
def CloseAnAccount(user):
    print("进行清算系统".center(117, '*'))
    print (UserShoppingTrolley)
    CommodityList = []
    if UserShoppingTrolley:                                                                                                                  #首先判断购物车里面是否有商品，有商品才进行结账操作
        UserChoice = input("是否进行结账y/n")
        if UserChoice == 'y':
            for i,j in UserShoppingTrolley.items():                                                                                          #把购物车所有商品*他们的单价放入字典
                for k,v in j.items():
                    CommodityList.append((int(v['price']) * int(v['buy'])))
            CommodityListEnd = sum(CommodityList)                                                                                           #计算所有商品的价格总和
            FromBankUserInfo = BankUserInfo()
            UserWallet = int(FromBankUserInfo[user]['wallet'])
            UserUse = UserWallet - int(FromBankUserInfo[user]['useruseamount'])
            if UserWallet >= CommodityListEnd:                                                                                              #对比用户金钱是否比商品总价多
                NowUserUse = UserUse + CommodityListEnd
                BankUserInfo('write',user,'useruseamount',NowUserUse)                                                                                          #如果用户金钱比商品总价多，那么调用算账模块
                print ("你的商品需要%s购买,余额将剩余%s"%(CommodityListEnd,UserWallet - NowUserUse))
                UserShoppingTrolley.clear()                                                                                                  #并且清空购物车
            else:
                print ("余额不足,返回购物车")

        else:
            return

    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return