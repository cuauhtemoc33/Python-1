# 变量

# a = 10
# print(a)
# def s():
#     b = 10
#     print(b)
#     b = 20
#     print(b)
#     global a
#     a = 20
#     print(a)
#
# s()
# print(a)

# a = {}
# def s():
#     a["day"] = 40
#
# s()
# print(a)

# b = 10
# def s():
#     c = b
#     c = 40
#     print(c)
#
# s()
# print(b)

# 序列解包，字典只解包key
# a = {"123": "18", "223": 35}
# b, c = a
# print(b, c)

# a = (1, 3, 6, 10, 19)
# b, c, *d = a
# print(b)
# print(c)
# print(d)


# 题目1
a = 1, 3, 2, 5
print(a)

# 题目2
b = 10
def s():
    global b
    b = 40
    print(b)
s()
print(b)

# 题目3
c = 20
d = 20
print(id(c))
print(id(d))