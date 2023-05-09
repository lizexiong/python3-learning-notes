#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/9 10:44
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : forms.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.forms import Form,ModelForm
from crm import models


class CustomerModelForm(ModelForm):
    class Meta:
        #获取Customer表的所有字段
        model = models.Customer
        exclude = ()

    def __init__(self,*args,**kwargs):
        #继承他然后重写我们一些功能，比如加样式
        super(CustomerModelForm,self).__init__(*args,**kwargs)

        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class':'form-control'})

