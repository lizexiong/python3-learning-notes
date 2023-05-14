from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


from bbs import models
from bbs import comment_hander
import json
from bbs import form


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
    for i  in article_list:
        print (i.id)
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
            #如果验证通过，那么跳转去主页,要么获取到next，代表用户在文章界面，并且想评论，那么就要跳转回文章界面。
            return redirect(request.GET.get('next') or '/bbs')
        else:
            #否则把报错返回给前端
            login_err = "Wrong username or password!"
            return render(request,'login.html',{"login_err":login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return redirect('/bbs')

def article_detail(request,article_id):
    '''
    文章详情页
    :param request:
    :param article_id: 根据前端传来的id来判断我是哪篇文章
    :return:
    '''
    article_obj = models.Article.objects.get(id=article_id)
    #把评论都传给专门处理评论树的函数
    comment_tree = comment_hander.build_tree(article_obj.comment_set.select_related())
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj,
                                                     "category_list":category_list,})

def comment(request):
    print (request.POST)
    if request.method == "POST":
        new_comment_obj = models.Comment(
            article_id = request.POST.get('article_id'),
            parent_comment_id = request.POST.get('parent_comment_id') or None,
            comment_type = request.POST.get("comment_type"),
            user_id = request.user.userprofile.id,
            comment = request.POST.get('comment')
        )
        new_comment_obj.save()
    return HttpResponse("post-comment-success")

def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_hander.build_tree(article_obj.comment_set.select_related())
    #1.总入口，通过这里去调用一些函数，把后台拼接好的html返回给全段
    tree_html = comment_hander.render_comment_tree(comment_tree)
    return HttpResponse(tree_html)


#一种比较low的方法，在点击发帖的时候，url跳转回变成account/login，但是我们没有这个url，所以需要设置accoutn/login变成login，牛逼的设置方法在setting里面
#@login_required(login_url='/login/')
@login_required()
def new_article(request):

    if request.method == 'GET':
        article_form = form.ArticleModelForm()
        return render(request,'bbs/new_article.html', {'article_form':article_form})
    elif request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        #前端form表单传过来，会在request.FILES里面
        article_form = form.ArticleModelForm(request.POST,request.FILES)
        if article_form.is_valid():
            data = article_form.cleaned_data
            #因为前端并没有给用户展示作者字段，所以后台我们需要自己拼接
            data['author_id'] = request.user.userprofile.id

            article_obj = models.Article(**data)
            article_obj.save()
            #article_form.save()
            return HttpResponse('new article has been published ')
        else:
            #r如果有错误，需要把错误返回给前端
            return render(request,'bbs/new_article.html', {'article_form':article_form})


def file_upload(request):

    print(request.FILES )
    file_obj = request.FILES.get('filename')
    with open('uploads/%s' % file_obj.name, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return render(request,'bbs/new_article.html')


def get_latest_article_count(request):
    #网页最后最后一篇文章的id传过来
    latest_article_id = request.GET.get("latest_id")
    if latest_article_id:
        #如果数据库里面有大于这个id的文章，全部返回给前端
        new_article_count = models.Article.objects.filter(id__gt = latest_article_id).count()

        print("new article count:",new_article_count)
    else:
        new_article_count = 0
    return HttpResponse(json.dumps({'new_article_count':new_article_count}))