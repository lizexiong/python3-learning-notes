#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/16 19:27
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : utils.py
# @Version  : Python 3.10.10
# @Project  : Stark
# @Software : PyCharm


import sys

from Arya import action_list
import django
django.setup()

from Stark import settings
from Arya import models
class ArgvManagement(object):
    '''
    接收用户指令并分配到相应模块
    '''
    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_parse()

    def help_msg(self):
        print("Available modules:")
        for registered_module in action_list.actions:
            print("  %s" % registered_module)
        exit()
    def argv_parse(self):
        #print(self.argvs)
        if len(self.argvs) <2:
            self.help_msg()
        #操作的模块名在用户输入的第二个参数上
        module_name = self.argvs[1]

        #这里是最出版本的利用反射获取有没有这个模块，后面会继续完善，现在啥都没有，插件也没写，所以用户输入啥都报错
        if '.' in module_name:
            mod_name,mod_method = module_name.split('.')
            module_instance  = action_list.actions.get(mod_name)
            print (module_instance)
            if module_instance:#matched
                #1.把配置文件传到 对应的模块的处理函数里面，比如state.apply，他需要通过settings知道配置文件在哪里
                module_obj = module_instance(self.argvs,models,settings)

                #2.什么提取主机，就是把你输入的主机信息从数据库里面提取出来，这系统就是脱裤子放屁
                module_obj.process() #提取 主机
                #3.利用反射，查看比如cmd里面有没有run方法，或者state里面有没有apply方法，如果有，就执行apply方法
                if hasattr(module_obj,mod_method):
                    module_method_obj = getattr(module_obj,mod_method)#解析任务，发送到队列，取任务结果
                    module_method_obj() #调用指定的指令
                else:
                    exit("module [%s] doesn't have [%s] method" % (mod_name,mod_method))

        else:
            exit("invalid module name argument")