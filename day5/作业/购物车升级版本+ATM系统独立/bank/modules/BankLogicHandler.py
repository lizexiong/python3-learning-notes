








import os,sys
from bank.dbhelper.BankDBHandler import BankUserInfo
from taobao.dbhelper.StoreDBHandler import StoreProductList,StoreUserInfo

#from taobao.modules.StoreHandler import ShoppingTrolley         #这里不能导入了,因为StoreHandler也会调用这里的模块，就造成了循环，导入就会报错,具体原因见




def UserMainInterface(user):
    print ("*" * 121)
    while True:
        FromBankUserInfo = BankUserInfo()
        print("欢迎进入银行系统".center(117, '*'))
        print ("用户:",user,"信用额度:",FromBankUserInfo[user]['wallet'],"已使用:",FromBankUserInfo[user]['useruseamount'],"现金：",FromBankUserInfo[user]['cash'])
        print ('请选择菜单 ：输入选择  | 余额充值(1) | 结帐(2) | 提现(3) |转账(4) | 查看账单(5) | 还款(6) | ATM操作日志(7)| 退出(q) : ')
        try:
            UserChoice = input("请输入需要的操作")
        except:
            print ("输入错误,请重新选择")
        if UserChoice == "1":
            UserPay(user)
        elif UserChoice == "2":
            CloseAnAccount(user)
        elif UserChoice == "3":
            WithdraDeposit(user)
        elif UserChoice == "q":
            break


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
    CommodityList = []
    UserShoppingCart=StoreUserInfo()[user]['usershoppingcart']
    print (UserShoppingCart)
    if UserShoppingCart:                                                                                                                  #首先判断购物车里面是否有商品，有商品才进行结账操作
        UserChoice = input("是否进行结账y/n")
        if UserChoice == 'y':
            for num,info in UserShoppingCart.items():                                                                                          #把购物车所有商品*他们的单价放入字典
                CommodityList.append((int(UserShoppingCart[num]['price']) * int(UserShoppingCart[num]['buy'])))
            SumCommodityList = sum(CommodityList)                                                                                           #计算所有商品的价格总和
            UserWallet = int(BankUserInfo()[user]['wallet'])
            UserAmount = int(BankUserInfo()[user]['useruseamount'])
            UserResidue = UserWallet - UserAmount
            if UserResidue >= SumCommodityList:                                                                                              #对比用户金钱是否比商品总价多
                NowUserUse = UserAmount + SumCommodityList
                BankUserInfo('write',user,'useruseamount',NowUserUse)                                                                                          #如果用户金钱比商品总价多，那么调用算账模块
                print ("你的商品需要%s购买,余额将剩余%s"%(SumCommodityList,UserWallet - NowUserUse))
                StoreUserInfo('write',user,'usershoppingcart','')                                                                        #并且清空购物车
            else:
                print ("余额不足,返回购物车")
        else:
            return

    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return

def WithdraDeposit(user):
    WithdrawalAmount = int(BankUserInfo()[user]['wallet'] / 2)
    UserBalance = BankUserInfo()[user]['wallet'] - BankUserInfo()[user]['useruseamount']
    if UserBalance >= WithdrawalAmount:
        print("您提现最高额度为%d,目前可提现余额为%d" %(WithdrawalAmount,WithdrawalAmount))
    else:
        print("您提现最高额度为%d,目前可提现余额为%d" % (WithdrawalAmount, UserBalance))
    UserCash = int(input("请输入要提现的金额"))
    UserChoice = input("确实是否进行提现？y/n")
    if UserChoice == "y":
        if UserCash <= UserBalance:
            UseUseAmount = BankUserInfo()[user]['useruseamount'] + UserCash
            BankUserInfo('write',user,'useruseamount',UseUseAmount)
            BankUserInfo('write', user, 'cash', UserCash)
        else:
            print ("可提现额度不足,返回主界面")
            return
    else:
        return

def TransferAccounts(user,touser):
    pass
