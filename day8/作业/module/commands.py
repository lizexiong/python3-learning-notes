#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 23:11
# @Author  : 李泽雄
# @Site    : 
# @File    : commands.py
# @Project : python3
# @Software: PyCharm


import sys
import os
import paramiko
from multiprocessing import Pool
from module.myexception import MyException
from module.common import write_log
from dbhelper import dbapi
from module.users import Users
from conf import settings

__command__ = ["show", "cmd", "sftp", "help"]

def exec_cmd(userobj,input_command):
    """

    :param userobj:   实例化用户对象，包括用户的用户名,可以管理的主机IP等信息
    :param input_command:   用户交互输入的命令
    :return:
    """
    try:
        #获取第一个命令指令
        command_list = input_command.split()
        command = command_list[0]
        if command not in __command__:
            raise MyException("103")
        else:
            #调用对应的命令
            #sys.modules[__name__]是该文件的绝对路径，然后使用反射，看看本文件，有没有对应的函数方法，有的话把用户实例化对象以及命令再次透传过去
            func = getattr(sys.modules[__name__],command)
            func(userobj,command_list)

    except MyException as e:
        write_log(e,"warning")
        print (e)
    except Exception as e:
        write_log(e,'error')



def show(userobj, input_command_list):
    """
    执行show命令，查看当前用户管理的所有服务器信息,可用命令：
        show hosts -a : 查看所有服务器IP、主机名、所属组
        show hosts -g gid: 查看组id（gid) 对应的所有主机信息
        show groups: 查看当前用户管理的所有组
    如果show跟其它参数 不认识
    :param userobj:  用户对象
    :param input_command_list: 用户输入的命令,split后的列表
    :return: 返回结果信息
    """
    try:
        show_args = ["hosts", "groups"]

        if len(input_command_list) < 2:
            raise MyException("106")
        else:
            input_args = input_command_list[1]

            if input_args == "hosts":
                # 如果有 -a
                if input_command_list.count("-a") > 0:
                    if len(input_command_list) > 3:
                        raise MyException("103")
                    else:
                        # 显示所有主机信息
                        user_gid_list = userobj.groups.split(",")
                # 没有 -a， 有 -g 吗
                elif input_command_list.count("-g") > 0:
                    user_gid_list = input_command_list[input_command_list.index("-g") + 1].split(",")

                else:
                    raise MyException("103")
                    # 开始显示信息
                for gid in user_gid_list:
                    # 根据用户的组ID,获取组对应的host信息字典
                    hosts_info = dbapi.load_host_by_gid(gid)
                    for host in hosts_info:
                        print("\033[1;30m \nIP: {0}  主机名: {1}  所属组ID: {2} \033[0m;".format(host["ip"],
                                                                                           host["hostname"],
                                                                                           gid))
            elif input_args == "groups":
                # 打印所有组信息
                user_gid = userobj.groups
                groups_dict = dbapi.load_group_info()
                # 从所有组信息中删除不在用户gid中的元素，剩下打印
                _total_gid_list = list(groups_dict.keys())
                for gid in _total_gid_list:
                    if gid not in user_gid.split(","):
                        del groups_dict[gid]
                # 显示用户组信息
                for k, v in groups_dict.items():
                    print("\033[1;30m GID: {0}, GNAME: {1}\033[0m;\n".format(k, v))

            else:
                raise MyException("106")

    except MyException as e:
        write_log(e, "error")
        print(e)
    except Exception as e:
        write_log(e, "error")

#装饰器，判断是否这个ip授权，也就是是不是归自己管理
#其实这里的逻辑也是做了一道，源码有点重复的冗长了，完全可以交给装饰器去判断，这个cmd相关的函数里面又判断了一遍
#@Users.auth_ip
def cmd(userobj, input_command_list):
    """
    在管理的服务器上执行cmd命令，命令支持:
    cmd -h 192.168.1.100,192.168.1.200 -c "df -hl"
    cmd -g G01 -c "df -hl"
    :param userobj:
    :param input_command_list:
    :return:
    """
    # 命令
    command_str = ""
    try:
        # 有命令吗?有的话-c后面的元素在" "之间的都是命令
        if input_command_list.count("-c") > 0:
            #-c +1 是因为-c后面的才是命令， 所以要+1
            start_index = input_command_list.index("-c") + 1
            end_index = len(input_command_list)
            #传入进来的是个列表，只有在-c后面的才是命令，先把命令拼接起来
            #传入进来的用户输入的列表示例:['cmd', '-h', '172.21.161.161', '-c', '"ifconfig"']
            for cmd_str in input_command_list[start_index:end_index]:
                command_str += " {0}".format(cmd_str)
                if cmd_str.endswith('"'):
                    #如果最后是单引号，那么就代表跳过
                    break
            # 去前后的双引号,可以看到ifconfig命令是有双引号的，要去除
            #这里就是用户最终要执行的命令
            command_str = command_str.replace('"', '')
        else:
            raise MyException("106")

        # 获取要执行的所有主机列表
        # 这里就获取到服务器的相关信息了
        #1.是否是授权主机，授权主机返回一个列表以及相关用户名以及密码信息
        #如示例[{'ip': '172.21.161.161', 'hostname': 'ubuntu', 'user': 'root', 'auth_type': '1', 'hostkey': 'huawei', 'port': '22'}]
        exec_host_info = _analyze_command(userobj, input_command_list)
        # 开始对这些服务器进行命令操作,开启进程池执行服务器登录
        pool = Pool(5)
        for host in exec_host_info:
            #这里的hosts可是一个字典信息
            pool.apply_async(_ssh_exec_cmd, args=(command_str,), kwds=host)
        pool.close()
        pool.join()
        # _ssh_exec_cmd(command_str, **host)


    except MyException as e:
        write_log(e, "warning")
        return e
    except Exception as e:
        write_log(e, "error")


def _analyze_command(userobj, input_command_list):
    """
    根据用户输入的命令，分析命令参数，返回一个要操作的所有主机信息的列表[{host_info}], host_info包括：
    {ip,loginuser,auth_type,key}
    :param userobj:  用户对象
    :param input_command_list: 用户命名 e.g:cmd -h 192.168.1.2 -g G01,G02 -c "df -hl"
    :return: 返回主机信息的列表
    """
    # 执行命令的主机ip列表
    ipadress_list = []
    # 包含所有host信息的列表文件，可能有重复的
    all_host_detail_info = []
    # 结果host列表,存放主机信息字典
    exec_host_info = []

    # 获取 -h 后面的Ip地址
    if input_command_list.count("-h") > 0:
        # 获取输入命令中的IP列表
        #可能有几个主机，通过逗号分隔，然后放入ipaddess_list里面去
        input_ip_list = input_command_list[input_command_list.index("-h") + 1].split(",")
        #为什么有一个专门ipaddress_list列表，因为你可能有多个主机，还有一个组，组里面也有多个主机，要把管理的ip给统计出来
        ipadress_list.extend(input_ip_list)
        # 获取主机IP对应的详细信息
        for ip in input_ip_list:
            #如果这个ip在用户组里面，就返回详细的信息
            #ip可以回去实例化对象里面多做一次验证，为了验证这个ip是不是我可以管理的，而组就不需要，直接调用load_host_by_gid函数返回详细主机信息
            host_detail = userobj.load_host_by_ip(ip)
            all_host_detail_info.append(host_detail)

    # 获取 -g 后面的组ID对应的所有IP地址
    if input_command_list.count("-g") > 0:
        input_gid_list = input_command_list[input_command_list.index("-g") + 1].split(",")
        for gid in input_gid_list:
            host_info_list = dbapi.load_host_by_gid(gid)
            all_host_detail_info.extend(host_info_list)
            # 得到列表中的主机IP
            for host in host_info_list:
                ipadress_list.append(host["ip"])


    # 对列表中的IP进行去重
    #这里就是用户输入的要去执行命令的主机ip
    ipadress_list = list(set(ipadress_list))

    # 获取要执行的IP列表中的IP对应服务器的信息，登录用户、验证方式、密码或密钥。
    # 并且过滤出来,用户输入的ip,是否在用户的管理列表里面，不在的话，就不放入执行主机列表里面
    for ip in ipadress_list:
        for host in all_host_detail_info:
            if host["ip"] == ip:
                exec_host_info.append(host)

    return exec_host_info


def _ssh_exec_cmd(commandstr, **host):
    """
    paramiko 执行命令方法
    :param hostlist: 主机列表
    :param commandstr: 执行的命令
    :return:
    """
    ip = host["ip"]
    port = int(host["port"])
    user = host["user"]
    key = host["hostkey"]
    hostname = host["hostname"]

    try:
        # 开始登录服务器并执行命令
        transport = paramiko.Transport(ip, port)
        if host["auth_type"] == "1":
            transport.connect(username=user, password=key)
        else:
            pkey = paramiko.RSAKey.from_private_key_file(os.path.join(settings.RSAKEY, "id_rsa"), password=key)
            transport.connect(username=user, pkey=pkey)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(command=commandstr)
        #一旦read后，值可就read完了，所以,read要保存在一个变量里面，源代码有问题，无法显示结果，这里做了优化

        res,err = stdout.read().decode(),stderr.read().decode()

        print("\033[1;31m IP -> {0} : \033[0m \n".format(ip))

        if len(res) > 0:
            print (res)
        if len(err) > 0:
            print (err)

        # if len(stderr.read().decode()) > 0 :
        #     print(stderr.read().decode())
        # if stdout:
        #     print(stdout.read().decode())

        transport.close()
    except Exception as e:
        print(e)
        write_log(e, "error")

@Users.auth_ip
def sftp(userobj, input_command_list):
    """
    这里就不多做解释，和cmd的方式基本一样
    1.先去获取管理ip的详细信息
    2.执行上传下载操作
    exec sftp operation
    :param userobj:
    :param input_command_list:
    :return:
    """
    exec_host_list = _analyze_command(userobj, input_command_list)
    try:
        # 判断是要上传文件还是下载文件 -u 上传  -d 下载，如果既有-u又有-d 命令无效
        if input_command_list.count("-u") > 0 and input_command_list.count("-d") > 0:
            raise MyException("108")
        elif input_command_list.count("-u") > 0:
            # exec upload file
            exec_type = "U"
        elif input_command_list.count("-d") > 0:
            exec_type = "D"
        else:
            # no -u and no -d
            raise MyException("109")
        # 判断-s -t合法性
        if input_command_list.count("-s") < 1 or input_command_list.count("-t") < 1:
            raise MyException("110")

        # 开始执行上传活下载操作
        # upload 获取要上传活下载的源文件
        source_file = input_command_list[input_command_list.index("-s") + 1].replace('"', '')
        distinct_file = input_command_list[input_command_list.index("-t") + 1].replace('"', '')
        # file does exiests??
        if exec_type == "U":
            if not os.path.exists(source_file):
                raise MyException("107")

        # 开启5个线程池
        pool = Pool(5)
        for host in exec_host_list:
            pool.apply_async(_ssh_exec_sftp, args=(source_file, distinct_file, exec_type), kwds=host)
        pool.close()
        pool.join()

    except MyException as e:
        write_log(e, "info")
        print(e)

def _ssh_exec_sftp(source, distinct, exec_type, **host):
    """
    执行文件传输任务
    :param source: 源文件
    :param distinct: 目标文件
    :param exec_type: 执行方式：U：上传 D：下载
    :param host: 发送或下载服务器的信息 字典
    :return:
    """
    try:
        ip = host["ip"]
        port = int(host["port"])
        user = host["user"]
        key = host["hostkey"]
        hostname = host["hostname"]

        transport = paramiko.Transport(ip, port)
        if host["auth_type"] == "1":
            transport.connect(username=user, password=key)
        else:
            pkey = paramiko.RSAKey.from_private_key_file(os.path.join(settings.RSAKEY, "{0}.rsa".format(hostname)))
            transport.connect(username=user, pkey=pkey)

        ssh_sftp = paramiko.SFTPClient.from_transport(transport)
        if exec_type == "U":
            ssh_sftp.put(source, distinct)
            print("\033[1;31m\n local[ {0} ] >>>>> upload to >>>>>> {1}[ {2} ]   finished \033[0m".format(source, ip, distinct))
        else:
            ssh_sftp.get(source, distinct)
            print("\033[1;31m\n local[ {0} ] <<<<< download from <<<<<< {1} [ {2} ] finished \033[0m".format(distinct, ip, source))

        transport.close()
    except Exception as e:
        write_log(e, "error")

def help():
    help_str = '''\033[1;31m
    -----------------------------------  help list  ----------------------------------------------
    command:
        help:
        show:  show [hosts -a | -g gid ],[groups]         # 查看用户的管理的组及组对应服务器信息 e.g: show groups, show hosts -a
        cmd:   cmd [-h ipaddress | -g gid] -c command     # 批量执行命令 e.g: cmd -g G01 -c "df -hl"
        sftp:  sftp [-u | -d]                             # 上传或下载文件 -u update -d download
                    [-h ipaddr | -g gid]                  # -s 原文件地址  -t 目的地址文件
                    -s filepath -t filepath               # e.g: sftp -u -g G01 -s /tmp/aaa -t /tmp/aaa

      \033[0m '''
    print(help_str)
