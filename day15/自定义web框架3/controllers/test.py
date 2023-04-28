#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/27 19:43
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : test.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from jinja2 import Template
import time

def f1():
    f = open('f1.html',encoding='utf-8')
    data = f.read()
    f.close()
    import time
    db_str = str(time.time())
    data = data.replace('F1',db_str)
    return data

def f2():

    f = open('f2.html',encoding='utf-8')
    result = f.read()
    template = Template(result)
    #接收值，进行特殊的替换
    data = template.render(name='lizexiong',user_list=['wuxinzhe','liuwen'])
    return data