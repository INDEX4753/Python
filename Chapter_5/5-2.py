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

#  类中的私有属性
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
    # 也可以通过特殊的语法访问私有属性，但不推荐使用
    print(p._Person__age)  # 不推荐使用这种方式访问私有属性