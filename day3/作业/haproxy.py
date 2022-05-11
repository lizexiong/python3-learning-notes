__author__ = 'Administrator'
#!/usr/bin/env python






import re
import argparse
import os
import time

BackendInfo = {}        #全局字典存储backend信息，不用return因为在新增和修改里面需要调用这个字典，当然函数也有返回，这里多做一个，调用的时候方便

#ip地址验证函数
def IpVerify(ipAddr):
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False

#判断weight和maxcoon输入的是不是数字
def NumVerify(num):
    try:
        if num.isdigit():
            return True
        else:
            return False
    except:
        return True

#查询backend信息函数，包含指定输入backend查询以及查询所有backend
def Query(operation=None,show=None):
    server_flag = False                                                                                                 #判断当配置文件到了backend的时候，是否需要继续循环取出这个backend下面的值
    with open('haproxy.cfg','r+') as config:
        for line in config.readlines():
            if re.match('backend',line):                                                                                #如果匹配到了backend这一行
                Backend = re.split('\s+',line)[1]                                                                       #那么下标为1就是backend的名称
                BackendInfo[Backend]={}                                                                                 #backend名称作为大字典的key，这样方便后面查询
                server_flag = True                                                                                      #这个标记很重要，如果标记为True了之后，那么才会认为下一行是正常的backend模块内容
            elif server_flag == True and re.match('\s+server',line):                                                   #看这个条件，必须标记为True以及等于server开头才认为是backend的模块内容
                Server = re.split('\s+',line)
                ServerName = Server[2]                                                                                  #然后取出server的值复制给字典，因为可能server有几行，所以这里的标记不能变为False，只有不是backend和server的时候才会是False
                BackendInfo[Backend][ServerName] = {}
                BackendInfo[Backend][ServerName]['ip'] = Server[3]
                BackendInfo[Backend][ServerName]['weight']= Server[5]
                BackendInfo[Backend][ServerName]['maxconn']= Server[7]
            else:
                server_flag = False

    if operation:                                                                                                       #这个是用户的操作，看看输入的是哪个backend
        if operation in BackendInfo.keys():                                                                             #如果用户输入要查询的backend在刚才生成的字典里面，才会下去判断
            print (operation)                                                                                           #因为backend名称只用打印一次，所以要放在循环外面。
            for i,j in BackendInfo.items():
                if show is not None:                                                                                   #如果需要展示，那么就打印出这个backend下的所有server
                    for k,v in j.items():
                        if i == operation:
                            print ('server %s %s weight %s maxconn %s'%(k,BackendInfo[i][k]['ip'],BackendInfo[i][k]['weight'],BackendInfo[i][k]['maxconn']))
        elif operation == 'all':                                                                                        #如果等于all，打印所有backend以及server信息
            for i,j in BackendInfo.items():
                if show is not None:
                    print (i)
                    for k,v in j.items():
                        print ('server %s %s weight %s maxconn %s'%(k,BackendInfo[i][k]['ip'],BackendInfo[i][k]['weight'],BackendInfo[i][k]['maxconn']))
        else:
            print ("没有这个backend")
            return False
    else:
        pass
    return BackendInfo                                                                                                  #这里返回一下，其实也有一个全局字典来存储，只是这里多做了一步而已，两种方式都可以


#用户的增加，修改，删除操作全部是调用这个函数。
def Action(backendname,servername,ip,weight,maxcoon,useraction):
    BackendList = Query(operation='all')

    ipVerify = IpVerify(ip)
    weightVerify =  NumVerify(weight)
    maxcoonVerify = NumVerify(maxcoon)


    if backendname not in BackendList.keys():                                                                           #这里判断用户输入的是否合法，当然这里有个不好的地方就是用户全部输入完成之后才判断的，当然也可以修改，但是这里没必要，因为作业逻辑主体不是这个。
        print ("backend名称为空或者没有这个backend")
    elif servername is None:
        print ("主机名为空")
    elif ipVerify is False:
        print ("IP输入不合法")
    elif weightVerify is False:
        print ("weight输入的不是数字")
    elif maxcoonVerify is False:
        print ("maxconn输入的不是数字")
    elif servername is not None and ipVerify is True and weightVerify is True and maxcoonVerify is True:           #当用户输入全部正确之后，才能进行判断
            AddTag =False
            with open('haproxy.cfg','r+') as old_file,open('haproxy.cfg.new','w') as new_file:                     #这里可以看到，读取旧文件，写入新文件，这里一个是为了能够备份老文件，第二个，没有想到在一个文件里面读取以及修改的方式。
                for line in old_file.readlines():
                    if re.match('backend',line):                                                                        #如果匹配的行等于backend，并且下一个if，用户输入的backendname等于配置文件中的backend的时候，那么tag变为True，为什么变为True，下面解释
                        if re.split('\s+',line)[0] == 'backend' and re.split('\s+',line)[1] == backendname:
                            '''
                      # 为什么用户的add在这里判断，因为看上面，最大的判断就是backend，而add就是依靠backend来判断新的记录写在哪里。所以add在这个嵌套判断里，而且根据情况，add只有这里才会触发，
                      所以不会影响主体逻辑判断。并且只有在这里的时候tag才会等会True，因为后面的mod和del，只有匹配到了自己的backend才能修改和删除，所以只有这里为True了，后面的server才予许更改和删除
                        '''
                            AddTag = True
                            if useraction == 'add':
                                new_file.write(line)
                                new_file.write("\t\t" + "server %s %s weight %s maxcoon %s \n"%(servername,ip,weight,maxcoon))
                            else:
                                new_file.write(line)
                        else:
                            new_file.write(line)
                    elif useraction == 'mod' and re.match('\s+server',line) and AddTag:                                 #如果用户是mod以及在用户输入的backend下的时候才能走修改逻辑（通过AddTag判断是不是用户输入的backend下）
                        if re.split('\s+',line)[2] == servername:
                            new_file.write("\t\t" + "server %s %s weight %s maxcoon %s \n"%(servername,ip,weight,maxcoon))
                        else:
                            new_file.write(line)
                    elif useraction == 'del' and re.match('\s+server',line) and AddTag:                                 #如果用户是del以及在用户输入的backend下的时候才能走修改逻辑（通过AddTag判断是不是用户输入的backend下）
                        if re.split('\s+',line)[2] == servername:
                            pass
                        else:
                            new_file.write(line)
                    else:
                        new_file.write(line)
                        AddTag = False                                                          #这里的False和102行的True是因为，mod和del只有自己的backend下面的时候才能操作，那么只要不是backend和下面的server操作之后，就会变为False，即使匹配到了，用户的操作是删除或者修改，那么也不能操作

            #因为每次都是写入新文件，基本都是每修改一次都会对文件做一次备份
            change_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            os.rename('haproxy.cfg','haproxy.cfg.%s'%(change_time))
            os.rename('haproxy.cfg.new','haproxy.cfg')
    else:
        pass


if __name__ == "__main__":
    while True:
        Query('all')
        #print ("欢迎进入Haproxy配置文件修改系统，输入'query'查询,输入'add'增加，输入'modify'修改,输入'delete'删除,输入'q'退出")
        action = input("欢迎进入Haproxy配置文件修改系统，输入'query'查询,输入'add'增加，输入'modify'修改,输入'delete'删除,输入'q'退出")
        if action == "query":
            print (str(BackendInfo.keys()))
            query_action = input("请输入您要查询的的backend，或者输入all，查询所有")
            Query(query_action,show='show')
        elif action == "add":
            print ("目前所有backend信息如以下。")
            Query('all','show')
            print ("请注意，所有信息输入完成后才会校验，请仔细输入你的选项")
            backendname = input("请输入backendname")
            servername = input("请输入servername")
            ip = input("请输入IP")
            weight = input("请输入weight")
            maxcoon = input("请输入maxcoon")
            Action(backendname,servername,ip,weight,maxcoon,'add')
            Query(backendname,'show')
        elif action == "mod":
            print ("目前所有backend信息如以下。")
            Query('all','show')
            print ("请注意，所有信息输入完成后才会校验，请仔细输入你的选项")
            backendname = input("请输入backendname")
            servername = input("请输入servername")
            ip = input("请输入IP")
            weight = input("请输入weight")
            maxcoon = input("请输入maxcoon")
            Action(backendname,servername,ip,weight,maxcoon,'mod')
            Query(backendname,'show')
        elif action == "del":
            print ("目前所有backend信息如以下。")
            Query('all','show')
            print ("请注意，所有信息输入完成后才会校验，请仔细输入你的选项")
            backendname = input("请输入backendname")
            servername = input("请输入servername")
            Action(backendname,servername,'1.1.1.1',None,None,'del')
            Query(backendname,'show')
        elif action == 'q':
            print ('系统退出')
            break
        else:
            pass


# Action('mysqlserver','mysql2','1.1.1.1',None,None,'del')


