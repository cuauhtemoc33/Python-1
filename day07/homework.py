import time
import re


def read_file():
    f = open("a.csv", "r", encoding="utf-8")
    line_head = f.readline()
    lines = f.readlines()
    head_list = line_head.replace("\n", "").split(",")
    for l in lines:
        li = l.replace("\n", "").split(",")
        yield dict(zip(head_list, li))
    f.close()


r = read_file()
print(next(r))
print(next(r))


# 使用列表推导式+join方法把下列字典转成键值对
d = {'name': '袁锋', 'age': '18', 'sex': '男'}
print("&".join("{}={}".format(k, v) for k, v in d.items()))


# 使用字典推导式，把下列列表转成字典
lists = [("name", "yuanfeng"), ("age", 18), ("sex", "male")]
newdict = {k: v for k, v in dict(lists).items()}
print(newdict)


# 递归函数
def s(d):
    if d == 1:
        return 1
    return d+s(d-1)


print(s(100))


# 时间戳
def count_time(func):
    print("时间正在流逝！")

    def swap(*args, **kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return results
    return swap


@count_time
def test():
    time.sleep(2)


test()


# 定义一个用户类，包含用户名、密码、手机号三个属性，无方法
class User:
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__mobile = None

    @property
    def username(self):
        return self.__username

    #  对数据做校验，用正则表达式
    @username.setter
    def username(self, value):
        # 长度6-8位的字母、数字
        r = "^[a-z][A-Z][\d]{6, 8}$"
        if re.match(r, value):
            self.__username = value
        else:
            print("username: 长度6-8位的字母、数字")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # 长度4-10位，必须包含字母和数字
        r = "^(?!\d+$)(?![a-zA-Z]+$)[0-9A-Za-z]{4, 10}$"
        if re.match(r, value):
            self.__password = value
        else:
            print("password: 长度4-10位，必须包含字母和数字")

    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, value):
        # 11位数字
        r = "^[\d]{11}$"
        if re.match(r, value):
            self.__mobile = value
        else:
            print("mobile: 11位数字")


u = User()
u.username = "asdasad"
print(u.username)

u.password = "asd123"
print(u.password)
