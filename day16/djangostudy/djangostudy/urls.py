"""
URL configuration for djangostudy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from djangostudy import views
from app01 import urls as payment_urls

urlpatterns = [
    url('admin/', admin.site.urls),
    url('articles/2003/$',views.special_case_2003),
    url('articles/([0-9]{4})/$',views.year_archive),
    url('articles/([0-9]{4})/([0-9]{2})/$',views.month_archive),
    url('articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$',views.articles_detail),
    url('payment/',include(payment_urls))
]

