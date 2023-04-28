from django.shortcuts import render

# Create your views here.



from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("APP01")


def news(request,n1,n2):
    return HttpResponse("静态路由测试" + "---" + n1 + "---" + n2 )

def page(request,n2,n1):
    nid = n1 + n2
    return HttpResponse(nid)