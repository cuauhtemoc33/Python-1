class Test:
    attr = "我是类变量"

    def __init__(self):
        self.attr1 = "我是实例变量"

    @classmethod
    def class_mtd(cls):
        print("我是类方法")

    def add_instance(self):
        print("我是实例方法")

    @staticmethod
    def static_mtd():
        print("我是静态方法")


# 用类名去调用类方法时，弹出框中的m为方法，f为属性
# __class__属性为类的type类型的实例，即类对象本身，Test也是对象
print(Test.__class__)
# __dict__属性为字典类型数据，存储了所有的方法和类属性
print(Test.__dict__)
# __doc__属性为类的注释文档，即三引号中的注释内容
print(Test.__doc__)
# __bases__属性为直接父类元组，即父类的继承，object类
print(Test.__bases__)
# 返回的类名字符串
print(Test.__name__)
# 如果不知道对象t里有哪些实例属性和方法，可以用内置函数dir()进行查看
t = Test()
print(dir(t))
# dir()为获取一个对象里的所有属性名和方法名
for i in dir(t):
    # startswith是以什么开头
    if not i.startswith("__"):
        # getattr为获取对象里所有的属性和方法地址
        results = getattr(t, i)
        # callable为判断当前对象是否可调用
        if callable(results):
            results()
        else:
            print(results)


a = "1234"


def aaa():
    pass


# 打印一个变量值
print(a)
# 打印一个方法的方法地址
print(aaa)
