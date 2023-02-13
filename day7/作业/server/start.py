



import sys
from conf import settings
from bin import server
from conf import template
from module.users import Users
from module import common



if __name__ == "__main__":
    #Server端启停标识
    SERVER_RUNNING_STATUS = False
    #程序退出标识
    SYS_EXIT_FLAG = False
    #服务端进程
    P_SERVER = None

    while not SYS_EXIT_FLAG:
        #打印开始菜单
        if not SERVER_RUNNING_STATUS:
            menu = template.MENU_START.format(menu1="[1] 启动服务",
                                              menu2="[2] 添加用户",
                                              menu3="[3] 结束程序"
                                              )
        else:
            menu = template.MENU_START.format(menu1="[1] 停止服务",
                                              menu2="[2] 添加用户",
                                              menu3="[3] 结束程序"
                                              )
        print (menu)
        command = input("请选择功能编号")
        if command not in ("1","2","3"):
            print ("请输入正确的功能编号")
            continue

        if command == "3":
            if SERVER_RUNNING_STATUS:
                confirm = input("FTP 服务端正在运行中,确认要退出系统吗？(y/n)").strip().lower()
                if confirm == "y":
                    #结束进程
                    P_SERVER.terminate()
                    SYS_EXIT_FLAG = True
                elif confirm == "n":
                    continue
                else:
                    if confirm not in ("y","n"):
                        print ("输入错误")
                        continue
            else:
                SYS_EXIT_FLAG = True
        elif command == "1":
            if SERVER_RUNNING_STATUS:
                # 服务端已经启动了,1则结束服务
                P_SERVER.terminate()
                SERVER_RUNNING_STATUS = False
                print("\033[1;31mFTP 服务端已停止!\033[0m;")
            else:
                # 服务端未启动,则启动服务端
                #这里其实才是第一步，因为这里是启动服务,启动了服务才有其它的操作
                P_SERVER = server.start()
                #ftpserver.doprocess()
                #启动之后将服务状态改为True
                SERVER_RUNNING_STATUS = True
                print("\033[1;30mFTP 服务端已启动!\033[0m;")
                #windows不加入这个break，这个循环不结束，无法启动服务，linux上正常
                break

        #创建用户是一个单独的功能模块
        elif command == "2":
            try:
                tmpflag = False
                while not tmpflag:
                    username = common.input_msg("输入用户名[q返回]: ")
                    if username == "q":
                        tmpflag = True
                        continue
                    # 创建用户对象,用户相关的操作,创建，有一个专门的类来处理
                    new_user = Users(username)
                    #如果用户不存在,那么开始一系列创建流程
                    if not new_user.exists:
                        userpasswd = common.input_msg("设置初始密码[默认12345]: ", default="12345")
                        totalspace = common.input_msg("设置磁盘配额[默认500M]: ", default=str(settings.HOME_QUOTA))
                        print("\n 正在初始化用户，请稍等.........\n")

                        #创建用户只有这里需要注意,这个encry_sha函数，就是加密用户密码
                        new_user.password = common.encry_sha(userpasswd)
                        new_user.islocked = 0
                        new_user.isdel = 0
                        new_user.totalspace = int(totalspace) * 1024 * 1024
                        new_user.usedspace = 0
                        new_user.create_user()

                        print("初始化成功!")
                    else:
                        print("\033[1;30m用户已经存在!\033[0m;\n")
                        continue
            except Exception as e:
                common.write_log("start - main - type2 - {0}".format(e), "error")

