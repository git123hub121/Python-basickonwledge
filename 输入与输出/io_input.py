#用户输入内容
#利用切片使字符串排序反向
def reverse(text):
    return text[::-1]   #步长为-1 从end往start开始 来对序列进行切片
    #return可返回数值、字符串、列表、表达式、函数以及True、False
#判断是否为回文
def is_palindrome(text):
    return  text == reverse(text)#调用了reverse函数
    #这里的 text == reverse(text) 与  text = reverse(text)是不同的
    #你可以发现浙商text是同一个，== 是表示相等，这里并不存在赋值

something = input("Enter text:")
if is_palindrome(something):
    print("Yes,it is a palindrome")
else:
    print("No, it is not a palindrome")

#原理：我们同样可以提供第三个参数来确定切片的步长（Step）。默认的步长为1,它会返回一份连续的文本。
# 如果给定一个负数步长，如	-1，将返回翻转过的文本

#这里的text是字符串，因为input()函数可以接受一个字符串作为参数
#一定要弄清楚，在函数外的是实参，函数内的是形参    text同名形参所获取的值是相同的
#你可以尝试，当我把第6行右边的text改为test是，你会发现程序报错，因为没用调用reverse(),所以无法获取相应的实参进行操作