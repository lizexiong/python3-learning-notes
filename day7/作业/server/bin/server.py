



import socketserver
from module import common
from module import ftpserver
from conf import settings
from multiprocessing import Process


class MyServer(socketserver.BaseRequestHandler):
    '''
    SocketServer内部使用
    IO多路复用
    以及 “多线程” 和 “多进程” ，从而实现并发处理多个客户端请求的Socket服务端。即：每个客户端请求连接到服务器时，Socket服务端都会在服务器是创建一个“线程”或者“进程” 专门负责处理当前客户端的所有请求。
    '''

    def handle(self):
        try:
            client_socket = self.request
            client_addr = self.client_address
            common.write_log("client {0} connected".format(client_addr),"info")
            #发送一个成功标识
            client_socket.send(bytes("OK", encoding='utf8'))

            #发送成功表示后,如果能收到客户端的正确命令，那么代表连接上了
            #定义一个客户端对象
            client_user = None
            while True:
                #从客户端获取命令

                recv_client_data  = client_socket.recv(100)

                #客户端退出了？
                if recv_client_data == b"":
                    common.write_log("client {0} disconnected".format(client_addr),"info")
                    client_socket.close()
                    break

                #取命令(auth,put,get,show,cd)
                cmd = str(recv_client_data,encoding='utf8').split("|")[0]
                common.write_log("client {0} send command {1}".format(client_addr,cmd),'info')

                #如果是登录认证
                if cmd == "auth":
                    #获取客户端对象
                    #如果是认证,那么把socket对象以及接收到的客户端发来的用户名和密码发送到auth专门的“函数里面去，接下来，认证工作全部交给auth函数处理”
                    client_user = ftpserver.auth(client_socket,str(recv_client_data,'utf-8'))

                else:
                    #如果用户已经登录成功,那么client_user就是返回的用户名
                    try:

                        #通过反射去module/server调用命令对应的方法
                        if hasattr(ftpserver,cmd):

                            func = getattr(ftpserver,cmd)
                            func(client_socket,client_user,str(recv_client_data,'utf8'))
                        else:
                            common.write_log("command {0} function not found".format(cmd), "info")
                    except Exception as e:
                        common.write_log("exec {0} error :{1}".format(cmd, e), "error")
                        client_socket.close()
        except Exception as e:
            common.write_log(e,"error")

def doprocess():
    """
    从配置文件获取ip:port，启动服务
    :return:
    """
    server_addr = (settings.FTP_SERVER_IP,settings.FTP_SERVER_PORT)
    server = socketserver.ThreadingTCPServer(server_addr,MyServer)
    server.serve_forever()

def start():
    '''
    该server不能在windows上使用，否则，各种报错
    :return:
    '''
    p = Process(target=doprocess,args=())
    p.start()
    return p








