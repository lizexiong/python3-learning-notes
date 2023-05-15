#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/14 19:00
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : form.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.forms import ModelForm

from bbs import models

class ArticleModelForm(ModelForm):

    class Meta:
        model = models.Article
        #给前端发帖，只显示这3个字段
        exclude = ('author','pub_date','priority')

    def __init__(self,*args,**kwargs):
        super(ArticleModelForm, self).__init__(*args, **kwargs)
        #self.fields['customer_note'].widget.attrs['class'] = 'form-control'

        for field_name in self.base_fields:
            field = self.base_fields[field_name]

            field.widget.attrs.update({'class': 'form-control'})
            #print("required:",field.required)
        #else:

