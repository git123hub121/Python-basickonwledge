#交换两个数的最快方法
a=6;b=5
a,b = b,a
print(a,b)

#特殊方法
# __init__(self, ...)这一方法在新创建的对象被返回准备使用时被调用
# __str__(self)当我们使用print函数时，或str()被使用时就会被调用
# __getitem__(self, key)使用	x[key]	索引操作时会被调用
# __len__(self)当针对序列对象使用内置len()函数时会被调用

#单语句块
flag = True
if flag: print('Yes')

#Lambda	表格
# lambda 需要一个参数，后跟一个表达式作为函数体，这一表达式执行的值将作为这个新函数的返回值
points = [{'x':2,'y':3},{'x':4,'y':1}]
points.sort(key=lambda i:i['y'])
print(points)

def t(e):
    return e[1]
r = [(2,2),(1,3),(4,1)]
r.sort(key=t)
print(r)

r1 = [(2,2),(1,3),(4,1)]
r1.sort(key=lambda x:x[0])
print(r1)

#列表推导
listone = [2,3,4]
listtwo = [2*i for i in listone if i>2]
print(listtwo)

#在函数中接收元组与字典
def sum(power,*args):
    total = 0
    for i in args:
        total += pow(i,power)
    return  total
p =sum(2,3,4)
print(p)

#	assert语句
mylist = ['item']
assert len(mylist) >= 1
# print(mylist.pop())
mylist.pop()
assert len(mylist) >= 1

