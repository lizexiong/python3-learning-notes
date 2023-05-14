#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/11 23:51
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : custom.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def truncate_url(img_url):
    #print (img_url.name,img_url.url)
    return img_url.name.split('/',maxsplit=1)[-1]

@register.simple_tag
def filter_comment(article_obj):
    #这老师用的方法比较low，因为聚合他忘了，所以委屈一点，就用这种方式
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count()
    }
    return comments