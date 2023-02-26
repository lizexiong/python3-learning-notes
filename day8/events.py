#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 15:09
# @Author  : 李泽雄
# @Site    : 
# @File    : events.py
# @Project : python3
# @Software: PyCharm


import threading,time
import random
def light():
    if not event.isSet():
        event.set() #wait不阻塞 #绿灯状态，不设置，就是event,wait，这里肯定是默认放行车辆
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count <13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count <20:
            if event.isSet():    #如果在13-20秒之间，那么肯定是红灯，那么如果设置了，那么就要清除set，变成wait，让人等着，就实现了红绿灯
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯，如果没有set，那么就是event.wait，那就是红灯
        time.sleep(1)
        count +=1
def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if  event.isSet(): #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." %n)
if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()