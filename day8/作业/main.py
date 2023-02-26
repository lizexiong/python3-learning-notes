#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 22:27
# @Author  : 李泽雄
# @Site    : 
# @File    : main.py
# @Project : python3
# @Software: PyCharm

import sys
from module import common
from module.users import Users
from module import commands


MENU = '''\033[1;32m
-----------------------------------------
|             简版堡垒机                |
-----------------------------------------
\033[0m'''

if __name__ == "__main__":
    trycount = 3
    count = 0

    while count < trycount:
        print(MENU)
        #调用inputs函数判断用户名和密码输入是否合规
        username = common.inputs("用户名: ").lower()
        passwd = common.inputs("密码: ")
        # 实例化一个用户对象
        userobj = Users(username)
        #首先判断用户是否存在
        if not userobj.exists:
            print("用户名或密码错误！\n")
            common.write_log("用户{0}登录, 用户名不存在".format(username), "info", "op")
            count += 1
            continue
        else:
            auth_stat = userobj.user_auth(passwd)
            if not auth_stat:
                common.write_log("用户{0}登录, 用户名密码不正确".format(username), "info", "op")
                print("登录失败！用户名或密码错误!")
                count += 1
                continue
            else:
                # 登录成功
                common.write_log("用户{0}登录, 登录成功!".format(username), "info", "op")
                print("欢迎登录堡垒机精简版(v1.0)\n")
                exit_flag = False
                while not exit_flag:
                    command_str = input("[ {username} ] (q to exit):\> ".format(username=username))
                    common.write_log("用户{0}执行命令{1}".format(username, command_str), "info", "op")
                    if command_str.strip().lower() == "q":
                        sys.exit(0)
                    elif command_str.strip().lower() == "help":
                        commands.help()
                    else:
                        #认证通过后，最后到了这里，开始把用户实例化对象+用户输入的命令传入进来，开始工作
                        commands.exec_cmd(userobj, command_str)
    else:
        print("尝试失败过多!")
        common.write_log("用户{0}尝试登录次数过多,系统退出!".format(username), "info", "op")



