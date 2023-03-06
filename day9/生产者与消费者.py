#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 02:05
# @Author  : 李泽雄
# @Site    : 
# @File    : 生产者与消费者.py
# @Project : python3
# @Software: PyCharm


import time,random
import queue,threading
q = queue.Queue()
def Producer(name):
  count = 0
  while True:
    time.sleep(random.randrange(3))
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1
    q.join()
    print ("没有包子了")

def Consumer(name):
  count = 0
  while count <1:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
        q.task_done()
    else:
        print("-----no baozi anymore----")
    count +=1
p1 = threading.Thread(target=Producer, args=('A',))
p2 = threading.Thread(target=Producer, args=('A_2',))
c1 = threading.Thread(target=Consumer, args=('B',))
c2 = threading.Thread(target=Consumer, args=('B_2',))
p1.start()
p2.start()
c1.start()
# c2.start()

