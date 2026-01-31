"""
6-3 字符串的检索和替换
"""

# 检索字符串
## find 方法和 index 方法
## str.find(sub[, start[, end]])
## str.index(sub[, start[, end]])
## sub 表示要检索的子字符串
## index 方法与 find 方法类似，但找不到子字符串时会引发 ValueError 异常
str1 = 'Hello, welcome to Python programming.'
pos1 = str1.find('Python')
pos2 = str1.index('welcome')
pos3 = str1.find('Java')
print(pos1)  # 输出 18
print(pos2)  # 输出 7
print(pos3)  # 输出 -1

# 替换字符串
## replace 方法
## str.replace(old, new[, count])
## old 表示要被替换的子字符串
## new 表示替换后的子字符串
## count 表示替换的次数，默认替换所有
str2 = str1.replace('Python', 'Java')
str3 = str1.replace('o', '0', 2)
print(str2)  # 输出 'Hello, welcome to Java programming.'
print(str3)  # 输出 'Hell0, welc0me to Python programming.'
