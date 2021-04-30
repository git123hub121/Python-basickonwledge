#软件的维护  增加了一个子目录

import  os
import time
#1.需要备份的文件与目录将被指定在一个列表中
#例如在	Windows	下：
source	=	['"D:\\My Documents"','D:\\Code']
#注意这里的空格，后面会讲到

#2.备份文件必须存储在一个主备份目录中
target_dir = 'D:\\Backup'
#要记得将这里的目录地址修改至你将使用的路径

#3.备份文件将打包压缩成zip文件
#4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')

#将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')
#zip文件命名格式
target = today +os.sep +now + '.zip'

#如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    #创建目录
#如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

#5.我们使用zip命令将文件打包成	zip格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
#字符串方法join来将列表source转换成字符串

#运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

#原理：利用每天的日期都是不相同的机制实现在主目录的下的子目录每天生成不同日期命名的zip文件
#