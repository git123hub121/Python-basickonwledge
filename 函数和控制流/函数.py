a = max(2,5)
print(a)
#注意：return语句用于从函数中返回，一定要有函数才能返回
#return max(2,5)    False

#函数通过def来定义
def print_max(a,b):#一般这里空格一行，以保证美观  , b
    if a>b:
        print(a,'is max')
    elif a == b:
        print(a,'is equal to',b)
    else:
        print(b,'is max')
print_max(3,5)
x=6
y=4
print_max(x,y)
print_max(y,x)
#print_max(x=9,y=9) #报错  print_max() got an unexpected keyword argument 'x'
#print_max(y=6,x=3) #报错  print_max() got an unexpected keyword argument 'y'
print_max(x==7,y==9)    #得到     False is equal to False
print_max(a=7,b=9)
print_max(b=2,a=4)

#原因：因为这里的x,y是全局变量，通过以参数的方式传递变量，这里是x,y是实参   从函数外读取x,y的值来赋给形参的a,b
#所以，在x,y给定的情况下，x,y位置可以变换    可以是x=>a,也可以是x=>b
#而print_max(x= ,y= )这是形参了，写在函数内部，也就是看似定义了，其实在代码中无法读取到x,y 所以并没有定义，x与对应的形参a相冲突

#局部变量   Local   全局变量    global
#函数内的局部变量x无法影响主代码块的x
#1
x=50    #全局变量
def func(x):
    print('x is',x)
    x=2  #局部变量
    print('x change is',x)
func(x)
print('x is still',x)   #1
#2
y=60    #全局变量
def func1(y):
    #global y  #将函数中的局部变量变成全局变量     #不知道为啥会报错
    print('y is',y)
    y=2  #局部变量
    print('y change is',y)
func1(y)
print('y have changed of',y)    #2

#默认参数值：放置在最后面
#*param 会被收集为元组     #**param 会被收集为字典
#docstrings     函数名._doc_
