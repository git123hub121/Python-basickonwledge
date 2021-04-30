# #函数递归
# #实现阶乘
# def jiecheng(num):
#     if num == 0:
#         return 1
#     else:
#         return num * jiecheng(num-1)
# a = eval(input('请输入一个整数：\n'))   #这里可以不要eval方法
# print('该数的阶乘为： ',jiecheng(abs(int(a))))
#
# #   eval函数就是实现list、dict、tuple与str之间的转化
# #   str函数把list，dict，tuple转为为字符串


# #实现字符串反向
# def zifuchuan(s):
#     if s == "":
#         return s
#     else:
#         return zifuchuan(s[1:]) + s[0]
#         #   return s[0] + zifuchuan(s[1:]) #    计算顺序很重要
# s = input('请输入一个字符串：\n')
# print(zifuchuan(s))

# # #排序 sorted()
# # a = sorted([1,5,3,9,6])
# # print(a)
#
# #有序——元组，列表， 无序——集合，字典
# #有序——可以索引访问，切片,长度  无序不能
# t = (1,2,3,1,(1,2,3),[1,2,3,4])
# print(t)
# s = {1,2,3,1,(5,6,7)}
# # s = {1,2,3,1,(5,6,7),[1,2,3]}
# print(s)
# #没有报错，但是实际没有将第四个元素读取，集合不予许存在相同的元素   元组是不可变数据类型
# #添加一个可变数据类型 列表，就报错了     可变数据类型包括    集合，列表，字典    集合中的元素不能是可变数据类型     unhashable type: 'list'
# #   set()用来生成集合 list()用来生成列表
# s1 = (1,'2',3,4,5)
# print(set(s1))
#
# z = {'zg':1,'c':1}
# print(z)

#   将csv格式转换为HTML

# #   json库
# import json
# dt = {'b':2,'c':4,'d':6}
# s1 = json.dumps(dt)
# s2 = json.dumps(dt,sort_keys=True,indent=4)#编码
# print(s1)
# print(s2)
#
# print(s1==s2)
#
# dt1 = json.loads(s2)#解码
# print(dt1,type(dt1))

