#!/usr/bin/env python
# -*- coding:utf-8 -*-
from redis_helper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg= redis_sub.parse_response() #听
    print(msg)