__author__ = 'Administrator'



import sys,os


Base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(Base)
from config import settings



def db_auth(configs):
    if configs.DATABASE['user'] == 'lizexiong' and configs.DATABASE['password'] == '123':
        print ('db auth passed')
    else:
        print ('db auth error')




def select(table):

    db_auth(settings)

    if table == 'user':
        user_info = {
            '001':['lizexiong']
        }
        return user_info

