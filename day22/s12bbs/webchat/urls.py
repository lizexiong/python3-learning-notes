#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/14 23:01
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.conf.urls import url,include
from webchat import views
urlpatterns = [

    url(r'^$', views.dashboard,name='chat_dashboard'),
    url(r'^msg_send/$', views.send_msg, name='send_msg'),
    url(r'^new_msgs/$', views.get_new_msgs, name='get_new_msgs'),
    url(r'^chat_file_upload/$', views.chat_file_upload, name='chat_file_upload'),
]
