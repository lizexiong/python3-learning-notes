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
                            module_obj = self.get_module_instance(base_mod_name=base_mod_name,os_type=os_type)
                            module_parse_result = module_obj.syntax_parser(section_name,mod_name,mod_data,os_type)
                            self.config_data_dic[os_type].append(module_parse_result)

                #代表上面所有的数据解析已经完成，接下来生成一个任务，并把任务放入队列
                print ("config_data_dic".center(60,"*"))
                print (self.config_data_dic)

            except IndexError as e:
                exit("state file must be provided after -f")

        else:
            exit("statefile must be specified.")