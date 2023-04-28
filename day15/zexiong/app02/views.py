from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse,render

def home(request):
    return HttpResponse("APP02.Home")


from app02 import models

def db_handle(request):
    #增加
    #models.UserInfo.objects.create(username='lizexiong',password='123',age=73)
    # dic = {"username": 'wuxinzhe', "password":'123',"age":73}
    # models.UserInfo.objects.create(**dic)

    #删除
    # models.UserInfo.objects.filter(username='wuxinzhe').delete()

    #改
    # models.UserInfo.objects.all().update(age=30)

    #查
    user_list_obj = models.UserInfo.objects.all()
    # models.UserInfo.objects.filter(age=30)
    # models.UserInfo.objects.filter(age=30).first()

    if request.method == "POST":
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'])

    return render(request,'app.html',{'user_list_obj':user_list_obj})
    #return HttpResponse("ok")
