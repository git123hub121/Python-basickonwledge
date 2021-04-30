def hi(name):
    #print('my {} is'.format(name))
    return 'my name is ' + name
greet = hi

greey = hi(name='jack')

print(greet)
print(greet(name='tom'))#greet() <==> hi()
print(greey)

print(hi)
print(hi('KID'))

del hi
print(greet)
print(greey)
try:
    print(hi('love'))
    print(hi)
except:
    print('hi未定义，已被删除！')
else:
    print('成功运行')

#理解函数的意义
#a=hi   a=hi() hi()

