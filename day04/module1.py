# 多种导入包的方法
import sys
print(sys.argv[0])

import sys as s
print(s.argv[0])

from sys import argv
print(argv[0])

from day04.module2 import sum
print(sum(3, 5))

