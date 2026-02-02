"""
6-7 正则表达式与 re 模块
"""

# 正则表达式是一种用于匹配字符串模式的强大工具。它由普通字符（例如字母和数字）和特殊字符（称为元字符）组成。
# 特殊字符具有特殊的含义，用于定义匹配的模式。
# 以下是一些常用的正则表达式元字符：

## . - 匹配任意单个字符（除了换行符）
## ^ - 匹配字符串的开头
## $ - 匹配字符串的结尾
## * - 匹配 preceding 字符的零次或多次出现
## + - 匹配 preceding 字符的一次或多次出现
## ? - 匹配 preceding 字符的零次或一次出现
## {n} - 匹配 preceding 字符恰好 n 次
## {n,} - 匹配 preceding 字符至少 n 次
## {n,m} - 匹配 preceding 字符至少 n 次，至多 m 次
## [] - 匹配方括号中的任意一个字符
## [^] - 匹配不在方括号中的任意一个字符
## | - 匹配左右任意一个表达式
## () - 分组，将多个字符作为一个单元进行匹配
## \ - 转义字符，用于匹配特殊字符本身
## \d - 匹配任意一个数字字符（0-9）
## \D - 匹配任意一个非数字字符
## \w - 匹配任意一个字母、数字或下划线字符
## \W - 匹配任意一个非字母、数字或下划线字符
## \s - 匹配任意一个空白字符（空格、制表符、换行符等）
## \S - 匹配任意一个非空白字符
## \b - 匹配单词边界
## \B - 匹配非单词边界
## \A - 匹配字符串的开头（与 ^ 相同）
## \Z - 匹配字符串的结尾（与 $ 相同）
## \z - 匹配字符串的结尾（与 $ 相同）
## \n - 匹配换行符
## \r - 匹配回车符
## \t - 匹配制表符
## \f - 匹配换页符

# 以上只是正则表达式的基础语法，实际应用中还可以使用更复杂的模式来匹配字符串。
# 正则表达式在文本处理、数据提取、验证等方面都有广泛的应用。
# 我们通常在正则表达式字符串前面加上 r 或 R 前缀，以表示原始字符串。
# 例如，r"\d+" 表示匹配一个或多个数字字符。
# 通过这种方式可以减少对特殊字符的转义。

# re 模块使用和compile，match方法

## compile方法
# compile 方法用于将正则表达式模式编译为一个正则表达式对象，以便后续的匹配操作。
# 它的语法如下：
# re.compile(pattern, flags=0)
# 其中，pattern 是要编译的正则表达式模式，flags 是可选的标志参数，用于指定匹配的行为。
# 例如，re.compile(r"\d+") 编译了一个匹配一个或多个数字字符的正则表达式对象。
# flags 参数用于指定匹配的行为，常用的标志包括：
# re.IGNORECASE（或 re.I） - 忽略大小写进行匹配
# re.MULTILINE（或 re.M） - 多行模式，^ 和 $ 匹配每一行的开头和结尾
# re.DOTALL（或 re.S） - 点号匹配任意字符，包括换行符
# re.VERBOSE（或 re.X） -  verbose 模式，允许在正则表达式中添加注释和空格
# 例如，re.compile(r"\d+", re.IGNORECASE) 编译了一个忽略大小写匹配一个或多个数字字符的正则表达式对象。

## match方法
# match 方法用于从字符串的开头开始匹配正则表达式模式。
# 它的语法如下：
# re.match(pattern, string, flags=0)
# 其中，pattern 是要匹配的正则表达式模式，string 是要匹配的字符串，flags 是可选的标志参数，用于指定匹配的行为。
# 例如，re.match(r"\d+", "123abc") 匹配了字符串 "123abc" 中的 "123"。
# 如果匹配成功，match 方法返回一个匹配对象；如果匹配失败，返回 None。
# 你可以使用匹配对象的方法来获取匹配的结果，例如 group() 方法用于获取匹配的字符串。

import re
str1 = 'Python is a great language.'
result1 = re.match(r'Python', str1, re.I)
print(result1)
print(result1.group())
result2 = re.match(r'python', str1, re.I)
print(result2)
print(result2.group())
str2 = """I like Python.
Python is a great language.
"""
result3 = re.match(r'Python', str2, re.I|re.M)
print(result3)
print(result3.group())
# 即使在多行模式下，match 方法也只能从字符串的开头开始匹配。
# 如果要在多行字符串中匹配多个模式，需要使用 findall 方法或 search 方法。

# 除了直接调用re模块的match方法，还可以使用compile方法编译正则表达式模式，
# 然后调用编译后的正则表达式对象的match方法进行匹配。
# 例如，result3 = re.compile(r'Python', re.I|re.M).match(str2) 也可以实现与 result3 相同的匹配结果。
pattern = re.compile(r'Python', re.I|re.M)
result4 = pattern.match(str2)
print(result4)
print(result4.group())
result5 = pattern.match(str2, pos=10)
print(result5)
print(result5.group())

# 使用compile方法编译正则表达式模式后，
# 可以多次调用match方法进行匹配，而不需要每次都编译正则表达式模式。
# 这在需要多次匹配相同模式的情况下可以提高效率。

## search方法
# search 方法用于在字符串中搜索正则表达式模式的第一个匹配项。
# 它的语法如下：
# re.search(pattern, string, flags=0)
# 其中，pattern 是要搜索的正则表达式模式，string 是要搜索的字符串，flags 是可选的标志参数，用于指定搜索的行为。
# 例如，re.search(r"\d+", "abc123def") 搜索了字符串 "abc123def" 中的 "123"。
# 如果搜索成功，search 方法返回一个匹配对象；如果搜索失败，返回 None。
# 你可以使用匹配对象的方法来获取匹配的结果，例如 group() 方法用于获取匹配的字符串。

import re
str1 = 'Python is a great language.'
str2 = 'I like Python.'
result1 = re.search(r'Python', str1, re.I)
print(result1)
print(result1.group())
result2 = re.search(r'python', str1, re.I)
print(result2)
print(result2.group())
result3 = re.search(r'python', str2, re.I)
print(result3)
print(result3.group())