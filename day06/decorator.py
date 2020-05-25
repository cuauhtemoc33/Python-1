# 装饰器
def fun_a(func):
    return "hello"


# 这个装饰器的意思是，把fun_b作为fun_a方法的参数传参看待
@fun_a
def fun_b():
    pass


print(fun_b)