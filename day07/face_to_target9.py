class Test:
    # 公有变量，在外部可以直接访问
    attr = 50
    # 私有变量，在外部可以直接访问，但无法修改
    _attr1 = 100
    # 私有变量，在外部不能直接访问，被改名了
    __attr2 = 200


t = Test()
print(t.attr)
print(t._attr1)
print(t._Test__attr2)
