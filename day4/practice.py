__author__ = 'Administrator'


#!/usr/bin/env python3

#迭代器
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#生成器实例
# def cash_out(amount):
#     while amount >0:
#         amount -= 100
#         print ('amount',amount)
#         yield 100
#
#
# cash = cash_out(500)
# print (type(cash))
#
#
# print (cash.__next__())
# print (cash.__next__())
# print ("我要去干点别的事情")
# print (cash.__next__())
# print (cash.__next__())
# print (cash.__next__())
# print (cash.__next__()) #第六次会报错


#使用yield实现单线程中的异步并发效果
# import time
# def consumer(name):
#     print ("%s 准备吃包子了" %name)
#     while True:
#         baozi = yield
#         print ("第[%s]包子来了,被[%s]吃了!" %(baozi,name))
#
# def producer(name):
#     c = consumer("A")                           #定义了2个消费者
#     c2 = consumer('B')
#     c.__next__()                                #这里的next就是为了打印 准备吃包子了这句话，碰到yield就返回了
#     c2.__next__()
#     print ("开始做包子了")
#     for i in range(1,6):
#         time.sleep(1)
#         print ("开始做包子")
#         '''
#         #yield不仅可以返回值，还可以接受值，就是通过send给他，
#         看到    baozi=yield了吗，就是通过这个特殊用法，首先send把只给yield，然后yield赋值给baozi。
#         所以这里yield不是返回值，而是接受值。 简单来说如果不是这种方式，yield后面的很难会print出来,yield无法直接赋值
#         '''
#         c.send(i)
#         c2.send(i)
#
# producer('lizexiong')


# def test(a):
#     a-=1
#     yield
#     print ('after',a)
#
# b= test(10)
# print (b.__next__())
# print (b.__next__())


#递归练习

# def calc(n):
#     print ('before',n)
#     if n/2 > 1:
#         calc(n/2)
#
#     print ('after',n)
#     return n
# test = calc(10)
# print (test)

# def func(arg1,arg2,stop):
#     if  arg1 == 0:
#         print (arg1,arg2)
#     arg3 = arg1 + arg2
#     print (arg3)
#     if arg3 < stop:
#         func(arg2,arg3,stop)
#
# func(0,1,30)


#二分算法
# def num_serarch(data,find):
#     mid = int(len(data)/2)
#     if len(data) >=1:
#         if find > data[mid]:
#             print ("data mid right %s" %mid)
#             num_serarch(data[mid:],find)
#         elif find < data[mid]:
#             print ("data mid left %s" %mid)
#             num_serarch(data[:mid],find)
#         else:
#             print ("num is %s" %find)
#     else:
#         print ("not found")
#
# data = list(range(1,500000,3))
# num_serarch(data,10000)
import sys

#二维数组翻转
# data = [[col for col in range(4)] for row in range(4)]
#
#
# '''
# #原始数据[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
#
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [0, 1, 2, 3]
#
# [0, 0, 0, 0]
# [1, 1, 1, 1]
# [2, 2, 2, 2]
# [3, 3, 3, 3]
# '''
#
#
# for r_index,row in enumerate(data):                 #该enumerate()方法将一个计数器添加到一个可迭代对象并返回它（枚举对象）。
#     # print (r_index)
#     for i in range(r_index,len(row)):
#         tmp = data[i][r_index]
#
#         data[i][r_index] = row[i]
#
#         data[r_index][i] = tmp
#
#     for r in data:print(r)
#
#
# #上面的方式使用了类似算法的办法，还有一种更简单取消的办法,具体的逻辑只能自己看代码理会。
#
# data = [[col for col in range(4)] for row in range(4)]
# for i in range(len(data)):
#     a = [data[i][i] for row in range(4)]

#为什么说这种方式是取巧，因为这种方式等于直接输出了



