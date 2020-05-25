# 把方法fun_b传给方法fun_a中返回的那个swap方法
def fun_a(func):
    # 内层函数接收参数
    def swap(*args, **kwargs):
        print("我被调用了")
        func(*args, **kwargs)
    return swap


@fun_a
def fun_b(name):
    print("hello, {}".format(name))


fun_b("袁锋")


@fun_a
def fun_c(name, age):
    print("hello, {}".format(name))
    print(age)


fun_c("小明", 18)
