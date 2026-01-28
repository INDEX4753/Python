'''
3-2 函数 2 
'''

## 高阶函数

def FunAdd(f, x, y):
    return f(x) + f(y)  # 将函数作为参数传入

def Square(x):
    return x**2

def Cube(s):
    return s**2

x = eval(input())
y = eval(input())
print(FunAdd(Square, x ,y))
print(FunAdd(Cube, x, y))

## Lambda 函数

k = lambda x, y: x**y   # 匿名函数也可以赋值给变量

print(k(eval(input()), eval(input())))

## 闭包

def outer(x):          # 外部函数（也叫封装函数）
    y = 10             # 外部函数的局部变量
    def inner(z):      # 内部函数（闭包函数）
        nonlocal x, y  # 声明使用外部函数的变量（非必须，但这里显式声明更清晰）
        return z + y + x
    return inner       # 返回内部函数对象，而非执行结果

# 1. 执行 outer(2)，返回 inner 函数对象，赋值给 f
f = outer(2)  
# 此时 outer 函数已经执行完毕，但其内部的 x=2、y=10 并没有被销毁
# f 本质是绑定了 x=2、y=10 的 inner 函数

# 2. 执行 outer(50)，返回新的 inner 函数对象，赋值给 g
g = outer(50)  
# 这里的 g 绑定的是 x=50、y=10 的 inner 函数，和 f 相互独立

# 3. 调用闭包函数
a = f(10)  # 执行 inner(10)，计算 10 + 10 + 2 = 22
b = g(20)  # 执行 inner(20)，计算 20 + 10 + 50 = 80
print(a)   # 输出 22
print(b)   # 输出 80

## 装饰器

# 基于闭包实现的装饰器（核心是增强原函数功能）
import time
def timer_decorator(func):  # 外部函数接收被装饰的函数
    # 闭包的核心：保留外部变量 func
    def wrapper(*args, **kwargs):  
        start = time.time()
        result = func(*args, **kwargs)  # 执行原函数
        end = time.time()
        print(f"函数 {func.__name__} 执行耗时：{end - start:.4f} 秒")
        return result
    return wrapper  # 返回闭包函数

# 使用装饰器增强函数
@timer_decorator  # 语法糖，等价于 add = timer_decorator(add)
def add(a, b):
    time.sleep(0.1)  # 模拟耗时操作
    return a + b

# 调用增强后的函数
print(add(2, 3))  # 输出：函数 add 执行耗时：0.1001 秒 → 5
