#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/1 13:47
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : views.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     book = models.Book(title="李泽雄",price=300,publish="小家电维修",pub_date="2008-8-8")
#     book.save()
#     return HttpResponse("<p>数据添加成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
#     print(books, type(books)) # Book object (18)
#     return HttpResponse("<p>数据添加成功！</p>")

# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.all()
#     print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
#     for i in books:
#         print (i.title)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.filter(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.exclude(pk=5)
#     print(books)
#     print("//////////////////////////////////////")
#     books = models.Book.objects.exclude(publish='小家电维修', price=300)
#     print(books, type(books))  # QuerySet类型，类似于list。
#     for i in books:
#         print (i.title)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     #books = models.Book.objects.get(pk=2)
#     books = models.Book.objects.get(pk=18)  # 报错，没有符合条件的对象
#     #books = models.Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
#     print(books, type(books))  # 模型类的对象
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.order_by("price") # 查询所有，按照价格升序排列
#     for i in books:
#         print (i.title)
#     books = models.Book.objects.order_by("-price") # 查询所有，按照价格降序排列
#     for i in books:
#         print (i.title)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     # 按照价格升序排列：降序再反转
#     books = models.Book.objects.order_by("-price").reverse()
#     for i in books:
#         print (i.title)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.count() # 查询所有数据的数量
#     print ("all_books",books)
#     books = models.Book.objects.filter(price=200).count() # 查询符合条件数据的数量
#     print ("book=200",books)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.first() # 返回所有数据的第一条数据
#     print (books.title)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     books = models.Book.objects.last() # 返回所有数据的最后一条数据
#     print (books.title)
#     return HttpResponse("<p>查找成功！</p>")

#app01/views.py: 文件代码：
from django.shortcuts import render,HttpResponse
from app01 import models
# def add_book(request):
#     books = models.Book.objects.exists()
#     print ("1:",books)
#     # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
#     books = models.Book.objects.count().exists()
#     print ("2:",books)
#     # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
#     books = models.Book.objects.first().exists()
#     print ("3:",books)
#     return HttpResponse("<p>查找成功！</p>")


#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     # 查询所有的id字段和price字段的数据
#     books = models.Book.objects.values("pk","price")
#     print(books[0]["price"],type(books)) # 得到的是第一条记录的price字段的数据
#     return HttpResponse("<p>查找成功！</p>")

#app01/views.py: 文件代码：
from django.shortcuts import render,HttpResponse
from app01 import models
# def add_book(request):
#     # 查询所有的price字段和publish字段的数据
#     books = models.Book.objects.values_list("price","publish")
#     print(books)
#     print(books[0][0],type(books)) # 得到的是第一条记录的price字段的数据
#     return HttpResponse("<p>查找成功！</p>")

#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     # 查询一共有多少个出版社
#     books = models.Book.objects.values_list("publish").distinct() # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
#     books = models.Book.objects.distinct()
#     print (books)
#     return HttpResponse("<p>查找成功！</p>")

#app01/views.py: 文件代码：
# from django.shortcuts import render,HttpResponse
# from app01 import models
# def add_book(request):
#     # 查询价格为200或者300的数据
#     books = models.Book.objects.filter(price__in=[200,300])
#     print (books)
#     return HttpResponse("<p>查找成功！</p>")


# def add_book(request):
#     #  获取出版社对象
#     pub_obj = models.Publish.objects.filter(pk=1).first()
#     #  给书籍的出版社属性publish传出版社对象
#         book = models.Book.objects.create(title="李泽雄", price=200, pub_date="2010-10-10", publish=pub_obj)
#     print(book, type(book))
#     return HttpResponse(book)

# def add_book(request):
#     #  获取出版社对象
#     pub_obj = models.Publish.objects.filter(pk=1).first()
#     #  获取出版社对象的id
#     pk = pub_obj.pk
#     #  给书籍的关联出版社字段 publish_id 传出版社对象的id
#     book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
#     print(book, type(book))
#     return HttpResponse(book)

# def add_book(request):
#     #  获取作者对象
#     chong = models.Author.objects.filter(name="令狐冲").first()
#     ying = models.Author.objects.filter(name="任盈盈").first()
#     #  获取书籍对象
#     book = models.Book.objects.filter(title="李泽雄").first()
#     #  给书籍对象的 authors 属性用 add 方法传作者对象
#     book.authors.add(chong, ying)
#     return HttpResponse(book)

# from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数
#
# from django.db.models import F
# from django.db.models import Q
#
# def add_book(request):
#     res = models.Book.objects.filter(Q(pub_date__year=2014) | Q(pub_date__year=1999), title__contains="李")
#     print(res)


# from django.shortcuts import render, HttpResponse
# from app01.My_Forms import EmpForm
# from app01 import models
# from django.core.exceptions import ValidationError
# # Create your views here.
#
#
# def add_emp(request):
#     if request.method == "GET":
#         form = EmpForm()
#         return render(request, "add_emp.html", {"form": form})
#     else:
#         form = EmpForm(request.POST)
#         if form.is_valid():  # 进行数据校验
#             # 校验成功
#             data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
#             data.pop('r_salary')
#             print(data)
#
#             models.Emp.objects.create(**data)
#             return HttpResponse(
#                 'ok'
#             )
#             #return render(request, "add_emp.html", {"form": form})
#         else:
#             print(form.errors)    # 打印错误信息
#             clean_errors = form.errors.get("__all__")
#             print(222, clean_errors)
#         return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})




# from django.shortcuts import render, HttpResponse
# from app01.My_Forms import EmpForm
# from app01 import models
# from django.core.exceptions import ValidationError
# # Create your views here.
#
#
#
# def add_emp(request):
#     if request.method == "GET":
#         form = EmpForm()  # 初始化form对象
#         return render(request, "add_emp.html", {"form":form})
#     else:
#         form = EmpForm(request.POST)  # 将数据传给form对象
#         if form.is_valid():  # 进行校验
#             data = form.cleaned_data
#             data.pop("r_salary")
#             models.Emp.objects.create(**data)
#             return redirect("/index/")
#         else:  # 校验失败
#             clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
#             return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})

# from django.contrib.auth.models import User
# User.objects.create(username='lizexiong',password='123')


def test(request):
    ying = models.Author.objects.filter(name="任盈盈").first()
    book = models.Book.objects.filter(title="冲灵剑法").first()
    print (ying.book_set.all())
    test = ying.all()
    for i in test:
        print (i.title)
    return HttpResponse('ok')