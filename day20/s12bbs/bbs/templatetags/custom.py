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
    print (img_url.name,img_url.url)
    return img_url.name.split('/',maxsplit=1)[-1]

