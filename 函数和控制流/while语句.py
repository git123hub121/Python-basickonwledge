number = 23
running = True
while running:
    guess = int(input('Enter a integer:     '))
    if guess == number:
        print('yes')
        running = False #这将导致while循环中断
    elif guess < number:
        print('g<n')
    else:
        print('g>n')
print('程序结束')
