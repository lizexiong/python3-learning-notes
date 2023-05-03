#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/3 16:14
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



from django.conf.urls import url
from app01 import views


urlpatterns = [
    url('cash/',views.pay),
    url('index/',views.index),
    url('page1/',views.page1),
    url('page1_1/',views.page1_1)
]
