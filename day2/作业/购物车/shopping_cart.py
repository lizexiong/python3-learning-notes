__author__ = 'Administrator'
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

#用户信息显示模块
def ShoppingList(username,wallet,balance,shoping_cart=0):
    # os.system('clear')
    ShoppingListStr =  '''
    *********************************************************************************
    *                                                                               *
    *                                 欢迎来到华为购物平台                           *
    *                                                                               *
    *********************************************************************************
    会员：%s\t金额：%s\t当前余额：%s\t购物车：%d\n
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

#动态获取金额模块
#因为with_open写入有延迟，这里动态获取玩家文件中的金额
def UserBalance():
    UserInfo=dict()
    with open('account.txt','r+') as db_file:
        for readline in db_file.readlines():
            if readline.split()[0] == LoginUser:
                UserWallet = readline.split()[2]
                return int(UserWallet)
            else:
                pass

#购买和退订商品
def Buy(num,inc=None):
    if ProductListNum.get(num):                                                                                                                                                         #判断用户输入的商品ID是否存在
        with open('account.txt','r+') as db_file:
            for readline in db_file.readlines():
                username= readline.split()[0]
                if username == LoginUser:                                                                                                                                               #打开账户文件,判断是否是当前用户
                    UserWallet = int(readline.split(' ')[2])                                                                                                                            #获取当前用户的钱总额
                    for i,j in ProductListNum.items():
                        if int(i) == num:
                            for k,v in j.items():
                                DbCommodity_prices = int(v['price'])                                                                                                                    #获取商品的单价
                                if UserWallet >= DbCommodity_prices:                                                                                                                     #如果用户的钱多余商品的价格
                                    if inc == "delete":                                                                                                                                 #如果用户输入的指令是删除商品，这个逻辑有点废了，但是改动太麻烦，就写上吧
                                        while True:
                                            try:
                                                # UserDel = int(input("请输入要删除的商品编号"))
                                                BuyNum = int(input("要删除的商品数量"))                                                                                                  #那么输入要删除的数量
                                                print (BuyShoppingTrolley[num][k]['buy'])
                                                if BuyShoppingTrolley[num][k]['buy'] >= BuyNum:                                                                                          #如果添加进入购物车的数量大于等于用户输入的要删除的数量
                                                    if  BuyShoppingTrolley[num][k]['buy'] <=1:                                                                                           #并且如果加购物车的商品数量小于等于1，那么就直接删除整个商品key
                                                        BuyShoppingTrolley.pop(num)
                                                        ProductList[k]['num'] +=1                                                                                                        #并且商店的商品+1件
                                                    else:
                                                        if BuyShoppingTrolley.get(num):
                                                            ProductList[k]['num'] = ProductList[k]['num']+BuyNum                                                                        #否者商店的商品+删除的商品数量
                                                            BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] -BuyNum                                               #购物车相对应的减去商品数量
                                                        else:
                                                            print ("购物车没有这个商品信息，请刷新系统缓存")
                                                    break
                                                else:
                                                    print ("您的购物车没有这么多商品，请重新输入")
                                                    return
                                            except ValueError as err:
                                                print (err)
                                    elif inc == None:                                                                                                                                    #否则用户操作不等于delete，那么就是等于add，这里add用None表示，因为在购买商品时，传入的add参数就是None
                                        while True:
                                            try:
                                                UserAdd = int(input("请输入要购买的商品数量"))
                                                if int(ProductList[k]['num']) >= UserAdd:                                                                                                #如果要购买的商品数量大于等于用户需要购买的数量，那么继续逻辑
                                                    PutInShoppingtrolley = input("是否放入购物车y/n")
                                                    if PutInShoppingtrolley == 'y':                                                                                                      #如果用户确认购买，那么商店减去商品库存量
                                                        ProductList[k]['num'] = ProductList[k]['num']-UserAdd
                                                        if BuyShoppingTrolley.get(num):
                                                            BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] +UserAdd                                              #如果这个商品在商店存在，那么就把这个商品放入购物车商品字典+要购买的商品数
                                                        else:
                                                            BuyShoppingTrolley[num] = {k:{'price':ProductList[k]['price'],'num':ProductList[k]['num'],'buy':int(UserAdd)}}           #否则初始化购物车字典
                                                        break
                                                    else:
                                                        break

                                                else:
                                                    print ("商品总量不够...请重新购买")
                                                    ShoppingTrolley()
                                                    return

                                            except ValueError as err:
                                                print (err)


                                            print ("已将商品加入购物车,可以进入购物车查看")
                                else:
                                    print ("余额不足，请充值")
    else:
        print ("没有这个商品")

#购物车界面以及购物车逻辑
def ShoppingTrolley():
    #os.system('clean')
    print (" *************************************欢迎进入购物车**************************************")
    if BuyShoppingTrolley:                                                                                                                  #如果购物车列表里面存在商品才会展示购物车
        print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品剩余数量(个)','商品已买数量(个)'))
        for i,j in BuyShoppingTrolley.items():                                                                                              #开始循环购物车
            for k,v in j.items():
                print('%-5s %-5s  %-20s  %-20d  %-20d  %-10d' % (' ',i,k,int(v['price']),ProductList[k]['num'],int(v['buy'])))      #这里的总商品数用的ProductList的，BuyShoppingTrolley字典没有存储总商品数量

        UserInc = input("请选择菜单 ：是否删除和新增商品,请输入'delete'或者'add',或者按'b'进行结算,否者返回主界面输入'q'")               #让用户选择操作
        if UserInc == "delete":                                                                                                            #接下来看是删除还是增加商品，那么就会调用Buy()函数
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

#算账功能，只有在充值和结账的时候才会调用
def Amount(CurrentUser,TotalAmountofGoods,inc=None):
    UserInfo=dict()
    with open('account.txt','r+') as db_file:                                                                                           #取出所有用户信息，包括用户名，密码，金钱，因为文件操作没有办法，只有全部取出然后在操作
        for readline in db_file.readlines():
            if readline.split()[0] == LoginUser:                                                                                           #如果是当前用户那么才改变金额
                UserWallet = readline.split()[2]
                if inc == 'add':
                    UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])+int(TotalAmountofGoods)}
                else:
                    UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])-int(TotalAmountofGoods)}
            else:
                UserInfo[readline.split()[0]] = {"pass":readline.split()[1],'amount':int(readline.split()[2])}                           #如果不是当前用户，那么只是读取出来，为了方便写入
            db_file.flush()
        db_file.close()

    with open('account.txt','w',) as db_file:                                                                                           #将字符串拼接成文件里面的格式，然后回写进文件
        for i,j in UserInfo.items():
            print (i + j['pass'] + str(j['amount']))
            db_file.write(i + " " + j['pass'] +  " " + str(j['amount']) + "\n")
            db_file.flush()
        db_file.close()

#用户充值模块，这个不多做解释
def UserPayment():
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

#结算模块
def CloseAnAccount():
    print (" *************************************进行清算系统**************************************")
    CommodityList = []
    if BuyShoppingTrolley:                                                                                                                  #首先判断购物车里面是否有商品，有商品才进行结账操作
        UserChoice = input("是否进行结账y/n")
        if UserChoice == 'y':
            for i,j in BuyShoppingTrolley.items():                                                                                          #把购物车所有商品*他们的单价放入字典
                for k,v in j.items():
                    CommodityList.append((int(v['price']) * int(v['buy'])))
            CommodityListEnd = sum(CommodityList)                                                                                           #计算所有商品的价格总和
            if UserWallet >= CommodityListEnd:                                                                                              #对比用户金钱是否比商品总价多
                Amount(LoginUser,CommodityListEnd)                                                                                          #如果用户金钱比商品总价多，那么调用算账模块
                print ("你的商品需要%s购买,余额将剩余%s"%(CommodityListEnd,UserWallet - CommodityListEnd))
                BuyShoppingTrolley.clear()                                                                                                  #并且清空购物车
            else:
                print ("余额不足,返回购物车")
                ShoppingTrolley()
        else:
            return

    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return

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
        UserWallet = UserBalance()
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

                    while True:                                                             #这里就不做多解释，循环调用那些功能模块
                        UserWallet = UserBalance()
                        ShoppingList(db_name,UserWallet,UserWallet)
                        ProductListdynamics(ProductList)
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
