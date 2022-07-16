

from taobao.template.ShoppingList import ProductList,UserShoppingTrolley
from taobao.modules.buy import Buy

#购物车界面以及购物车逻辑
def ShoppingTrolley(user):
    #os.system('clean')
    print (" *************************************欢迎进入购物车**************************************")
    if UserShoppingTrolley:                                                                                                                  #如果购物车列表里面存在商品才会展示购物车
        print('%-4s %-5s  %-15s  %-10s  %-10s  %-10s' % (' ','编号','商品名称','商品价格(元)','商品剩余数量(个)','商品已买数量(个)'))
        for k,v in UserShoppingTrolley.items():                                                                                              #开始循环购物车
            print('%-5s %-5s  %-20s  %-20d  %-15d  %-10d' % (' ',k,UserShoppingTrolley[k]['name'],int(UserShoppingTrolley[k]['price']),int(ProductList[k]['num']),int(UserShoppingTrolley[k]['buy'])))      #这里的总商品数用的ProductList的，BuyShoppingTrolley字典没有存储总商品数量

        UserInc = input("请选择菜单 ：是否删除和新增商品,请输入'delete'或者'add',或者按'b'进行结算,否者返回主界面输入'q'")               #让用户选择操作
        if UserInc == "delete":                                                                                                            #接下来看是删除还是增加商品，那么就会调用Buy()函数
            ProductID = int(input("请输入商品编号"))
            Buy(ProductID,user,UserInc)
            ShoppingTrolley(user)
        elif UserInc == 'add':
            ProductID = int(input("请输入商品编号"))
            Buy(ProductID,user)
            ShoppingTrolley(user)
        elif UserInc == 'b':
            CloseAnAccount()
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