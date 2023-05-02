#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/30 23:26
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : search.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.http import HttpResponse
from django.shortcuts import render


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
