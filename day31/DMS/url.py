#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/30 18:46
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from handler.user import Login, \
                          Logout
from handler.node import Main, \
                        NodeManage, \
                        Top, \
                        LeftGroup, \
                        GroupList, \
                        RightNode, \
                        ConCreate, \
                        ConAction, \
                        ConStart, \
                        ConStop, \
                        ConDestroy, \
                        ConRestart, \
                        ConManage, \
                        ConModify



urls = [
    (r"/",           Login),
    (r"/login",      Login),
    (r"/logout",     Logout),
    (r"/main",       Main),
    (r"/base", Top),
    (r"/leftgroup", LeftGroup),
    (r"/grouplist", GroupList),
    (r"/nodemanage", NodeManage),
    (r"/node", RightNode),
    (r"/concreate", ConCreate),
    (r"/conaction", ConAction),
    (r"/constart", ConStart),
    (r"/constop", ConStop),
    (r"/conrestart", ConRestart),
    (r"/condestroy", ConDestroy),
    (r"/conmanage", ConManage),
    (r"/conmodify", ConModify),
]
