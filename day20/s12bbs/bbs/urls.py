#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/10 23:13
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : urls.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



from django.urls import path,re_path
from bbs import views


urlpatterns = [
    re_path('^$',views.index),
    re_path('^category/(\d+)/$',views.category),
    re_path('^detail/(\d+)/$',views.article_detail,name='article_detail'),
    re_path('^comment/$',views.comment,name='post_comment'),
    re_path('^comment_list/(\d+)/$',views.get_comments,name="get_comments")

]
