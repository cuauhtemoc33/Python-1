# 数据读取，打开一个文件
f = open("a.csv", "r", encoding="utf-8")
# 获取表头列表
header_list = f.readline().replace("\n", "").split(",")
# 按行读取文件中所有的剩余数据，并存在一个列表中
lines = f.readlines()
# 存储序列化后的所有数据
data_list = []
for l in lines:
    # 去空格和切片
    line_list = l.replace("\n", "").split(",")
    # 把表头和数据组成一个字典
    d = dict(zip(header_list, line_list))
    # 把字典存入data_list中
    data_list.append(d)
print(data_list)
# 关闭文件
f.close()


# 过滤出列表中所有的偶数
def filters(m):
    return filter(lambda x: x % 2 == 0, m)


print(list(filters([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# 偏函数
from functools import partial
filterses = partial(filter, lambda x: x % 2 == 0)
print(list(filterses([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


def pnt(name, age):
    print("我叫{}，我今年{}岁了".format(name, age))


# 按照位置传参
pnt("袁锋", "18")
# 按照关键字传参
pnt(name="袁锋", age="18")

# 偏函数传参
p = partial(pnt, age="18")
# 位置对应好，传参可用位置传参
p("袁锋")
# 关键字传参无视位置
p(name="袁锋")


# 闭包函数，求某个数的n次方
def sqr(n):
    def swap(num):
        return num ** n
    return swap


sqr_2 = sqr(2)
print(sqr_2(2))

