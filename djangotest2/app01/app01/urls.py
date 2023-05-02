"""app01 URL Configuration

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
from django.urls import path
from . import views

# urlpatterns = [
#     path('add_book/', views.add_book),
#     path('add_emp/', views.add_emp)
#
# ]

from django.contrib import admin
from django.urls import path
from cookie import views
from cookie import views as session_views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/', views.login),
    # path('index/', views.index),
    # path('logout/', views.logout),
    # path('order/', views.order),

    path('session_login/', session_views.login),
    path('s_index/', session_views.s_index),
    path('s_logout/', session_views.s_logout),


    ]


