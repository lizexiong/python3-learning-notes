#!/usr/bin/env python
"""
select 详细解释，用线程的IO多路复用实现一个读写分离的、支持多客户端的连接请求
"""
import socket
import queue
from select import select

SERVER_IP = ('127.0.0.1', 9999)

# 保存客户端发送过来的消息,将消息放入队列中
message_queue = {}
input_list = []
output_list = []

if __name__ == "__main__":
    server = socket.socket()
    server.bind(SERVER_IP)
    server.listen(10)
    # 设置为非阻塞,没有数据也不阻塞，只有不阻塞，才有可能单线程下实现异步
    server.setblocking(False)

    # 初始化将服务端加入监听列表
    '''
    为什么要将server放到input里面？
    这个server就是刚才那个socket.socket()，他本身就是一个句柄，需要监测，所以放到socket
    刚开始什么连接都没有，所以只能监测server自己
    '''
    input_list.append(server)

    while True:
        # 开始 select 监听,对input_list中的服务端server进行监听
        '''
        select放入三个监听,1进1出，第三个input_list为什么？因为你不知道哪个会报错，所以把input_list都放进去，里面哪个有异常，在返回给我
        '''
        stdinput, stdoutput, stderr = select(input_list, output_list, input_list)

        # 循环判断是否有客户端连接进来,当有客户端连接进来时select将触发
        '''
        什么情况下？这个stdinput代表有返回回来？
        那就是刚才select监测的活动有新的连接进来了，server有人连接了，那么这里就有返回了
        并且确认,if obt == server，那么肯定是有个新连接过来了
        
        下面这个for不就是循环的所有链接吗？这就是select
        '''
        for obj in stdinput:
            # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时,说明有新客户端连接进来了
            if obj == server: 
                # 接收客户端的连接, 获取客户端对象和客户端地址信息
                conn, addr = server.accept()
                print("Client {0} connected! ".format(addr))
                # 将客户端对象也加入到监听的列表中, 因为不知道客户端有没有给我发数据，所以我也把这个接收客户端数据放入到select的监听列表中， 当客户端发送消息时 select 将触发
                input_list.append(conn)
                # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息，这样新连接过来初始化的工作就完成了
                message_queue[conn] = queue.Queue()

            else:
                # 如果不是新连接过来，那么可能就是刚才放入监听的一个存在的链接。
                # 由于客户端连接进来时服务端接收客户端连接请求，将客户端加入到了监听列表中(input_list)，客户端发送消息将触发
                # 所以判断是否是客户端对象触发
                try:
                    recv_data = obj.recv(1024)
                    # 如果接收有数据过来，那么代表客户端未断开
                    if recv_data:
                        print("received {0} from client {1}".format(recv_data.decode(), addr))
                        # 将收到的消息放入到各客户端的消息队列中
                        message_queue[obj].put(recv_data)

                        # 将回复操作放到output列表中，让select监听
                        # output_list是自己维护的，只要里面有数据，交给select监听，就会马上返回
                        if obj not in output_list:
                            output_list.append(obj)

                except ConnectionResetError:
                    # 客户端断开连接了，将客户端的监听从input列表中移除
                    input_list.remove(obj)
                    # 移除客户端对象的消息队列
                    del message_queue[obj]
                    print("\n[input] Client  {0} disconnected".format(addr))

        # 如果现在没有客户端请求,也没有客户端发送消息时，开始对发送消息列表进行处理，是否需要发送消息
        for sendobj in output_list:
            try:
                # 如果消息队列中有消息,从消息队列中获取要发送的消息
                if not message_queue[sendobj].empty():
                    # 从该客户端对象的消息队列中获取要发送的消息
                    send_data = message_queue[sendobj].get()
                    sendobj.sendall(send_data)
                else:
                    # 将监听移除等待下一次客户端发送消息
                    output_list.remove(sendobj)

            except ConnectionResetError:
                # 客户端连接断开了
                del message_queue[sendobj]
                output_list.remove(sendobj)
                print("\n[output] Client  {0} disconnected".format(addr))
