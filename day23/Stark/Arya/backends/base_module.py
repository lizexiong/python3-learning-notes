#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/16 19:48
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : base_module.py
# @Version  : Python 3.10.10
# @Project  : Stark
# @Software : PyCharm



class BaseSaltModule(object):
    def __init__(self,sys_argvs,db_models,settings):
        self.db_models = db_models
        self.settings = settings
        self.sys_argvs = sys_argvs


    def get_selected_os_types(self):
        data = {}
        for host in self.host_list:
            data[host.os_type] = []
        print('--->data',data)
        return data

    def process(self):
        self.fetch_hosts()
        self.config_data_dic = self.get_selected_os_types()

    def require(self,*args,**kwargs):
        pass

    def fetch_hosts(self):
        print('--fetching hosts---')
        #如果有-h和-g在参数里面，才会执行下面的内容
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                # -h +1 ,那么就是主机ip
                host_str_index = self.sys_argvs.index('-h') + 1
                #如果所有参数小于 -h+1，那么参数一定不合法
                if len(self.sys_argvs) <= host_str_index:
                    exit("host argument must be provided after -h")
                else:  # get the host str
                    #那么就获取host
                    host_str = self.sys_argvs[host_str_index]
                    #如果有多台主机，那么用 逗号分割放入列表里面
                    host_str_list = host_str.split(',')
                    #然后到数据库里面查询一下这些主机是否在数据库里面
                    host_list += self.db_models.Host.objects.filter(hostname__in=host_str_list)
            #原理和主机一样
            if '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g') + 1
                if len(self.sys_argvs) <= group_str_index:
                    exit("group argument must be provided after -g")
                else:  # get the group str
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(',')
                    group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list)
                    for group in group_list:
                        host_list += group.hosts.select_related()
            #去重，可能2个组机组里面有重复的主机
            self.host_list = set(host_list)
            return True
            print('----host list:', host_list)
        else:
            exit("host [-h] or group[-g] argument must be provided")

    def syntax_parser(self,section_name,mod_name,mod_data):
        print("-going to parser state data:",section_name,mod_name)

        for state_item in mod_data:
            print("\t",state_item)
            for key,val in state_item.items():
                #简单来比如，group里面有没有 处理gid的函数，没有，就提示没有这个模块
                if hasattr(self,key):
                    state_func = getattr(self,key)
                    state_func(val)
                else:
                    exit("Error:module [%s] has no argument [%s]" %( mod_name,key ))