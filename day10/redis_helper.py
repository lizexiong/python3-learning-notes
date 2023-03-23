#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host='10.0.4.45')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm88.7'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub() #打开 收音机
        pub.subscribe(self.chan_sub) #拧到那个台
        pub.parse_response() #准备听
        return pub