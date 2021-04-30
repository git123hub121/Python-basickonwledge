#你可以通过raise语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出（Thrown）异常的对象。
#你能够引发的错误或异常必须是直接或间接从属于 Exception（异常）类的派生类
#	encoding=UTF-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def	__init__(self, length, atleast):
        Exception.__init__(self)
        self.length	= length
        self.atleast = atleast

try:
    text = input('Enter	something	-->	')
    if	len(text) <	3:
        raise ShortInputException(len(text), 3)
    #其他工作能在此处继续正常运行
except EOFError:
    print('Why	did	you	do	an	EOF	on	me?')
except ShortInputException	as	ex:
    print(('ShortInputException:	The	input	was	'	+
           '{0}	long,	expected	at	least	{1}')
          .format(ex.length,ex.atleast))
else:
    print('No	exception	was	raised.')

#如果输入长度<3，则会提示异常，>=3，正常运行
#ctrl+d 出现  第一种情况   EOF
