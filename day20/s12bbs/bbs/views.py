from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


from bbs import models



category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')

def index(request):
    '''
    2.
    默认输入/bbs的主页url的时候，会默认进入全部，并且全部是高亮显示
    category_obj是告诉前端，我的位置位1，那么我高亮
    article_list是默认进入主页，显示所有已发布的文章
    '''
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status="published")
    return render(request,'bbs/index.html',{"category_list":category_list,
                                            'article_list':article_list,
                                            'category_obj':category_obj})


def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    '''
    1.
    把文章展示在前端，并且全部里面也有内容
    如果position_index == 1，那么代表是全部，那么现实所有文章
    PS:本节课1,2小点，老师实现的方式都非常low，将就着用吧
    '''
    if category_obj.position_index == 1:
        article_list = models.Article.objects.filter(status="published")
    else:
        article_list = models.Article.objects.filter(category_id=category_obj, status="published")
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list})

def acc_login(request):
    if request.method == "POST":
        print (request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password')
                            )
        #如果不为空就是验证通过,否则返回用户对象
        if user is not None:
            #加session
            login(request,user)
            #如果验证通过，那么跳转去主页
            return redirect('/bbs')
        else:
            #否则把报错返回给前端
            login_err = "Wrong username or password!"
            return render(request,'login.html',{"login_err":login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return redirect('/bbs')