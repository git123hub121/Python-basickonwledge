poem = '''\
Programing is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
#打开文件以编辑（'w'riting)
f = open('poem.txt','w')#这个w是写入模式
#向文件中编写文本
f.write(poem)
#关闭文件
f.close()

#如果没有特别指定,将假定启用默认的阅读（'r'ead）模式
f = open('poem.txt') #“阅读文本文件”是默认的，不需要‘r’
while True:
    line = f.readline()#跟java一样，读取到末尾为空字符时，break退出
    #零长度指示 eof
    if len(line) == 0:  #0，-1以及-1...都可以
        break
    #每行的（‘line’）的末尾都已经有了换行符，因为它是从一个文件中进行读取的
    print(line,end='')
#关闭文件
f.close()

#我们使用内置的 open 函数并指定文件名以及我们所希望使用的打开模式来打开一个 文件。
# 打开模式可以是阅读模式（	'r'	），写入模式（'w'	）和追加模式（'a'	）。
# 我们还 可以选择是通过文本模式（'t'）还是二进制模式（'b'）来读取、写入或追加文本。
# 实际 上还有其它更多的模式可用， help(open) 会给你有关它们的更多细节

#在含有转义符的字符串前加‘r’表示字符串内按原始含义解释，不做转义处理
#这对于我们处理路径大有帮助，window默认是\，而\在python中是转义字符，代表换行
#open()可以直接读取路径 如open(r'D:\poem.txt','r')   open('D:/poem.txt')

#额，该bug好像在python3中没有，可以用\   /   都可以
