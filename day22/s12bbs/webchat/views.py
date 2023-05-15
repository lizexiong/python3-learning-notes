

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse
import json,time,queue
from webchat import models


GLOBAL_MSG_QUEUES ={

}

def dashboard(request):

    return render(request,'webchat/dashboard.html')

def send_msg(request):
    print(request.POST)
    print(request.POST.get("msg"))
    #if request.POST.get()
    #获取前端传过来的消息
    msg_data = request.POST.get('data')
    if msg_data:
        msg_data = json.loads(msg_data)
        msg_data['timestamp'] = time.time()
        if msg_data['type'] == 'single':
            #如果这个联系人没有聊天队列，那么就创建一个，如果有，那么把消息放到队列里面
            #这里msg_data['to']一定要转成int，因为村进入的时候是字符串，读取来也是字符串，不转换成为int，那么在get_new_msgs消息的时候找不到用户id
            if not GLOBAL_MSG_QUEUES.get(int(msg_data['to']) ):
                GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msg_data["to"])].put(msg_data)
        else: #否则类型就是group
            #首先判断是发送到那个组
            group_obj = models.WebGroup.objects.get(id=msg_data['to'])
            #然后循环组里面的所有成员，往所有成员的queue里面put一份数据
            for member in group_obj.members.select_related():
                if not GLOBAL_MSG_QUEUES.get(member.id):
                    GLOBAL_MSG_QUEUES[member.id] = queue.Queue()
                #如果成员id不等于用户id，那么代表不是自己，那么只要不是自己，那么就是群成员，全部put消息过去
                if member.id != request.user.userprofile.id:
                    GLOBAL_MSG_QUEUES[member.id].put(msg_data)

    print(GLOBAL_MSG_QUEUES)
    #if not GLOBAL_MSG_QUEUES.get()
    return HttpResponse('---msg recevied---')

def get_new_msgs(request):
    #如果这个用户不存在队列，那么就创建一个
    if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
        print("no queue for user [%s]" %request.user.userprofile.id,request.user)
        GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()
    msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()
    q_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
    msg_list = []
    #如果msg_count大于0，那么代表有消息
    if msg_count >0:

        for msg in range(msg_count):
            #那么把消息获取放到msg_list里面，然后返回给前端
            msg_list.append(q_obj.get())

        print("new msgs:",msg_list)
        #如果没消息，为什么要挂起？
        #因为不论是在前端设置定时器还是等待等办法，前端要么无法实时获取消息，要么就是占用大量客户端资源
        #而这里60秒超时，没有消息就等待60秒返回空，有消息就实时返回，这样客户可以实时获取消息，利用的资源也是最小的
    else:#没消息,要挂起
        print("no new msg for ",request.user,request.user.userprofile.id)
        #print(GLOBAL_MSG_QUEUES)

        try:
            msg_list.append(q_obj.get(timeout=60))
        except queue.Empty:
            print("\033[41;1mno msg for [%s][%s] ,timeout\033[0m" %(request.user.userprofile.id,request.user))
    return HttpResponse(json.dumps(msg_list))