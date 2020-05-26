class Test:
    def __call__(self):
        print("hello")
    pass


t = Test()
# __call__魔法函数即可以使对象调用自身，当成方法来用
t()



