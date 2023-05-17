#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule


class User(BaseSaltModule):
    def uid(self,*args,**kwargs):
        self.argv_validation('uid',args[0],int)
        cmd = "-u %s" %args[0]
        return cmd
    def gid(self,*args,**kwargs):
        self.argv_validation('gid',args[0],int)
        cmd = "-g %s" %args[0]
        return cmd
    def shell(self,*args,**kwargs):
        self.argv_validation('shell',args[0],str)
        cmd = "-s %s" %args[0]
        return cmd
    def home(self,*args,**kwargs):
        self.argv_validation('home',args[0],str)
        cmd = "-d %s" %args[0]
        return cmd
    def present(self,*args,**kwargs):
        pass

class UbuntuUser(User):
    def gid(self,*args,**kwargs):
        pass

