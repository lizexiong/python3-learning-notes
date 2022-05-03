#!/usr/bin/env python3



import sys


count_name = 0
count_pass = 0


while count_name <3:
    username = input("Please input your name")
    db = open('account.txt','r+')
    db_lock = open('account_lock.txt','r+')


    for i in db.readlines():
        #print (i.strip())                                                                  #因为打出来会有两个\n，会有一个空格，所以这里取消掉自带的空格和换行的空格
        db_info = i.strip().split(' ',2)                                                    #这里从account.txt取出用户名和密码，然后使用split进行切割成单独的用户和密码
        db_name = db_info[0]
        db_pass = db_info[1]
        if username != db_name :                                                           #判断,输入的用户名是否存在acccount里面，如果没有，那么退出这次循环，并且count_name计数器+1
            print ('not user')
            count_name +=1
        else:                                                                              #尽然不是用户不存在，那么就是存在，开始下一步
            for i in db_lock.readlines():                                                  #判断account_lock，判断用户是否被锁定
                db_lock_name = i.strip()
                if db_lock_name == username:
                    db.close()
                    sys.exit('用户锁定')                                                    #如果被锁定，就直接退出程序了
            while count_pass < 3:                                                           #如果没有被锁定，那么将有3次输入密码的机会
                userpass = input("Please input your password")
                if userpass == db_pass:                                                      #如果成功，那么程序登录成功
                    db.close()
                    sys.exit("登录成功")
                else:                                                                       #如果不成功，那么count_pass计数器+1，并跳出这次循环，进行下一次循环
                    count_pass +=1
                    print ("密码错误，请重新输入")
                    continue
            else:                                                                           #如果count_pass大于3次，那么写入lock文件，并且系统退出
                db_lock.write(username + "\n")
                db_lock.close()                                                             #并关闭文件
                db.close()
                sys.exit("输错3次，系统退出")


