



import os
from conf import setting
from database import DBApi


class Penson(object):
    __database = "{0}.db".format(os.path.join(setting.DATABASE['dbpath'], setting.DATABASE["tables"]["role"]))
    def __init__(self,type,name,age,money):
        self.type = type
        self.name = name
        self.age = age
        self.money = money
        self.vit = setting.vit
        self.sleeping = setting.sleeping
        self.userinfo = self.DBLoad()

    def DBLoad(self):
        RoleInfo=DBApi.LoadDataFromDB(self.__database)
        if RoleInfo:
            try:
                UserInfo = RoleInfo[self.name]
                return RoleInfo
            except Exception as e:
                pass
        else:
            pass
        NewUserInfo={self.name:{"type":self.type,'age':self.age,"money":self.money,"vit":self.vit,'sleeping':self.sleeping,'sleeptime':""}}
        if RoleInfo is None:
            DBApi.AppendDB(NewUserInfo,self.__database)
        else:
            RoleInfo[self.name] = {"type": self.type, 'age': self.age, "money": self.money,"vit":self.vit,'sleeping':self.sleeping,'sleeptime':""}
            DBApi.AppendDB( RoleInfo,self.__database)
        return RoleInfo

    def SleepTime(self,StartTime=None,EndTime=None):
        import datetime
        if StartTime == None and EndTime == None:
            UserSleepTime = datetime.datetime.strptime(self.userinfo[self.name]['sleeptime'],'%Y-%m-%d %H:%M:%S')
            NowTime = datetime.datetime.now()
            SleepDifference = (NowTime - UserSleepTime).total_seconds() / 60 / 60
            if SleepDifference >= 8:
                UserRemainVit=int(DBApi.LoadDataFromDB(self.__database)[self.name]['vit']) + 50
            else:
                UserRemainVit = int(DBApi.LoadDataFromDB(self.__database)[self.name]['vit']) + 20
            DBApi.ModifyDB(self.name, 'vit', UserRemainVit, self.__database)

        else:
            StartTime = datetime.datetime.strptime(str(datetime.datetime.now().date()) + StartTime, '%Y-%m-%d%H:%M')
            EndTime = datetime.datetime.strptime(str(datetime.datetime.now().date()) + EndTime, '%Y-%m-%d%H:%M')
            NowTime = datetime.datetime.now()
            if StartTime < NowTime < EndTime:
                return True
            return False


    def SleepStatus(self,rouse='no'):
        status = self.userinfo[self.name]['sleeping']
        if status == "True":
            if rouse == "yes":
                self.userinfo[self.name]['sleeping'] = "False"
                DBApi.AppendDB(self.userinfo,self.__database)
                return False
            else:
                return True
        else:
            return False

    def Settlement(self):
        sleeptime = DBApi.LoadDataFromDB()[self.time]['sleeptime']



    def AddVit(self,action,num):
        UserInfo = self.userinfo
        if action == "inc":
            UserVit = int(UserInfo[self.name]['vit']) + num
        elif action == "red":
            UserVit = int(UserInfo[self.name]['vit']) - num
        UserInfo[self.name]['vit'] = UserVit
        DBApi.AppendDB(UserInfo, self.__database)


    def Eat(self,eat):
        UserInfo = self.userinfo
        if self.SleepStatus() is False:
            if int(UserInfo[self.name]['money']) >= 20:
                if self.SleepTime("12:00","13:00") or self.SleepTime("17:00","18:00"):
                    if eat == "yes":
                        print("现在是饭点,20块钱能增加20点体力")
                        UserVit = int(UserInfo[self.name]['vit']) + 20
                        UserMoney = int(UserInfo[self.name]['money']) - 20
                        UserInfo[self.name]['money'] = UserMoney
                    elif eat == "no":
                        UserVit = int(UserInfo[self.name]['vit']) - 20
                        UserVit =UserVit if UserVit > 0 else 0
                    UserInfo[self.name]['vit'] = UserVit
                    DBApi.AppendDB(UserInfo,self.__database)
                else:
                    if eat == "yes":
                        print ("现在不是饭点,20块钱只能增加10点体力")
                        UserVit = int(UserInfo[self.name]['vit']) + 10
                        UserMoney = int(UserInfo[self.name]['money']) - 20
                        UserInfo[self.name]['money'] = UserMoney
                    else:
                        pass
                    UserInfo[self.name]['vit'] = UserVit
                    DBApi.AppendDB(UserInfo, self.__database)
            else:
                print ("没钱吃饭,吃屎吧你")
        else:
            print ("睡觉中,无法进行任何操作")

    def Sleep(self,sleep):
        import datetime
        UserInfo = self.userinfo
        if self.SleepStatus() is False:
            if self.SleepTime("00:00","09:00"):
                if sleep == "yes":
                    print("现在是睡觉的点,睡觉能增加20点体力,进入睡眠状态")
                    UserVit = int(UserInfo[self.name]['vit']) + 20
                    UserInfo[self.name]['sleeptime'] = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
                elif sleep == "no":
                    print ("熬夜减20点体力")
                    UserVit = int(UserInfo[self.name]['vit']) - 20
                    UserVit =UserVit if UserVit > 0 else 0
                UserInfo[self.name]['vit'] = UserVit
                DBApi.AppendDB(UserInfo,self.__database)
            else:
                if sleep == "yes":
                    print ("现在是睡觉的点,睡觉能增加10点体力")
                    UserVit = int(UserInfo[self.name]['vit']) + 10
                    UserInfo[self.name]['sleeptime'] = datetime.datetime.now()
                else:
                    pass
                UserInfo[self.name]['vit'] = UserVit
                DBApi.AppendDB(UserInfo, self.__database)
        else:
            print ("已经正在睡觉中....")



obj1 = Penson('staff','wuxinzhe','29','100')
#obj1.Sleep('yes')
obj1.SleepTime()

# test = DBApi.ModifyDB('wuxinzhe','vit','200','database/role.db')
