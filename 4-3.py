"""
4-3 集合
"""

# 集合的创建

set1 = set([1, 1, 4, 5, 1, 4])
print(set1)
set2 = set([])

# 元素插入

## s.add(x)  将元素x插入集合s中  其中 x 不能是可变类型
set2.add(6)
## s.update(xs)  将可迭代对象xs中的每个元素插入集合s中
set2.update([7, 8, 9])

languages = set(["Python", "Java", "C++"])
languages.update(["C#", "Go", "JavaScript"])
print(set2)
print(languages)

alphabets = set()
alphabets.update("abcde")
print(alphabets)

# 集合的运算
A = set([1, 2, 3, 4, 5])
B = set([4, 5, 6, 7, 8])
## 交集
C = A & B # C = A.intersection(B)
print(C)
## 并集
D = A | B # D = A.union(B)
print(D)
## 差集
E = A - B # E = A.difference(B)
print(E)
## 对称差集
F = A ^ B # F = A.symmetric_difference(B)
print(F)
## 子集
print(A.issubset(D))
## 超集
print(D.issuperset(B))
## 无交集
G = set([9, 10])
print(A.isdisjoint(G))

# 集合元素个数
print(len(A))

# 删除集合中的元素
A.remove(1)
print(A)
A.discard(10)  # 删除元素10，如果元素不存在也不会报错
print(A)

# 清空集合
A.clear()
print(A)
print(len(A))

# 集合的遍历
for lang in languages:
    print(lang)

# 集合推导式
squares = {x**2 for x in range(10)}
print(squares)