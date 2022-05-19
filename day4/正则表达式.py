#!/usr/bin/env python3




#!/usr/bin/python

# import re
# print(re.match('www', 'www.google.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.google.com'))         # 不在起始位置匹配




#!/usr/bin/python3
# import re
#
# line = "Cats are smarter than dogs"
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")


#!/usr/bin/python3

# import re
#
# print(re.search('www', 'www.google.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.google.com').span())         # 不在起始位置匹配


#!/usr/bin/python3
# import re
#
# phone = "2004-959-559 # 这是一个电话号码"
#
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print ("电话号码 : ", num)
#
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print ("电话号码 : ", num)


#!/usr/bin/python

# import re
#
# # 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))



import re

result1 = re.findall(r'\d+','lizexiong 123 google 456')

pattern = re.compile(r'\d+')   # 查找数字
result2 = pattern.findall('lizexiong 123 google 456')
result3 = pattern.findall('lize88xiong123google456', 0, 15)

print(result1)
print(result2)
print(result3)