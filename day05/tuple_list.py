list_demo = []
tuple_demo = ()

print(list_demo.__sizeof__())
print(tuple_demo.__sizeof__())

import timeit
print(timeit.timeit(stmt='x=[1,2,3,4,5,6]', number=100000))
print(timeit.timeit(stmt='x=(1,2,3,4,5,6)', number=100000))

# 访问命名元组
from collections import namedtuple
# 把命名元组的类型用一个类存起来
Student = namedtuple("Student", ["name", "age", "sex"])
# 创建对象，并把类型的参数传进来
s = Student("小明", 18, "男")
print(s.name)
print(s.age)
print(s.sex)

# 散列类型
d = {"name": "Robert", "age": "18"}
print("gender".__hash__())
print("gender".__hash__() % 20)
m = 20
entry = [
    ["-609877620", "name", "Robert"],
    [],
    [],
    ["-1996802197", "age", "18"],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# 散列类型优化
id = [
    [0], [], [], [1], []
]
# id列表内，对应有索引值的为hash算法的存储地址


# 三目运算符，即一行代码完成if-else语句，格式为exp1 if condition else exp2
# 如果if条件成立，返回if前边表达式的值；如果if条件不成立，返回else后边表达式的值
b = 11
a = 5 if b > 10 else 3
print(a)

# 推导式简化前
l = []
for i in range(1, 101):
    l.append(i)
print(l)
# 推导式简化后，性能上比l.append()好，append需要扩容
li1 = [i for i in range(1, 101)]
li2 = [i**2 for i in range(1, 101)]
print(li1)
print(li2)

# 把字典中写反了的key和value恢复正常
di = {"18": "age", "小明": "name"}
dic = {}
for k, v in di.items():
    dic[v] = k
print(dic)

# 推导式解决
d = {v: k for k, v in di.items()}
print(d)






