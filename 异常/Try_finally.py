import	sys
import	time

f = None
try:
    #f = open("poem.txt")
    f = open("D:\poem.txt")
    #我们常用的文件阅读风格
    while	True:
        line = f.readline()
        if len(line) ==	0:
            break
        print(line,	end='')
        sys.stdout.flush()
        print("Press ctrl+c	now")
        #为了确保它能运行一段时间
        time.sleep(2)
except	IOError:
    print("Could not find file poem.txt")
except	KeyboardInterrupt:
    print("!! You cancelled	the	reading	from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed	the	file)")

# 我们按照通常文件读取进行操作，但是我们同时通过使用	time.sleep函数任意在每打印一 行后插入两秒休眠，使得程序运行变得缓慢（在通常情况下Python运行得非常快速）。
# 当程 序在处在运行过过程中时，按下	ctrl+c	来中断或取消程序。   可能是输入法的问题
# 你会注意到	KeyboardInterrupt异常被抛出，尔后程序退出。不过，在程序退出之前，finally子句得到执行，文件对象总会被关闭。