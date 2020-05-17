# 面向对象的逻辑是：我把我的所有公共属性和特征的所有变量和方法封装到一个类里面，如果要用只要实例化这个类就行
class People(object):
    # name = "袁锋"
    # sex = "男"
    # age = "35"

    # 设置初始化方法，调用时方便传值
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def hello(self):
        print("hello")

    def bye(self):
        print("good bye")

    def eat(self):
        print("eat")


people = People("袁锋", "男", "35")
people.hello()
people.bye()
people.eat()


# 类名括号里不填，默认继承object类，object类中自带init方法
# 如果父类里有写init方法，那子类继承父类后必须重写init方法，且必须调用父类的init方法，并传所有父类init方法的参数
class Child(People):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def sing(self):
        print("sing")


child = Child("袁小锋", "男", "18")
child.sing()
child.hello()
child.bye()
child.eat()

