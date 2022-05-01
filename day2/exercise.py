__author__ = 'Administrator'

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-



# counter = 100 # 赋值整型变量
# miles = 1000.0 # 浮点型
# name = "John" # 字符串
#
# print (counter)
# print (miles)
# print (name)




# str = 'Hello World!'
#
# print (str)           # 输出完整字符串
# print (str[0])        # 输出字符串中的第一个字符
# print (str[2:5])      # 输出字符串中第三个至第六个之间的字符串
# print (str[2:])       # 输出从第三个字符开始的字符串
# print (str * 2)       # 输出字符串两次
# print (str + "TEST")  # 输出连接的字符串                        #+号被称为万恶的加号，每次使用+号，都会在内存从从新开辟一块空间





#
# list = [ 'lizexiong', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
#
# print (list)               # 输出完整列表
# print (list[0])            # 输出列表的第一个元素
# print (list[1:3])          # 输出第二个至第三个元素
# print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
# print (tinylist * 2)       # 输出列表两次
# print (list + tinylist)    # 打印组合的列表




# tuple = ( 'lizexiong', 786 , 2.23, 'john', 70.2 )
# tinytuple = (123, 'john')
#
# print (tuple)               # 输出完整元组
# print (tuple[0])            # 输出元组的第一个元素
# print (tuple[1:3])          # 输出第二个至第四个（不包含）的元素
# print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
# print (tinytuple * 2)       # 输出元组两次
# print (tuple + tinytuple)   # 打印组合的元组

# tuple = ( 'lizexiong', {'k2':"wuxinzhe"})
# new_tuple = tuple[1]['k2']='wuxinzhesb'
# print (new_tuple)



#
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'lizexiong','code':9150, 'dept': 'sd2'}
#
#
# print (dict['one'])          # 输出键为'one' 的值
# print (dict[2])              # 输出键为 2 的值
# print (tinydict)             # 输出完整的字典
# print (tinydict.keys())      # 输出所有键
# print (tinydict.values())    # 输出所有值



#
# int()               # 不传入参数时，得到结果0
#
# int(3)
#
# int(3.6)
#
# int('12',16)        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
# 18
# int('0xa',16)
# 10
# int('10',8)
# 8



# s="物品\t单价\t数量\n包子\t1\t2"
# print(s)
# print(repr(s))

#NUMBER
#abs()函数
#!/usr/bin/python3

# print ("abs(-45) : ", abs(-45))
# print ("abs(100.12) : ", abs(100.12))
# #以上实例运行后输出结果为：



#ceil()
# import math   # This will import math module
#
# print ("math.ceil(-45.17) : ", math.ceil(-45.17))
# print ("math.ceil(100.12) : ", math.ceil(100.12))
# print ("math.ceil(100.72) : ", math.ceil(100.72))
# print ("math.ceil(math.pi) : ", math.ceil(math.pi))


#exp()
#!/usr/bin/python
# import math   # 导入 math 模块
#
# print ("math.exp(-45.17) : ", math.exp(-45.17))
# print ("math.exp(100.12) : ", math.exp(100.12))
# print ("math.exp(100.72) : ", math.exp(100.72))
# print ("math.exp(math.pi) : ", math.exp(math.pi))

#fabs()
# import math   # 导入数学模块
#
# print ("math.fabs(-45.17) : ", math.fabs(-45.17))
# print ("math.fabs(100.12) : ", math.fabs(100.12))
# print ("math.fabs(100.72) : ", math.fabs(100.72))
# print ("math.fabs(math.pi) : ", math.fabs(math.pi))

#floor()
#!/usr/bin/python
# import math   # This will import math module
#
# print ("math.floor(-45.17) : ", math.floor(-45.17))
# print ("math.floor(100.12) : ", math.floor(100.12))
# print ("math.floor(100.72) : ", math.floor(100.72))
# print ("math.floor(math.pi) : ", math.floor(math.pi))


#log()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import math   # 导入 math 模块
#
# print ("math.log(100.12) : ", math.log(100.12))
# print ("math.log(100.72) : ", math.log(100.72))
# print ("math.log(math.pi) : ", math.log(math.pi))
# # 设置底数
# print ("math.log(10,2) : ", math.log(10,2))


#log10()
#!/usr/bin/python
# import math   # 导入 math 模块
#
# print ("math.log10(100.12) : ", math.log10(100.12))
# print ("math.log10(100.72) : ", math.log10(100.72))
# print ("math.log10(math.pi) : ", math.log10(math.pi))

#max()
#!/usr/bin/python

# print ("max(80, 100, 1000) : ", max(80, 100, 1000))
# print ("max(-20, 100, 400) : ", max(-20, 100, 400))
# print ("max(-80, -20, -10) : ", max(-80, -20, -10))
# print ("max(0, 100, -400) : ", max(0, 100, -400))


#modf()
# import math   # This will import math module
#
# print ("math.modf(100.12) : ", math.modf(100.12))
# print ("math.modf(100.72) : ", math.modf(100.72))
# print ("math.modf(math.pi) : ", math.modf(math.pi))


#pow()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import math   # 导入 math 模块
#
# print ("math.pow(100, 2) : ", math.pow(100, 2))
# # 使用内置，查看输出结果区别
# print ("pow(100, 2) : ", pow(100, 2))
#
# print ("math.pow(100, -2) : ", math.pow(100, -2))
# print ("math.pow(2, 4) : ", math.pow(2, 4))
# print ("math.pow(3, 0) : ", math.pow(3, 0))


#sqrt()
#!/usr/bin/python
# import math   # This will import math module
#
# print ("math.sqrt(100) : ", math.sqrt(100))
# print ("math.sqrt(7) : ", math.sqrt(7))
# print ("math.sqrt(math.pi) : ", math.sqrt(math.pi))


#choice()
#!/usr/bin/python
# import random
#
# print ("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
# print ("choice('A String') : ", random.choice('A String'))


#!/usr/bin/python
# import random
#
# # 输出 100 <= number < 1000 间的偶数
# print ("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
#
# # 输出 100 <= number < 1000 间的其他数
# print ("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))


#random()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import random
#
# print (random.random())
# print (random.random())
#
# print ("------- 设置种子 seed -------")
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())
#
# # 生成同一个随机数
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())
#
# # 生成同一个随机数
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())
#



#shuffle
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import random
#
# list = [20, 16, 10, 5]
# random.shuffle(list)
# print ("随机排序列表 : ",  list)
#
# random.shuffle(list)
# print ("随机排序列表 : ",  list)


#acos()
#!/usr/bin/python
# import math
#
# print ("acos(0.64) : ",  math.acos(0.64))
# print ("acos(0) : ",  math.acos(0))
# print ("acos(-1) : ",  math.acos(-1))
# print ("acos(1) : ",  math.acos(1))

#asin()
#!/usr/bin/python
# import math
#
# print ("asin(0.64) : ",  math.asin(0.64))
# print ("asin(0) : ",  math.asin(0))
# print ("asin(-1) : ",  math.asin(-1))
# print ("asin(1) : ",  math.asin(1))

#atan()
#!/usr/bin/python
# import math
#
# print ("atan(0.64) : ",  math.atan(0.64))
# print ("atan(0) : ",  math.atan(0))
# print ("atan(10) : ",  math.atan(10))
# print ("atan(-1) : ",  math.atan(-1))
# print ("atan(1) : ",  math.atan(1))



#atan2()
#!/usr/bin/python
# import math
#
# print ("atan2(-0.50,-0.50) : ",  math.atan2(-0.50,-0.50))
# print ("atan2(0.50,0.50) : ",  math.atan2(0.50,0.50))
# print ("atan2(5,5) : ",  math.atan2(5,5))
# print ("atan2(-10,10) : ",  math.atan2(-10,10))
# print ("atan2(10,20) : ",  math.atan2(10,20))


#cos()
#!/usr/bin/python
# import math
#
# print ("cos(3) : ",  math.cos(3))
# print ("cos(-3) : ",  math.cos(-3))
# print ("cos(0) : ",  math.cos(0))
# print ("cos(math.pi) : ",  math.cos(math.pi))
# print ("cos(2*math.pi) : ",  math.cos(2*math.pi))

#hypot()
#!/usr/bin/python
# import math
#
# print ("hypot(3, 2) : ",  math.hypot(3, 2))
# print ("hypot(-3, 3) : ",  math.hypot(-3, 3))
# print ("hypot(0, 2) : ",  math.hypot(0, 2))


#sin()
#!/usr/bin/python
# import math
#
# print ("sin(3) : ",  math.sin(3))
# print ("sin(-3) : ",  math.sin(-3))
# print ("sin(0) : ",  math.sin(0))
# print ("sin(math.pi) : ",  math.sin(math.pi))
# print ("sin(math.pi/2) : ",  math.sin(math.pi/2))


#tan()
#!/usr/bin/python
# import math
#
# print ("tan(3) : ",  math.tan(3))
# print ("tan(-3) : ",  math.tan(-3))
# print ("tan(0) : ",  math.tan(0))
# print ("tan(math.pi) : ",  math.tan(math.pi))
# print ("tan(math.pi/2) : ",  math.tan(math.pi/2))
# print ("tan(math.pi/4) : ",  math.tan(math.pi/4))


#degress()
#!/usr/bin/python
# import math
#
# print ("degrees(3) : ",  math.degrees(3))
# print ("degrees(-3) : ",  math.degrees(-3))
# print ("degrees(0) : ",  math.degrees(0))
# print ("degrees(math.pi) : ",  math.degrees(math.pi))
# print ("degrees(math.pi/2) : ",  math.degrees(math.pi/2))
# print ("degrees(math.pi/4) : ",  math.degrees(math.pi/4))


#radians()
#!/usr/bin/python
# import math
#
# print ("radians(90) : ",  math.radians(90))
# print ("radians(45) : ",  math.radians(45))
# print ("radians(30) : ",  math.radians(30))


#字符串

#!/usr/bin/python

# var1 = 'Hello World!'
# var2 = "Python Lizexiong"
#
# print ("var1[0]: ", var1[0])
# print ("var2[1:5]: ", var2[1:5])


#字符串拼接
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# var1 = 'Hello World!'
#
# print ("输出 :- ", var1[:6] + 'Lizexiong!')


#字符串运算符
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = "Hello"
# b = "Python"
#
# print ("a + b 输出结果：", a + b)                #万恶的加号，使用加号会在内存中重新申请空间
# print ("a * 2 输出结果：", a * 2 )
# print ("a[1] 输出结果：", a[1])
# print ("a[1:4] 输出结果：", a[1:4])
#
# if( "H" in a) :
#     print ("H 在变量 a 中")
# else :
#     print ("H 不在变量 a 中")
#
# if( "M" not in a) :
#     print ("M 不在变量 a 中")
# else :
#     print ("M 在变量 a 中")
#
# print (r'\n')
# print (R'\n')

#字符串格式化
#!/usr/bin/python

# print ("My name is %s and weight is %d kg!" % ('LiZeXiong', 62))


#endswith()
#!/usr/bin/python

# str = "this is string example....wow!!!";
#
# suffix = "wow!!!";
# print (str.endswith(suffix))
# print (str.endswith(suffix,20))
#
# suffix = "is";
# print (str.endswith(suffix, 2, 4))
# print (str.endswith(suffix, 2, 6))


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# str = "zxiong\t12345\tabc"
# print('原始字符串: {}'.format(str))
#
# # 默认 8 个空格
# # zxiong 有 6 个字符，后面的 \t 填充 2 个空格
# # 12345 有 5 个字符，后面的 \t 填充 3 个空格
# print('替换 \\t 符号: {}'.format(str.expandtabs()))
#
# # 2 个空格
# # zxiong 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# # 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
# print('使用 2 个空格替换 \\t 符号: {}'.format(str.expandtabs(2)))
#
# # 3 个空格
# print('使用 3 个空格: {}'.format(str.expandtabs(3)))
#
# # 4 个空格
# print('使用 4 个空格: {}'.format(str.expandtabs(4)))
#
# # 5 个空格
# print('使用 5 个空格: {}'.format(str.expandtabs(5)))
#
# # 6 个空格
# print('使用 6 个空格: {}'.format(str.expandtabs(6)))


#find()
#!/usr/bin/python
#
# str1 = "this is string example....wow!!!";
# str2 = "exam";
#
# print (str1.find(str2))
# print (str1.find(str2, 10))
# print (str1.find(str2, 40))


#format格式化函数
#!/usr/bin/python
# -*- coding: UTF-8 -*-


# print("网站名：{name}, 地址 {url}".format(name="huawei", url="www.lizexiong.com"))
#
# # 通过字典设置参数
# site = {"name": "huawei", "url": "www.lizexiong.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
#
# # 通过列表索引设置参数
# my_list = ['huawei', 'www.lizexiong.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# class AssignValue(object):
#     def __init__(self, value):
#         self.value = value
# my_value = AssignValue(6)
# print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# print ("{} 对应的位置是 {{0}}".format("lizexiong"))


#index()
#!/usr/bin/python

# str1 = "this is string example....wow!!!";
# str2 = "exam";
#
# print (str1.index(str2))
# print (str1.index(str2, 10))
# print (str1.index(str2, 40))

#isalnum()
#!/usr/bin/python
# -*- coding: UTF-8 -*-


# str = "this2009";  # 字符中没有空格
# print (str.isalnum())
#
# str = "this is string example....wow!!!";
# print (str.isalnum())

#isalpha()
#!/usr/bin/python
# coding=utf-8

# str = "lizexiong";
# print (str.isalpha())
#
# str = "lizexiong华为";
# print (str.isalpha())
#
# str = "this is string example....wow!!!";
# print (str.isalpha())


#isdecimal()
# str = u"this2009";
# print (str.isdecimal());
#
# str = u"23443434";
# print (str.isdecimal());


#isdigit
# str = "123456";  # Only digit in this string
# print (str.isdigit());
#
# str = "this is string example....wow!!!";
# print (str.isdigit());

#islower()
# str = "THIS is string example....wow!!!";
# print (str.islower());
#
# str = "this is string example....wow!!!";
# print (str.islower());


#isnumeric()
# str = u"this2017";
# print (str.isnumeric());
#
# str = u"23443434";
# print (str.isnumeric());

#isspace()
# str = "       ";
# print (str.isspace());
#
# str = "This is string example....wow!!!";
# print (str.isspace());

#istitle()
# str = "This Is String Example...Wow!!!";
# print (str.istitle());
#
# str = "This is string example....wow!!!";
# print (str.istitle());

#isupper()
# str = "THIS IS STRING EXAMPLE....WOW!!!";
# print ( str.isupper() );
#
# str = "THIS is string example....wow!!!";
# print ( str.isupper() );


#join()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# str = "-";
# seq = ("a", "b", "c"); # 字符串序列
# print (str.join( seq ));


#ljust()
#!/usr/bin/python

# str = "this is string example....wow!!!";
#
# print (str.ljust(50, '0'));



#rfind()

# str = "this is really a string example....wow!!!";
# substr = "is";
#
# print (str.rfind(substr));
# print (str.rfind(substr, 0, 10));
# print (str.rfind(substr, 10, 0));
#
# print (str.find(substr));
# print (str.find(substr, 0, 10));
# print (str.find(substr, 10, 0));



# str = "this is string example....wow!!!";
#
# print (str.rjust(50, '0'));


#rstrip()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# random_string = 'this is good    '
#
# # 字符串末尾的空格会被删除
# print(random_string.rstrip())
#
# # 'si oo' 不是尾随字符，因此不会删除任何内容
# print(random_string.rstrip('si oo'))
#
# # 在 'sid oo' 中 'd oo' 是尾随字符，'ood' 从字符串中删除
# print(random_string.rstrip('sid oo'))
#
# # 'm/' 是尾随字符，没有找到 '.' 号的尾随字符, 'm/' 从字符串中删除
# website = 'www.lizexiong.com/'
# print(website.rstrip('m/.'))
#
#
# # 移除逗号(,)、点号(.)、字母 s、q 或 w，这几个都是尾随字符
# txt = "banana,,,,,ssqqqww....."
# x = txt.rstrip(",.qsw")
# print(x)
# # 删除尾随字符 *
# str = "*****this is string example....wow!!!*****"
# print (str.rstrip('*'))
# print(x)


#split()
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print (str.split( ));       # 以空格为分隔符，包含 \n
# print (str.split(' ', 1 )); # 以空格为分隔符，分隔成两个


#
# txt = "Google#lizexiong#Taobao#Facebook"
#
# # 第二个参数为 1，返回两个参数列表
# x = txt.split("#", 1)
#
# print (x)


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import re
# a='Beautiful, is; better*than\nugly'
# # 四个分隔符为：,  ;  *  \n
# x= re.split(',|; |\*|\n',a)
# print(x)



#strip()
# str = "00000003210lizexiong01230000000";
# print (str.strip( '0' ));  # 去除首尾字符 0
#
#
# str2 = "   lizexiong      ";   # 去除首尾空格
# print (str2.strip());


#swapcase()
#!/usr/bin/python

# str = "LIZEXIONG!!!";
# print ( str.swapcase() );
#
# str = "lizexiong!!!";
# print ( str.swapcase() );
#
# str = "abCDE--LiZeXiong!!!";
# print ( str.swapcase() );


#translate()
#from string import maketrans  # 引用 maketrans 函数。在python3.4之后已内建，不需要导入

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
#
# str = "this is string example....wow!!!";
# print (str.translate(trantab));

#!/usr/bin/python

#from string import maketrans   # Required to call maketrans function.

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
#
# str = "this is string example....wow!!!";
# print (str.translate(trantab, 'xm'))


#upper()
#!/usr/bin/python
#
# str = "this is string example....wow!!!";
#
# print ("str.upper() : ", str.upper())


#zfill
# str = "this is string example....wow!!!";
#
# print (str.zfill(40));
# print (str.zfill(50));



#list()
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
#
# print ("list1[0]: ", list1[0])
# print ("list2[1:5]: ", list2[1:5])


#tuple()
# tuple1, tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
#
# print ("Max value element : ", max(tuple1))
# #print "Max value element : ", max(tuple2)


#dict()



#算数运算符
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 21
# b = 10
# c = 0
#
# c = a + b
# print ("1 - c 的值为：", c)
#
# c = a - b
# print ("2 - c 的值为：", c)
#
# c = a * b
# print ("3 - c 的值为：", c)
#
# c = a / b
# print ("4 - c 的值为：", c)
#
# c = a % b
# print ("5 - c 的值为：", c)
#
# # 修改变量 a 、b 、c
# a = 2
# b = 3
# c = a**b
# print ("6 - c 的值为：", c)
#
# a = 10
# b = 5
# c = a//b
# print ("7 - c 的值为：", c)


#比较运算符
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 21
# b = 10
# c = 0
#
# if  a == b :
#    print ("1 - a 等于 b")
# else:
#    print ("1 - a 不等于 b")
#
# if  a != b :
#    print ("2 - a 不等于 b")
# else:
#    print ("2 - a 等于 b")
#
# #<>python3废弃
# #if  a <> b :
# #   print ("3 - a 不等于 b")
# #else:
# #   print ("3 - a 等于 b")
#
# if  a < b :
#    print ("4 - a 小于 b" )
# else:
#    print ("4 - a 大于等于 b")
#
# if  a > b :
#    print ("5 - a 大于 b")
# else:
#    print ("5 - a 小于等于 b")
#
# # 修改变量 a 和 b 的值
# a = 5
# b = 20
# if  a <= b :
#    print ("6 - a 小于等于 b")
# else:
#    print ("6 - a 大于  b")
#
# if  b >= a :
#    print ("7 - b 大于等于 a")
# else:
#    print ("7 - b 小于 a")



#赋值运算符
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 21
# b = 10
# c = 0
#
# c = a + b
# print ("1 - c 的值为：", c)
#
# c += a
# print ("2 - c 的值为：", c)
#
# c *= a
# print ("3 - c 的值为：", c)
#
# c /= a
# print ("4 - c 的值为：", c)
#
# c = 2
# c %= a
# print ("5 - c 的值为：", c)
#
# c **= a
# print ("6 - c 的值为：", c)
#
# c //= a
# print ("7 - c 的值为：", c)


#位运算
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 60            # 60 = 0011 1100
# b = 13            # 13 = 0000 1101
# c = 0
#
# c = a & b;        # 12 = 0000 1100
# print ("1 - c 的值为：", c)
#
# c = a | b;        # 61 = 0011 1101
# print ("2 - c 的值为：", c)
#
# c = a ^ b;        # 49 = 0011 0001
# print ("3 - c 的值为：", c)
#
# c = ~a;           # -61 = 1100 0011
# print ("4 - c 的值为：", c)
#
# c = a << 2;       # 240 = 1111 0000
# print ("5 - c 的值为：", c)
#
# c = a >> 2;       # 15 = 0000 1111
# print ("6 - c 的值为：", c)


#逻辑运算符
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 10
# b = 20
#
# if  a and b :
#    print ("1 - 变量 a 和 b 都为 true")
# else:
#    print ("1 - 变量 a 和 b 有一个不为 true")
#
# if  a or b :
#    print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#    print ("2 - 变量 a 和 b 都不为 true")
#
# # 修改变量 a 的值
# a = 0
# if  a and b :
#    print ("3 - 变量 a 和 b 都为 true")
# else:
#    print ("3 - 变量 a 和 b 有一个不为 true")
#
# if  a or b :
#    print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#    print ("4 - 变量 a 和 b 都不为 true")
#
# if not( a and b ):
#    print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
# else:
#    print ("5 - 变量 a 和 b 都为 true")

#成员运算符
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ];
#
# if ( a in list ):
#    print ("1 - 变量 a 在给定的列表中 list 中")
# else:
#    print ("1 - 变量 a 不在给定的列表中 list 中")
#
# if ( b not in list ):
#    print ("2 - 变量 b 不在给定的列表中 list 中")
# else:
#    print ("2 - 变量 b 在给定的列表中 list 中")
#
# # 修改变量 a 的值
# a = 2
# if ( a in list ):
#    print ("3 - 变量 a 在给定的列表中 list 中")
# else:
#    print ("3 - 变量 a 不在给定的列表中 list 中")

#身份运算符
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 20
# b = 20
#
# if ( a is b ):
#    print ("1 - a 和 b 有相同的标识")
# else:
#    print ("1 - a 和 b 没有相同的标识")
#
# if ( a is not b ):
#    print ("2 - a 和 b 没有相同的标识")
# else:
#    print ("2 - a 和 b 有相同的标识")
#
# # 修改变量 b 的值
# b = 30
# if ( a is b ):
#    print ("3 - a 和 b 有相同的标识")
# else:
#    print ("3 - a 和 b 没有相同的标识")
#
# if ( a is not b ):
#    print ("4 - a 和 b 没有相同的标识")
# else:
#    print ("4 - a 和 b 有相同的标识")



#运算符优先级
# a = 20
# b = 10
# c = 15
# d = 5
# e = 0
#
# e = (a + b) * c / d       #( 30 * 15 ) / 5
# print ("(a + b) * c / d 运算结果为：",  e)
#
# e = ((a + b) * c) / d     # (30 * 15 ) / 5
# print ("((a + b) * c) / d 运算结果为：",  e)
#
# e = (a + b) * (c / d);    # (30) * (15/5)
# print ("(a + b) * (c / d) 运算结果为：",  e)
#
# e = a + (b * c) / d;      #  20 + (150/5)
# print ("a + (b * c) / d 运算结果为：",  e)


#if
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 例3：if语句多个条件

# num = 9
# if num >= 0 and num <= 10:    # 判断值是否在0~10之间
#     print ('hello')
# # 输出结果: hello
#
# num = 10
# if num < 0 or num > 10:    # 判断值是否在小于0或大于10
#     print ('hello')
# else:
#     print ('undefine')
# # 输出结果: undefine
#
# num = 8
# # 判断值是否在0~5或者10~15之间
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
#     print ('hello')
# else:
#     print ('undefine')
# # 输出结果: undefine


#!/usr/bin/python

# count = 0
# while count < 5:
#    print (count, " is  less than 5")
#    count = count + 1
# else:
#    print (count, " is not less than 5")


# var = 100
#
# if ( var  == 100 ) : print ("变量 var 的值为100")
#
# print ("Good bye!")

# flag = 1
#
# while (flag): print ('Given flag is really true!')
#
# print ("Good bye!")



#for
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# for letter in 'Python':     # 第一个实例
#    print("当前字母: %s" % letter)
#
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # 第二个实例
#    print ('当前水果: %s'% fruit)
#
# print ("Good bye!")


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# for num in range(10,20):  # 迭代 10 到 20 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          j=num/i          # 计算第二个因子
#          print ('%d 等于 %d * %d' % (num,i,j))
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       print ('%d 是一个质数' % num)


#循环嵌套
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j): break
#       j = j + 1
#    if (j > i/j) : print (i, " 是素数")
#    i = i + 1
#
# print ("Good bye!")


# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       break
#    print ('当前字母 :', letter)
#
# var = 10                    # 第二个实例
# while var > 0:
#    print ('当前变量值 :', var)
#    var = var -1
#    if var == 5:   # 当变量 var 等于 5 时退出循环
#       break
#
# print ("Good bye!")


# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print ('这是 pass 块')
#    print ('当前字母 :', letter)
#
# print ("Good bye!")



#str
# str = 'Lizexiong'
#
# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
# print (str + "TEST") # 连接字符串


# list = [ 'abcd', 786 , 2.23, 'Lizexiong', 70.2 ]
# tinylist = [123, 'Lizexiong']
#
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表

#
# def reverseWords(input):
#
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
#
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords=inputWords[-1::-1]
#
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#
#     return output
#
# if __name__ == "__main__":
#     input = 'I like lizexiong'
#     rw = reverseWords(input)
#     print(rw)

# tuple = ( 'abcd', 786 , 2.23, 'lizexiong', 70.2  )
# tinytuple = (123, 'lizexiong')
#
# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组


#!/usr/bin/python3

# dict = {}
# dict['one'] = "1 - 华为"
# dict[2]     = "2 - 三星"
#
# tinydict = {'name': 'lizexiong','code':1, 'site': 'www.lizexiong.com'}
#
#
# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值


#set
#!/usr/bin/python3

# sites = {'Google', 'Taobao', 'Lizexiong', 'Facebook', 'Zhihu', 'Baidu','lizexiong'}
#
# print(sites)   # 输出集合，重复的元素被自动去掉
#
# # 成员测试
# if 'Lizexiong' in sites :
#     print('Lizexiong 在集合中')
# else :
#     print('Lizexiong 不在集合中')
#
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)     # a 和 b 的差集
#
# print(a | b)     # a 和 b 的并集
#
# print(a & b)     # a 和 b 的交集
#
# print(a ^ b)     # a 和 b 中不同时存在的元素

# num_int = 123
# num_flo = 1.23
#
# num_new = num_int + num_flo
#
# print("datatype of num_int:",type(num_int))
# print("datatype of num_flo:",type(num_flo))
#
# print("Value of num_new:",num_new)
# print("datatype of num_new:",type(num_new))

#
# num_int = 123
# num_str = "456"
#
# print("num_int 数据类型为:",type(num_int))
# print("类型转换前，num_str 数据类型为:",type(num_str))
#
# num_str = int(num_str)    # 强制转换为整型
# print("类型转换后，num_str 数据类型为:",type(num_str))
#
# num_sum = num_int + num_str
#
# print("num_int 与 num_str 相加结果为:",num_sum)
# print("sum 数据类型为:",type(num_sum))


#!/usr/bin/python3
# import math   # 导入 math 模块
#
# print ("math.ceil(-45.17) : ", math.ceil(-45.17))
# print ("math.ceil(100.12) : ", math.ceil(100.12))
# print ("math.ceil(100.72) : ", math.ceil(100.72))
# print ("math.ceil(math.pi) : ", math.ceil(math.pi))


# import math   # 导入 math 模块
#
# print ("math.exp(-45.17) : ", math.exp(-45.17))
# print ("math.exp(100.12) : ", math.exp(100.12))
# print ("math.exp(100.72) : ", math.exp(100.72))
# print ("math.exp(math.pi) : ", math.exp(math.pi))


# import math   # 导入 math 模块
#
# print ("math.fabs(-45.17) : ", math.fabs(-45.17))
# print ("math.fabs(100.12) : ", math.fabs(100.12))
# print ("math.fabs(100.72) : ", math.fabs(100.72))
# print ("math.fabs(math.pi) : ", math.fabs(math.pi))

# import math
# print ("math.floor(-45.17) : ", math.floor(-45.17))
# print ("math.floor(100.12) : ", math.floor(100.12))
# print ("math.floor(100.72) : ", math.floor(100.72))
# print ("math.floor(math.pi) : ", math.floor(math.pi))

#!/usr/bin/python3
# import math   # 导入 math 模块
#
# print ("math.log(100.12) : ", math.log(100.12))
# print ("math.log(100.72) : ", math.log(100.72))
# print ("math.log(math.pi) : ", math.log(math.pi))

#!/usr/bin/python3
# import math   # 导入 math 模块
#
# print ("math.log10(100.12) : ", math.log10(100.12))
# print ("math.log10(100.72) : ", math.log10(100.72))
# print ("math.log10(119) : ", math.log10(119))
# print ("math.log10(math.pi) : ", math.log10(math.pi))

# import math   # 导入 math 模块
#
# print ("math.modf(100.12) : ", math.modf(100.12))
# print ("math.modf(100.72) : ", math.modf(100.72))
# print ("math.modf(119) : ", math.modf(119))
# print ("math.modf(math.pi) : ", math.modf(math.pi))


# import math   # 导入 math 模块
#
# print ("math.pow(100, 2) : ", math.pow(100, 2))
# # 使用内置，查看输出结果区别
# print ("pow(100, 2) : ", pow(100, 2))
# print ("math.pow(100, -2) : ", math.pow(100, -2))
# print ("math.pow(2, 4) : ", math.pow(2, 4))
# print ("math.pow(3, 0) : ", math.pow(3, 0))


#!/usr/bin/python3

# print ("round(70.23456) : ", round(70.23456))
# print ("round(56.659,1) : ", round(56.659,1))
# print ("round(80.264, 2) : ", round(80.264, 2))
# print ("round(100.000056, 3) : ", round(100.000056, 3))
# print ("round(-100.000056, 3) : ", round(-100.000056, 3))


# import random
#
# random.seed()
# print ("使用默认种子生成随机数：", random.random())
# print ("使用默认种子生成随机数：", random.random())
#
# random.seed(10)
# print ("使用整数 10 种子生成随机数：", random.random())
# random.seed(10)
# print ("使用整数 10 种子生成随机数：", random.random())
#
# random.seed("hello",2)
# print ("使用字符串种子生成随机数：", random.random())

#!/usr/bin/python3
# import math
#
# print ("radians(90) : ",  math.radians(90))     # 1 弧度等于大概 57.3°
# print ("radians(45) : ",  math.radians(45))
# print ("radians(30) : ",  math.radians(30))
# print ("radians(180) : ",  math.radians(180))  # 180 度的弧度为 π
#
# print("180 / pi : ", end ="")
# print (math.radians(180 / math.pi))

# para_str = """这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。
# """
# print (para_str)


#!/usr/bin/python3

# str = "李泽雄";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
#
# print(str)
#
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
#
# print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
# print("GBK 解码：", str_gbk.decode('GBK','strict'))


#!/usr/bin/python3
#
# #s = '²3455'
# s = '\u00B23455'
# print(s.isnumeric())
# # s = '½'
# s = '\u00BD'
# print(s.isnumeric())
#
# a = "\u0030" #unicode for 0
# print(a.isnumeric())
#
# b = "\u00B2" #unicode for ²
# print(b.isnumeric())
#
# c = "10km2"
# print(c.isnumeric())

# txt = "Lizexiong!"
# mytable = txt.maketrans("L", "X")
# print(txt.translate(mytable))
#
# # 使用字符串设置要替换的字符，一一对应
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
#
# str = "this is string example....wow!!!"
# print (str.translate(trantab))

# txt = "Google Lizexiong Taobao!"
# x = "mSa"
# y = "eJo"
# z = "odnght"   # 设置删除的字符
# mytable = txt.maketrans(x, y, z)
# print(txt.translate(mytable))


# str1 = "this is string example....wow!!!";
# str2 = "is";
#
# print (str1.rindex(str2));
# print (str1.rindex(str2,30));

#
# str = "lizexiong2022"
# print (str.isdecimal())
#
# str = "23443434"
# print (str.isdecimal())

#
# list = ['Google', 'Lizexiong', 1997, 2000]
#
# print ("第三个元素为 : ", list[2])
# list[2] = 2001
# print ("更新后的第三个元素为 : ", list[2])
#
# list1 = ['Google', 'Lizexiong', 'Taobao']
# list1.append('Baidu')
# print ("更新后的列表 : ", list1)

# aTuple = (123, 'Google', 'Lizexiong', 'Taobao')
# list1 = list(aTuple)
# print ("列表元素 : ", list1)
#
# str="Hello World"
# list2=list(str)
# print ("列表元素 : ", list2)


# list1 = ['Google', 'Lizexiong', 'Taobao', 'Baidu']
# list2 = list1.copy()
# print ("list2 列表: ", list2)
#
#
#
# list3 = ['Google', 'Lizexiong', 'Taobao', {'Baidu':{'chanpin':'baiduyunpan'}}]
# list4 = list3.copy()
# print ("list4 列表: ", list4)


# site= {'name': '华为', 'alexa': 10000, 'url': 'www.lizexiong.com'}
#
# # ('url': 'www.lizexiong.com') 最后插入会被删除
# result = site.popitem()
#
# print('返回值 = ', result)
# print('site = ', site)
#
# # 插入新元素
# site['nickname'] = 'lizexiong'
# print('site = ', site)
#
# # 现在 ('nickname', 'lizexiong') 是最后插入的元素
# result = site.popitem()
#
# print('返回值 = ', result)
# print('site = ', site)



# names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# new_names = [name.upper()for name in names if len(names)>10]
# print (new_names)

# new_names = [print (i) for i in range(30) if i%3==0]


# listdemo = ['Google','Lizexiong', 'Taobao']
# newdict = {key:len(key) for key in listdemo}
# print (newdict)


# def change(a):
#     print(id(a))   # 指向的是同一个对象
#     a=10
#     print(id(a))   # 一个新对象
#
# a=1
# print(id(a))
# change(a)


# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print ("arg1", arg1)
#    for var in vartuple:
#       print (var)
#    return
#
# # 调用printinfo 函数
# printinfo( 10 )
# printinfo( 70, 60, 50 )




# 可写函数说明
# def printinfo( arg1, **vardict ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print ('arg1',arg1)
#    print ('vardict',vardict)
#
# # 调用printinfo 函数
# printinfo(1, a=2,b=3)


class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)