try:
    text = input('Enter	something	-->	')
except	EOFError:
    print('Why	did	you	do	an	EOF	on	me?')
except	KeyboardInterrupt:
    print('You	cancelled	the	operation.')
else:
    print('You	entered	{}'.format(text))

#Enter	something	-->	^D      Why	did	you	do	an	EOF	on	me?

#ctrl+c 打不出来        尴尬！

