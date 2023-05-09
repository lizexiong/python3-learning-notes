#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/8 0:21
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



from django.contrib import admin
from django.urls import path,re_path
from crm import views

urlpatterns = [
    re_path('^index', views.dashboard),
    re_path("^customers/$",views.customers,name="customers_list"),
    re_path('customers/(\d+)/$', views.customer_detail,name="customer_detail"),
]
