#类  方法  self    _init_方法    类变量与对象变量	继承
#1.类
class Person:
    pass  #一个空的代码块
p = Person()    #p相当于一个实例
print(p)
#结果告诉我们我们在Person类的	__main__ 模块中拥有了一个实例
#<__main__.Person object at 0x00000287911FB710>

#2.self 调用类本身   量引用的是对象本身

#3.方法
class Person1:
    def say_hi(self):
        print('Hello,how are you')
p =Person1()
p.say_hi()
#前面两行同样可以写作 Person1().say_hi()
# say_hi 这一方法不需要参数，但是依 旧在函数定义中拥有	self变量

#4._init_方法
#	__init__方法会在类的对象被实例化（Instantiated）时立即运行
#	这一方法可以对任何你想进行操作的目标对象进行初始化（Initialization）操作
class Person2:
    def __init__(self, name):
        self.name = name
    def say(self):
        print('{} love you'.format(self.name))
p = Person2('Jack')
p.say()
#实例化p1
p1 = Person2('Tom')
#p1.__init__('Tom') 会自动，如果调用会报错 找对目标对象即可
p1.say()
#我们可以把self理解为无参变量，所以(self, name)这里只有name一个变量

#类变量与对象变量
#类变量（Class	Variable）是共享的（Shared）——它们可以被属于该类的所有实例访问
#该类变量只拥有一个副本

#对象变量（Object	variable）由类的每一个独立的对象或实例所拥有
# 对象都拥有属于它自己的字段的副本
class Robot:
    """表示有一个带有名字的机器人"""
    #一个类变量，用来计数机器人的数量
    population = 0  #类变量    共享  类变量<==>全局变量

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))    #name   对象变量    局部变量，以对象为基准
        #	当有人被创建时，机器人
        #	将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))
#python中双字符串和单字符串的区别
        # 使用单字符串，若字符串最后一个字符如果也是单引号，则需加一个转义字符\ 做区分
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say(self):
        """来自机器人的诚挚问候
				没问题，你做得到。"""
        print("Greetings, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

d = Robot("ATM")
d.say()
Robot.how_many()   #冒号  :   一定要记得

d1 = Robot("LWX")
d1.say()
Robot.how_many()

print("\nRobots can do some work here. \n")

print("Robots have finished their work,so let's destroy them.")
d.die()
d1.die()

Robot.how_many()
