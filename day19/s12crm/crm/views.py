from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from crm import models

def dashboard(request):
    return render(request,'crm/dashboard.html')

def customers(request):
    customer_list = models.Customer.objects.all()
    return render(request,'crm/customers.html',{"customer_list":customer_list})

