# 对象的生命周期，Test()为对象


class Token():
    __instance = None
    token = {}

    # def __init__(self):
    #     print("对象创建完成")

    # new方法主要实现单例模式，不管实例化多少次，都是取的第一次
    def __new__(cls, *args, **kwargs):
        if Token.__instance is None:
            # print("对象正在被创建")
            # 如果重写了方法，必须调用父类的方法
            Token.__instance = super().__new__(__class__, *args, **kwargs)
        return Token.__instance

    def get_token(self, username):
        return Token.token[username]

    def add_token(self, username, token):
        Token.token[username] = token

    # def __del__(self):
    #     print("对象被销毁了")


# 实例化
t1 = Token()
t1.add_token("yuanfeng", "123123123")
t2 = Token()
print(t2.get_token("yuanfeng"))
# print(id(t1))
# print(id(t2))
'''
__new__:根据对象创建实例(分配资源)，返回一个类的实例
__init__:给新创建的对象，进行初始化操作
__del__:类销毁时，使用
'''
'''
传递公共数据
'''


# 抽象类的设计理念为：所有的事情全部外包出去做，做好了拿回来自己用
# 抽象类的实现
class Test():
    def __init__(self, cursor):
        self.cursor = cursor


import abc


# 继承自元类abc.ABCMeta，并且类中包含抽象方法
class JDBC(metaclass=abc.ABCMeta):
    # 定义抽象类，使用@abc.abstractmethod装饰器可以把类的抽象方法转换成实例方法
    @abc.abstractmethod
    # 数据库连接
    def connect(self):
        pass

    # 获取游标
    def get_cursor(self):
        a = self.connect()
        return a.cursor

    # 查询
    def query(self):
        self.get_cursor()
        return "查询到好多数据"


# 子类继承父类，必须重写类方法
class MySQL(JDBC):
    def connect(self):
        return Test('123')


mysql = MySQL()
# 方法已返回，对象创建完毕后，调用实例化方法写法必须为 print(对象.实例方法)，而不是 对象.实例方法
print(mysql.query())


# 散列存储
# 'abc'这个字符串 -> 通过hash算法 -> 把事先分配好的一块存储空间进行hash算法得出结果的取余
# 例如分配的存储空间为10，hash算法结果为123，则123%10为3，则被存储到索引为3的一块空间内
