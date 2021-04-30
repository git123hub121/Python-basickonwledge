#将注释添加到zip文件命名中
import  os
import time
#1.需要备份的文件与目录将被指定在一个列表中
#例如在	Windows	下：
source	=	['"D:\\My Documents"','D:\\Code']
#注意这里的空格，后面会讲到
#在这里要注意到我们必须在字符串中使用双引号
# #用以括起其中包含空格的名称
#2.备份文件必须存储在一个主备份目录中
target_dir = 'D:\\Backup'
#要记得将这里的目录地址修改至你将使用的路径

#3.备份文件将打包压缩成zip文件
#4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
#将当前时间作为	zip	文件的文件名
now = time.strftime('%H%M%S')

#添加一条来自用户的注释以创建  zip文件的文件名
comment = input('Enter a comment ---> ')#这里是需要自己写备注，评论，从而个性化
#检查是否有评论键入
if len(comment) ==0:
    target = today +os.sep +now + '.zip'
else:
    target = today +os.sep +now + '_' \
             +comment.replace(' ','_') + '.zip'
#这里的逻辑行被分成了两行物理行
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

#仔细观察，我们会发现有一独立的逻辑行被分成了两行物理行，但我们并未指定这两行物理 行应该是一起的。
# 基本上，Python	已经发现了该逻辑行中的加法运算符（+）没有任何操作数，因此它不知道接下来应当如何继续
#1.	    What/做什么（分析）
# 2.	How/怎么做（设计）
# 3.	Do	It/开始做（执行）
# 4.	Test/测试（测试与修复错误）
# 5.	Use/使用（操作或开发）
# 6.	Maintain/维护（改进
#算是完整版了