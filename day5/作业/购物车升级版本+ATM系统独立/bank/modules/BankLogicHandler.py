








import os,sys,re,datetime
from bank.dbhelper.BankDBHandler import BankUserInfo
from bank.dbhelper.BankReportDBHandler import TransactionRecord
from taobao.dbhelper.StoreDBHandler import StoreProductList,StoreUserInfo

#from taobao.modules.StoreHandler import ShoppingTrolley         #这里不能导入了,因为StoreHandler也会调用这里的模块，就造成了循环，导入就会报错,具体原因见


#用户信用卡主接口,以下所有模块全是属于银行的模块
#这个模块就不做过多解释,基本就是输入什么选择对应的模块去实现对应的功能
def UserMainInterface(user):
    print ("*" * 121)
    while True:
        FromBankUserInfo = BankUserInfo()
        print("欢迎进入银行系统".center(117, '*'))
        print ("用户:",user,"信用额度:",FromBankUserInfo[user]['wallet'],"已使用:",FromBankUserInfo[user]['useruseamount'],"现金：",FromBankUserInfo[user]['cash'])
        print ('请选择菜单 ：输入选择  | 余额充值(1) | 结帐(2) | 提现(3) |转账(4) | 查看账单(5) | 还款(6) | ATM操作日志(7) | 退出(q) : ')
        try:
            UserChoice = input("请输入需要的操作")
        except:
            print ("输入错误,请重新选择")
        if UserChoice == "1":
            UserPay(user)
        elif UserChoice == "2":
            CloseAnAccount(user)
        elif UserChoice == "3":
            WithdraDeposit(user)
        elif UserChoice == "4":
            TransferAccounts(user)
        elif UserChoice == "5":
            BankExpenseCalendar(user,'write')
        elif UserChoice == "6":
            Repayment(user)
        elif UserChoice == "7":
            AtmLog(user)
        elif UserChoice == "q":
            break

#用户充值模块，这个不多做解释
def UserPay(user):
    #下面两行就是获取单个用户的总金额
    FromBankUserInfo = BankUserInfo()
    UserWallet = int(FromBankUserInfo[user]['wallet'])
    print ("当前可用额度：",int(FromBankUserInfo[user]['wallet'])-int(FromBankUserInfo[user]['useruseamount']))
    while True:
        UserChoice = input("是否需要充值,y/n")
        if UserChoice == 'y':
            UserInBalance=int(input("输入要充值的金额"))
            #直接把用户数据的金额加上用户输入的金额写入数据库就完成充值了
            BankUserInfo('write',user,'wallet',UserWallet+UserInBalance)
            break
        elif UserChoice == 'n':
            break
        else:
            print ("请输入正确的选项")

#用户结算模块
#只要是结账,转账,提现操作的模块,在函数里一定有调用账单统计的功能模块
def CloseAnAccount(user):
    print("进行清算系统".center(117, '*'))
    #计算商品价格总和的临时列表
    CommodityList = []
    #首先还是获取用户购物车信息
    UserShoppingCart=StoreUserInfo()[user]['usershoppingcart']
    #print (UserShoppingCart)
    if UserShoppingCart:                                                                                                                  #首先判断购物车里面是否有商品，有商品才进行结账操作
        UserChoice = input("是否进行结账y/n")
        if UserChoice == 'y':
            #然后计算用户购物车里面的商品总价：商品单价 * 商品数量,然后放入CommodityList里面
            for num,info in UserShoppingCart.items():                                                                                          #把购物车所有商品*他们的单价放入字典
                CommodityList.append((int(UserShoppingCart[num]['price']) * int(UserShoppingCart[num]['buy'])))
            SumCommodityList = sum(CommodityList)                                                                                           #计算所有商品的价格总和
            UserWallet = int(BankUserInfo()[user]['wallet'])
            UserAmount = int(BankUserInfo()[user]['useruseamount'])
            UserResidue = UserWallet - UserAmount
            if UserResidue >= SumCommodityList:                                                                                              #对比用户金钱是否比商品总价多
                NowUserUse = UserAmount + SumCommodityList
                BankUserInfo('write',user,'useruseamount',NowUserUse)                                                                                          #如果用户金钱比商品总价多，那么调用算账模块
                #结账后调用账单模块,将账单信息写入账单数据库
                TransactionRecord(action='write',type="bill",user=user,**UserShoppingCart)
                print ("你的商品需要%s购买,余额将剩余%s"%(SumCommodityList,UserWallet - NowUserUse))
                StoreUserInfo('write',user,'usershoppingcart','')                                                                        #并且清空购物车
            else:
                print ("余额不足,返回购物车")
        else:
            return

    else:
        print ("购物车没有任何信息")
        UserInc = input("按任意键返回主菜单")
        if UserInc:
            return

#提现模块
#只要是结账,转账,提现操作的模块,在函数里一定有调用账单统计的功能模块
def WithdraDeposit(user):
    #所有金额的一半才是可取现金额
    WithdrawalAmount = int(BankUserInfo()[user]['wallet']) / 2
    #用户总金额 - 已经用掉的金额 = 可用金额
    UserBalance = int(BankUserInfo()[user]['wallet']) - int(BankUserInfo()[user]['useruseamount'])
    #如果可用金额 大于 可提现金额,那么才予许提现
    if UserBalance >= WithdrawalAmount:
        print("您提现最高额度为%d,目前可提现余额为%d" %(WithdrawalAmount,WithdrawalAmount))
    else:
        print("您提现最高额度为%d,目前可提现余额为%d" % (WithdrawalAmount, UserBalance))
    UserCash = int(input("请输入要提现的金额"))
    UserChoice = input("确实是否进行提现？y/n")
    if UserChoice == "y":
        #如果用户要提现的金额小于等于用户现在的余额才予许提现
        if UserCash <= UserBalance:
            #用户最新的使用金额 =  用户目前使用金额 + 需要提现的金额
            UseUseAmount = BankUserInfo()[user]['useruseamount'] + UserCash
            #然后将最新金额信息写入数据库
            BankUserInfo('write',user,'useruseamount',UseUseAmount)
            #然后更新用户现金字段到数据库
            NewUserCash = int(BankUserInfo()[user]['cash']) + UserCash
            BankUserInfo('write', user, 'cash', NewUserCash)
            #这里好像是行多余的代码,但是因为代码过多,这里就不调试了，保留
            WithdrawalAmount = int(BankUserInfo()[user]['wallet']) / 2
            # 因为需要获取最新余额写入数据库
            UserBalance = int(BankUserInfo()[user]['wallet']) - int(BankUserInfo()[user]['useruseamount'])
            UserOperationRecords = {'1':{"usercash":UserCash,"userbalance":UserBalance}}
            #提现也会写入账单记录
            TransactionRecord(action='write', type="atm", user=user, **UserOperationRecords)
        else:
            print ("可提现额度不足,返回主界面")
            return
    else:
        return

#转账模块
#只要是结账,转账,提现操作的模块,在函数里一定有调用账单统计的功能模块
def TransferAccounts(user):
    ToAccount = input("请输入对方帐号")
    #获取所有用户信息
    FromBankUserInfo = BankUserInfo()
    #在数据库里面有这个用户名才能进行转账操作
    if FromBankUserInfo.get(ToAccount):
        TransferMoney = int(input("请输入要转账的金额"))
        #查询一下用户余额,只有用户余额大于转账金额的时候才允许转账
        UserBalance = int(BankUserInfo()[user]['wallet']) - int(BankUserInfo()[user]['useruseamount'])
        if TransferMoney < UserBalance:
            #转账人的已用金额更新到数据库
            BankUserInfo('write',user,'useruseamount',int(BankUserInfo()[user]['useruseamount'])+int(TransferMoney))
            #被转账人的总金额更新到数据库
            BankUserInfo('write',ToAccount,'wallet',int(BankUserInfo()[ToAccount]['wallet']) + int(TransferMoney))
            #最新用户余额，被转账人，转账金额写入账单
            UserBalance = int(BankUserInfo()[user]['wallet']) - int(BankUserInfo()[user]['useruseamount'])
            UserOperationRecords = {"1":{"transfermoney":TransferMoney,'touser':ToAccount,'userbalance':UserBalance}}
            TransactionRecord(action='write', type="transferaccounts", user=user, **UserOperationRecords)
            print ("转账成功%d,可用余额%d"%(TransferMoney,UserBalance))
        else:
            print ("余额不足,请重新选择")
    else:
        print ("没有这个帐号名")
        return

#信用卡管理模块
def CreditCardManagerment(user):
    while True:
        #首先判断用户是不是admin权限,如果不是,没有权限进入这个界面,直接退出
        IsAdmin = BankUserInfo()[user]['privilege']
        if IsAdmin == "admin":
            #首先获取所有用户信息,方便等会管理界面的时候展示出来
            AllUserInfo = BankUserInfo()
            print("信用卡后台管理".center(117, '*'))
            print('%-4s %-10s  %-10s  %-10s  %-10s' % (' ', '姓名', '总额度', '已使用金额', '状态'))
            for name,info in AllUserInfo.items():
                #这里用了一个if简写,就是把true改成正常,false改成冻结来显示
                info['lock'] = '正常' if info['lock'] == "False" else "冻结"
                print('%-4s %-10s  %-15s  %-10s  %-10s' % (' ', name, info['wallet'], info['useruseamount'],info['lock']))
            print('请选择菜单 ：输入选择  | 冻结信用卡账户(1) | 解冻信用卡账户(2)| 任意键退出信用卡管理')
            UserChoice = input("请输入需要的操作:")
            #如果用户输入等于1或者2,那么才会继续逻辑操作
            if UserChoice == "1" or UserChoice == "2":
                UserCreditAccount = input("请输入需要'冻结/解冻'的信用卡账户名称")
                #如果用户存在,才会进入逻辑操作
                if AllUserInfo.get(UserCreditAccount,None):
                    UserCreditAccountStatus = BankUserInfo()[UserCreditAccount]['lock']
                    if UserChoice == "1":
                        #如果发现要冻结的用户已经是冻结状态,那么提示已冻结并返回信用卡管理界面
                        if UserCreditAccountStatus == "True":
                            print ("%s信用卡已经是冻结状态"%UserCreditAccount)
                        else:
                            BankUserInfo('write',UserCreditAccount,'lock','True')
                            print ("账户已冻结，返回信用卡管理账户查看")
                    #解冻也是和冻结逻辑一样
                    elif UserChoice == "2":
                        if UserCreditAccountStatus == "False":
                            print ("%s信用卡已经是解冻状态"%UserCreditAccount)
                        else:
                            BankUserInfo('write',UserCreditAccount,'lock','False')
                    else:
                        break
                else:
                    print ("没有这个账户")
            else:
                break
        else:
            print ("该用户为普通用户，没有权限，返回商城首页")
            input("输入任意键退出")
            break

#ATM的日志展示
def AtmLog(user):
    import re
    print(" *************************************历史账单管理界面**************************************")
    # print('%-4s %-25s  %-20s  %-10s   %-10s ' % (' ', '时间', '地点', '剩余余额', '提现金额'))
    try:
        SinleUserAtmInfo = TransactionRecord('read',user)[user]
    except:
        print ("当前用户没有atm取现记录")
        return
    UserInputTime = input("请输入要查询的日期：如2022-01-01,不输入默认查询最近一个月")
    print('%-4s %-25s  %-20s  %-10s   %-10s ' % (' ', '时间', '地点', '剩余余额', '提现金额'))
    count = 0
    for ordernum, orderinfo in SinleUserAtmInfo.items():
        import datetime
        Nowtoday = datetime.datetime.now()
        LastOneMonth = Nowtoday - datetime.timedelta(days=30)

        for num,info in orderinfo.items():
            if UserInputTime != "" and re.match('\d{4}-\d{1,2}',UserInputTime):
                if  re.match(UserInputTime,info['time']) and info['type'] == "atm" :
                    print('%-4s %-25s  %-22s  %-13s   %-10s ' % (
                        ' ', info['time'], '上海398', info['userbalance'],
                        info['usercash'],))
                    count += 1
                else:
                    pass
            elif UserInputTime == "":
                billtime = datetime.datetime.strptime(info['time'], "%Y-%m-%d %H:%M:%S")
                if Nowtoday >= billtime >= LastOneMonth and info['type'] == "atm":
                    print('%-4s %-25s  %-22s  %-13s   %-10s ' % (
                        ' ', info['time'], '上海398', info['userbalance'],
                        info['usercash'],))
                    count += 1
                else:
                    pass
            else:
                print ("输入错误,退出atm账单查询")
                return

    if count == 0:
        print ("该月没有atm提现记录")
    input("按任意键退出")

def BankExpenseCalendar(user,action="read"):
    try:
        SinleUserALlInfo = TransactionRecord('read',user)[user]
    except:
        print ("当前用户没有账单")
        return
    # UserInputTime = input("请输入要查询的日期：如2022-01,不输入默认查询最近一个月")
    if action == "write":
        print(" *************************************信用卡历史账单管理界面**************************************")
        if SinleUserALlInfo is not None:
            print('%-4s %-25s  %-20s  %-10s  %-10s  %-10s' % (' ', '订单号', '订单时间','类型','操作', '消费金额'))


        UserInputTime = input("请输入要查询的日期：如2022-01,不输入默认查询最近一个月")


        if UserInputTime != "" and re.match('\d{4}-\d{1,2}',UserInputTime):
            NowToday = datetime.datetime.strptime(UserInputTime + "-" + "15" + " " + "00:00:00", "%Y-%m-%d %H:%M:%S")
        elif UserInputTime == "":
            NowToday = datetime.datetime.now()
        else:
            print ("日期输入错误，返回")
            return
    else:
        NowToday = datetime.datetime.now()

    #print (NowToday)
    LastOneMonth = NowToday - datetime.timedelta(days=30)
    NowYearMonth = str(NowToday)[0:7]
    # NowMonth = str(Nowtoday)[5:7]
    LastYearMonth = str(LastOneMonth)[0:7]
    #EndDate = NowYearMonth + "-" + "15" + " " + "00:00:00"
    EndDate = datetime.datetime.strptime(NowYearMonth + "-" + "15" + " " + "00:00:00", "%Y-%m-%d %H:%M:%S")
    #StartDate = LastYearMonth + "-" + "15" + " " + "00:00:00"
    StartDate = datetime.datetime.strptime(LastYearMonth + "-" + "15" + " " + "00:00:00", "%Y-%m-%d %H:%M:%S")

    #print ("start:",StartDate,"end:",EndDate)
#start 2022-07-15 00:00:00 end 2022-08-15 00:00:00

    AllPriceSum = []
    count = 0
    for ordernum, orderinfo in SinleUserALlInfo.items():
        SinleOrderPriceSum = []
        #print (ordernum,orderinfo)
        for num,info in orderinfo.items():
            billtime = datetime.datetime.strptime(info['time'], "%Y-%m-%d %H:%M:%S")
            # print ("billtime",billtime,"StartDate",StartDate,"EndDate",EndDate)
            if StartDate <= billtime <= EndDate:
                #print("billtime", billtime, "StartDate", StartDate, "EndDate", EndDate)
                if info['type'] == "bill":
                    SinleOrderChildPriceSum = int(info['price']) * int(info['buy'])
                    AllPriceSum.append(SinleOrderChildPriceSum)
                    SinleOrderPriceSum.append(SinleOrderChildPriceSum)
                elif info['type'] == "atm":
                    AllPriceSum.append(info['usercash'])
                elif info['type'] == "transferaccounts":
                    AllPriceSum.append(info['transfermoney'])
                count += 1

        if StartDate <= billtime <= EndDate and action=='write':
            if info['type'] == "bill":
                print('%-4s %-25s  %-25s  %-10s  %-10s  %-10s' % (' ', ordernum, info['time'], '账单', '购物', sum(SinleOrderPriceSum)))
            elif info['type'] == "atm":
                print('%-4s %-25s  %-25s  %-10s  %-10s  %-10s' % (' ', ordernum, info['time'], 'atm操作', '提现', info['usercash']))
            elif info['type'] == "transferaccounts":
                print('%-4s %-25s  %-25s  %-10s  %-11s  %-10s' % (' ', ordernum, info['time'], '转账', info['touser'], info['transfermoney']))
        # print (SinleOrderPriceSum)

    if count >= 1:
        print ('%-72s %-1s %-1s ' %('','本月账单共计:',sum(AllPriceSum)))
        UserCreditCardBill = BankUserInfo()[user]['creditcardbill']
        try:
            UserCreditCardBill[NowYearMonth]
            UserCreditBillCurrent =BankUserInfo()[user]['creditcardbill']
        except Exception as e:
            UserCreditBillCurrent = {NowYearMonth:{}}
        UserCreditBillCurrent[NowYearMonth]['bill'] = sum(AllPriceSum)
        BankUserInfo('write',user,'creditcardbill',UserCreditBillCurrent)
    else:
        print ("该月没有账单")

def Repayment(user):
    UserRepaymentInformation = BankUserInfo()[user]['creditcardbill']
    BankExpenseCalendar(user)       #自动默认查询当月账单
    NowToday = datetime.datetime.now()
    NowYearMonth = str(NowToday)[0:7]

    try:
        UserTotalBillMonth = BankUserInfo()[user]['creditcardbill'][NowYearMonth]['bill']
    except Exception as e:
        UserTotalBillMonth = 0
        print ("没有发现信用卡账单，返回")
        return

    try:
        UserRepayment = BankUserInfo()[user]['creditcardbill'][NowYearMonth]['userrepayment']
    except Exception as e:
        UserRepayment = 0

    print ("本月账单总金额:",UserTotalBillMonth,"本月已还金额：",UserRepayment,"本月剩余未还:",int(UserTotalBillMonth)-int(UserRepayment))
    UserChoice = input("请输入需要还款的金额:(仅支持还款当月账单)")
    if UserChoice != "":
        UserCreditCardBill = BankUserInfo()[user]['creditcardbill']

        try:
            UserCreditCardBill[NowYearMonth]
            UserRepaymentCurrent = BankUserInfo()[user]['creditcardbill']
            try:
                UserRepayment = BankUserInfo()[user]['creditcardbill'][NowYearMonth]['userrepayment']
            except Exception as e:
                UserRepayment = 0
        except Exception as e:
            UserRepaymentCurrent ={NowYearMonth: {}}

        UserRepaymentCurrent[NowYearMonth]['userrepayment'] =  int(UserChoice) + int(UserRepayment)
        BankUserInfo('write',user,'creditcardbill',UserRepaymentCurrent)
    else:
        print ("输入为空,返回信用卡管理主界面")
        return