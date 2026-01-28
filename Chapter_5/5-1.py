"""
5-1 类的定义和创建实例及添加属性
"""

# 类的定义

## 定义一个空类
class Student0:
    pass    # 一个空语句，占位，表示无属性和方法

class Student1:
    name = 'Unknown'

if __name__ == '__main__':
    stu1 = Student0() # 创建一个实例
    print(stu1, type(stu1))

    print(Student1.name)
    stu2 = Student1()
    print(stu2.name)
    Student1.name = "未知"  # 更改类属性
    print(stu2.name)    # 随之改变
    stu2.name = "李明"
    print(stu2.name)
    Student1.name = "学生"
    print(Student1.name)
    print(stu2.name)    # 实例中的属性被初始化之后就不会随类属性的改变而改变了

    stu1.age = 20  # 动态给实例添加属性
    print(stu1.age)
    ## 注意，给实例添加新属性并不会给其他实例或类添加该属性

