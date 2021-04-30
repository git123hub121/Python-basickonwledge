#数据结构——元组   ()  将多个对象保存到一起  不可变
#元组同时也是一个序列，因为也有长度  len()
zoo = ('Python','elephant','penguin')
print('Number of animals in the zoo is ',len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is ',len(new_zoo))

print('All animals in new zoo are',new_zoo)

print('Animals brought from old zoo are',new_zoo[2])

print('Last animal brought from old zoo is',new_zoo[2][2])

print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2])) #3-1+3=5

#包含0或1个项目的元组
ty = ()         #0个项目的元组
ty1 = (2)       #对象
ty2 = (2, )     #1个项目的元组

#利用一个对象来存储另一个对象

