#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/16 19:25
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : salt.py
# @Version  : Python 3.10.10
# @Project  : Stark
# @Software : PyCharm



import os,sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stark.settings")
    #这里是为了把saly.py放到变量里面，因为saly.py导入的 很多模块，比如 actions是stark级别，我们需要把这些模块都要加入到环境变量，否则报错
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(BASE_DIR)
    sys.path.append(BASE_DIR)

    #有哪些动作，也就是命令分发的意思，比如cmd执行命令让cmd的模块去管理，动作都在这from Arya.action_list import actions下
    from Arya.action_list import actions
    #用户命令解析，我们的格式就是比如 python saly.py cmd.run ....  ，总不能让用户瞎输入，所以，这里就是解析用户的命令对不对
    from Arya.backends.utils import ArgvManagement
    #把用户输入的参数传给专门处理解析命令的类
    obj = ArgvManagement(sys.argv)
