# 显示隐藏字符
a = '1\n'
print(repr(a))

# csv文件取一行(每一列之间用逗号隔开)，字符串切割
aa = "果芽, 测开, 大佬"
print(aa.split(','))

# 推导式
aaa = {"username": "袁锋", "age": "35"}
list1 = []
for k in aaa:
    list1.append(k+'='+aaa[k])
print("&".join(list1))
