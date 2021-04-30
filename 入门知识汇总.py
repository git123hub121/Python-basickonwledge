# #zip
# #导入类
# import os
# import time
# #目标文件路径
# tarfile = 'D:\Code'
# #存储的路径
# sourse = 'D:\Backup'
# #新建文件夹并以时间命名
# today = sourse + os.sep + time.strftime('%Y%m%d')
# #再此新建子文件夹以时间命名
# now = time.strftime('%H%M%S')
# #最终存储路径
# tar = today + os.sep +now + '.zip'
# #判断路径是否存在，如果不存在，则新建
# if not os.path.exists(sourse):
#     os.mkdir(sourse)
# if not os.path.exists(today):
#     os.mkdir(today)
# #打包zip，输出存储路径和目标文件路径
# zip_p = 'zip -r {0} {1}'.format(tar,tarfile)#这句中的tar很是关键
# #调用system实现打包
# print(zip_p)
# os.system(zip_p) == 0
# #尝试不需要print、语句直接实现打包    6.7任务

#with   as 用法 实现写入和读取
# poem1 = '''I love you !
#         and I need you love me.'''
# with open('poem1.txt','w') as f:
#     f.write(poem1)
#     # f.close()#第一种是和with结合使用，主要用于文件的读写操作，省去了关闭文件的麻烦
# with open('poem1.txt') as f:
#     print(f.read())
#     # f.close()

# #input获取的都是字符串，如钥匙其他类型，则需要 类型(input())    如：int(input())
# t = input('what enter it')
# print(t)

#from 模块名 import 方法名
# #也可以写成  from random import randint
# import random
# a = random.randint(5,10)#因为random是模块，而我们调用的是randint()方法来生成随机数，不能直接用模块来调用
# b = random.random()#用来生成0,1之间的浮点数，随机数包括浮点数和整数
# #random()这种写法是错误的！
# print(a)
# print(b)
# from random import randint
# a = randint(5,10)
# print(a)

# a = int(input())
# if a==3:
#     print('y')
# else:
#     if a>3:
#         print('h')
#     else:
#         print('f')
# #上述语句等价于'y' if a==3 else 'h' if a<3 else'f'
# [(lambda a:print('y' if a==3 else 'h' if a<3 else 'f')) (int(input())) for i in range(6)]
## [(lambda a:print('y' if a==3 'h' elif a<3  else 'f')) (int(input())) for i in range(6)]  这一句修改失败
# #(lambda 变量名:print(条件语句)（这里是values 也常用a[values]）_) (类型(input()) for 变量 in range(输入次数))
# #这里的括号起到了语句块的作用 【】  整合语句快   ——纯属本人猜测

# print('I\'m a "good" teacher.')#字符串书写格式，需要    可以用转义字符\    如\n 换行  \t tab  \\ \(表示单斜杠) \ 换行
# print('I\'m a \"good\" teacher.')#在三个引号中，可以直接不需要转义字符来换行
##可以用+将字符串进行拼接

##用%对字符串进行格式化   如 'my age is %d' %age   这里的age可以用整数直接去替代
# print('my age is %d' %18)
# print('my name is %s' %'jacklove')
# print('my grade is %f' %99.5)
# print('the num is %.2f' %3.1415926)
# print('my name is %s and my age is %d.' %('javk',19))
# print('my name is {} and my age is {}.'.format('javk',19))

# #bool
# a = ''#''这是空的
# print(bool(a))
# b = '123'
# if b:
#     print('True')
# #注意，这里的b    如果b不为空  则会自动会识别为布尔值   True    即代表条件成立   b:  默认代表    True
# c = False
# if c == False:
#     print('yes')
# else:
#     print('no')

#打包py文件为exe，是在cmd或者终端里面完成的
#常用两个命令 1.pyinstaller -F -w 文件路径    2.cx_freeze     cxfreeze 打包文件路径 --target-dir dist 目标存放exe文件的文件路径（打包好的文件路径）

#只有函数才有返回值  return

#
# for i in range(1,10):
#     print(i)
# print(list(range(1,10)))
# for i in [1,3,5,7,9]:
#     print(i)

# l = [1,2,3,4]
# print(l[1:-1])
# print(l[:])
# print(l[::1])
# print(l[::-1])

#
# for i in range(3):
#     print(i)#结果是0,1,2

# #字符串的分割成list
# sentence = 'I am a good boy !'
# print(sentence.split())
# #split默认按照空格进行对字符串的分割，分割后的每一段都是一个新的字符串，并最终返回成一个list，这意味着可以用切片和下标去访问
# #也可以按照\n,\t进行分割

# #连接list
# print(' '.join(['abcd','!=','efgh']))
# #jion用来将列表连接成字符串，'' ' ' '\n'等等都是以某种方式来进行连接
#
# #字符串的索引、切片跟list差不多  不同的是字符串不能被修改
# word = 'qwerty'
# for i in word:
#     print(i)
# #i从0开始，可以理解为遍历字符串中的每个字符

# #join也可以对字符串使用,但会连接组成一个新的字符串
# net = '.'.join('qwerty')
# print(net)

#读写文件用with最快了，哈哈，readline()按行读取 read()按字节读取 write同
# #处理一个简单的excel统计分数的功能，先写入，再读取，用with
# grade = '''刘备 23 35 44 47 51
# 关羽 60 77 68
# 张飞 97 99 89 91
# 诸葛亮 100'''
#
# results = []    #定义一个空列表
# with open('grade.txt', 'w', encoding='utf-8') as f:
#     f.write(grade)
#     #f.writelines(grade)
#
# with open('grade.txt', encoding='utf-8') as f:
#     #print(f.read())#数据以字符串方式出现
#     #print(f.readlines())   #将每行数据以字符串的方式通过列表形式出现   ['刘备 23 35 44 47 51\n', '关羽 60 77 68\n', '张飞 97 99 89 91\n', '诸葛亮 100']
#     lines = f.readlines()   #lines为一个列表，因为四行，所以有四个元素（每行看作一个整体）
#     #print(type(lines))
#     for line in lines:  #对每一行进行字符串分割
#         #print(line.split())     #将一个列表变成四个，split将字符串输出成列表   ['刘备', '23', '35', '44', '47', '51']
#         data =line.split()
#         #print(data)
#         #print(data[0])
#         #print(type(data))   #data也是一个list
#         sum = 0
#         grade_list = data[1:]       #通过切片得到一个新的只含有成绩的列表
#         #print(grade_list)          #['23', '35', '44', '47', '51']
#         for score in grade_list:    #这个for是在上个for里面，故有循环嵌套  这里的score是str类型，要进行类型转换
#             sum += int(score)
#         result = '{}\t： {}\n'.format(data[0],sum)    #名字和总分
#         #result = '{}\t：{}\n'.format(data[0:1], sum)
#         #result = '%s\t：%d\n' %(data[0],sum)
#         #print(result)
#         #print(type(result))    #这里得到的是字符串
#         results.append(result)  #将字符串添加到列表中
#     print(results)  #输出最终的列表
#     #print(type(results))    #这里是列表
# with open('results.txt','w',encoding='utf-8') as f:
#     f.writelines(results)

#for循环就是遍历列表中的每一项
#format()用法：格式化 设置参数

# #break
# for i in range(10):
#     a =input()
#     print(a)
#     print(type(a))  #input输出的是字符串哦
#     if a == '0':
#         break

# 异常处理
# try:
#     #with open('poem1.txt') as f:
#     with open('poem.txt') as f:
#         print('file opend!')
#         print(f.read())
# except:
#     print('not exists1')
# print('done')

# results = []
# with open('grade.txt',encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         data = line.split()
#         grade_list = data[1:]
#         sum = 0
#         for score in grade_list:
#             sum += int(score)
#         result = '%s\t : %d\n' %(data[0],sum)
#         results.append(result)
# print(results)

# #遍历列表中的元素，并储存为变量
# a = ['1','2',3,'love']
# b,c,d,e = a
# f =b,c,d,e
# print(f)    #结果是一个元组
# print(b,c,d,e)    #结果是四个字符串

# #random库的使用
# import random
# w = random.randint(1,10)
# r = random.random()
# t = random.choice([1,3,5])
# print(w , r , t)

# #面向对象   继承  比面向过程优化的地方
# #共同属性为速度和距离
# class Che:
#     def __init__(self,speed):
#         self.speed = speed
#     def drive(self,distance):
#         print('need %f hours' %(distance/self.speed))
# class Bick(Che):
#     pass
# class Car(Che):
#     def __init__(self,fuel,speed):
#         Che.__init__(self,speed)#重写父类的方法，对speed进行操作
#         self.fuel =fuel
#     def drive(self,distance):
#         Che.drive(self,distance)
#         print('need %f fuels' %(distance * self.fuel))
# b = Bick(15)
# b.drive(100)
# c = Car(0.12,80)
# c.drive(100)

# class Che:            #2
#     def __init__(self,speed,distance):
#         self.speed = speed
#         self.distance = distance
#     def drive(self):
#         print('need %f hours' %(self.distance/self.speed))
# class Bick(Che):
#     pass
# class Car(Che):
#     def __init__(self,fuel,speed,distance):
#         Che.__init__(self,speed,distance)#重写父类的方法，对speed进行操作
#         self.fuel =fuel #子类特有变量
#     def drive(self):
#         Che.drive(self)
#         print('need %f fuels' %(self.distance * self.fuel))
# b = Bick(15,100)
# b.drive()
# c = Car(0.12,80,100)
# c.drive()

#   True a      False  b    保证a不为假时，才会有该效果  因为  bool and a or b
# a= "me"
# b = "you"
# c = True and a or b
# d = False and a or b
# print(c,d)
# f = ''  #空
# e = (True and [f] or [b])[0]
# g = True and f or b
# print(e,g)

# #元组
# def jisuan(n):
#     return (n/2,n*2)
# #通过元素个数
# x,y = jisuan(50)
# print(x,y)
# #通过索引
# pos = jisuan(60)
# print(pos[0],pos[1])
# #通过遍历
# pos1 =jisuan(70)
# for pos in pos1:
#     print(pos)

# #数学运算
# import  math
# print(math.pi)
# print(math.e)
#
# print(math.ceil(2.5))
# print(math.floor(2.5))
#
# print(math.fabs(-8))
# print(math.sqrt(4))
#
# print(math.pow(8,4))
# print(math.log(100))
# print(math.log(100,10))#第二个参数用来改变基底，默认为e

# #正则表达式
# # []  \b
# import re
# text = 'hi,woshi nide his baHi shyhiY'
# print("\bhi")
# print(r"\bhi")
# print("\\bhi")
# c = re.findall(r"hi",text)  #匹配所有符合条件的，并返回为list
# print(c)
# #   "."    "*"
# “.”在正则表达式中表示除换行符以外的任意字符
# 是“\S”，它表示的是不是空白符的任意字符
# []这个符号。在正则表达式中，[]表示满足括号中任一字符
# “\b”在正则表达式中表示单词的开头或结尾
# 用“?”表示任意一个字符，“*”表示任意数量连续字符，这种被称为通配符。但在正则表达式中，任意字符是用“.”表示，而“*”则不是表示字符，而是表示数量：它表示前面的字符可以重复任意多次（包括0次）

# #计时
# import time
# # time.sleep(n)    #让程序暂停n秒
# print(1)
# time.sleep(2)   #暂停
# print(2)

# #列表解析
# list_1 = [1,2,3,5,8,13,22]
# list_2 = []
# for i in list_1:
#     if i%2 == 0:
#         list_2.append(i)
# print(list_2)
# #上述程序简化
# list_3 = [ i for i in list_1 if i%3 == 0]   #可以这样写
# print(list_3)

# #
# print([i for i in range(1,101) if i%2 == 0 and i%3 == 0 and i%5 == 0]) #输出新的列表
# print(";".join([str(i) for i in range(1,101) if i%2 == 0 and i%3 == 0 and i%5 == 0])) #最终是以分号连接的一个字符串

# #函数参数传递一
# def a(b,c=2):
#     return b+c
# print(a(1,4))

#函数传递二
# def func(x, y=5, *a, **b):
#     print(x, y, a, b)
#
# func(1)
# func(1, 2)
# func(1, 2, 3)
# func(1, 2, 3, 4)
# func(x=1)
# func(x=1, y=1)
# func(x=1, y=1, a=1)
# func(x=1, y=1, a=1, b=1)
# func(1, y=1)
# func(1, 2, 3, 4, a=1)
# func(1, 2, 3, 4, k=1, t=2, o=3)

# #map 是 Python 自带的内置函数，它的作用是把一个函数应用在一个（或多个）序列上，
# # 把列表中的每一项作为函数输入进行计算，再把计算的结果以列表的形式返回
# list1 = [1,2,3,4,5]
# list2 = map(lambda x:x*2,list1)
# print(list2)
# print(list2(list2))
# #这里要转为列表形式，注意
# #map 中的函数会从对应的列表中依次取出元素，作为参数使用，同样将结果以列表的形式返回。所以要注意的是，
# # 函数的参数个数要与 map 中提供的序列组数相同，即函数有几个参数，就得有几组数据。
# #对于每组数据中的元素个数，如果有某组数据少于其他组，map 会以 None 来补全这组参数。

# #map 可以看作是把一个序列根据某种规则，映射到另一个序列。reduce 做的事情就是把一个序列根据某种规则，归纳为一个输出
# #在对于一个序列进行某种统计操作的时候，比如求和，或者诸如统计序列中元素的出现个数等（可尝试下如何用 reduce 做到），可以选择使用 reduce 来实现
# from _functools import reduce
# sum = reduce((lambda  x,y:x+y),range(1,101))
# print(sum)


#字典就是一个 键/值对 的集合
#键值对，键唯一    列表不能作为建，但是可以作为值
#字典也可以用for进行遍历
