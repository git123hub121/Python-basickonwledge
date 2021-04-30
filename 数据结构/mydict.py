#数据结构——字典 {}    将键值keys与值values联立起来 注意：键值唯一且不可变
#
ab = {
    'a':'111@qq.com',
    'b':'113@qq.com',
    'c':'115@qq.com',
    'd':'121@qq.com'
}
print("a's address is",ab['a'])

#删除一对键值——值配对
del ab['d']
print('There are {} contacts in the address-book'.format(len(ab)))
for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

#添加一对键值——值配对
ab['e'] = '133@qq.com'

if 'e' in ab:
    print("e's address is", ab['e'])

