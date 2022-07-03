__author__ = 'Administrator'

import pickle
import json


def login():
    print ("This is wirte login")


f = open('user.txt','wb')

info = {
    'lizexiong':'123',
    'func': login
}


#f.write(pickle.dumps(info))
pickle.dump(info,f)
print (info)
f.close()