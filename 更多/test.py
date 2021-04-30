# a=5
# b=6
# print(a,b)
# a,b=b,a
# print(a,b)

# flag = False
# if flag:
#     print('it is right!')
# else:
#     print('so regret!')

def t(e):
    return e[1]
r = [(2,2),(1,3),(4,1)]
r.sort(key=t)
print(r)