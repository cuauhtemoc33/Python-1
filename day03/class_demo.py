# GuoYa是类，类名必须大写
class GuoYa():
    # name是类变量，需要用类去调用(在类名里，类方法外的都是类变量)
    name = '果芽软件'

    def __init__(self, value):
        # value是实例化变量(在类方法里的是实例化变量)
        self.value = value

    def z(self):
        print("新增")

    def s(self):
        print("删除")

    def g(self):
        print("修改")

    def c(self):
        print("查询")

    # 第一个传参为方法本身
    @classmethod
    def hi(cls):
        print("你好")

    # 静态方法可以不传任何参数
    @staticmethod
    def bye():
        # 但是在静态方法里，无法调用类方法和实例化方法，因为没有变量来接收
        print("再见")


# s1,s2,s3都是类创建的对象,对象可以调用实例化方法
s1 = GuoYa(1)
s1.g()
s2 = GuoYa(2)
s2.g()
s3 = GuoYa(3)
s3.g()

# 类调用类变量
GuoYa.name = '果芽学院'
# 使用类属性
print(GuoYa.name)

# 类调用类方法，第一个传参为方法本身
GuoYa.hi()

# 静态方法可以不传任何参数
GuoYa.bye()
s1.bye()
