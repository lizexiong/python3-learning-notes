#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/8 19:10
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : custom_tags.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def zx_upper(val):
    return val.upper()


@register.simple_tag
#current_page是想现在第几页
#loop_num是一共有多少分页
# 假设现在是第4页，一共有6页传入以下函数
def guess_page(current_page,loop_num):
    #4-6绝对值为2
    offset = abs(current_page - loop_num)
    #那么小于3，所以分页前后只会显示3页
    if offset < 3:
        if current_page == loop_num:
            #因为前端没办法存储变量，所以这里直接把html代码返回给前端，这是一种方式，牛逼的代码，所有分页在这里都处理完成了，这里只是完成了一部分，做个演示
            #如果是当前页，那么页码加个颜色
            page_ele = '''<li class="active"><a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)
        else:
            page_ele = '''<li class=""><a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)
        return format_html(page_ele)
    else:
        return ''