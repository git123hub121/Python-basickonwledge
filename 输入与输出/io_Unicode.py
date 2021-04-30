#当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们 的	Unicode	字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”。我们可以在 这一格式下进行读取与写入，只需使用一个简单的关键字参数到我们的标准open函数中：
#encoding-utf-8
import io
f = io.open("abc.txt","wt",encoding="utf-8")\
write(u"Imagine non-English language here")
f.close()
#f = io.open("abc.txt","wt",encoding="utf-8").write(u"Imagine non-English language here")
#这时不需要f.close() 原因还未知！  哈哈！
text = io.open("abc.txt",encoding="utf-8").read()
print(text)
#类似于io_input.py
#希望能够读写其它非英语语言，我们需要使用unicode类型，它全都以字母u开头，例如u"hello world"

