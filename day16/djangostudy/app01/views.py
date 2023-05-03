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