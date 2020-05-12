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

# 字母出现次数
str1 = "&".join(list1)
print(str1.count("a"))

# 查找字符串(查找到的是该字符串的第一次出现的索引值，如果该字符串没有出现过，则索引值为-1)
print(str1.find("m"))

# 左边对齐，右边填充(ljust()，括号里填字符串扩充后的总长度, 用什么字符串填充)
print(len(str1))
print(repr(str1.ljust(30, "p")))
# 左边填充(rjust())，居中center()

# 以什么字符串开头startswith，以什么字符串结尾endswith，输入为布尔类型
print(str1.startswith("u"))
print(str1.startswith("a"))
print(str1.endswith("5"))

# 魔法函数__contains__()，判断括号里的字符串是否被包含
print(str1.__contains__("c"))

# 每个单词的首字母转成大写title()
print(str1.title())
# 大写转小写lower()，小写转大写upper()
print(str1.lower())
print(str1.upper())

# 去空格strip()，去左侧空格lstrip()，去右侧空格rstrip()
print("    321    ".strip())
