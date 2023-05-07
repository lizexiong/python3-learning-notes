#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/6 12:48
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : orm_test.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm





import os
import sys
#因为djangostudy在上一级目录，需要把上级目录添加进入环境变量
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#主要是这里，我们就可以初始化一个django环境了，需要找到配置文件
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangostudy.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangostudy.settings')
import django
django.setup()


from blog.models import Blog
from blog.models import Entry
entry = Entry.objects.get(pk=1)


from blog import models

# #通过id获取文章金品梅
# entry = models.Entry.objects.get(pk=4)
# #通过名字获取Blog分类科技
# tech_blog = models.Blog.objects.get(name='科技')
# #entry的blog字段等于 tech_blog就可以修改了
# entry.blog = tech_blog
# entry.save()

# print (entry,tech_blog)

# #通过Blog关联查询 边城是什么类别的博客
# print (models.Blog.objects.filter(entry__headline__contains='边城'))
#
# #通过Entry关联查询，Blog类别文艺的文章有哪些
# print (models.Entry.objects.filter(blog__name="文艺"))


from django.db.models import F,Q

#同一个models表中，n_comments的值小于n_pingbacks的
# objs = models.Entry.objects.filter(n_comments__lt=F('n_pingbacks'))
# print (objs)

#查询 n_comments大于n_pingbacks的，并且，初版日期大于0519的看看有几个
# objs = models.Entry.objects.filter(n_comments__gt=F('n_pingbacks'),
#                              pub_date__gt="2023-05-19"
#                              )

#查询 n_comments小于n_pingbacks的，活着，初版日期大于0519的看看有几个
# objs = models.Entry.objects.filter(Q(n_comments__lt=F('n_pingbacks')) | Q(pub_date__gt="2023-05-19"))
#
# print (objs)

# from django.db.models import Avg,Sum,Min
#
# #求pingbacks的平均值，最大值，最小值
# print (models.Entry.objects.all().aggregate(Avg('n_pingbacks'),Sum('n_pingbacks'),Min('n_pingbacks')))

from django.db.models import Avg,Sum,Min,Count
from app01 import models as book_models
# #查询出第一个出版社是什么
# pub_obj = book_models.Publisher.objects.first()
# #book_set反向关联，只有反向关联，会自动生成一个_set，可以根据_set，反向查出所有数据
# print (pub_obj.name,pub_obj.book_set.select_related())

# pub_obj = book_models.Publisher.objects.annotate(book_nums=Count('book'))
# for publisher in pub_obj:
#     print (publisher.name,publisher.book_nums)

print (book_models.Book.objects.values_list('publication_date').annotate(book_nums=Count('publication_date')))
