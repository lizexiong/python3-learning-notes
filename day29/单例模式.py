#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/26 23:49
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 单例模式.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm

#实现__new__方法
#并在将一个类的实例绑定到类变量_instance上,
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
#如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(Singleton,cls) #farther class
            cls._instance =  orig.__new__(cls)
        return cls._instance #具体的实例

class MyClass(Singleton):
    def __init__(self,name):
        self.name = name


a = MyClass("Alex")
print(a.name)
b = MyClass("Jack")



print(b.name)