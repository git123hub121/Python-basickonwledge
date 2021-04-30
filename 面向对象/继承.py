class SchoolMember:
    '''代表任何学校里的成员。'''
    def	__init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized	SchoolMember: {})'.format(self.name))#自动执行，自动初始化

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age),	end=" ")

class Teacher(SchoolMember):
    '''代表一位老师。'''
    def	__init__(self, name, age, salary):
        SchoolMember.__init__(self,	name, age)
        self.salary	=	salary
        print('(Initialized	Teacher: {})'.format(self.name))

    def	tell(self):
        SchoolMember.tell(self)#子类——教师类调用父类——学校成员类的tell()
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生。'''
    def	__init__(self, name, age, marks):
        SchoolMember.__init__(self,	name, age)
        self.marks	= marks
        print('(Initialized	Student: {})'.format(self.name))

    def	tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
#	打印一行空白行
print()
members	= [t,s]#这样写的目的时符合逻辑，适应我们的思维方式
for	member	in	members:
    #对全体师生工作
    member.tell()
#最后还是用了遍历，这是我想象不到的
print(t)
print(s)
#从这里你就可以看出  <__main__.Teacher object at 0x0000028FE28717B8>并不是你想逃的结果，实际上t只是一个实例化对象，这里返回的是他的类型
t.tell()
s.tell()
#等价于上面的遍历，但是当数据成员庞大时，遍历会更加具有优化性和可修改性以及更加简便优美