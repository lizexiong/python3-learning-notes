#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/15 19:00
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : common.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


import logging
from conf import settings



def get_log_level():
    level = settings.LOG_LEVEL
    result = logging.INFO
    if level == "debug":
        result = logging.DEBUG
    if level == "warning":
        result = logging.WARNING
    if level == "error":
        result = logging.ERROR
    return result

def write_log(msg, msgtype, log_type="sys"):
    '''
    日志记录模块
    :param msg: 日志消息
    :param msgtype:  日志等级
    :param log_type:   日志类型
    :return:
    '''
    log = logging.getLogger("SSHLOG")
    log.setLevel(get_log_level())

    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # 记录到文件
    if log_type == "sys":
        filehandle = logging.FileHandler(settings.SYSLOG_FILE)
    else:
        filehandle = logging.FileHandler(settings.OPLOG_FILE)
    filehandle.setLevel(logging.INFO)
    log.addHandler(filehandle)
    filehandle.setFormatter(log_format)

    # 打印屏幕,只打印错误日志
    if settings.LOG_PRING:
        screenhandle = logging.StreamHandler()
        screenhandle.setLevel(logging.INFO)
        log.addHandler(screenhandle)
        screenhandle.setFormatter(log_format)

    if msgtype == "info":
        log.info(msg)
    if msgtype == "error":
        log.error(msg)
    if msgtype == "debug":
        log.debug(msg)

    log.removeHandler(filehandle)
    if settings.LOG_PRING:
        log.removeHandler(screenhandle)