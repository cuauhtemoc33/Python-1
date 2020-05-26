class Animal(object):
    def run(self):
        print("共同特性: 都会动")


class Cat(Animal):
    def run(self):
        print("这个是猫")


class Dog(Animal):
    def run(self):
        print("这个是狗")


def func(obj):
    # 弱类型语言需要做类型判断
    if isinstance(obj, Animal):
        obj.run()
    else:
        print("请输入正确的对象")


c = Cat()
d = Dog()
func(c)
func(d)


# 强类型
class Test(Animal):
    pass


t = Test()
func(t)


# 弱类型，没有继承父类，只是写了同样的run方法
class TestDemo():
    def run(self):
        print("test")


func(t)
