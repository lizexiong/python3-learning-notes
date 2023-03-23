#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/21 17:18
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : rabbitMQ_topic_pub.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm

# 生产者代码，基本不变，只需将exchange_type改为topic（测试：python rabbitMQ_topic_pub.py rabbitmq.red
# red color is my favorite
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明一个名为direct_logs的direct类型的exchange
# direct类型的exchange
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

# 从命令行获取basic_publish的配置参数
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 向名为direct_logs的exchange按照设置的routing_key发送message
channel.basic_publish(exchange='topic_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()