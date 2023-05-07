from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,HttpResponse


def pay(request):
    return HttpResponse("这里是pay支付功能" + lizexiong)


def index(request):
    if request.method == "GET":
        user_info = [{'username':'lizexiong','password': '123'},
                     {'username': 'wuxinzhe', 'password': '123'},
                     {'username': 'liuwen', 'password': '123'},
                     {'username': 'zhuwenjing', 'password': '123'},
                     ]
        return render(request,'app01/index.html',{"user_obj":user_info})


def page1(request):
    return render(request,'app01/page1.html')

def page1_1(request):
    return render(request,'app01/page1_1.html')

from app01 import models
from app01 import forms
def book_form(request):


    if request.method == "POST":
        print (request.POST)
        #1.把post的请求传入到我们的FORM里面去进行认证
        form = forms.BookForm(request.POST)
        #2.如果验证没有错误
        if form.is_valid():
            print ("form is ok")
            print (form.cleaned_data)
            #3.获取form里面的数据格式，过滤掉不需要的信息
            form_data = form.cleaned_data
            #4.将过滤的数据直接保存进入数据库。
            book_obj = models.Book(**form_data)
            book_obj.save()
        else:
            print (form.errors)

        return render(request, 'app01/book_form.html', {'book_form': form, })
    else:
        # 1.导入我们自己的from验证表单，不是django的，是我们自己写的
        # 这里要导入的原因是前端get需要使用
        form = forms.BookForm()
        #publisher_list = models.Publisher.objects.all()
        return render(request,'app01/book_form.html',{'book_form':form,})


def book_modelform(request):

    if request.method == "POST":
        print (request.POST)
        #1.把post的请求传入到我们的FORM里面去进行认证
        form = forms.BookModelForm(request.POST)
        # 2.如果验证没有错误
        if form.is_valid():
            print ("modelform is ok")
            # 3.获取form里面的数据格式，过滤掉不需要的信息
            print (form.cleaned_data)
            #4. modelform和form的保存数据的区别在于，modelform不需要cleaned_data,直接保存就行
            form.save()

        else:
            print (form.errors)
        return render(request, 'app01/book_modelform.html', {'book_form': form, })
    else:
        # 1.导入我们自己的Modelfrom验证表单，不是django的，是我们自己写的
        # 这里要导入的原因是前端get需要使用
        form = forms.BookModelForm()
        return render(request, 'app01/book_modelform.html', {'book_form': form, })

