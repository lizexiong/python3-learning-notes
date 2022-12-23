



import os
from conf import setting
from database import DBApi
from module import role,common


# # obj1 = role.Penson('boss','lizexiong','29','20000')
# # print ('test')
#
#
# obj1 = role.Staff('staff','zhuwenjing','32','200','yes')
# print (obj1.Interview())


def main():
    '''
    主函数没什么好说的
    1.外层while循环控制玩家创角或读取玩家信息
    2.内存while循环控制玩家一天的日常逻辑
    :return:
    '''
    while True:
        CreateRole = input ("欢迎来到天选打工人系统,你是否需要创建角色？")
        if CreateRole == "yes":
            Name = input("请输入角色名称")
            Age = input("请输入角色年龄")
            Obj = role.Staff('staff', Name, Age, )
        else:
            Name = input("请输入登录角色名称")
            Obj = role.Staff('staff', Name, '12', )

        print ("进入游戏主界面,打印游戏信息")
        while True:
            ObjInfo = Obj.DBLoad()
            print ("姓名:",Name,"年龄：",ObjInfo[Name]['age'],"体力：",ObjInfo[Name]['vit'],"金钱：",ObjInfo[Name]['money'])
            UserChoice = input('输入1打工,2吃饭,3睡觉')
            if UserChoice == "1":
                UserWorkChoice = input("确认要打工吗？请确保体力足够哟")
                if UserWorkChoice == "yes":
                    Obj.Work('yes')
                else:
                    Obj.Work('no')
            elif UserChoice == "2":
                UseEatChoice = input("确认要吃饭吗？你有钱？")
                if UseEatChoice == "yes":
                    Obj.Eat('yes')
                else:
                    Obj.Eat('no')
            elif UserChoice == "3":
                UseSleepChoice = input("确认要睡觉吗？")
                if UseSleepChoice == "yes":
                    Obj.Sleep('yes')
                else:
                    Obj.Sleep('no')

if __name__ == "__main__":

    main()
