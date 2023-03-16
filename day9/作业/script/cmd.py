#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/15 19:16
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : cmd.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



import os
import sys
import paramiko
from multiprocessing import Pool
from module import parser
from conf import settings
from module.common import write_log


def run(*args):
    '''
    接收args参数，解析，然后从hosts.yaml获取远程主机信息，然后调用_ssh_exec_cmd执行命令
    :param args:    web_server cmd.run "df -hl" 参数
    :return:
    '''

    groups = args[0]
    cmd = args[2]
    # 对所有配置的服务器执行命令
    if groups == "*":
        #获取所有主机信息
        hosts = parser.load_host_all()
    else:
        # 根据组名执行命令
        #返回信息{'172.21.161.161': [{'user': 'root'}, {'auth_type': 1}, {'key': 'huawei'}, {'group': 'web_server'}, {'port': 22}]}
        hosts = parser.search_host_by_group(groups)
    if len(hosts) == 0:
        print("\033[31;1m no group name ' {0} ' found \033[0M".format(groups))
        sys.exit(0)

    # 设置5个进程池
    pool = Pool(5)
    for ip in hosts.keys():
        host_info = parser.host_info_by_ip(ip)
        #最后调用_ssh_exec_cmd执行命令，这个函数就没有过多可以解释的了
        pool.apply_async(_ssh_exec_cmd, args=(cmd,), kwds=host_info)
    pool.close()
    pool.join()

def _ssh_exec_cmd(commandstr, **host):
    """
    paramiko 执行命令方法
    :param hostlist: 主机列表{ip:[{user: , key: , auth_type: }]}
    :param commandstr: 执行的命令
    :return:
    """
    ip = list(host.keys())[0]
    host_item = host[ip]
    port = int(host_item["port"])
    user = host_item["user"]
    key = host_item["key"]

    try:
        # 开始登录服务器并执行命令
        transport = paramiko.Transport(ip, port)
        if host_item["auth_type"] == 1:
            transport.connect(username=user, password=key)
        else:
            pkey = paramiko.RSAKey.from_private_key_file(os.path.join(settings.RSAKEY, "id_rsa"), password=key)
            transport.connect(username=user, pkey=pkey)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(command=commandstr)

        print("\033[1;31m IP -> {0} : \033[0m \n".format(ip))
        err_result = stderr.read().decode()
        out_result = stdout.read().decode()
        #上一节课强调过这个std的结果接收一次就消失，这里还是强调一下，要存储到变量里面才能为接下来做判断
        if len(err_result) > 0:
            print(err_result)
        if len(out_result) > 0:
            print(out_result)

        transport.close()
    except Exception as e:
        print(e)
        write_log(e, "error")
