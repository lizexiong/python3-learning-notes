#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/25 18:32
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : api_urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'data/report/',views.data_report),
]
