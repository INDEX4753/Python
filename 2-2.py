'''
2-2 string
'''

str1 = "Hello, World!"
str2 = '你好，世界！'

strnum1 = "123456789"
strnum2 = "335.0336"
a = int(strnum1)
b = int(strnum1, 16)
c = float(strnum2)
print(a, b, c)
'''
转义字符和C/C++里面一样，基于ASCII码
'''

# 子串截取
# str1 = "Hello, World!"
#         0123456789    正索引
# str2 = '你好，世界！'
#             -4-3-2-1  负索引
str3 = str1[1:5]
print(str1, '\n', str3)
str4 = str2[-3:-1]
print(str4, '\n', str2)
char1 = str1[0]
char2 = str1[-1]
print(char1,' ', char2)
