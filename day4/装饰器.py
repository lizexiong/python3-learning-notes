__author__ = 'Administrator'



#装饰器练习

def login(func):
    print ("passed user verification")
    return func

def home(name):
    print ("welcome [%s] to home page"%name)

def tv():
    print ("welcome [%s] to tv page")

def image(name):
    print ("welcome [%s] to image page"%name)


tv = login(tv)
tv()

