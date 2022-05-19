__author__ = 'Administrator'



#装饰器练习

# def login(func):
#     def inner(*args,**kwargs):
#         print ("passed user verification")
#         return func(*args,**kwargs)
#     return inner
#
# def home(name):
#     print ("welcome [%s] to home page"%name)
#
# @login
# def tv(name,passwd):
#     print ("welcome [%s] to tv page[%s]"%(name,passwd))
#     return ('123')
#
# def image(name):
#     print ("welcome [%s] to image page"%name)
#
#
# # tv = login(tv)
# obj = tv('lizexiong','123456')
# print (obj)


def Before(request,kargs):
    print ('Before')

def After(request,kargs):
    print ('After')

def Filter(before_func,after_func):
    def outer(main_func):
        def inner(request,kargs):
            before_func_result = before_func(request,kargs)

            main_func1_result = main_func(request,kargs)       #被装饰的函数

            after_func1_result = after_func(request,kargs)

        return inner

    return outer

@Filter(Before,After)
def Index(name,passwd):
    print (name,passwd)
    print ('index')

Index('lizexiong','123')