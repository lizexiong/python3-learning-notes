












'''
#类和构造方法演示代码
class Role(object):
    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def buy_weapon(self,weapon):
        #4.所以这里为什么有一个self，并且能调用到self.name，self.weapon，所以说self就是实例本身自己
        print ("%s is buying [%s]" %(self.name,weapon))
        self.weapon = weapon


p1 = Role("lizexiong","Police",'ak47',100)
#1.p1其实就等于Role(p1 = Role("lizexiong","Police",'ak47',100))
#2.p1叫做实例，是role的实例，把一个抽象的类变成一个具体的对象的过程叫实例化,所以p1包含了self.name,self.role,self.weapon等。
#3.所以self是实例本身,谁调用这个类，这个self就是谁，所以p1.buy_weapon。相当于把p1的self.name,self.role等传入到buy_weapon里面了
t1 = Role("wuxinzhe","Terrorist","m60",90)

p1.buy_weapon("an94")   #Role.buy_weapon(p1,"an94") ,p1就是self，self就是自己
t1.buy_weapon("m70")

print (p1.weapon)
print (t1.weapon)


'''


'''
#类变量与实例变量
class Role(object):

    ac = None

    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def buy_weapon(self,weapon):
        print ("%s is buying [%s]" %(self.name,weapon))
        self.weapon = weapon


p1 = Role("lizexiong","Police",'ak47',100)
t1 = Role("wuxinzhe","Terrorist","m60",90)

p1.buy_weapon("an94")
t1.buy_weapon("m70")

p1.ac = "China"
Role.ac = "Janpanese"
Role.weapon = "jiatelin"


print (p1.weapon,p1.ac)
print (t1.weapon,t1.ac)
'''

'''
#类变量与实例变量:类变量的作用
class Role(object):

    members = 0

    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        Role.members+=1

    def buy_weapon(self,weapon):
        print ("%s is buying [%s]" %(self.name,weapon))
        self.weapon = weapon
'''


class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()
    def enroll(self):
        print ("SchoolMember [%s] is enrolled!" %self.name)
    def tell(self):
        print ("Hello my name is %s" %self.name)

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,course,salary):   #1.先重写，在继承
        super(Teacher,self).__init__(name,age,sex)   #2.如果不继承父类的这几个变量，父类的_init_的变量就被覆盖了。就得单独写自己的，这是没有必要的重复代码
        #SchoolMember.__init__(self.name,age.sex) 经典类写法，旧的写法，不再推荐
        self.course = course   #3.这里就是自己的成员属性了，肯定要写
        self.salary = salary

    def teaching(self):
        print ("Teacher [%s] is teaching [%s]" %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        super(Student,self).__init__(name,age,sex)
        self.course = course
        self.tuition = tuition
    def pay_tuition(self):
        print ("student [%s]  paying tution %s" %(self.name,self.tuition))


t1 = Teacher('lizexiong',30,'F',"Py",30000)
t2 = Teacher('wuxxinzhe',40,'F',"Py",10000)

s1 = Student('zhuwenjing',30,'N',"Py","1000")
s2 = Student('qinhaiwei',35,'F',"Py","2000")

t1.tell()
t1.teaching()

s1.tell()
s1.pay_tuition()

