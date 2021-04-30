#使用标准库模块
import sys
from 函数 import print_max
print('the command line arguments are:')
for i in sys.argv:
    print(i)
print('the pathonpath is',sys.path,'')
#一般来说，我们要尽量避免使用from...import
 #_name_    if _name_ = '_main_':
 #.py实际上就是个模块，模块可以自己编写
 #dir() 查看模块属性  能够对任何对象工作
 #包 <==> 文件夹    模块 <==> 文件
 

