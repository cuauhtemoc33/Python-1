# 单例模式-2，即为一个类创建N个实例，并且每个实例的内存地址都是一样的
def singleton(func):
    instance = {}

    def swap(*args, **kwargs):
        if len(instance) == 0:
            instance["key"] = func(*args, **kwargs)
        return instance["key"]
    return swap


@singleton
class Test:
    pass


t1 = Test()
print(t1)
t2 = Test()
print(t2)
t3 = Test()
print(t3)
t4 = Test()
print(t4)
