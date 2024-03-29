



import os
import socket
from module import common
from conf import codes,settings


class FtpClient(object):

    """
    客户端的主要类
    1.连接服务器功能
    2.put,get,show方法都在里面
    3.向服务端的登录验证也在里面
    """


    server_ftp_family = socket.AF_INET
    server_ftp_type = socket.SOCK_STREAM

    def __init__(self,host,port,):
        #源代码里这里没有用,这里还是贴出来
        self.__down_path = settings.DOWNLOAD_FILE_PATH
        self.usename = ""
        #客户端登录状态
        self.login_status = False
        #客户端总空间大小
        self.totalspace = 0
        #客户端已使用空间大小
        self.usedspace = 0

        self._server = (host,port)
        #连接句柄
        self.socket = socket.socket(self.server_ftp_family,self.server_ftp_type)


    def connect(self):
        '''
        客户端连接方法,连接失败记录日志，返回状态码
        :return: 成功10000 / 失败10001
        '''
        try:
            self.socket.connect(self._server)
            #连接后客户端马上会返回一个OK,如果没有返回OK,那么返回连接错误代码
            recv_server_data = self.socket.recv(100)
            if str(recv_server_data,'utf-8') == "OK":
                return codes.CONN_SUCC
            else:
                return codes.CONN_FAIL
        except Exception as e:
            common.write_log(e,"error")
            return codes.CONN_FAIL

    def login(self,user,passwd):
        '''
        客户端登录方法，服务端返回结果状态
            0:登录成功
            1:用户名错误
            2:用户名或密码错误，登录失败
        :return:
        '''
        #客户端发送"auth"+帐号密码服务端验证
        sendmsg = "{cmd}|{user}|{passwd}".format(cmd="auth",
                                                 user=user,
                                                 passwd=passwd)
        self.socket.send(bytes(sendmsg,'utf8'))
        #接收服务端的验证结果
        auth_status = self.socket.recv(100).decode('utf8')
        #根据服务端返回的不同状态码，判断用户的状态
        if auth_status == "0":
            #如果验证成功,更改用户的登录状态属性为True，代表验证通过
            self.login_status = True
            self.username = user

            #验证成功后获取客户端的空间信息
            space_info = self.socket.recv(100).decode('utf8')
            self.totalspace = int(space_info.split("|")[0])
            self.usedspace = int(space_info.split("|")[1])
            return codes.AUTH_SUCC
        if auth_status == "1":
            return codes.AUTH_USER_ERROR
        elif auth_status == "2":
            return codes.AUTH_LOCKED
        elif auth_status == "3":
            return codes.AUTH_FAIL

    def put(self,command):

        file_name = command.split("|")[1]

        #判断文件是否存在
        if os.path.isfile(file_name):
            #去掉路径，获取文件名
            fname = os.path.basename(file_name)
            #获取文件大小
            fsize = os.path.getsize(file_name)
            fmd5 = common.encry_md5(file_name)

            #将基本信息发给服务端
            cmd = "put"
            file_msg = "{cmd}|{file}|{filesize}|{filemd5}".format(cmd=cmd,
                                                                  file=fname,
                                                                  filesize=fsize,
                                                                  filemd5=fmd5)
            self.socket.send(bytes(file_msg,encoding='utf8'))
            common.write_log("send file basic info:{0}".format(file_msg), "info")

            #获取服务器端返回状态(是否是新文件及接收到的大小)
            #未收过 "0|0",断电续传"1|recved_size"
            ack_by_server = self.socket.recv(100)
            common.write_log("upload file, received from server:{0}".format(str(ack_by_server, 'utf-8')), "info")

            if str(ack_by_server,encoding='utf-8').split("|")[0] == "0":
                #新文件
                sended_size = 0
                #判断文件是否超过磁盘配额空间
                if self.usedspace + fsize > self.totalspace:
                    return "超过磁盘配额，无法上传文件，请联系管理员!"
                else:
                    self.usedspace += fsize
            else:
                #是否断点续传，是通过服务那边发送消息过来，客户端确认的，断点续传的信息存储在服务端
                sended_size = int(str(ack_by_server,encoding='utf-8').split("|")[1])
                print ("此文件已发送过,但未发送完毕，开始端点续传!......")

            try:
                with open(file_name,'rb') as f:
                    #设置文件的偏移量，简单来说就是看看传到哪了，下次从这里开始传
                    f.seek(sended_size)

                    #如果文件大小-偏移量 大于2048,那么代表还有很多需要传，不是最后一次
                    while fsize -sended_size >2048:
                        contant = f.read(2048)

                        r_size = len(contant)
                        #发送文件
                        self.socket.send(contant)
                        #然后把偏移量+已经传输的，依次循环
                        sended_size += r_size
                        common.print_process(fsize,sended_size)
                    else:
                        contant = f.read(fsize - sended_size)
                        self.socket.send(contant)
                        common.print_process(fsize,fsize)

                common.write_log("upload file<{0}> successful".format(file_name), "info")
                return "\n文件发送成功"
            except Exception as e:
                common.write_log("upload file failed!{0}".format(e), "error")
                return "文件发送失败!"
        else:
            print ("文件不存在")
            return ("文件不存在")

    def get(self, command):
        """
        从服务器端下载文件,下载必须进入到文件所在的目录
        :param command: 下载命令 "get|filename"
        :return: 结果
        """
        return_result = ""
        # 发送基本信息到服务端 (command,username,file)
        self.socket.send(bytes(command, encoding='utf-8'))
        # 先接收到命令是否正确标识,1 文件存在, 0 文件不存在
        ack_by_server = self.socket.recv(100)
        try:
            # 文件名错误,当前路径下找不到
            if str(ack_by_server, encoding='utf-8') == "0":
                return_result = "\n当前目录下未找到指定的文件,请到存在目录下执行get操作!"
            else:
                # 给服务端回应收到，防止连包
                self.socket.send(bytes("ok", 'utf8'))

                # 文件存在,开始接收文件基本信息(大小,文件名)
                file_info = self.socket.recv(100).decode()
                file_size = int(file_info.split("|")[0])
                file_name = file_info.split("|")[1]
                file_md5 = file_info.split("|")[2]

                # 2 发送 ready 标识，准备开始接收文件
                self.socket.send(bytes("ready", 'utf8'))

                # 3 开始接收数据了,每次接收2048
                recv_size = 0
                with open(os.path.join(settings.DOWNLOAD_FILE_PATH, file_name), 'a+b') as fw:
                    while file_size - recv_size > 2048:
                        recv_data = self.socket.recv(2048)
                        fw.write(recv_data)
                        recv_size += len(recv_data)
                        common.print_process(file_size, recv_size)
                    else:
                        recv_data = self.socket.recv(file_size - recv_size)
                        fw.write(recv_data)
                        common.print_process(file_size, file_size)
                return_result = "\n文件下载成功"
                common.writelog("download file<{0}> from server successful".format(file_name), "info")

                # md5 验证
                check_md5 = common.encry_md5(os.path.join(settings.DOWNLOAD_FILE_PATH, file_name))
                if check_md5 == file_md5:
                    common.writelog("md5 check for file<{0}> succ!".format(file_name), "info")
                    return_result += ", MD5 验证成功! "
                else:
                    return_result += ", MD5 验证不匹配啊! "

            return return_result

        except Exception as e:
            common.write_log(e, "error")


    def show(self, *args):
        """
        客户端执行show命令
        :param args: 对于此方法此参数无效
        :return:返回文件列表
        """
        try:
            # 发送命令到服务端
            self.socket.send(bytes("show|", encoding='utf8'))
            # 接收服务端发送结果的大小
            total_data_len = self.socket.recv(100).decode()
            # 收到了 发送一个ready标识
            self.socket.send(bytes("ready", 'utf8'))

            #服务端一下子全部发送过来,当然服务端也可以优化成每次只发送2048，看个人，为了省事，这里就不做了
            # 开始接收数据， 客户端每次接收2048bytes
            recved_data_len = 0
            exec_result = bytes("", 'utf8')
            #和get以及put的逻辑都是一样
            while recved_data_len < int(total_data_len):
                if int(total_data_len) - recved_data_len > 2048:
                    recv_data = self.socket.recv(2048)
                    recved_data_len += len(recv_data)
                    # exec_result += str(recv_data, 'utf-8')
                    exec_result += recv_data
                else:
                    # 小于2048了
                    recv_data = self.socket.recv(int(total_data_len) - recved_data_len)
                    # exec_result += str(recv_data, 'utf-8')
                    recved_data_len += len(recv_data)
                    exec_result += recv_data

            # 获取结果中文件及文件夹的数量
            return_result = str(exec_result, 'utf-8')
            print ("文件总数量为 {0}".format(return_result.split("|")[0]))
            print (return_result.split("|")[1])
            file_count = int(return_result.split("|")[0])
            if file_count == 0:
                return_result = "目前无上传记录"
            else:
                return_result = return_result.split("|")[1]
            return return_result
        except Exception as e:
            common.write_log("client - show - {0}".format(e), "error")


    def cd(self, command):
        """
        目录切换
        :param command: "cd|foldername"
        :return: 返回切换状态
        """
        # 发送命令到服务端
        self.socket.send(bytes(command, 'utf8'))
        # 获取结果
        recv_server_data = self.socket.recv(200)
        # 根据结果进行判断，使用0，1，2来展示层级关系
        result = str(recv_server_data, 'utf-8')
        result_stat = result.split("|")[0]
        result_folder = result.split("|")[1]
        if result_stat == "0":
            # 已经是根目录了
            return_value = "已经到达根目录了!"
        elif result_stat == "1":
            return_value = "目录切换到 {0}!".format(result_folder)
        elif result_stat == "2":
            return_value = "切换失败, {0} 不是一个目录".format(result_folder)
        return return_value









