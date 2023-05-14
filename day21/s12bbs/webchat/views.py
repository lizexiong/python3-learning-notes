

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse
import json,time,queue


GLOBAL_MSG_QUEUES ={

}

def dashboard(request):

    return render(request,'webchat/dashboard.html')

def send_msg(request):
    print(request.POST)
    print(request.POST.get("msg"))
    #if request.POST.get()
    msg_data = request.POST.get('data')
    if msg_data:
        msg_data = json.loads(msg_data)
        msg_data['timestamp'] = time.time()
        if msg_data['type'] == 'single':
            if not GLOBAL_MSG_QUEUES.get(int(msg_data['to']) ):
                GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msg_data["to"])].put(msg_data)
    print(GLOBAL_MSG_QUEUES)
    #if not GLOBAL_MSG_QUEUES.get()
    return HttpResponse('---msg recevied---')