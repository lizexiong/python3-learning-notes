#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/16 19:29
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : state.py
# @Version  : Python 3.10.10
# @Project  : Stark
# @Software : PyCharm


from Arya.backends.base_module import  BaseSaltModule
import os

class State(BaseSaltModule):
    print ("State")
    def load_state_files(self, state_filename):
        '''
            这个函数就是读取yaml文件，解析之后return，没什么特别的
            讲道理应该单独写个文件，但是这里为了方便，就放在这里了
        :param state_filename:
        :return:
        '''
        from yaml import load, dump
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper
        state_file_path = "%s/%s" % (self.settings.SALT_CONFIG_FILES_DIR, state_filename)
        if os.path.isfile(state_file_path):
            with open(state_file_path) as f:
                data = load(f.read(), Loader=Loader)
                return data
        else:
            exit("%s is not a valid yaml config file" % state_filename)

    def apply(self):
        '''
        1. load the configurations file
        2. parse it
        3. create a task and sent it to the MQ
        4. collect the result with task-callback id
        :return:
        '''

        if '-f' in self.sys_argvs:
            #获取 配置文件的索引
            yaml_file_index = self.sys_argvs.index('-f') + 1
            try:
                yaml_filename = self.sys_argvs[yaml_file_index]
                #加载yaml配置文件存储到state_data
                state_data = self.load_state_files(yaml_filename)
                #print('state data:',state_data)

                #首先要判断操作系统类型，如果操作系统不是默认centos，那么就需要去找ubuntn的类
                for os_type,os_type_data in self.config_data_dic.items(): #按照不同的操作系统单独生成一份配置文件
                    for section_name,section_data in state_data.items():
                        print('Section:',section_name)

                        for mod_name,mod_data in section_data.items():
                            #mod-name一般是字符串user.present
                            base_mod_name = mod_name.split(".")[0]
                            #然后找到模块名（模块路径要提前在settings里面设置）
                            plugin_file_path = "%s/%s.py" % (self.settings.SALT_PLUGINS_DIR,base_mod_name)
                            #如果存在这个模块名
                            if os.path.isfile(plugin_file_path):
                                #导入 模块

                                module_plugin = __import__('plugins.%s' %base_mod_name)
                                special_os_module_name = "%s%s" %(os_type.capitalize(),base_mod_name.capitalize())
                                #print('dir module plugin:',module_plugin,base_mod_name)
                                #getattr(module_plugin,base_mod_name)
                                module_file= getattr(module_plugin, base_mod_name) # 这里才是真正导入模块
                                #在这个模块里面判断，有没有专门基于这个操作系统的特殊方法，如果没有，那么就用默认的方法
                                if hasattr(module_file, special_os_module_name): #判断有没有根据操作系统的类型进行特殊解析 的类，在这个文件里
                                    module_instance = getattr(module_file, special_os_module_name)
                                else:
                                    module_instance = getattr(module_file, base_mod_name.capitalize())

                                #开始调用 此module 进行配置解析
                                module_obj = module_instance(self.sys_argvs,self.db_models,self.settings)
                                module_obj.syntax_parser(section_name,mod_name,mod_data )
                            else:
                                print ("module [%s] is not exist" % base_mod_name)
                            # for state_item in mod_data:
                            #    print("\t",state_item)

            except IndexError as e:
                exit("state file must be provided after -f")

        else:
            exit("statefile must be specified.")