"""
5-2 类中的方法
"""

# 类中普通方法的定义和调用
class Student:
    name = 'Unknown'

    def SetName(self, name):   # 定义一个普通方法
        self.name = name    # 给实例添加属性
    
    def PrintName(self):   # 定义一个普通方法
        print("学生的名字是：", self.name)

if __name__ == '__main__':
    stu1 = Student()
    stu2 = Student()
    stu1.SetName("李晓明")
    stu2.SetName("马冬梅")
    stu1.PrintName()
    stu2.PrintName()
    ## 注意：类中普通方法的调用必须通过实例来调用，并且第一个参数必须是self，表示调用该方法的实例本身。不可以使用类名来调用
    # Student.SetName(stu1, "张三")  # 这种调用方式虽然可以，但不推荐

# 类中的私有属性
class Person:
    name = 'UNknown'
    __age = 0   # 私有属性
    def SetInfo(self, name, age):
        self.name = name
        self.__age = age
    def PrintInfo(self):
        print("姓名：", self.name)
        print("年龄：", self.__age)

if __name__ == '__main__':
    p = Person()
    p.SetInfo("张三", 25)
    p.PrintInfo()
    # print(p.__age)  # 直接访问私有属性会报错
    # 私有属性不能在类的外部直接访问，但可以通过类内部的方法间接访问
    # 也可以通过以下语法访问私有属性，但不推荐使用
    print(p._Person__age)  # 不推荐使用这种方式访问私有属性

# 类中的构造方法
class StuScore:
    def __init__(self, name, score = 60):  # 构造方法，初始化属性
        self.name = name
        self.score = score
    def PrintScore(self):
        print(f"{self.name}的成绩是：{self.score}")

if __name__ == '__main__':
    stu1 = StuScore("李四", 85)
    stu2 = StuScore("王五")  # 使用默认成绩60
    stu1.PrintScore()
    stu2.PrintScore()

# 类中的析构方法
class TempFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"创建临时文件：{self.filename}")
    
    def __del__(self):  # 析构方法
        print(f"删除临时文件：{self.filename}")

if __name__ == '__main__':
    temp = TempFile("temp.txt")
    # 当对象被销毁时，析构方法会被自动调用
    del temp  # 手动删除对象，触发析构方法
    temp2 = TempFile("temp2.txt")
    temp3 = temp2
    del temp2  # 删除temp2，不会触发析构方法，因为temp3还引用着该对象
    del temp3  # 现在对象没有引用了，触发析构方法

# 常用的内置方法
## __str__ 方法 用于定义对象的字符串表示 
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

if __name__ == '__main__':
    c = Complex(3, 4)
    print(c)  # 自动调用 __str__ 方法

## 比较运算的内置方法
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other):  # 小于 <
        return self.volume < other.volume

    def __le__(self, other):  # 小于等于 <=
        return self.volume <= other.volume

    def __eq__(self, other):  # 等于 ==
        return self.volume == other.volume
    
    def __ne__(self, other):  # 不等于 !=
        return self.volume != other.volume
    
    def __gt__(self, other):  # 大于 >
        return self.volume > other.volume
    
    def __ge__(self, other):  # 大于等于 >=
        return self.volume >= other.volume
    
if __name__ == '__main__':
    box1 = Box(100)
    box2 = Box(200)
    print("box1 < box2:", box1 < box2)
    print("box1 <= box2:", box1 <= box2)
    print("box1 == box2:", box1 == box2)
    print("box1 != box2:", box1 != box2)
    print("box1 > box2:", box1 > box2)
    print("box1 >= box2:", box1 >= box2)
