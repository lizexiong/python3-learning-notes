#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/1 16:50
# @Author  : 李泽雄
# @Site    :
# @File    : template.py
# @Project : python3
# @Software: PyCharm

import hashlib
import io
from datetime import datetime
from conf import settings


def input_msg(message, limit_value=tuple(), default=""):
    """
    判断input输入的信息是否为空的公共检测函数,为空继续输入,不为空返回输入的信息
    :param default: 默认值
    :param limit_value: 对输入的值有限制,必须为limit_value的值;ex:("admin","user")
    :param message: input()函数的提示信息
    :return: 返回输入的信息
    """
    is_null_flag = True
    while is_null_flag:
        input_value = input(message).strip().lower()
        # 没有限制值
        if not input_value:
            # 没有默认值，就必须输入
            if not default:
                print("\033[1;30m输入不能为空!\033[0m")
                continue
            else:
                input_value = default
                is_null_flag = False
        # 有限制值
        elif len(limit_value) > 0:
            if input_value not in limit_value:
                print("\033[1;30m输入的值不正确,请重新输入!\033[0m")
                continue
            else:
                is_null_flag = False
        else:
            is_null_flag = False
            continue
    return input_value


def encry_md5(file):
    """
    获取文件的MD5值，用于MD5校验
    :param file: 文件名
    :return: MD5值
    """
    fmd = hashlib.md5()
    file = io.FileIO(file, 'r')
    byte = file.read(2048)
    while byte != b'':
        fmd.update(byte)
        byte = file.read(2048)
    file.close()
    md5value = fmd.hexdigest()
    return md5value

def write_log(content, types):
    """
    写错误日志
    :param content: 日志信息
    :param types: 日志信息类型 error  info
    :return: 无返回，写入文件 error.log
    """
    _content = "\n{0} - {1} - {2} ".format(datetime.now().strftime("%Y-%m-%d %X"), types, content)
    with open(settings.LOGS, "a+") as fa:
        fa.write(str(_content))
    # print(_content)

def encry_sha(string):
    """
    用户密码加密函数 sha224加密
    :param string: 明文字符串
    :return: 加密字符串
    """
    sha = hashlib.sha224()
    sha.update(string.encode())
    sha_value = sha.hexdigest()
    return sha_value
