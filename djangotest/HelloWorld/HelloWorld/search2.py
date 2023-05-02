#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/30 23:42
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : search2.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)



# def login(request):
#     if request.method == "GET":
#         return HttpResponse("李泽雄")
#     else:
#         username = request.POST.get('username')
#         pwd = request.POST.get('pwd')
#         if username == 'lizexiong' and pwd == '123':
#             return HttpResponse("李泽雄")
#         else:
#             return redirect(reverse('login'))

# def login(request):
#     if request.method == "GET":
#         return HttpResponse("李泽雄")
#     else:
#         username = request.POST.get('username')
#         pwd = request.POST.get('pwd')
#         if username == 'lizexiong' and pwd == '123':
#             return HttpResponse("李泽雄")
#         else:
#             return redirect(reverse('login',args=(10,)))

def login(request):
    if request.method == "GET":
        return HttpResponse("李泽雄")
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'lizexiong' and pwd == '123':
            return HttpResponse("李泽雄")
        else:
            return redirect(reverse(reverse('app01:login'))) #加上命名空间写法