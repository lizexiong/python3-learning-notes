#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/1 13:45
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : models.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.db import models

# class Book(models.Model):
#     id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
#     title = models.CharField(max_length=32) # 书籍名称
#     price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
#     publish = models.CharField(max_length=32) # 出版社名称
#     pub_date = models.DateField() # 出版时间

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()


class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)


class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)


class Dep(models.Model):
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)