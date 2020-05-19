# 迭代器
class StrDemo:
    def __init__(self, s):
        self.s = s
        self.len = len(s)
        self.step = 0

    def __next__(self):
        if self.step >= self.len:
            raise StopIteration("访问越界了")
        else:
            c = self.s[self.step]
            self.step += 1
            return c

    # 调用iter方法后，成为迭代器
    def __iter__(self):
        return self

# 可迭代对象
s = StrDemo("1234567890")
for i in s:
    print(i)
