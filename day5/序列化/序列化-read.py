__author__ = 'Administrator'


import pickle
import json


def login():
    print ("This is read login")

f = open('user.txt','rb')

#data_from_write = pickle.loads(f.read())
data_from_write = pickle.load(f)
print (data_from_write)
print ("data_from_write type",type(data_from_write))
data_from_write['func']()

for i in data_from_write:
    print (i)