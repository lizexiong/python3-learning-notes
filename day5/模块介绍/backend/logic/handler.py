__author__ = 'Administrator'



from backend.db.sql_api import select


def home():
    print ("welcome to home page")
    q_data = select('user')
    print (q_data)

def movie():
    print ("welcome to movie page")

def tv():
    print ("welcome to tv page")