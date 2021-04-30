#创建你自己的命令行 地址簿 程序。在这个程序中，
#你可以添加、修改、删除和搜索你的联系人（朋友、家人和同事等等）
#以及它们的信息（诸如电子邮件地址和/或电话号码）。
#这些详细信息应该被保存下来以便以后提取。
# python version 3.4.3
import pickle as p
import sys
import os

filename = 'phonebook.data'

#创建一个类表示人的信息
class member:
    def __init__(self,name,mail,phone):
        self.name = name
        self.mail = mail
        self.phone = phone

#将对象写入文件中
def writebypickle(infos,filename):
    f = open(filename,'wb')
    p.dump(infos,f)
    f.close()

#从文件中取出对象并返回
def readbypickle(filename):
    f = open(filename,'rb')
    infos = p.load(f)
    f.close()
    return infos

#key in someone,receive the info
def scanall():
    infos = readbypickle(filename)
    for name,info in infos.items():
        print(name,'\t',info)
    del infos
    #infos在这里是对象，用完记得清掉

def search():
    infos = readbypickle(filename)
    person = input('Please enter the name you are search:')
    if person in infos:
        print('Result:',infos[person])
    else:
        print('No data!')
    del infos

def add():
    info = input('Please enter your updating info like:someone,abc@163.com,123: \n')
    info_1 = info.split(',')
    temp = member(info_1[0],info_1[1],info_1[2])
    infos = readbypickle(filename)
    infos[temp.name] = temp.mail + ',' + temp.phone
    writebypickle(infos,filename)
    del infos

# def update():


def delete():
    infos = readbypickle(filename)
    info = input('Please enter the name that you want to delete: ')
    try:
        del infos[info]
    except:
        print('delete failed,please check your input.')
    finally:
        print(infos)
        writebypickle(infos,filename)
        del infos

def main():
    while True:
        command = input('\n==========Menu==========\n1 scan\n2 search\n3 add\n4 delete\n5 update\n6 exit\n')
        if command == '1':
            scanall()
        elif command == '2':
            search()
        elif command == '3':
            add()
        elif command == '4':
            delete()
        elif command == '5':
            update()
        else:
            sys.exit()
print('VersionInfo:',sys.version)
if(os.path.exists(filename)):
    main()
else:
    infos = {'Rebecah':'Rebecah@163.com,12345'}
    writebypickle(infos,filename)
    main()

#缺陷：没有update()