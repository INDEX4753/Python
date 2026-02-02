"""
6-9 re模块findall()方法和finditer()方法
"""

# re.findall()方法可以获取所有匹配的字符串，返回一个列表。
# 语法格式：re.findall(pattern, string, flags=0)
# pattern：正则表达式模式
# string：要匹配的字符串
# flags：可选参数，用于指定匹配模式，如re.I表示忽略大小写
import re
result1 = re.findall(r'python', 'Python is a great language.', re.I)
print(result1)  # ['Python', 'python']

# re.finditer()方法可以获取所有匹配的字符串，返回一个迭代器。
# 语法格式：re.finditer(pattern, string, flags=0)
# pattern：正则表达式模式
# string：要匹配的字符串
# flags：可选参数，用于指定匹配模式，如re.I表示忽略大小写
result2 = re.finditer(r'python', 'Python is a great language.', re.I)
print(result2)  # <callable_iterator object at 0x0000020D00000048>
for item in result2:
    print(item)