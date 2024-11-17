def my_fun_case1(fun):
    #
    def second_fun(x,y):
        res = fun(x,y)
        return res*y**x
    return second_fun

def my_fun_case2(fun):
    #
    def second_fun(x,y):
        res = fun(x,y)
        return res*y**x**2
    return second_fun




@my_fun_case2
def my_fun_base(x,y):
    z = x+y
    return z

# def my_fun_new(x,y):
#     res = my_fun(x,y)
#     return res+x+y





