#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/28 0:07
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



from django.contrib import admin
from django.urls import path
from app02 import views

urlpatterns = [

    path('home/',views.home),
    path('db_handle/',views.db_handle),
]
