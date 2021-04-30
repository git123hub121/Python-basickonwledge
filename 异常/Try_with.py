with open("D:\poem.txt") as f:
    for	line in	f:
        print(line,	end='')
    #2,3行等价于 print f.read()

#with open("文件路径","读写方式") as 赋值变量:
    #执行代码块

#   with...as...
#第一种是和with结合使用，主要用于文件的读写操作，省去了关闭文件的麻烦
#第二种    导入模块起别名
#第三种    except结合使用，...as e  将捕获到的异常对象赋值给e     Try_finally.py中有涉及
