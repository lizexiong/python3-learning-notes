

from django.conf.urls import url,include

from  Robb import views

urlpatterns = [

    url(r'^api/',include('Robb.rest_urls')),
    url(r'^$',views.dashboard ),
    url(r'^dashboard/$',views.dashboard ,name='dashboard' ),
    url(r'^triggers/$',views.triggers,name='triggers' ),
    url(r'hosts/$',views.hosts ,name='hosts'),
    url(r'host_groups/$',views.host_groups ,name='host_groups'),
    url(r'hosts/(\d+)/$',views.host_detail ,name='host_detail'),
    url(r'trigger_list/$',views.trigger_list ,name='trigger_list'),
]
