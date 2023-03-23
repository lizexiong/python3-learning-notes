#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/21 15:21
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : rabbitMQ_1_recv.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm

import pika

#credentials = pika.PlainCredentials('chuan', '123')
# BlockingConnection:同步模式
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               #virtual_host='/',
                                                                ))
channel = connection.channel()
# 申明消息队列。当不确定生产者和消费者哪个先启动时，可以两边重复声明消息队列。
channel.queue_declare(queue='hello', durable=False)
# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    # 手动发送确认消息
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())
    # 告诉生产者，消费者已收到消息

# 告诉rabbitmq，用callback来接收消息
# 默认情况下是要对消息进行确认的，以防止消息丢失。
# 此处将auto_ack明确指明为True，不对消息进行确认。
channel.basic_consume('hello',
                      on_message_callback=callback)
                      # auto_ack=True)  # 自动发送确认消息
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()