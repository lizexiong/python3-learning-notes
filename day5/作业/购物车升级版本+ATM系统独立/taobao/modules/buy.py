



from taobao.template.ShoppingList import ProductList,UserShoppingTrolley
from taobao.databases.StoreUserDBHandler import StoreUserInfo
from bank.databases.BankUserDBHandler import BankUserInfo







#购买和退订商品
def Buy(num,user,inc=None):
    if ProductList.get(num):
        FromDBBankUserInfo = BankUserInfo()
        UserWallet = FromDBBankUserInfo[user]['wallet']
        # for ProductNum,ProductInfo in ProductList.items():
        ProductPrice = ProductList[num]['price']
        ProductName = ProductList[num]['name']
        if inc == 'delete':
            while True:
                try:
                    DelProductNum = int(input("要删除的商品数量"))
                    if UserShoppingTrolley[num]['buy'] >= DelProductNum:
                        if UserShoppingTrolley[num]['buy'] <=1:
                            UserShoppingTrolley.pop(num)
                            ProductList[num]['num'] += 1
                        else:
                            ProductList[num]['num'] = ProductList[num]['num'] + DelProductNum
                            UserShoppingTrolley[num]['buy'] = UserShoppingTrolley[num]['buy'] - DelProductNum
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
                    if ProductList[num]['num'] >= UserAdd:
                        PutInShoppingtrolley = input("是否放入购物车y/n")
                        if PutInShoppingtrolley == "y":
                            ProductList[num]['num'] = ProductList[num]['num'] - UserAdd
                            if UserShoppingTrolley.get(num):
                                UserShoppingTrolley[num]['buy'] = UserShoppingTrolley[num]['buy'] + UserAdd
                            else:
                                UserShoppingTrolley[num] = {'name':ProductName, 'price': ProductPrice, 'buy': int(UserAdd)}
                            print (UserShoppingTrolley)
                            print("已将商品加入购物车,可以进入购物车查看")
                            break
                        else:
                            break
                    else:
                        print ("商品数量不够,请重新购买")
                        break
                except :
                    print ("输入了可能不存在商品,请重新输入")
                    break
    else:
        print("没有这个商品")


