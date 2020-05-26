# 反射调用: 不管方法名叫什么，都可以调用
class Test:
    def add(self):
        '''
        创建
        :return:
        '''
        self.a = 10
        print("创建a的变量")

    def delete(self):
        '''
        删除
        :return:
        '''
        self.a = None
        print("删除a的值")

    def get(self):
        '''
        获取
        :return:
        '''
        print("获取a的值")
        return self.a


t = Test()

for i in dir(t):
    results = getattr(t, i)
    if callable(results):
        if (results.__doc__ and "创建" in results.__doc__):
            results()


