


import json

from taobao.dbhelper.StoreDBHandler import StoreProductList,StoreUserInfo
from bank.dbhelper.BankDBHandler import BankUserInfo
from bank.dbhelper.BankReportDBHandler import TransactionRecord
from bank.modules.BankLogicHandler import CloseAnAccount               #不能再调用了，不然就调用循环了

#购买和退订商品
def Buy(num,user,inc=None):
    #
    UserShoppingTrolleyTmp = dict()
    #调用dbhelpler函数,获取所有的商品信息
    ProductList = StoreProductList()
    if ProductList.get(num):
        FromDBBankUserInfo = BankUserInfo()
        FromDBStoreUserInfo = StoreUserInfo()
        UserWallet = FromDBBankUserInfo[user]['wallet']
        ProductPrice = ProductList[num]['price']
        ProductName = ProductList[num]['name']

        UserShoppingCart = FromDBStoreUserInfo[user]['usershoppingcart']
        if UserShoppingCart != "":
            UserShoppingCart = eval(str(FromDBStoreUserInfo[user]['usershoppingcart']))
        else:
            UserShoppingCart = {}

        if inc == 'delete':
            while True:
                try:
                    DelProductNum = int(input("要删除的商品数量"))
                    if UserShoppingCart[num]['buy'] >= DelProductNum:
                        if UserShoppingCart[num]['buy'] <=1:
                            UserShoppingCart.pop(num)
                            ProductNum = ProductList[num]['num'] + 1
                        else:
                            UserShoppingCart[num]['buy'] = UserShoppingCart[num]['buy'] - DelProductNum
                            ProductNum = ProductList[num]['num'] + DelProductNum
                        StoreUserInfo('write', user, 'usershoppingcart', UserShoppingCart)
                        StoreProductList('write',num,'num',ProductNum)
                        break
                    else:
                        print("您的购物车没有这么多商品，请重新输入")
                except:
                    print ("输入了可能不存在商品,请重新输入")
                    break
        elif inc == None:
            while True:
                try:
                    UserAdd = int(input("请输入要购买的商品数量"))
                    ProductListNum = int(ProductList[num]['num'])
                    if ProductListNum >= UserAdd:
                        PutInShoppingtrolley = input("是否放入购物车y/n")
                        if PutInShoppingtrolley == "y":
                            ProductListNum = ProductListNum - UserAdd
                            StoreProductList('write',num,'num',ProductListNum)

                            if UserShoppingCart.get(num,None):
                                UserShoppingCart[num]['buy'] = UserShoppingCart[num]['buy'] + int(UserAdd)
                                UserShoppingTrolleyTmp[num] = {'name': ProductName, 'price': ProductPrice,'buy': UserShoppingCart[num]['buy']}
                            else:
                                UserShoppingTrolleyTmp[num] = {'name':ProductName, 'price': ProductPrice, 'buy': int(UserAdd)}
                            UserShoppingCart.update(UserShoppingTrolleyTmp)
                            StoreUserInfo('write', user, 'usershoppingcart', UserShoppingCart)
                            print("已将商品加入购物车,可以进入购物车查看")
                            break
                        else:
                            break
                    else:
                        print ("商品数量不够,请重新购买")
                        break
                except :
                    print ("输入了可能不正常的指令")
                    break
    else:
        print("没有这个商品")

#购物车界面以及购物车逻辑
def ShoppingTrolley(user):
    #os.system('clean')
    print (" *************************************欢迎进入购物车**************************************")
    ProductList = StoreProductList()
    FromDBStoreUserInfo = StoreUserInfo()
    UserShoppingCart = FromDBStoreUserInfo[user]['usershoppingcart']
    if UserShoppingCart :                                                                                                                  #如果购物车列表里面存在商品才会展示购物车
        UserShoppingCart = eval(str(FromDBStoreUserInfo[user]['usershoppingcart']))
        print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品剩余数量(个)','商品已买数量(个)'))
        for k,v in UserShoppingCart.items():                                                                                              #开始循环购物车
            print('%-5s %-5s  %-20s  %-20d  %-15d  %-10d' % (' ',k,UserShoppingCart[k]['name'],int(UserShoppingCart[k]['price']),int(ProductList[k]['num']),int(UserShoppingCart[k]['buy'])))      #这里的总商品数用的ProductList的，BuyShoppingTrolley字典没有存储总商品数量

        UserInc = input("请选择菜单 ：是否删除和新增商品,请输入'delete'或者'add',或者按'b'进行结算,否者返回主界面输入'q'")               #让用户选择操作
        if UserInc == "delete":                                                                                             #接下来看是删除还是增加商品，那么就会调用Buy()函数
            ProductID = input("请输入商品编号")
            Buy(ProductID,user,UserInc)
            ShoppingTrolley(user)
        elif UserInc == 'add':
            ProductID = input("请输入商品编号")
            Buy(ProductID,user)
            ShoppingTrolley(user)
        elif UserInc == 'b':
            CloseAnAccount(user)
        elif UserInc == 'q':
            return
        else:
            print ("请输入正确的选择")

            ShoppingTrolley(user)
    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return

def ExpenseCalendar(user):
    import re
    SinleUserBillInfo = TransactionRecord('read',user)[user]
    print (SinleUserBillInfo)
    if SinleUserBillInfo is not None:
        print (" *************************************历史账单管理界面**************************************")
        print('%-4s %-25s  %-20s  %-10s  %-10s  %-10s' % (' ', '订单号', '订单时间','商品名称', '商品价格(元)',  '商品购买数量(个)',))
        count = 0
        for ordernum,orderinfo in SinleUserBillInfo.items():
            TotalPriceCalc = []
            for num,info in orderinfo.items():
                if info['type'] == "bill":
                    TotalPriceCalc.append(int(info['price']) * int(info['buy']))
                    if count <1 :
                        print('%-4s %-25s  %-25s  %-15s  %-15s  %-10s' % (
                        ' ', ordernum,info['time'], info['product'], info['price'], info['buy'], ))
                    else:
                        print('%-4s %-25s  %-25s  %-15s  %-15s  %-10s' % (
                        ' ', ' '*25, ' '*20,info['product'], info['price'], info['buy'], ))
                    count +=1
                else:
                    pass
            if count >= 1:
                print ('%-87s %-1s %-25s ' % (' ','总价:',sum(TotalPriceCalc)))
                count = 0
    else:
        print ("用户没有消费记录")
    input("按任意键退出")