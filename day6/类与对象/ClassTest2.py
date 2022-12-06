



'''

class Animal(object):
    def __init__(self,name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)

class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


def func(obj):   #一个接口，多种形态
    obj.talk()

c1 = Cat("朱文静")
d1 = Dog("吴鑫哲")

func(c1)
func(d1)
'''
import sys

'''
#类方法，静态方法代码
class Animal(object):
    def __init__(self,name):
        self.name = name

    hobbie = 'meat'

    @classmethod   #类方法，不能访问实例变量,可以访问类变量
    def talk(self):
        print ("%s is talking..." %self.name)

    # @staticmethod  #不能访问类变量和实例变量，所以连self都不能加了，完全是一个普通的函数
    # def walk():
    #     print ("%s is walking..." )

    @property   #把方法变成属性
    def habit(self):
        print ("%s habit is travel..." %self.name)

w = Animal('wuxinzhe')
w.habit
'''

'''
#私有字段
class C:

    __name = "公有静态字段"

    def func(self):
        print (C.__name)

class D(C):

    def show(self):
        print (C.__name)


C.__name       # 类访问            ==> 错误

obj = C()
obj.func()     # 类内部可以访问     ==> 正确

obj_son = D()
obj_son.show() # 派生类中可以访问   ==> 错误
'''


'''
class D:

    def bar(self):
        print ('D.bar')


class C(D):

    def bar(self):
        print ('C.bar')


class B(D):

    def bar(self):
        print ('B.bar')


class A(B, C):

    def bar(self):
        print ('A.bar')

a = A()
a.bar()
'''

'''
class WebServer(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def start(self):
        print ("Server is starting...")

    def stop(self):
        print("Server is stoping...")

    def restart(self):
        self.stop()
        self.start()

def test_run(name,obj):
    print ("%s Server is %s runing..."%(name,obj.host))


if __name__ == "__main__":
    server = WebServer('localhost',3306)

    delattr(WebServer,'start')
    server.restart()

    # server2.run('wuxinzhe',server2)


    # server2.run('wuxinzhe',server2)
    # if hasattr(server,sys.argv[1]):
    #     func = getattr(server,sys.argv[1])
    #     func()



    # cmd_dic = {
    #     'start': server.start,
    #     'stop': server.stop
    # }
    # if sys.argv[1] in cmd_dic:
    #     cmd_dic[sys.argv[1]]()


# 创建类
class Foo:

    def Bar(self):
        print
        'Bar'

    def Hello(self, name):
        print
        'i am %s' % name

'''












class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self,):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goods()
obj.PRICE         # 获取商品价格
obj.PRICE = 200   # 修改商品原价
del obj.PRICE     # 删除商品原价




















































