# python中所有类的父类是object
class Col(object):
    # 如果父类中重写了init方法，子类里就必须重写init方法，并且调用父类的init方法来实例化，且类的对象创建必须穿init方法中的值
    def __init__(self, name):
        self.name = name
    students = []

    # 父类的方法被重写了，左边会有⚪和向下的箭头
    def teach(self):
        print("IT测开培训")


class Col2():
    def teach(self):
        print("教室")


# GY继承了Col,可以直接调用Col类里的类变量
class GY(Col, Col2):
    # 如果父类中重写了init方法，子类里就必须重写init方法，并且调用父类的init方法来实例化，且类的对象创建必须穿init方法中的值
    def __init__(self, name):
        # 通过super函数，可以在子类中调用父类的方法或属性
        # 多继承中super函数只能调用第一个类方法
        super().__init__(name)

    url = 'stu.guoyasoft.com'
    class_name = ''

    # 重写了父类的方法，左边会有⚪和向上的箭头
    # 通过重写父类的方法实现多态
    def teach(self):
        # 通过super函数，可以在子类中调用父类的方法或属性
        # 多继承中super函数只能调用第一个类方法
        super().teach()
        # 多继承中第2到第n个父类中的同名方法，只能通过类名去调用
        Col2.teach(self)
        print("学前教育")


gy = GY("果芽软件")
GY.name = '果芽软件'
GY.class_name = '2004B'
GY.students = ['老刘', '老袁', '老李', '老薛']
print(GY.students)
print(GY.class_name)
print(GY.name)

Col.teach(123)
gy.teach()