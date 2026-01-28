"""
4-6 生成器
"""

grt = (x**2 for x in range(10))
print(type(grt))  # 输出: <class 'generator'>
for val in grt:
    print(val, end=' ')  # 输出: 0 1 4 9 16 25 36 49 64 81

# yield 关键字示例
def faclist(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result  # 使用 yield 生成中间结果

for value in faclist(5):
    print(value, end=' ')  # 输出: 1 2 6 24 120






