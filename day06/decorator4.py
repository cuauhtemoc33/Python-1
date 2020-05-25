def fun_a(arg_a):
    print("调用fun_a方法，收到了装饰器参数arg_a:{}".format(arg_a))

    # 内层函数接收参数
    def swap(func):
        print("调用swap方法")

        def funcfunc(*args, **kwargs):
            print("调用内层函数swap")
            # 给类加装饰器，必须把最里层方法的执行结果返回
            return func(*args, **kwargs)
        return funcfunc
    return swap


@fun_a("执行fun_b函数")
class Test():
    def pnt(self):
         print("我是Test类中的pnt方法")
    pass


t = Test()
t.pnt()
