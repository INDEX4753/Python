"""
6-5 字符串的其他常用操作
"""

# 复制字符串
## 直接使用赋值运算符即可

# 连接字符串
## 直接使用拼接运算即可'+'
## join 方法
## str.join(ls)
## 把列表中的元素用 str 连接起来
str1 = ' '
list1 = ['I','like','XiaoBai']
str2 = str1.join(list1)
print(str2)

# 获取字符串长度
## len(str) 函数
print(len(str2))

# 判断子串
## 可以直接检索或者使用'in'运算符
print('XiaoBai' in str2)

