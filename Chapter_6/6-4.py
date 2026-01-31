"""
6-4 去除字符串空白字符和大小写转换
"""

# 去除字符串空白字符
## strip 方法
## str.strip(chars = None)
## str.lstrip(chars = None)
## str.rstrip(chars = None)
## chars 表示要去除的字符，默认去除空白字符（空格，制表，换行）
## replace(' ', '') 效果类似，但 strip 方法只去除字符串开头和结尾的空白字符
str1 = '   Hello, Python!   \n'
str2 = '\t\tHello, Python!\t\t'
str3 = '---Hello, Python!---'
cleaned_str1 = str1.strip()
cleaned_str2 = str2.lstrip()
cleaned_str3 = str3.rstrip('-')
print(f"'{cleaned_str1}'")
print(f"'{cleaned_str2}'")
print(f"'{cleaned_str3}'")

# 大小写转换
## capitalize 方法
## 将字符串的第一个字母大写
## lower 方法
## 将字符串的所有字母小写
## upper 方法
## 将字符串的所有字母都大写
## swapcase 方法
## 大写转小写，小写转大写
str4 = 'hello, world!'
str5 = str4.capitalize()
str6 = str5.lower()
str7 = str5.upper()
str8 = str5.swapcase()
print(str5, str6, str7, str8)
