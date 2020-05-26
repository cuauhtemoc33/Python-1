# 魔术方法
class Test(object):
    # init方法在创建实例时触发
    def __init__(self):
        print("-----init方法-----")

    #  new方法在实例化一个对象时触发
    def __new__(cls, *args, **kwargs):
        print("-----new方法-----")
        return super().__new__(cls, *args, **kwargs)


t = Test()
print(t)

