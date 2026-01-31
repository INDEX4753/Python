"""
6-6 占位符和format方法
"""

# 占位符 %xxx 是 Python 中用于字符串格式化的一种方式。它允许你在字符串中插入变量或表达式。
# 常见的占位符包括：
# %s - 字符串 (String)
# %d - 十进制整数 (Decimal Integer)
# %f - 浮点数 (Floating Point)
# %x - 十六进制整数 (Hexadecimal Integer)
# %o - 八进制整数 (Octal Integer)
# %e - 科学计数法表示的浮点数 (Exponential Notation)
# %c - 单个字符 (Character)
# 还可以进行格式化处理
# %.2f - 浮点数保留两位小数
# %5d - 整数占用至少5个字符宽度，右对齐
# %-5d - 整数占用至少5个字符宽度，左对齐
# %05d - 整数占用至少5个字符宽度，前面补零
# %.5e - 科学计数法表示的浮点数，保留5位小数
## 基本用法
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))

# format方法是Python中另一种字符串格式化的方法。它提供了更强大和灵活的方式来插入变量或表达式。
# 基本语法是使用大括号 {} 作为占位符，然后调用字符串的 format 方法，并将变量作为参数传递进去。
# 你可以在大括号中使用索引或关键字参数来指定要插入的变量。
# 还可以进行格式化处理
# 语法格式
# str.format(*args, **kwargs)
## 基本用法
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# 使用索引
print("My name is {0} and I am {1} years old. {0} is learning Python.".format(name, age))
# 使用关键字参数
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
# 格式化处理
pi = 3.141592653589793
print("Pi rounded to 2 decimal places: {:.2f}".format(pi))
## 使用f字符串（Python 3.6及以上版本）
name = "Charlie"
age = 28
print(f"My name is {name} and I am {age} years old.")
## 注：可以访问实参属性