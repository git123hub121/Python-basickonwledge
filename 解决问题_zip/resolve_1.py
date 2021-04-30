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
#4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
             time.strftime('%Y%m%d%H%M%S') + '.zip'
#如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    #创建目录

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