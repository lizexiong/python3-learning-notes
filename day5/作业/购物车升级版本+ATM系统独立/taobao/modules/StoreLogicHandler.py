


import json

from taobao.dbhelper.StoreDBHandler import StoreProductList,StoreUserInfo
from bank.dbhelper.BankDBHandler import BankUserInfo
from bank.dbhelper.BankReportDBHandler import TransactionRecord
from bank.modules.BankLogicHandler import CloseAnAccount               #不能再调用了，不然就调用循环了

#购买和退订商品
def Buy(num,user,inc=None):
    #在本章写会数据库里面有详细解释,就是为了把新的购物车信息和老的购物车信息进行整合在写回数据库的作用
    UserShoppingTrolleyTmp = dict()
    #调用dbhelpler函数,获取所有的商品信息
    ProductList = StoreProductList()
    #如果用户输入的商品编号在商品数据库里面，那么才会开始购买或者取消订单的逻辑
    if ProductList.get(num):
        #首先获取所有用户的信息银行卡信息,比如金钱等
        FromDBBankUserInfo = BankUserInfo()
        #获取所有用户淘宝商城的个人信息，比如购物车等
        FromDBStoreUserInfo = StoreUserInfo()
        #过滤出用户的总金额信息
        UserWallet = FromDBBankUserInfo[user]['wallet']
        #下面2行代码获取商品的价格和名称信息
        ProductPrice = ProductList[num]['price']
        ProductName = ProductList[num]['name']
        #从所有用户信息里面获取单个用户的购物车信息
        UserShoppingCart = FromDBStoreUserInfo[user]['usershoppingcart']
        print (FromDBStoreUserInfo[user]['usershoppingcart'],type(FromDBStoreUserInfo[user]['usershoppingcart']))
        #如果用户购物车里面不等于空，也就是有商品信息存在
        if UserShoppingCart != "":
            #那么将这些信息转换成为字典类型,这里就是需要转一遍，否则为字符串,讲道理不需要转,但有时候报错,有时候不报错,这里转一遍比较保险,也学习一下eval的用法
            UserShoppingCart = eval(str(FromDBStoreUserInfo[user]['usershoppingcart']))
            #UserShoppingCart = FromDBStoreUserInfo[user]['usershoppingcart']
        else:
            #否则用户购物车等于空
            UserShoppingCart = {}

        #如果用户的操作是删除
        if inc == 'delete':
            while True:
                try:
                    DelProductNum = int(input("要删除的商品数量"))
                    #如果用户购物车里面的商品购买数量大于或者等于要删除的数量，才会进入正常的逻辑
                    if UserShoppingCart[num]['buy'] >= DelProductNum:
                        #如果用户购买的数量小于等于1,那么代表购物车里面只有一件商品,那么直接在用户购物车里面删除这件商品信息,并且在总商品列表里面+1即可
                        if UserShoppingCart[num]['buy'] <=1:
                            UserShoppingCart.pop(num)
                            ProductNum = ProductList[num]['num'] + 1
                        #如果用户购物车里面的商品购买总量>1,那么就仔细看看用户要删除几件商品,然后对应的在用户购物车里面减去对应数量,在总商品列表里面加上对应数量
                        else:
                            UserShoppingCart[num]['buy'] = UserShoppingCart[num]['buy'] - DelProductNum
                            ProductNum = ProductList[num]['num'] + DelProductNum
                        #不管用户购物车数量是小于等于1还是大于1,都会把最新的用户购物车信息写入回数据库,方便下次获取到最新的信息
                        StoreUserInfo('write', user, 'usershoppingcart', UserShoppingCart)
                        #总商品列表里面的信息也要实时写入回数据库
                        StoreProductList('write',num,'num',ProductNum)
                        break
                    else:
                        print("您的购物车没有这么多商品，请重新输入")
                except:
                    print ("输入了可能不存在商品,请重新输入")
                    break
        #或者用户的操作是None，如果为None,这里的程序就判定为增加购买操作
        elif inc == None:
            while True:
                try:
                    UserAdd = int(input("请输入要购买的商品数量"))
                    #获取商品列表里面单个商品的总数量
                    ProductListNum = int(ProductList[num]['num'])
                    #如果单个商品的总数量大于用户要购买的数量,才能进行购买
                    if ProductListNum >= UserAdd:
                        PutInShoppingtrolley = input("是否放入购物车y/n")
                        if PutInShoppingtrolley == "y":
                            #如果用户确认购买,那么商品总数量就要减去用户购买的数量
                            ProductListNum = ProductListNum - UserAdd
                            #并且实时刷新回数据库
                            StoreProductList('write',num,'num',ProductListNum)
                            if UserShoppingCart.get(num,None):
                                # 如果用户购物车里面get到这个商品,也就是购物车里面之前加过
                                #那么用户购物车里面的在加上用户最新购买的数量,就是最新的总数
                                UserShoppingCart[num]['buy'] = UserShoppingCart[num]['buy'] + int(UserAdd)
                                #并将该最新信息存入临时的用户购物车信息里面,这个临时的字典作用在函数开篇讲解过
                                UserShoppingTrolleyTmp[num] = {'name': ProductName, 'price': ProductPrice,'buy': UserShoppingCart[num]['buy']}
                            else:
                                #如果用户购物车里面没有这个信息,那么直接写入临时字典
                                UserShoppingTrolleyTmp[num] = {'name':ProductName, 'price': ProductPrice, 'buy': int(UserAdd)}
                            #这里在说明一遍临时购物车字典的作用,是因为可能原有的用户购物车里面有信息,也需要保留,这里是全部取出来,然后更新上用户更新购买的信息,然后写入数据库
                            #比如,原有数据库买了一台华为手机,然后又买了一台三星手机,如果不先全部取出来操作,只写回数据库最新信息,那么老的购买的商品在用户购物车就不存在了
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
    #首先获取所有商品的信息,等会打印剩余总商品数量的时候用
    ProductList = StoreProductList()
    #或者淘宝商城所有用户的信息
    FromDBStoreUserInfo = StoreUserInfo()
    #通过淘宝商城所有用户的信息获取单个用户购物车的信息
    UserShoppingCart = FromDBStoreUserInfo[user]['usershoppingcart']
    #如果用户购物车有数据,那么就是存在商品
    if UserShoppingCart :                                                                                                                  #如果购物车列表里面存在商品才会展示购物车
        #这里的eval和 购买函数里面的用法一样,也是不需要的,但是会报错,具体哪个场景忘了,这里加了也没错
        UserShoppingCart = eval(str(FromDBStoreUserInfo[user]['usershoppingcart']))
        print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品剩余数量(个)','商品已买数量(个)'))
        #开始循环,打印购物车的信息以及总商品列表最新的剩余商品个数信息
        for k,v in UserShoppingCart.items():                                                                                              #开始循环购物车
            print('%-5s %-5s  %-20s  %-20d  %-15d  %-10d' % (' ',k,UserShoppingCart[k]['name'],int(UserShoppingCart[k]['price']),int(ProductList[k]['num']),int(UserShoppingCart[k]['buy'])))      #这里的总商品数用的ProductList的，BuyShoppingTrolley字典没有存储总商品数量
        #以下就简单了,判断用户是否购买还是删除购物车操作,重新调用购买商品函数(buy)就行了
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

#淘宝商城的账单信息
def ExpenseCalendar(user):
    import re
    #获取单个用户的账单历史信息
    #这里解释一下,只有结账后才会生成账单信息,因为模拟环境,所有关于钱的信息和账单都在银行那边,所以需要调用银行的模块,账单也不例外
    SinleUserBillInfo = TransactionRecord('read',user)[user]
    #print (SinleUserBillInfo)
    #如果有账单信息,那么就开始打印所有账单,因为是淘宝的账单信息,所以没有选择查询时间,有账单就打印了
    if SinleUserBillInfo is not None:
        print (" *************************************历史账单管理界面**************************************")
        print('%-4s %-25s  %-20s  %-10s  %-10s  %-10s' % (' ', '订单号', '订单时间','商品名称', '商品价格(元)',  '商品购买数量(个)',))
        count = 0
        for ordernum,orderinfo in SinleUserBillInfo.items():
            TotalPriceCalc = []
            for num,info in orderinfo.items():
                #这里简单解释一下,账单分为三个类型:atm,转账,bill,等于bill就是淘宝的购物账单
                if info['type'] == "bill":
                    TotalPriceCalc.append(int(info['price']) * int(info['buy']))
                    if count <1 :
                        #这里为什么<1打印多了两个ordernum和info['time'],因为可能一个账单里面有2个商品,所以账单号和购买时间肯定是一样的,没必要重复打印
                        print('%-4s %-25s  %-25s  %-15s  %-15s  %-10s' % (
                        ' ', ordernum,info['time'], info['product'], info['price'], info['buy'], ))
                    else:
                        print('%-4s %-25s  %-25s  %-15s  %-15s  %-10s' % (
                        ' ', ' '*25, ' '*20,info['product'], info['price'], info['buy'], ))
                    count +=1
                else:
                    pass
            #(注意这里2层循环)等内循环完成了,代表单个账单循环完成了,那么就输出单个账单总价，最后将count=0,下一个账单的时候重新计算
            if count >= 1:
                print ('%-87s %-1s %-25s ' % (' ','总价:',sum(TotalPriceCalc)))
                count = 0
    else:
        print ("用户没有消费记录")
    input("按任意键退出")