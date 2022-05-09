__author__ = 'Administrator'


#!/usr/bin/env python

#不用将argparse作为文件名，否则报错
# import argparse
#
# parser = argparse.ArgumentParser(description='处理一些整数.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='累加器的整数')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='对整数求和(默认值:找出最大值)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))


import argparse

parser = argparse.ArgumentParser(description="Welcome to xx system")    # 这些参数都有默认值，当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，
parser.add_argument('-n',dest='num',type=int,default=1,
                    help="Please enter a number")                       #这里有用户指定输入的参数以及，这里n是变量，类型是int，如果不是int会报错，help是提示
                                                                           #dest和-n都可以接受用户输入的值
parser.add_argument('-a',dest='oper',type=str,default='add',
                    help="Please enter operation")
args = parser.parse_args()

print (args.oper)

