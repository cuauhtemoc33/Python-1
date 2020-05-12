# 序列切片操作
# sname[start:end:step]，sname[start:end]遵循左闭右开区间
a = 'abcdefg'
print(a[-2:0:-1])

# 序列相加
print("果芽"+"测开"+"学院")
# 序列相乘
abc = '果芽测开学院'
print(abc*3)
# 序列断言
print('果芽' in abc)
aaa = '1234567'
# str转字符串是整体转成一个字符串
print(str(aaa))
# repr转字符串是整体转成一个字符串，并显示隐藏的符号
print(repr(aaa))
# list转列表是列表中每一个都转成字符串
print(list(aaa))
# 以下两种显示方式一样
print(sorted(aaa, reverse=True))
print(list(aaa[::-1]))