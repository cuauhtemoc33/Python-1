# 内置装饰器（不用导包）
class Test():
    __a = 10

    # 装饰器@property，能用方法a直接调用它的一些内置方法
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if isinstance(value, int):
            self.__a = value

    @a.deleter
    def a(self):
        self.__a = None

t = Test()
t.a = 123
print(t.a)
t.a = "asdf"
print(t.a)


