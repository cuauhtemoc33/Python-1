class MyMeta(type):
    def __init__(cls, name, bases=None, dicts=None):
        super().__init__(name, bases, dicts)
        print("init")

    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("call")
        return super().__call__(*args, **kwargs)


class Test(metaclass=MyMeta):
    attr = "我是attr"
    pass


# m = MyMeta("Test", (), dict(Test.__dict__))
# print(m())
print(Test().attr)



