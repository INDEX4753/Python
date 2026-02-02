"""
6-8 re模块匹配对象
"""

# 使用前面介绍的match方法和search方法，
# 可以获取到匹配（Match）对象。匹配对象包含了匹配的结果以及其他相关信息。匹配失败时则返回None。

import re
result1 = re.search(r'python', 'Python is a great language.', re.I)
print(result1)
if result1: 
    print(result1)  # 匹配成功时返回匹配对象

    # 匹配对象的group()方法可以获取匹配的字符串。
    print(result1.group())  # 获取匹配的字符串
    # group()方法可以获取匹配的字符串，
    # 也可以指定分组编号获取分组匹配的字符串。
    print(result1.group(0))  # 获取匹配的字符串
    # 分组匹配的字符串可以通过group(1)、group(2)等方法获取。
    print(result1.group(1))  # 获取第一个分组匹配的字符串
    # 如果正则表达式中没有分组，
    # 则group(1)等方法会抛出IndexError异常。
    # 可以使用groups()方法获取所有分组匹配的字符串。
    print(result1.groups())  # 获取所有分组匹配的字符串 （没有分组时为空元组）

    # 匹配对象的start()方法可以获取匹配的起始位置。
    print(result1.start())  # 获取匹配的起始位置

    # 匹配对象的end()方法可以获取匹配的结束位置。
    print(result1.end())    # 获取匹配的结束位置

    # 匹配对象的span()方法可以获取匹配的起始位置和结束位置。    
    print(result1.span())   # 获取匹配的起始位置和结束位置
else:
    print('匹配失败')