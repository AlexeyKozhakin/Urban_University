import os

def divide(first, second):
    return 'Ошибка' if second==0 else first/second

# print(__file__)
# print(__all__)
# print(__path__)
print('fake_math = ',__name__)
if __name__ == 'math_divide.fake_math':
    print('sdflsjaldfjlsajlfjsljfdldskj')

if __name__ == '__main__':
    print('test 10/2=',divide(10,2))
    print('в файле fake_math.py __name__=',__name__)

    # if second == 0:
    #     return 'Ошибка'
    # else:
    #     return first/second



# a = -10

#print(a) if a>=0 else print(-a)
#
# if a>=0:
#     print(a)
# else:
#     print(-a)
