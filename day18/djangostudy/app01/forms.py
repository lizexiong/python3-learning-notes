#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/5 15:46
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : forms.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm

#1.导入这个模块
from django import forms

class BookForm(forms.Form):


    user_type_choice = (
        (1, '华山出版社'),
        (2, '明教出版社'),
    )


    #这里所有的字段必须和数据库的字段完全一致，否则报错
    #2.那么字段，字段要和数据库里面一样
    title = forms.CharField(max_length=10)
    #3选择出版社，出版社是可以选择的，并且可以给这个选择框一个样式------这老师课堂上没有把这个搞出来
    publisher_id = forms.IntegerField(widget=forms.widgets.Select(choices=user_type_choice,
                                                                attrs={'class':'form-control'}))
    #4.初版的日期
    publication_date = forms.DateField()


from app01 import models

class BookModelForm(forms.ModelForm):

    #固定格式
    class Meta:
        #数据库里面的Book表
        model = models.Book
        #到时候前端显示哪些字段，要跟数据库里面的字段名相同
        #fields = ('title','publication_date')
        #显示数据库里面的所有字段
        exclude = ()
        #给前端的标签提前加上样式
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control'})
        }

