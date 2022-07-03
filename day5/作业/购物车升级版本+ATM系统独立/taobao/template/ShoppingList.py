__author__ = 'Administrator'










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