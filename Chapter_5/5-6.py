"""
5-6 类方法和静态方法
"""

# 类方法是使用@classmethod修饰的方法
# 其第一个参数是类本身
# 也可以使用实例来调用

# 静态方法是指使用@staticmethod修饰的方法
# 静态方法的调用和类方法一样
# 静态方法无类参数，也就是没有第一个参数

class Complex:
    def __init__(self, real = 0, image = 0):
        self.real = real
        self.image = image
    
    def __str__(self):
        return f"{self.real} + {self.image}i"
    
    @classmethod
    def add(cls, c1 ,c2):
        # print(cls)
        c = Complex()
        c.real = c1.real + c2.real
        c.image = c1.image + c2.image
        return c
    
    @staticmethod
    def times(c1, c2):
        c = Complex()
        c.real = c1.real * c2.real - c1.image * c2.image
        c.image = c1.real * c2.image - c1.image * c2.real
        return c
    
if __name__ == '__main__':
    c1 = Complex(1, 2.3)
    c2 = Complex(2.2, 9.3)
    c = Complex.add(c1, c2) # 也可以使用实例来调用，但是一般情况下不推荐
    z = Complex.times(c1, c2)
    print(c, z)
    