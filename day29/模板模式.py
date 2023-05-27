#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/27 1:19
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 模板模式.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


class Register(object):
    '''用户注册接口'''

    def register(self):
        pass
    def login(self):
        pass

    def auth(self):
        self.register()
        self.login()

class RegisterByQQ(Register):
    '''qq注册'''

    def register(self):
        print("---用qq注册-----")

    def login(self):
        print('----用qq登录-----')



class RegisterByWeiChat(Register):
    '''微信注册'''

    def register(self):
        print("---用微信注册-----")

    def login(self):
        print('----用微信登录-----')


if __name__ == "__main__":

    register1 = RegisterByQQ()
    register1.auth()

    register2 = RegisterByWeiChat()
    register2.auth()