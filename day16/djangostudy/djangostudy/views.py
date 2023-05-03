#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/3 15:12
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : views.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.shortcuts import render,HttpResponse

def special_case_2003(request):
    return HttpResponse("matched 2003")


def year_archive(request,year):
    return HttpResponse(year)

def month_archive(request,year,month):
    return HttpResponse(year + "---" + month)

def articles_detail(request,year,month,articles_id):
    return HttpResponse("year:" + year + "month:" + month + "article:" +articles_id)