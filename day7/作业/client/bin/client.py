





from module import common
from module.ftpclient import FtpClient
from conf import codes
from conf import template

def start():
    """
    客户端主入口,所有的逻辑从这里开始的
    :return:
    """
    #这里本来尅手动输入的,为了测试方便，所以写死了
    # server_ip = input("输入服务器IP")
    # server_port = int(input("输入服务器端口"))
    # server_ip = "172.21.161.149"
    server_ip = "127.0.0.1"
    server_port = int(8888)

    #调用日志显示颜色的函数,把模版用颜色演示出来
    common.show_message(template.START_MENU,"INFO")
    common.show_message("正在连接FTP服务器 {0}:{1} .....".format(server_ip, server_port),"INFO")

    #调用客户端对象
    #创建一个client对象
    client = FtpClient(server_ip,server_port)
    #连接服务器,返回结果,
    conn_result = client.connect()
    #连接成功
    if conn_result  == codes.CONN_SUCC:
        common.show_message("连接成功","NOTICE")

        #客户端登录,如果登录成功，会把login_status改为True
        #这里的操作会比较多，通过专门登录验证的函数去做验证，把FtpClient的客户端对象传入到client_login函数里面
        #接下来就要看client_login函数的操作
        client_login(client)

        #登录成功,如果ftpclient 的对象 里面login_status为True，那么就认为登录成功
        if client.login_status:
            #退出系统
            exit_flag = False
            while not exit_flag:
                #显示登录的菜单
                show_menu = template.LOGINED_MENU.format(client.username,
                                                         str(int(client.totalspace / 1024 /1024)),
                                                         str(int(client.usedspace / 1024 / 1024)))
                common.show_message(show_menu,"NOTICE")
                #输入命令串
                input_command = common.input_command("[输入命令]:")
                if input_command == "quit":
                    exit_flag = True
                else:
                    #获取命令的command（命令一定是要有固定格式）
                    cmd_func = input_command.split("|")[0]
                    try:
                        #通过反射调用Client类的对应command方法,并返回执行结果
                        if hasattr(FtpClient,cmd_func):
                            func = getattr(FtpClient,cmd_func)
                            exec_result = func(client,input_command)
                        else:
                            common.write_log("Client {0} 未找到".format(input_command), "error")
                    except Exception as e:
                        print (e)
                        common.write_log(e,"error")
        else:
            common.show_message("连接失败","ERROR")

def client_login(user_obj):
    """
    客户端登录操作
    :param UserObj: 当前客户端对象
    :return:  没有返回
    """
    tmp_flag = False
    while not tmp_flag:
        #调用input_msg函数,所有代码就这里调用一下,也是为了代码美观
        username = common.input_msg("请输入用户名:")
        password = common.input_msg("请输入密码:")
        #这里是把加密的密码发送到服务端验证
        password = common.encry_sha(password)
        #开始登录认证
        #user_obj,就是FtpClient对对象,调用对象的login进行验证
        auth_status = user_obj.login(username,password)

        #通过FtpClient对象返回的不同状态码,确认客户端状态，给出不同提示
        #start函数中45行代码，client_status的状态并不是这里的，这里的auth_status只是状态码，这里代码就到头了，不管成功失败都结束了。client_status是FtpClient里面的一个字段属性，这里不要搞混了
        if auth_status == codes.AUTH_SUCC:
            common.show_message("登录成功","NOTICE")
            tmp_flag = True
        elif auth_status == codes.AUTH_FAIL:
            common.show_message("用户名或密码错误", "ERROR")
        elif auth_status == codes.AUTH_LOCKED:
            common.show_message("账户已被锁定,联系管理员", "ERROR")
        else:
            common.show_message("用户不存在", "ERROR")



