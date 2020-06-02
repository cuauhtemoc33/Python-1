class Test:
    pass


# 实际在创建对象时，调用的是元类的__call__方法
t = Test()
# t()调用的是__call__方法
t()
# 存到内存
# 1.创建一个type类型的对象
