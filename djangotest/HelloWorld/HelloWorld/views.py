#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/30 18:48
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : views.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")


def lizexiong(request):
    name ="李泽雄-statics"
    return render(request, "lizexiong.html", {"name": name})














