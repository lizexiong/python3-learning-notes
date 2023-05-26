from django.shortcuts import render,HttpResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from app01.data_handler import DataProcess
from app01.backends import redis_conn
from MonitorTreasure import settings
from app01 import models
from django.core.cache import cache
import queue

from app01 import data_handler
from app01.backends import ip_lookup
REDIS_OBJ = redis_conn.redis_conn(settings)
GLOBAL_REALTIME_WATCHING_QUEUES = {} #如果前端页面打开了实时监测,所有指定区域来的数据到放到相应的Queue里


#print("loading ip db file".center(50,'-'))
IP_DB_DATA = ip_lookup.IPLookup(ip_db_filename=settings.IP_DB_FILE).ip_db_data


def data_report(request):
    print (request.POST,request.GET)
    data_process_obj = DataProcess(request,REDIS_OBJ,GLOBAL_REALTIME_WATCHING_QUEUES,IP_DB_DATA)
    if data_process_obj.is_valid():
        data_process_obj.save()

    else:
        print("invalid data:")
        pass #invalid data
    msg = 'jsonpcallback({"Email":"alex@126.com","Remark":"我来自服务器端哈哈"})'
    return  HttpResponse(msg)