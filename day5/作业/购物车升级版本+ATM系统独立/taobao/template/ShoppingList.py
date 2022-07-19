__author__ = 'Administrator'










#用户信息显示模块
def ShoppingList(username,wallet,balance,shoping_cart=0):
    # os.system('clear')
    ShoppingListStr =  '''
    *********************************************************************************   
    *                                                                               *
    *                                欢迎来到淘宝                                     *
    *                                                                               *
    *********************************************************************************
    会员：%s\t金额：%s\t当前余额：%s\t购物车：%d\n
    ''' %(username,wallet,balance,shoping_cart)
    print (ShoppingListStr)


#商品动态信息
def ProductListdynamics(ProductList):
    print('     =================================================================================')
    print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品总数量(个)','商品剩余数量(个)'))
    for ProductKey,ProductValue in ProductList.items():
        print('%-5s %-5s  %-20s  %-20d  %-20d  %-10d' % (' ',ProductKey,ProductValue['name'],int(ProductValue['price']),int(ProductValue['sum']),int(ProductValue['num'])))
