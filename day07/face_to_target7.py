# 算术运算函数
class StrDemo:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + str(other)


# __add__触发的时前面那一项
print(StrDemo("1") + 1)

