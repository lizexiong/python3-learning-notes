#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
pool = redis.ConnectionPool(host='10.0.4.45')
r = redis.Redis(connection_pool=pool)
#r.delete("uv_count")
r.setbit("uv_count",5,1)
r.setbit("uv_count",8,1)
r.setbit("uv_count",3,1)
r.setbit("uv_count",3,1)
r.setbit("uv_count",5,1)
r.setbit("uv_count",15,1)
print("uv count:",r.bitcount("uv_count"))


n ="371"
r.set('t',n)
for i in n:
    print(i,ord(i),bin(ord(i)))

r.setbit("t",4,1)
print("res:",r.get("t"))
'''
r.set("id","3")
#00000011
r.setbit("id",1,bin(1))
print(r.getbit("id",6) )
print(r.get("id"))
#r.setrange("id",3,"AAA")
#print(r.getrange("id", 0,-1))
'''

