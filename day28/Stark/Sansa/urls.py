#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/21 0:30
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm




from django.conf.urls import url,include

from Sansa import views

urlpatterns = [


    url('report/',views.asset_report),

]