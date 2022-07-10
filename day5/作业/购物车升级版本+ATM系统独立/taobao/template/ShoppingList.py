__author__ = 'Administrator'








#商品列表
ProductList = {
    'huawei':{'price':'5000','sum':10,'num':10},
    'apple':{'price':'1000','sum':15,'num':0},
    'sanxing':{'price':'4000','sum':20,'num':20},
    'xiaomi':{'price':'1000','sum':10,'num':10},
}


#用户信息显示模块
def ShoppingList(username,wallet,balance,shoping_cart=0):
    # os.system('clear')
    ShoppingListStr =  '''
    *********************************************************************************
    *                                                                               *
    *                                欢迎来到淘宝                                    *
    *                                                                               *
    *********************************************************************************
    会员：%s\t金额：%s\t当前余额：%s\t购物车：%d\n
    ''' %(username,wallet,balance,shoping_cart)
    print (ShoppingListStr)


ProductListNum=dict()      #全局变量，存储新的ProductList信息，包括编号
#商品动态信息
def ProductListdynamics(ProductList):
    print('     =================================================================================')
    print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品总数量(个)','商品剩余数量(个)'))
    i=1 #商品编号
    for ProductKey,ProductValue in ProductList.items():
        print('%-5s %-5d  %-20s  %-20d  %-20d  %-10d' % (' ',i,ProductKey,int(ProductValue['price']),int(ProductValue['sum']),int(ProductValue['num'])))
        ProductListNum[i]=({ProductKey:{'price':int(ProductValue['price']),'sum':int(ProductValue['sum']), 'num':int(ProductValue['num'])}})
        i+=1
