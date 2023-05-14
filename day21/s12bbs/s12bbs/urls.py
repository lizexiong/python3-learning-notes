"""s12bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import include
from bbs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^bbs/',include('bbs.urls')),
    re_path('^chat/',include('webchat.urls')),
    re_path('^login/',views.acc_login,name='login'),
    re_path('^logout/',views.acc_logout,name='logout'),
    re_path(r'^file_upload/$', views.file_upload,name="file_upload"),
]
