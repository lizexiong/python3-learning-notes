#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/15 17:46
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : salts.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


import sys
from module import common



if __name__ == "__main__":
    #截断除了脚本名之后的参数
    args = sys.argv[1:]
    '''
    python执行两类命令如下:
    1.salts.py  web_server cmd.run "df -hl"
    2.salts.py  web_server  ftp.run httpd
    cmd就是执行命令
    ftp是通过配置文件来上传下载，目标ip，目标文件夹，源文件夹都是通过package里面的配置文件来识别的
    '''
    #args = ['web_server', 'ftp.cuu', 'mysql']
    #print(args)
    try:
        #第一个参数动作，判断是执行命令还是ftp
        exec_module = args[1]
        #如果参数cmd.run语法错误，直接抛异常
        if exec_module.count(".") == 0:
            raise IndexError

        #获取执行的模块名称cmd or ftp
        modulename = exec_module.split(".")[0]
        funcname = exec_module.split(".")[1]
        #导入模块
        #__import__就是导入当前脚本目录下，查看当前目录线下有没有script.cmd或者script.ftp
        modobj = __import__("script.{0}".format(modulename))
        #接下来就是反射
        modobj = getattr(modobj,modulename)
        funcobj = getattr(modobj, funcname)
        #最后把*args参数(如web_server cmd.run "df -hl)传入到cmd或者ftp的run函数里
        funcobj(*args)
    except (ImportError, IndexError):
        common.write_log("Import module error", "error")
        print("\033[33;1m no module {0} found \033[0m".format(exec_module))
    except Exception as e:
        common.write_log(e, "error")
        print("\033[33;1m system run Error,check logs\033[0m")


