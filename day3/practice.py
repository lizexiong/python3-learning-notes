__author__ = 'Administrator'


#!/usr/bin/env python3



#练习实例1
# 练习：寻找差异
# 数据库中原有
# old_dict = {
#     "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
#     "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
#     "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
# }
#
# # cmdb 新汇报的数据
# new_dict = {
#     "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
#     "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
#     "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
# }
#
# # 需要删除：？
# # 需要新建：？
# # 需要更新：？ 注意：无需考虑内部元素是否改变，只要原来存在，新汇报也存在，就是需要更新
#
# old_set = set(old_dict.keys())
# update_list = list(old_set.intersection(new_dict.keys()))           #首先返回集合的交集  ['#3', '#1']
#
# new_list = []
# del_list = []
# for i in new_dict.keys():
#     if i not in update_list:                                        #如果新字典的key不在老的和新字典的交集里面，那么就是新的，那就加入new_list
#         new_list.append(i)
#
# for i in old_dict.keys():
#     if i not in update_list:                                        #如果老字典的key不在老的和新字典的交集里面，那么就删除
#         del_list.append(i)
#
# print ("update_list",update_list,"new_list",new_list,"del_list",del_list)


#练习实例2
# from collections import Counter
#
# test = Counter('sadfsadfsadfsdfsdfsdfsdf')
# print (test)

#练习实例3-有序字典
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# lis = ['k1','k2','k3']
#
# for i in lis:
#     print (dic[i])
# from collections import OrderedDict
# dic = OrderedDict()
# dic['k1'] = 'v1'
# dic['k2'] = 'v2'


#练习实例3-单向队列
#
# import queue
# q = queue.Queue()

# #练习实例4-可命名元祖
# import collections
#
# Mytuple = collections.namedtuple('Mytuple',['x', 'y', 'z'])
#
# obj = Mytuple(11,22,33)
#
# print (obj.x)


# import copy
# n1 = 123
# print (id(n1))
# n2 = n1
# print (id(n2))
#
# n2 = copy.copy(n1)
# print(id(n2))
#
# # ## 深拷贝 ##
# n3 = copy.deepcopy(n1)
# print(id(n3))

# import copy
# import copy
# n1 = {"k1": "li", "k2": 123, "k3": ["zexiong", 456]}
# n3 = copy.deepcopy(n1)
#
# print (id(n1['k3']),)
# print (id(n3['k3']),)

# import copy
# dic = {
#     "cpu": [80,],
#     "mem": [80,],
#     "disk":[80,]
# }
#
# print ("before dic",dic)
# new_dic = copy.deepcopy(dic)
# new_dic["cpu"][0] = 50
# print ("after dic",dic)
# print ("new_dic",new_dic)


#函数的动态参数实例

# def show(*args,**kwargs):
#     print (args,type(args))
#     print (kwargs,type(kwargs))
#
# l = [11,22,33,44,55]
# d = {'k1':'v1','k2':'v2'}
# show(*l,**d)


# test = "{name} is {what}"
#
# d = {'name':'lizeixong','what':'6p'}
# #obj = test.format(name='lizexiong',what='6p')
# obj = test.format(**d)
# print (obj)


#lambda

# def func(a):
#     a+=1
#     return a
#
# print ("func:",func(1))
#
#
#
# lambda_func = lambda a:a+1
# print ("lambda_func",lambda_func(2))


# class Coordinate:
#     x = 10
#     y = -5
#     z = 0
#
# point1 = Coordinate()
# print(hasattr(point1, 'x'))
# print(hasattr(point1, 'y'))
# print(hasattr(point1, 'z'))
# print(hasattr(point1, 'no'))  # 没有该属性

# 字符串
seqString = 'Lizexiong'
print(list(reversed(seqString)))

# 元组
seqTuple = ('L', 'i', 'z', 'e', 'x', 'i','o','n','g')
print(list(reversed(seqTuple)))

# range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# 列表
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))