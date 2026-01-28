"""
4-7 迭代器
"""

# 区分可迭代对象和迭代器
from collections.abc import Iterable, Iterator
lst = [1, 2, 3, 4, 5]
print(isinstance(lst, Iterable))  # 输出: True
print(isinstance(lst, Iterator))  # 输出: False
g = (x**2 for x in range(5))
print(isinstance(g, Iterable))  # 输出: True
print(isinstance(g, Iterator))  # 输出: True

# 使用 iter() 函数将可迭代对象转换为迭代器
it = iter(lst)
print(isinstance(it, Iterator)) # 输出: True

# 使用 next() 函数获取迭代器的下一个值
print(next(it))  # 输出: 1  
print(next(it))  # 输出: 2
print(next(it))  # 输出: 3
## 注意：迭代有范围，如果越界，则会报错

class Faclist:
    def __init__(self):
        self.n = 1  
        self.fac = 1
    def __next__(self):
        self.fac *= self.n
        self.n += 1
        return self.fac
    def __iter__(self):
        return self

if __name__ == '__main__':
    facs = Faclist()
    print(isinstance(facs, Iterator))  # 输出: True
    for _ in range(5):
        print(next(facs), end=' ')  # 输出: 1 2 6 24 120
