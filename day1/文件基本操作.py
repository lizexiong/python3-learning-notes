#!/usr/bin/env python3



import os
import sys


# Python3 File(文件) 方法
# open()方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# 注意：    使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# open()    函数常用形式是接收两个参数：文件名(file)和模式(mode)。
# open(file, mode='r')
# 完整的语法格式为：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数说明:
# file:     必需，文件路径（相对或者绝对路径）。
# mode:     可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors:   报错级别
# newline:  区分换行符
# closefd:  传入的file参数类型
# opener:   设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# 模式	描述
# t	    文本模式 (默认)。
# x	    写模式，新建一个文件，如果该文件已存在则会报错。
# b	    二进制模式。
# +	    打开一个文件进行更新(可读可写)。
# U	    通用换行模式（Python 3 不支持）。
# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
#       默认为文本模式，如果要以二进制模式打开，加上 b 。


# file 对象
# file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

# 序号	方法及描述
# file.close()
# 关闭文件。关闭后文件不能再进行读写操作。

# file.flush()
# 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

# file.fileno()
# 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

# file.isatty()
# 如果文件连接到一个终端设备返回 True，否则返回 False。

# file.next()
# Python 3 中的 File 对象不支持 next() 方法。

# 返回文件下一行。

# file.read([size])
# 从文件读取指定的字节数，如果未给定或为负则读取所有。

# file.readline([size])
# 读取整行，包括 "\n" 字符。

# file.readlines([sizeint])
# 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

# file.seek(offset[, whence])
# 移动文件读取指针到指定位置

# file.tell()
# 返回文件当前位置。

# file.truncate([size])
# 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。

# file.write(str)
# 将字符串写入文件，返回的是写入的字符长度。

# file.writelines(sequence)
# 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

# file.writable()
# 文件可写返回True 否则返回False

# file.readable()
# 文件可读返回True 否则返回False

# file.seekable()
# 文件可以seek返回True 否则返回False

# 打开文件
f1 = open("myfile.txt", "w+")
f1.writelines("hello world 1\n")
f1.writelines("hello world 2\n")
f1.writelines("hello world 3\n")
f1.writelines("hello world 4\n")
f1.writelines("hello world 5\n")

# write(str) 返回写入字节数
wdlen = f1.write("abcdefghijklmnopqrstuvwxyz")
print("write byte:%d" % (wdlen))

# 刷新缓存
f1.flush()
# 关闭文件
f1.close()

# myfile.txt 文件内容
# hello world 1
# hello world 2
# hello world 3
# hello world 4
# hello world 5

f2 = open("myfile.txt", "r")
print("文件描述:", f2.fileno())
ret = f2.isatty()
print("返回值:", ret)

# 逐行读取内容
for index in range(5):
    line = next(f2)
    print("第%d行 : %s" % (index, line))

f2.close()


fw = open("1.wav", "rb")
print("file name:", fw.name)        # file name: 1.wav
print("file isatty:",fw.isatty())   # file isatty: False
buffer = fw.read(128)
print("read buffer:%s" % (buffer))  # b'RIFF\xd4\x88\x08\x00WA'

# seek() 方法用于移动文件读取指针到指定位置。
# 语法
# seek() 方法语法如下：
# fileObject.seek(offset[, whence])
# 参数
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
# whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；
#   0 代表从文件开头开始算起，
#   1 代表从当前位置开始算起，
#   2 代表从文件末尾算起。
#   返回值如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。


# 开始位置 正向偏移44个字节
fw.seek(44, 0)
buffer = fw.read(16)
print(buffer)
print("current pos:%d" % (fw.tell()))

# 当前位置 反向偏移8个字节
fw.seek(8, 1)
buffer = fw.read(16)
print(buffer)
print("current pos:%d" % (fw.tell()))

# 末尾位置 反向偏移128个字节
fw.seek(-128, 2)
buffer = fw.read(16)
print(buffer)
print("current pos:%d" % (fw.tell()))

# 计算文件size
fw.seek(0, 2)
print("file size:%d" % (fw.tell()))

# truncate([size])从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；
#   截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
# fw.truncate(16)

fw.close()


fs = open("myfile.txt", "rb") #rb  or  rt

#readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
rdline = fs.readline()
print(type(rdline))#<class 'bytes'>
print(rdline)   #b'hello world 1\r\n'

rdline_num = fs.readline(3) #实参值最大不超过一行的长度
print(type(rdline_num)) #<class 'bytes'>
print(rdline_num)   #b'hel'  读取一行的3个字节

# readlines() 读取所有行(直到结束符 EOF)并返回列表, 返回的是<class 'list'>列表类型
rdlines = fs.readlines()
print(type(rdlines))#<class 'list'>
print(rdlines)
#[b'lo world 2\r\n', b'hello world 3\r\n', b'hello world 4\r\n', b'hello world 5\r\n', b'abcdefghijklmnopqrstuvwxyz']

# 设置文件偏移到开始位置
fs.seek(0, 0)
print(fs.readlines())
#[b'hello world 1\r\n', b'hello world 2\r\n', b'hello world 3\r\n', b'hello world 4\r\n', b'hello world 5\r\n', b'abcdefghijklmnopqrstuvwxyz']

print(fs.writable())    #False

print(fs.readable())    #True

print(fs.seekable())    #True

fs.close()
