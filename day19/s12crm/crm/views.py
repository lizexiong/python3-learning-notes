from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from crm import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.forms import Form,ModelForm
from crm import forms
from crm import permissions

def dashboard(request):
    return render(request,'crm/dashboard.html')

def customers(request):
    customer_list = models.Customer.objects.all()
    #把customer的值分页，每页只有1个数据
    paginator = Paginator(customer_list,1)
    #获取前端传过来的数值是需要第几页
    page = request.GET.get('page')
    try:
        #根据前端传来的数据获取第几页
        customer_objs = paginator.page(page)
    except PageNotAnInteger:
        #如果前端传来的页数没有，那么默认返回第一页，一般在刚打开网页的时候什么都没传的时候会用这个
        customer_objs = paginator.page(1)
    except EmptyPage:
        #如果输入的数超过了最大界限，那么返回最大的页数
        customer_objs = paginator.page(paginator.num_pages)
    return render(request,'crm/customers.html',{"customer_list":customer_objs})

@permissions.check_permission
def customer_detail(request,customer_id):
    #根据id获取这个用户的信息
    customer_obj = models.Customer.objects.get(id=customer_id)
    if request.method == "POST":
        #将这些信息全部传入这个form表单
        #要传入前端的信息和之前后端拿出来的信息对比，否则不知道改什么，所以下面要哦传2个参数
        form = forms.CustomerModelForm(request.POST,instance=customer_obj)
        if form.is_valid():
            form.save()
            #获取前面的请求，提交完成后返回修改之前的页面，这里是动态参数，不能写静态url
            base_url = "/".join(request.path.split("/")[:-2])
            return redirect(base_url)
    else:
        form = forms.CustomerModelForm(instance=customer_obj)
    return render(request,'crm/customer_detail.html',{"customer_form":form})