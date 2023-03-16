#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/15 19:26
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : parser.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


import yaml
from conf import settings

hostconfig = settings.hosts_config

def host_info_by_ip(ip):
    """
    根据 IP 地址获取该ip对一个的服务器信息，返回一个字典
    :param ip: ip地址
    :return: 信息字典{ip:{user:'test',auth_type：1}},{'172.21.161.161': {'user': 'root', 'auth_type': 1, 'key': 'huawei', 'group': 'web_server', 'port': 22}}
    """
    return_dict = {}
    with open(hostconfig, 'r',encoding='utf-8') as f:
        hosts_dict = yaml.safe_load(f)
        host = hosts_dict[ip]
        for item in host:
            for k, v in item.items():
                return_dict[k] = v
    return {ip: return_dict}


def search_host_by_group(groupname):
    """
    从服务器信息文件hosts.yaml中读取指定组的主机信息
    :param groupname: 组名称
    :return: 返回服务器信息字典{ip:[{'user':'test'},{'key':'124'}]},{'172.21.161.161': [{'user': 'root'}, {'auth_type': 1}, {'key': 'huawei'}, {'group': 'web_server'}, {'port': 22}]}
    """
    return_dict = {}
    tmp_dict = {}
    with open(hostconfig, 'r',encoding='utf-8') as f:
        hosts_dict = yaml.safe_load(f)
        for ip, host_info in hosts_dict.items():
            for item in host_info:
                for k, v in item.items():
                    tmp_dict[k] = v
                    if k == "group" and v == groupname:
                        return_dict[ip] = host_info
    return return_dict

def load_host_all():
    """
    从服务器信息文件hosts.yaml中读取所有的主机信息
    :return: 服务器信息字典,{'172.21.161.149': [{'user': 'root'}, {'auth_type': 2}, {'key': '12345'}, {'group': 'db_server'}, {'port': 22}], '172.21.161.161': [{'user': 'root'}, {'auth_type': 1}, {'key': 'huawei'}, {'group': 'web_server'}, {'port':
 22}]}
    """
    with open(hostconfig, 'r',encoding='utf-8') as f:
        print (yaml.safe_load(f))
        return yaml.safe_load(f)

def get_package_date(package_file):
    """
    执行ftp操作，从package文件读取信息，返回字典数据
    :param package_file: 处理文件
    :return: 字典信息
    put:{'exec_method': 'file.put', 'hosts': 'all', 'source': 'file_source/httpd.conf', 'name': '/data/www/httpd.conf'}
    get:{'exec_method': 'file.get', 'hosts': '172.21.161.161', 'source': '/data/www/my.cnf', 'name': 'file_source/my.cnf'}
    """
    data_dict = {}
    with open(package_file, 'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data_dict['exec_method'] = list(data.keys())[0]
    for method, data_info in data.items():
        for item in data_info:
            for k, v in item.items():
                data_dict[k] = v
    return data_dict