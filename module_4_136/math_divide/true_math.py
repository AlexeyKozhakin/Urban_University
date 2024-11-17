from math import inf
def divide(first, second):
    return inf if second==0 else first/second



if __name__ == '__main__':
    print('test=',divide(1,0))
