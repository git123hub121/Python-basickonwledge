while True:
    s = input('Enter a integer:     ')
    if s == 'quit':
        break   #退出当前循环
    if len(s) < 3:
        print('too small')
        continue    #跳过下面语句，继续循环
    print('len is',len(s))

print('程序结束')
