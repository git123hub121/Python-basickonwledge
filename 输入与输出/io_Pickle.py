import  pickle
#The name of the file where we will store the object
shoplistfile = 'shoplist.data'
#The list of things to buy
shoplist = ['apple','mango','carrot']

#write to the file
f = open(shoplistfile,'wb')
#Dump the object to a file
pickle.dump(shoplist, f)
f.close()

#Destroy the shoplist variable
del shoplist
#虽然删除了该文件中的，但是他已经被写入到了.data文件中
#Read back from the storage
f = open(shoplistfile,'rb')
#Load the object from the file
storedlist = pickle.load(f)
print(storedlist)

#z这里是一个.data文件，需要以二进制的方式写入和读取
#Python	提供了一个叫作 Pickle	 的标准模块，通过它你可以将任何纯 Python 对象存储到一 个文件中，永久保存
# 并在稍后将其取回

#要想将一个对象存储到一个文件中，我们首先需要通过open以写入（write）二进制 （binary）模式打开文件，然后调用pickle	模块的dump函数。这一过程被称作封装 （Pickling）。
#接着，我们通过pickle	模块的load函数接收返回的对象。这个过程被称作拆封（Unpickling）