#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/21 15:25
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : rabbitMQ_1_send.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


import pika


#credentials = pika.PlainCredentials('chuan', '123')  # mq用户名和密码，没有则需要自己创建
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               virtual_host='/',
                                                               ))

# 建立rabbit协议的通道
channel = connection.channel()
# 声明消息队列，消息将在这个队列传递，如不存在，则创建。durable指定队列是否持久化
channel.queue_declare(queue='hello', durable=False)

# message不能直接发送给queue，需经exchange到达queue，此处使用以空字符串标识的默认的exchange
# 向队列插入数值 routing_key是队列名
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello world！')
# 关闭与rabbitmq server的连接
connection.close()