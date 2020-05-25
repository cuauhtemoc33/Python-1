# 装饰器嵌套，语法糖执行顺序
def fun_a(func):
    print("装饰器fun_a")
    def function():
        res = func()
        return res
    return function

def fun_b(func):
    print("装饰器fun_b")
    def function():
        res = func()
        return res
    return function

def fun_c(func):
    print("装饰器fun_c")
    def function():
        res = func()
        return res
    return function

@fun_a
@fun_b
@fun_c
def fun():
    print("执行fun函数")


# 注意点：多个语法糖的执行逻辑是从下到上，从内到外
# 而闭包函数的执行顺序是从外到里
# 有调用fun()和没有调用fun()的结果是完全两样的
# 没有调用fun()，则只执行语法糖逻辑，即从下到上，从内到外
