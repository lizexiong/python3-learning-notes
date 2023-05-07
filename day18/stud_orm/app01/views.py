from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

@login_required()
def index(request):
    return render(request,'index.html')

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
            return redirect('/')
        else:
            #否则把报错返回给前端
            login_err = "Wrong username or password!"
            return render(request,'login.html',{"login_err":login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return redirect('/')
