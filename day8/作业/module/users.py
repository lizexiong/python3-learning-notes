#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 22:39
# @Author  : 李泽雄
# @Site    : 
# @File    : users.py
# @Project : python3
# @Software: PyCharm

from conf import settings
from dbhelper import dbapi
from module import common
from module.myexception import MyException


class Users(object):

    __userdb = settings.DB_USERS

    def __init__(self, uname):
        self.username = uname
        self.name = ""
        self.passwd = ""
        self.role = "user"
        self.inputcmd = ""
        self.groups = ""
        self.exists = True
        self.manage_ip = []

        self.__load_user_info()

    def __load_user_info(self):
        """
        从users.xml文件获取用户信息，如果不存在则exists标识为False，否则load所用信息
        :return:
        """
        #调用加载用户的函数，查看是否有用户信息
        user = dbapi.load_users(self.username)
        if not user:
            self.exists = False
        else:
            #如果有用户信息，
            #1.那么开始初始化复制给对象
            #2.把用户表示设置True，代表有这个用户
            #3.加载管理IP（这里的管理IP是这个用户有权限看到的机器）
            self.name = user["name"]
            self.passwd = user["password"]
            self.role = user["role"]
            self.groups = user["groups"]
            self.exists = True
            self.__load_manage_ip()

    def __load_manage_ip(self):
        """
        根据用户管理的组ID号，获取所有可以管理的主机IP列表，去重后返回唯一IP
        :return:
        """
        ip_list = []
        for gid in self.groups.split(","):
            #还是去dbapi从xml文件去获取可以管理的主机IP列表
            hosts_in_gid = dbapi.load_host_by_gid(gid)
            for host in hosts_in_gid:
                ip_list.append(host["ip"])
        # 通过set转换一下，去重
        self.manage_ip = list(set(ip_list))

    def user_auth(self, password):
        """
        登录验证，由于用户密码在第一步就加载了，所以判断用户输入的密码和实例化对象里面的密码是否相同，认证通过返回True，否则返回False
        :param password: 用户输入密码
        :return:
        """
        try:
            if not self.exists:
                auth_status = False
            else:
                encry_passwd = common.encry_sha(password)
                if self.passwd == encry_passwd:
                    auth_status = True
                else:
                    auth_status = False
            return auth_status

        except Exception as e:
            common.write_log(e, "error")

    def load_host_by_ip(self, ip):
        '''
        根据传入进来的IP，
        :param ip:
        :return:
        '''
        for gid in self.groups.split(","):
            #根据用户的ip返回这个组下面的所有服务器信息
            host_info_list = dbapi.load_host_by_gid(gid)
            #如果传入的ip在这个用户组里，那么就返回
            for host in host_info_list:
                if host["ip"] == ip:
                    return host

    @staticmethod
    def auth_ip(func):
        def inner(userobj, input_command_list):
            try:
                # 用户输入即无 -h ，也无 -g 语法错误
                if input_command_list.count("-h") == 0 and input_command_list.count("-g") == 0:
                    raise MyException("103")

                # 用户输入 -h e.g: cmd -h 192.168.1.1,192.168.1.2,存在未授权IP
                if input_command_list.count("-h") > 0:
                    input_ip_list = input_command_list[input_command_list.index("-h") + 1].split(",")
                    for ip in input_ip_list:
                        if ip not in userobj.manage_ip:
                            print ("testerror")
                            #这里发现一个问题，装饰器里面的异常不会主动爆出来？
                            raise MyException("104")

                # 用户输入 -g e.g: cmd -g gid 存在未授权 组，
                if input_command_list.count("-g") > 0:
                    # 获取组信息
                    input_gid_list = input_command_list[input_command_list.index("-g") + 1].split(",")
                    for gid in input_gid_list:
                        # 如果gid不在用户管理的gid内，报异常
                        if gid not in userobj.groups:
                            raise MyException("104")

                return func(userobj, input_command_list)

            except MyException as e:
                common.write_log(e, "warning")
            except Exception as e:
                common.write_log(e, "error")
        return inner