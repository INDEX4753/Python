"""
6-2 字符串比较与切割
"""

# 比较规则：字典序（按照ASCII码）
str1 = 'Python'
str2 = 'C++'
str3 = 'Python3.14'
str4 = 'Java'
str5 = 'python'
str6 = 'JavaScript'

print(str1 > str2)
print(str2 < str3)
print(str1 < str3)
print(str4 == str6)
print(str4 != str6)

# 切割字符串
## split 方法
## str.split(sep = None, maxsplit = -1)
## sep 表示切割标识符，默认空白（空格，制表，换行）
## maxsplit 表示最大切割次数，默认不限次数
str8 = 'It is a book!'
str9 = 'C++##Python##Java##PHP'
ls1 = str8.split()
ls2 = str9.spilt('##')
ls3 = str8.spilt('##', 2)
print(ls1, ls2, ls3)

## splitlines 方法
## str.splitlines(keepends = False)
## keepends 表示是否保留换行符，默认不保留
## keepends=True 时，保留换行符
str = '''人生苦短，
我用Python。'''
ls4 = str.splitlines()
print(ls4)
ls5 = str.splitlines(keepends=True)
print(ls5)