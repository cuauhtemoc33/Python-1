# 求1000以内的水仙花数
# for n in range(1, 1001):
#     m = n
#     s = 0
#     while True:
#         a = m % 10
#         s += a ** 3
#         m //= 10
#         if m == 0:
#             break
#     if s == n:
#         print(n)

# 求一个字符串内各字符出现的次数
# s = 'wdqwdadfawqefasdfeweasdfdefeewdfewrfaaqeqefsdfsq'
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#
# print(d)

# 求1000以内的完数(完数是除本身外所有能被其整除的数之和等于本身)
# for n in range(1, 1000):
#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s += i
#     if s == n:
#         print(n)

# 用for循环反向输出字符串
# a = 'qwewejfopfpoporifflfkoqwepqlfldeqwufhdsflkdsfkjuikjfdkjs'
# s = ''
# for i in a:
#     s = i + s
# print(s)

# 过滤列表中的空值
# def filter_list(d):
#     s = []
#     for i in d:
#         if i == '' or not i:
#             pass
#         else:
#             s.append(i)
#     return s
#
# l = filter_list(['', 'hello', None, 'python'])
# print(l)




