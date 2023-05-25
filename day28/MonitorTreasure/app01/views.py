from django.shortcuts import render,HttpResponse

# Create your views here.



def data_report(request):
    print (request.POST)

    return HttpResponse('data_report')