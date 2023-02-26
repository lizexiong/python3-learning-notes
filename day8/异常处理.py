#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 23:41
# @Author  : 李泽雄
# @Site    : 
# @File    : 异常处理.py
# @Project : python3
# @Software: PyCharm



class lizexiongError(Exception):
    def __init__(self,msg=None):
        self.message = msg

    def __str__(self):
        if self.message:
            return self.message
        else:
            print ("返回为空")


a = 1

try:
    #判断这个条件a是不是等于1，这里a等于2，那么直接报错
    assert  a == 2
    #要结合自定义异常使用
except lizexiongError as e:
    print (e)


# try:
#     #raise lizexiongError("海鸥不在眷念大海,可以飞更远")
#     print ("else作用，这里不能有异常，自定义异常也不行")
# except Exception as e:
#     print (e)
# else:
#     print ("执行没有出错，这里才回执行")
# finally:
#     print ("不管有没有异常，这里都会执行")