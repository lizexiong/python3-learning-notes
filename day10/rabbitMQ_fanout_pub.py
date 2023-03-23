#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/21 17:07
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : rabbitMQ_fanout_pub.py.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 生产者代码
import pika


#credentials = pika.PlainCredentials('chuan', '123')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               virtual_host='/',
                                                               #credentials=credentials
                                                               ))
# 建立rabbit协议的通道
channel = connection.channel()
# fanout: 所有绑定到此exchange的queue都可以接收消息（实时广播）
# direct: 通过routingKey和exchange决定的那一组的queue可以接收消息（有选择接受）
# topic： 所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息（更细致的过滤）
channel.exchange_declare('logs', exchange_type='fanout')


#因为是fanout广播类型的exchange，这里无需指定routing_key
for i in range(10):
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body='Hello world！%s' % i)

# 关闭与rabbitmq server的连接
connection.close()