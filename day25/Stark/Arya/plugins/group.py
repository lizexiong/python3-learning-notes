#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule


class Group(BaseSaltModule):

    def gid(self,*args,**kwargs):
        pass

    def present(self,*args,**kwargs):
        cmd_list = []
        username = kwargs.get('section')
        self.raw_cmds.insert(0,"useradd %s" %username)

        cmd_list.append(' '.join(self.raw_cmds))
        cmd_list.extend(self.single_line_cmds)
        print (cmd_list)

    def is_required(self, *args, **kwargs):
        name = args[1]
        cmd = '''more /etc/group | awk -F':' '{print $1}' | grep -w %s -q ;echo $?''' % name
        return cmd

