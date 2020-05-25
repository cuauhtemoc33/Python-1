# 三层闭包函数
def fun_a(arg_a):  # 1
    print("调用fun_a方法，收到了装饰器参数arg_a:{}".format(arg_a))  # 2

    # 内层函数接收参数
    def swap(func):  # 5
        print("调用swap方法")  # 6

        def funcfunc(*args, **kwargs):  # 9
            print("调用内层函数swap")  # 10
            func(*args, **kwargs)  # 11
        return funcfunc  # 7
    return swap  # 3


# 语法糖
@fun_a('fun_a')  # 4
def fun_b(arg_b):  # 12
    print(arg_b)  # 13


fun_b("执行fun_b函数")  # 8


# 过程讲解：#1-2为语法糖逻辑，#3-4为调用fun_b逻辑
# 1.调用fun_a('fun_a')方法，返回值为swap，即swap = fun_a('fun_a')
# 2.还会再调用一次@fun_a，把返回值给fun_b，即fun_b = swap(fun_b)
# 3.fun_b("执行fun_b函数") <==> funcfunc("执行fun_b函数")
# 4.func(*args, **kwargs) <==> fun_b(*args, **kwargs)，等于调用原函数fun_b
