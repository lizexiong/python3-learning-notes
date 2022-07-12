



from taobao.template.ShoppingList import ProductList
from taobao.databases.StoreUserDBHandler import StoreUserInfo




#购买和退订商品
def Buy(num,inc=None):
    if ProductList.get(num):
        FromDBStoreUserInfo = StoreUserInfo()
        print (FromDBStoreUserInfo)
    else:
        print("没有这个商品")




# #购买和退订商品
# def Buy(num,inc=None):
#     if ProductListNum.get(num):                                                                                                                                                         #判断用户输入的商品ID是否存在
#         with open('account.txt','r+') as db_file:
#             for readline in db_file.readlines():
#                 username= readline.split()[0]
#                 if username == LoginUser:                                                                                                                                               #打开账户文件,判断是否是当前用户
#                     UserWallet = int(readline.split(' ')[2])                                                                                                                            #获取当前用户的钱总额
#                     for i,j in ProductListNum.items():
#                         if int(i) == num:
#                             for k,v in j.items():
#                                 DbCommodity_prices = int(v['price'])                                                                                                                    #获取商品的单价
#                                 if UserWallet >= DbCommodity_prices:                                                                                                                     #如果用户的钱多余商品的价格
#                                     if inc == "delete":                                                                                                                                 #如果用户输入的指令是删除商品，这个逻辑有点废了，但是改动太麻烦，就写上吧
#                                         while True:
#                                             try:
#                                                 # UserDel = int(input("请输入要删除的商品编号"))
#                                                 BuyNum = int(input("要删除的商品数量"))                                                                                                  #那么输入要删除的数量
#                                                 print (BuyShoppingTrolley[num][k]['buy'])
#                                                 if BuyShoppingTrolley[num][k]['buy'] >= BuyNum:                                                                                          #如果添加进入购物车的数量大于等于用户输入的要删除的数量
#                                                     if  BuyShoppingTrolley[num][k]['buy'] <=1:                                                                                           #并且如果加购物车的商品数量小于等于1，那么就直接删除整个商品key
#                                                         BuyShoppingTrolley.pop(num)
#                                                         ProductList[k]['num'] +=1                                                                                                        #并且商店的商品+1件
#                                                     else:
#                                                         if BuyShoppingTrolley.get(num):
#                                                             ProductList[k]['num'] = ProductList[k]['num']+BuyNum                                                                        #否者商店的商品+删除的商品数量
#                                                             BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] -BuyNum                                               #购物车相对应的减去商品数量
#                                                         else:
#                                                             print ("购物车没有这个商品信息，请刷新系统缓存")
#                                                     break
#                                                 else:
#                                                     print ("您的购物车没有这么多商品，请重新输入")
#                                                     return
#                                             except ValueError as err:
#                                                 print (err)
#                                     elif inc == None:                                                                                                                                    #否则用户操作不等于delete，那么就是等于add，这里add用None表示，因为在购买商品时，传入的add参数就是None
#                                         while True:
#                                             try:
#                                                 UserAdd = int(input("请输入要购买的商品数量"))
#                                                 if int(ProductList[k]['num']) >= UserAdd:                                                                                                #如果要购买的商品数量大于等于用户需要购买的数量，那么继续逻辑
#                                                     PutInShoppingtrolley = input("是否放入购物车y/n")
#                                                     if PutInShoppingtrolley == 'y':                                                                                                      #如果用户确认购买，那么商店减去商品库存量
#                                                         ProductList[k]['num'] = ProductList[k]['num']-UserAdd
#                                                         if BuyShoppingTrolley.get(num):
#                                                             BuyShoppingTrolley[num][k]['buy'] = BuyShoppingTrolley[num][k]['buy'] +UserAdd                                              #如果这个商品在商店存在，那么就把这个商品放入购物车商品字典+要购买的商品数
#                                                         else:
#                                                             BuyShoppingTrolley[num] = {k:{'price':ProductList[k]['price'],'num':ProductList[k]['num'],'buy':int(UserAdd)}}           #否则初始化购物车字典
#                                                         break
#                                                     else:
#                                                         break
#
#                                                 else:
#                                                     print ("商品总量不够...请重新购买")
#                                                     ShoppingTrolley()
#                                                     return
#
#                                             except ValueError as err:
#                                                 print (err)
#
#
#                                             print ("已将商品加入购物车,可以进入购物车查看")
#                                 else:
#                                     print ("余额不足，请充值")
#     else:
#         print ("没有这个商品")