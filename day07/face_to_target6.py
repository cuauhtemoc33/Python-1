# 上下文管理器
with open("a.csv", "r", encoding="utf-8") as f:
    print(f.readlines())


class Test:
    def __enter__(self):
        pass

    # 1.读取csv文件中抛异常了，会调用__exit__方法。2.读取完csv文件，关闭进程了会调用__exit__方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
