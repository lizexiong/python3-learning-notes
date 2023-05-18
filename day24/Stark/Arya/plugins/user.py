#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule


class User(BaseSaltModule):
    def uid(self,*args,**kwargs):
        self.argv_validation('uid',args[0],int)
        cmd = "-u %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd
    def gid(self,*args,**kwargs):
        self.argv_validation('gid',args[0],int)
        cmd = "-g %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd
    def shell(self,*args,**kwargs):
        self.argv_validation('shell',args[0],str)
        cmd = "-s %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd
    def home(self,*args,**kwargs):
        self.argv_validation('home',args[0],str)
        cmd = "-d %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd
    def present(self,*args,**kwargs):
        cmd_list = []
        username = kwargs.get('section')
        self.raw_cmds.insert(0,"useradd %s" %username)

        cmd_list.append(' '.join(self.raw_cmds))
        cmd_list.extend(self.single_line_cmds)
        #把present处理好的所有命令返回给 调用他的present处理逻辑，在base_module的syntax_parser的for else后面就是调用者
        # print (cmd_list)
        return cmd_list

    def is_required(self,*args,**kwargs):
        username = args[1]
        print ("checking user required",args,kwargs)


class UbuntuUser(User):
    def password(self,*args,**kwargs):
        username = kwargs.get('section')
        password = args[0]
        cmd = ''' echo "%s:%s" | sudo chpasswd''' %(username,password)
        self.single_line_cmds.append(cmd)


