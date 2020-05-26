# 单例模式，即为一个类创建N个实例，并且每个实例的内存地址都是一样的
class Test(object):
    # 创建一个为空的私有变量__instance
    __instance = None

    # init方法在创建实例时触发
    def __init__(self):
        print("-----init方法-----")

    #  new方法在实例化一个对象时触发
    def __new__(cls, *args, **kwargs):
        print("-----new方法-----")
        if not __class__.__instance:
            __class__.__instance = super().__new__(cls, *args, **kwargs)
        return __class__.__instance


t = Test()
print(t)
