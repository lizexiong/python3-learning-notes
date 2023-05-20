#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/16 19:25
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : action_list.py
# @Version  : Python 3.10.10
# @Project  : Stark
# @Software : PyCharm


from Arya.plugins import cmd,state
actions = {
    'cmd': cmd.CMD,
    'state':state.State
}