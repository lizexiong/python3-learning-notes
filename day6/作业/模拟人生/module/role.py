



import os
from conf import setting
from database import DBApi
from module.common import write_file


class Penson(object):
    __role_db = "{0}.db".format(os.path.join(setting.DATABASE['dbpath'], setting.DATABASE["tables"]["role"]))
    __npc_db = "{0}.db".format(os.path.join(setting.DATABASE['dbpath'], setting.DATABASE["tables"]["npc"]))
    def __init__(self,type,name,age,):
        self.type = type
        self.name = name
        self.age = age
        self.money = setting.money
        self.vit = setting.vit
        self.sleeping = setting.sleeping
        self.working = setting.working
        self.DBLoad()
        #self.userinfo = self.DBLoad()  #该条作废,如果不是每次去数据库读取,那么都是老的数据
        #self.SleepTime()            #上线第一件事就是判断用户有没有睡过觉

    def DBLoad(self):
        '''
        主要负责处理存储角色信息
        1.如果么有该角色信息，那么存储进数据库，并返回所有角色信息
        2.如果有角色信息,直接返回所有角色信息
        :return:
        '''
        #调用dbapi接口,返回数据库所有数据
        RoleInfo=DBApi.LoadDataFromDB(self.__role_db)
        #如果数据库有数据
        if RoleInfo:
            try:
                #并且有当前用户数据
                UserInfo = RoleInfo[self.name]
                #那么就还是返回所有数据,有没有当前用户数据只是判断有没有当前用户
                return RoleInfo
            except Exception as e:
                #否则直接pass,走下面的逻辑,如果没有该用户的记录，那肯定是新用户了
                pass
        else:
            pass
        #新用户的字段
        NewUserInfo={self.name:{"type":self.type,'age':self.age,"money":self.money,"vit":self.vit,'sleeping':self.sleeping,'sleeptime':"",'working':self.working}}
        #下面的if是判断是空数据库还是数据库有数据只是没有这个用户的,根据方法来像数据库去存储
        if RoleInfo is None:
            #如果数据库没数据,那就是第一个用户,直接把新用户数据存储到数据库即可
            DBApi.AppendDB(NewUserInfo,self.__role_db)
        else:
            #否则肯定是加上现有用户数据+新用户数据追加到数据库
            RoleInfo[self.name] = {"type": self.type, 'age': self.age, "money": self.money,"vit":self.vit,'sleeping':self.sleeping,'sleeptime':"",'working':self.working}
            DBApi.AppendDB( RoleInfo,self.__role_db)
        return RoleInfo

    def NpcDBLoad(self):
        '''
        直接调用数据库接口,返回所有npc信息
        :return:
        '''
        NpcInfo = DBApi.LoadDataFromDB(self.__npc_db)
        return NpcInfo


    def SleepTime(self,StartTime=None,EndTime=None):
        '''
        该函数2个作用
        1.如果没有开始时间和结束时间,那么就计算玩家睡眠时间的， 一般都是上线后检查用户是不是在睡觉的,如果在睡觉状态,就要根据睡眠时间增加体力
        2.如果有开始时间和结束时间,那么就仅仅判断当前时间在不在合理时间范围内（如睡觉时间）
        :param StartTime:
        :param EndTime:
        :return:
        '''
        #首先加载用户数据库所有数据
        UserInfo = self.DBLoad()
        #因为是上线前调用,所以调用检查是否正在睡觉的模块,如果返回真,就代表睡过觉了,可以计算睡觉体力,所以这里返回True是正确的
        if self.SleepStatus():
            import datetime
            #因为函数两个作用,就是通过有没有开始时间和结束时间判断
            if StartTime == None and EndTime == None:
                #把用户数据库的的睡眠开始时间字符串转换为时间格式方便对吧
                UserSleepTime = datetime.datetime.strptime(UserInfo[self.name]['sleeptime'],'%Y-%m-%d %H:%M:%S')
                NowTime = datetime.datetime.now()
                #现在的时间-开始睡觉的时间就是已经睡觉的时间
                #total_seconds,因为只有计算这个区间段所有的秒数的函数,所以自己换算成为小数
                SleepDifference = (NowTime - UserSleepTime).total_seconds() / 60 / 60
                #如果睡眠时间大于8小时,那么加50点体力,否则睡眠不足,只能加20
                if SleepDifference >= 8:
                    UserRemainVit=int(UserInfo[self.name]['vit']) + 50
                else:
                    UserRemainVit = int(UserInfo[self.name]['vit']) + 20
                DBApi.ModifyDB(self.name, 'vit', UserRemainVit, self.__role_db)
                DBApi.ModifyDB(self.name, 'sleeping', 'False', self.__role_db)
                #记录日志
                write_file(self.name + "睡眠" + SleepDifference + "小时" , 'info', setting.LOG_PATH + "/game.log")
            else:
                #计算当前时间在不在一个时间内的功能
                StartTime = datetime.datetime.strptime(str(datetime.datetime.now().date()) + StartTime, '%Y-%m-%d%H:%M')
                EndTime = datetime.datetime.strptime(str(datetime.datetime.now().date()) + EndTime, '%Y-%m-%d%H:%M')
                NowTime = datetime.datetime.now()
                if StartTime < NowTime < EndTime:
                    return True
                return False
        else:
            pass

    def SleepStatus(self,choice='no'):
        '''
        判断用户是否在睡眠中的函数,如果不是,返回False,如果是，让用户判断是否需要强制唤醒
        :param choice:  yes或者no,让玩家选择是否要强制唤醒睡眠
        :return:
        '''
        #取出用户数据库中的睡眠状态
        status = self.DBLoad()[self.name]['sleeping']
        #如果为真
        if status == "True":
            #如果用户输入需要强制唤醒
            if choice == "yes":
                #那么改变用户数据状态,强制唤醒
                DBApi.ModifyDB(self.name,'sleeping','False',self.__role_db)
                write_file(self.name + "睡眠强制唤醒", 'info', setting.LOG_PATH + "/game.log")
                return False
            else:
                return True
        else:
            return False

    def Eat(self,eat):
        '''
        用户吃饭函数
        1.用户可以选择是否吃饭
        2.吃饭时间是否饭点，如果是饭点，增加20点体力,减少20元,如果不是饭点,增加10点体力,减少20元
        :param eat:  让用户选择是否要吃饭
        :return:
        '''
        #首先取出所有用户数据
        UserInfo = self.DBLoad()
        #如果不是在睡觉状态,才会开始逻辑
        if self.SleepStatus() is False:
            #如果用户金钱大于20,才会开始逻辑
            if int(UserInfo[self.name]['money']) >= 20:
                #如果这个时间这是饭点
                if self.SleepTime("12:00","13:00") or self.SleepTime("17:00","18:00"):
                    #玩家选择要吃饭,那么金钱减少20，体力增加20，并计入数据库
                    if eat == "yes":
                        print("现在是饭点,20块钱能增加20点体力")
                        UserVit = int(UserInfo[self.name]['vit']) + 20
                        UserMoney = int(UserInfo[self.name]['money']) - 20
                        DBApi.ModifyDB(self.name,'money',UserMoney,self.__role_db)
                        write_file(self.name + "吃饭,增加20点体力,金钱减少20", 'info', setting.LOG_PATH + "/game.log")
                    #否则饭点不吃饭,掉20点体力
                    elif eat == "no":
                        print ("不吃饭掉20点体力吧")
                        UserVit = int(UserInfo[self.name]['vit']) - 20
                        UserVit =UserVit if UserVit > 0 else 0
                        write_file(self.name + "不吃饭,减少20点体力", 'info', setting.LOG_PATH + "/game.log")
                    DBApi.ModifyDB(self.name,'vit',UserVit,self.__role_db)
                else:
                    #如果不是饭点,那么花20块钱只能增加10点体力
                    if eat == "yes":
                        print ("现在不是饭点,20块钱只能增加10点体力")
                        UserVit = int(UserInfo[self.name]['vit']) + 10
                        UserMoney = int(UserInfo[self.name]['money']) - 20
                        DBApi.ModifyDB(self.name,'money',UserMoney,self.__role_db)
                        DBApi.ModifyDB(self.name, 'vit', UserVit, self.__role_db)
                        write_file(self.name + "不是饭点,增加10点体力,金钱减少20", 'info', setting.LOG_PATH + "/game.log")
                    else:
                        print ("现在不是吃饭时间,不吃就不吃吧")
            else:
                print ("没钱吃饭,吃屎吧你")
        else:
            print ("睡觉中,无法进行任何操作")
            #让用户选择是否需要强制唤醒
            UserChoice = input("是否要强制唤醒")
            if UserChoice == "yes":
                self.SleepStatus('yes')

    def Sleep(self,sleep):
        '''
        用户睡觉函数
        1.用户可以选择是否睡觉
        2.是否睡觉的时间，如果是，增加20点体力，否则增加10点(不是及时增加,在睡醒后结算,中断睡眠不加体力)，该功能未实现，在结算函数实现，不是这里，差不多就得了
        3.如果确认睡觉，将用户睡眠时间计入数据库，并更改用户睡眠状态
        :param sleep:  用户确认是否开始睡觉
        :return:
        '''
        import datetime
        UserInfo = self.DBLoad()

        #判断用户是否正在睡眠中
        if self.SleepStatus() is False:
            #如果是睡觉的点
            if self.SleepTime("00:00","09:00"):
                #并且用户确认睡觉,那么就
                #1.记录用户开始睡觉时间. 2.修改用户睡眠状态
                if sleep == "yes":
                    print("现在是睡觉的点,睡觉能增加20点体力,进入睡眠状态")
                    #UserVit = int(UserInfo[self.name]['vit']) + 20
                    DBApi.ModifyDB(self.name,'sleeptime',datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"),self.__role_db)
                    DBApi.ModifyDB(self.name,'sleeping','True',self.__role_db)
                    write_file(self.name + "开始睡觉", 'info', setting.LOG_PATH + "/game.log")
                #否则直接控制20点体力
                elif sleep == "no":
                    print ("熬夜减20点体力")
                    UserVit = int(UserInfo[self.name]['vit']) - 20
                    UserVit =UserVit if UserVit > 0 else 0
                    write_file(self.name + "不睡觉,减少20点体力", 'info', setting.LOG_PATH + "/game.log")
                    DBApi.ModifyDB(self.name, 'vit', UserVit, self.__role_db)
            else:
                #并且用户确认睡觉,那么就
                #1.记录用户开始睡觉时间. 2.修改用户睡眠状态
                if sleep == "yes":
                    print ("现在不是睡觉的点,睡觉能增加10点体力")
                    #UserVit = int(UserInfo[self.name]['vit']) + 10
                    DBApi.ModifyDB(self.name,'sleeptime',datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"),self.__role_db)
                    DBApi.ModifyDB(self.name,'sleeping','True',self.__role_db)
                    write_file(self.name + "不是睡觉的点睡觉", 'info', setting.LOG_PATH + "/game.log")
                else:
                    pass
        else:
            print ("已经正在睡觉中....")
            UserChoice = input("是否要强制唤醒")
            if UserChoice == "yes":
                self.SleepStatus('yes')

class Staff(Penson):
    '''
    员工类,员工现有属性打工
    '''
    __role_db = "{0}.db".format(os.path.join(setting.DATABASE['dbpath'], setting.DATABASE["tables"]["role"]))   #私有属性不能继承和调用,所以只能在写一遍
    __npc_db = "{0}.db".format(os.path.join(setting.DATABASE['dbpath'], setting.DATABASE["tables"]["npc"]))

    def __init__(self,type,name,age,):
        super(Staff,self).__init__(type,name,age,)
        print ("欢迎你,天选打工人,欢迎来到打工系统")
        #有新员工注册,就记录进日志
        write_file("新员工" + self.name + "注册", 'info', setting.LOG_PATH + "/game.log")


    def WorkStatus(self,choice='no'):
        '''
        和睡眠状态一样的逻辑，这里不做过多解释
        :param choice:
        :return:
        '''
        status = self.DBLoad()[self.name]['working']
        if status == "True":
            if choice == "yes":
                DBApi.ModifyDB(self.name, 'working', 'False', self.__role_db)
                write_file(self.name + "打工强制中断", 'info', setting.LOG_PATH + "/game.log")
                return False
            else:
                return True
        else:
            return False

    def Work(self,work):
        '''
        无限打工函数,只要有力气,就能干到死
        :param work: 玩家确认是否要工作
        :return:
        '''
        UserInfo = self.DBLoad()
        #如果玩家不再睡眠状态
        if self.SleepStatus() is False:
            #并且玩家体力大于10才能打工
            UserRemainVit = UserInfo[self.name]['vit']
            if UserRemainVit >= 10:
                #玩家确认打工
                if work == "yes":
                    NpcInfoMoney = self.NpcDBLoad()['wuxinzhe']['money']
                    print("打工给钱,无限打工,只要你有力气")
                    #并且老板有钱发工资
                    #那么10点体力换10块钱
                    if NpcInfoMoney >=10:
                        UserMoney = int(UserInfo[self.name]['money']) + 10
                        UserVit = int(UserInfo[self.name]['vit']) - 10
                        NpcMoney = int(NpcInfoMoney) - 10
                        DBApi.ModifyDB(self.name,'money',UserMoney,self.__role_db)
                        DBApi.ModifyDB(self.name, 'vit', UserVit, self.__role_db)
                        DBApi.ModifyDB('wuxinzhe', 'money', NpcMoney, self.__npc_db)
                        write_file(self.name + "打工增加10块钱,减少10点体力", 'info', setting.LOG_PATH + "/game.log")
                    else:
                        print ("老板没钱跑路了,面试去吧")
                elif work == "no":
                    print ("不打工你去卖屁股吗？")
            else:
                print ("体力已不够10,无法打工")
                write_file(self.name + "体力已不够10,无法打工", 'info', setting.LOG_PATH + "/game.log")
        else:
            print ("睡觉中,无法进行任何操作")
            UserChoice = input("是否要强制唤醒")
            if UserChoice == "yes":
                self.SleepStatus('yes')


