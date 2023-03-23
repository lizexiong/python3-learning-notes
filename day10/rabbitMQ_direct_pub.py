#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/21 17:12
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : rabbitMQ_direct_pub.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


# 生产者代码，测试命令可以使用：python rabbitMQ_direct_pub.py error 404error
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明一个名为direct_logs的direct类型的exchange
# direct类型的exchange
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# 从命令行获取basic_publish的配置参数
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 向名为direct_logs的exchage按照设置的routing_key发送message
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()