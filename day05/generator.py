# 生成器
def s():
    print("首先")
    yield
    print("最后")


a = s()
next(a)
print("然后")
try:
    next(a)
except:
    pass

