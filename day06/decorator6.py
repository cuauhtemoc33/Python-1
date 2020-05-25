# 内层调用逻辑顺序
def fun_a(func):
    def function():
        print("执行装饰器fun_a内层方法")
        res = func()
        return res
    return function

def fun_b(func):
    def function():
        print("执行装饰器fun_b内层方法")
        res = func()
        return res
    return function

def fun_c(func):
    def function():
        print("执行装饰器fun_c内层方法")
        res = func()
        return res
    return function

@fun_a
@fun_b
@fun_c
def fun():
    print("执行fun函数")

fun()