__author__ = 'Administrator'
#!/usr/bin/env python




#!/usr/bin/env python3



import sys,os

ProductList = {
    'huawei':{'price':'5000','sum':10,'num':10},
    'apple':{'price':'1000','sum':15,'num':0},
    'sanxing':{'price':'4000','sum':20,'num':20},
    'xiaomi':{'price':'1000','sum':10,'num':10},
}


BuyShoppingTrolley={}       #全局变量，用来判断用户购物车是否有东西
ProductListNum=dict()      #全局变量，存储新的ProductList信息，包括编号
LoginUser=None            #记录登录的用户名，对比价格和结算时判断是否当前用户
UserWallet= None           #用户剩余的金额
#购物车显示函数
def ShoppingList(username,wallet,balance,shoping_cart=0):
    # os.system('clear')
    ShoppingListStr =  '''
    *********************************************************************************
    *                                                                               *
    *                                 欢迎来到华为购物平台                           *
    *                                                                               *
    *********************************************************************************
    会员：%s\t金额：%d\t当前余额：%d\t购物车：%d\n
    ''' %(username,wallet,balance,shoping_cart)
    print (ShoppingListStr)


#商品动态信息
def ProductListdynamics(ProductList):
    print('     =================================================================================')
    print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品总数量(个)','商品剩余数量(个)'))
    i=1 #商品编号
    for ProductKey,ProductValue in ProductList.items():
        print('%-5s %-5d  %-20s  %-20d  %-20d  %-10d' % (' ',i,ProductKey,int(ProductValue['price']),int(ProductValue['sum']),int(ProductValue['num'])))
        ProductListNum[i]=({ProductKey:{'price':int(ProductValue['price']),'sum':int(ProductValue['sum']), 'num':int(ProductValue['num'])}})
        i+=1




# def ChangeWalletAndBuy(num):
#     with open('account.txt','r+') as db_file:
#         for readline in db_file.readlines():
#             username= readline.split()[0]
#             if username == LoginUser:
#                 userwallet = int(readline.split(' ')[2])
#                 if userwallet > DbCommodity_prices:
#                     for i,j in ProductListNum.items():
#                         if int(i) == num:
#                             for k,v in j.items():
#                                 DbCommodity_prices = int(v['price'])
#                                 if ProductList[k]['num'] > 0:
#                                     ProductList[k]['num'] = ProductList[k]['num']-1
#
#                                     # print (BuyShoppingTrolley.get(num),BuyShoppingTrolley,num)
#                                     if BuyShoppingTrolley.get(num):
#                                         BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] +1
#
#                                     else:
#                                         BuyShoppingTrolley[num] = {k:{'price':ProductList[k]['price'],'num':ProductList[k]['num'],'buy':int(1)}}
#                     print ("已将商品加入购物车,可以进入购物车查看")
#                 else:
#                     print ("余额不足，请充值")


def Buy(num,inc=None):
    if ProductListNum.get(num):
        with open('account.txt','r+') as db_file:
            for readline in db_file.readlines():
                username= readline.split()[0]
                if username == LoginUser:
                    UserWallet = int(readline.split(' ')[2])
                    for i,j in ProductListNum.items():
                        if int(i) == num:
                            for k,v in j.items():
                                DbCommodity_prices = int(v['price'])
                                if UserWallet > DbCommodity_prices:
                                    if ProductList[k]['num'] > 0:
                                        if inc == "delete":
                                            while True:
                                                try:
                                                    # UserDel = int(input("请输入要删除的商品编号"))
                                                    BuyNum = int(input("要删除的商品数量"))
                                                    if int(v['num']) >= BuyNum:
                                                        if  int(v['num']) >=1:
                                                            BuyShoppingTrolley.clear()
                                                        else:
                                                            ProductList[k]['num'] = ProductList[k]['num']+BuyNum
                                                            if BuyShoppingTrolley.get(num):
                                                                BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] -BuyNum
                                                            else:
                                                                # BuyShoppingTrolley[num] = {k:{'price':ProductList[k]['price'],'num':ProductList[k]['num'],'buy':int(1)}}
                                                                print ("购物车没有这个商品信息，请刷新系统缓存")
                                                        break
                                                    else:
                                                        print ("您的购物车没有这么商品，请重新输入")
                                                        return
                                                except ValueError as err:
                                                    print (err)
                                        elif inc == None:
                                            while True:
                                                try:
                                                    UserAdd = int(input("请输入要购买的商品数量"))
                                                    if int(ProductList[k]['num']) >= UserAdd:
                                                        PutInShoppingtrolley = input("是否放入购物车y/n")
                                                        if PutInShoppingtrolley == 'y':
                                                            ProductList[k]['num'] = ProductList[k]['num']-UserAdd
                                                            if BuyShoppingTrolley.get(num):
                                                                BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] +UserAdd
                                                            else:
                                                                BuyShoppingTrolley[num] = {k:{'price':ProductList[k]['price'],'num':ProductList[k]['num'],'buy':int(UserAdd)}}
                                                            UserWallet = 100
                                                            break
                                                        else:
                                                            pass

                                                    else:
                                                        print ("商品总量不够...请重新购买")
                                                        ShoppingTrolley()
                                                        return

                                                except ValueError as err:
                                                    print (err)
                                    else:
                                        print ("商品数量不足，请重新购买")
                                        return

                                    print ("已将商品加入购物车,可以进入购物车查看")
                                else:
                                    print ("余额不足，请充值")
    else:
        print ("没有这个商品")

def ShoppingTrolley():
    #os.system('clean')
    print (" *************************************欢迎进入购物车**************************************")
    if BuyShoppingTrolley:
        print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品剩余数量(个)','商品已买数量(个)'))
        for i,j in BuyShoppingTrolley.items():
            for k,v in j.items():
                print('%-5s %-5s  %-20s  %-20d  %-20d  %-10d' % (' ',i,k,int(v['price']),ProductList[k]['num'],int(v['buy'])))      #这里的总商品数用的ProductList的，BuyShoppingTrolley字典没有存储总商品数量

        UserInc = input("请选择菜单 ：是否删除和新增商品,请输入'delete'或者'add',或者按'b'进行结算,否者返回主界面输入'q'")
        if UserInc == "delete":
            ProductID = int(input("请输入商品编号"))
            Buy(ProductID,UserInc)
            ShoppingTrolley()
        elif UserInc == 'add':
            ProductID = int(input("请输入商品编号"))
            Buy(ProductID)
            ShoppingTrolley()
        elif UserInc == 'b':
            CloseAnAccount()
        elif UserInc == 'q':
            return
        else:
            print ("请输入正确的选择")
            ShoppingTrolley()
    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return


def Amount(CurrentUser,TotalAmountofGoods,inc=None):
    UserInfo=dict()
    with open('account.txt','r+') as db_file:
        for readline in db_file.readlines():
            if readline.split()[0] == LoginUser:
                if inc == 'add':
                    UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])+int(TotalAmountofGoods)}
                else:
                    UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])-int(TotalAmountofGoods)}
            else:
                UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])}
            db_file.flush()
        db_file.close()

    with open('account.txt','w',) as db_file:
        for i,j in UserInfo.items():
            print (i + j['pass'] + str(j['amount']))
            db_file.write(i + " " + j['pass'] +  " " + str(j['amount']) + "\n")
            db_file.flush()
        db_file.close()

    # db_file = open('account.txt','r+')
    # for readline in db_file.readlines():
    #     if readline.split()[0] == LoginUser:
    #         if inc == 'add':
    #             UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])+int(TotalAmountofGoods)}
    #         else:
    #             UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])-int(TotalAmountofGoods)}
    #     else:
    #         UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])}
    #     db_file.flush()
    #     db_file.close()
    #
    # db_file = open('account.txt','w',)
    # for i,j in UserInfo.items():
    #     print (i + j['pass'] + str(j['amount']))
    #     db_file.write(i + " " + j['pass'] +  " " + str(j['amount']) + "\n")
    #     db_file.flush()
    # db_file.close()
    # return


def UserPayment():
    print ("用户剩余金额：",UserWallet)
    while True:
        UserChoice = input("是否需要充值,y/n")
        if UserChoice == 'y':
            UserInBalance=input("输入要充值的金额")
            Amount(LoginUser,UserInBalance,inc='add')
            break
        elif UserChoice == 'n':
            break
        else:
            print ("请输入正确的选项")


def CloseAnAccount():
    print (" *************************************进行清算系统**************************************")
    CommodityList = []
    if BuyShoppingTrolley:
        for i,j in BuyShoppingTrolley.items():
            for k,v in j.items():
                CommodityList.append((int(v['price']) * int(v['buy'])))
        CommodityListEnd = sum(CommodityList)
        Amount(LoginUser,CommodityListEnd)
        print ("你的商品需要%s购买,余额将剩余%s"%(CommodityListEnd,UserWallet))
        BuyShoppingTrolley.clear()

    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return

#用户菜单选择模块
# def MenuSelection():
#     while True:
#         user_choice = input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 退出(q) : ')
#         if user_choice.isdigit():
#             user_choice = int(user_choice)
#             Buy(user_choice)

    #return user_choice





count_name = 0
count_pass = 0
while count_name <3:
    username = input("Please input your name")
    db = open('account.txt','r+')
    db_lock = open('account_lock.txt','r+')


    for i in db.readlines():
        #print (i.strip())                                                                  #因为打出来会有两个\n，会有一个空格，所以这里取消掉自带的空格和换行的空格
        db_info = i.strip().split(' ',3)                                                    #这里从account.txt取出用户名和密码，然后使用split进行切割成单独的用户和密码和用户余额
        db_name = db_info[0]
        LoginUser=db_name
        db_pass = db_info[1]
        db_wallet = int(db_info[2])
        if username != db_name :                                                           #判断,输入的用户名是否存在acccount里面，如果没有，那么退出这次循环，并且count_name计数器+1
            print ('not user')
            count_name +=1
        else:                                                                              #尽然不是用户不存在，那么就是存在，开始下一步
            for i in db_lock.readlines():                                                  #判断account_lock，判断用户是否被锁定
                db_lock_name = i.strip()
                if db_lock_name == username:
                    db.close()
                    sys.exit('用户锁定')                                                    #如果被锁定，就直接退出程序了
            while count_pass < 3:                                                           #如果没有被锁定，那么将有3次输入密码的机会
                userpass = input("Please input your password")
                if userpass == db_pass:                                                      #如果成功，那么程序登录成功
                    db.close()

                    while True:
                        UserWallet =  db_wallet
                        #print (UserWallet)
                        ShoppingList(db_name,db_wallet,UserWallet)
                        ProductListdynamics(ProductList)
                        # MenuSelection()
                        user_choice = input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 退出(q) : ')
                        if user_choice.isdigit():
                            user_choice = int(user_choice)
                            Buy(user_choice)
                            continue
                        elif user_choice == 'c':
                            ShoppingTrolley()
                            continue
                        elif user_choice == 'r':
                            UserPayment()
                            continue
                        elif user_choice == 'b':
                            CloseAnAccount()
                        elif user_choice == 'q':
                            print ("退出系统")
                            break
                    sys.exit()
                else:                                                                       #如果不成功，那么count_pass计数器+1，并跳出这次循环，进行下一次循环
                    count_pass +=1
                    print ("密码错误，请重新输入")
                    continue
            else:                                                                           #如果count_pass大于3次，那么写入lock文件，并且系统退出
                db_lock.write(username + "\n")
                db_lock.close()                                                             #并关闭文件
                db.close()
                sys.exit("输错3次，系统退出")


