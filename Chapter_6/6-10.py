"""
6-10 re模块split()方法、sub()方法和subn()方法
"""

# re.split()方法可以根据正则表达式模式将字符串分割为一个列表。
# 语法格式：re.split(pattern, string, maxsplit=0, flags=0)
# pattern：正则表达式模式
# string：要匹配的字符串
# maxsplit：可选参数，用于指定最大分割次数，默认值为0表示不限制次数
# flags：可选参数，用于指定匹配模式，如re.I表示忽略大小写
import re
result1 = re.split(r'\s+', 'Python is a great language.')
print(result1)  # ['Python', 'is', 'a', 'great', 'language.']

# re.sub()方法可以根据正则表达式模式替换字符串中的匹配项。
# 语法格式：re.sub(pattern, repl, string, count=0, flags=0)
# pattern：正则表达式模式
# repl：替换字符串
# string：要匹配的字符串
# count：可选参数，用于指定替换次数，默认值为0表示替换所有匹配项
# flags：可选参数，用于指定匹配模式，如re.I表示忽略大小写
result2 = re.sub(r'python', 'Java', 'Python is a great language.', re.I)
print(result2)  # Java is a great language.

# re.subn()方法可以根据正则表达式模式替换字符串中的匹配项，返回一个元组，
# 第一个元素为替换后的字符串，第二个元素为替换次数。
# 语法格式：re.subn(pattern, repl, string, count=0, flags=0)
# pattern：正则表达式模式
# repl：替换字符串
# string：要匹配的字符串
# count：可选参数，用于指定替换次数，默认值为0表示替换所有匹配项
# flags：可选参数，用于指定匹配模式，如re.I表示忽略大小写
result3 = re.subn(r'python', 'Java', 'Python is a great language.', re.I)
print(result3)  # ('Java is a great language.', 2)