"""
5-7 动态扩展类与实例和__slots__变量的使用
"""

from types import MethodType

class Student0:
    pass

def SetName(self, name):
    self.name = name

def SetID(self, stuID):
    self.stuID = stuID

if __name__ == '__main__':
    stu1 = Student0()
    stu2 = Student0()
    stu1.SetName = MethodType(SetName, stu1)
    # 为 stu1 对象绑定 SetName 方法
    Student0.SetID = SetID
    # 为 Student0 类绑定 SetID 方法
    stu1.SetName('XiaoMing')
    stu1.SetID('S00001')
    # 不可以使用 stu2 调用 SetName 方法
    stu2.SetID('S00002')

#  在定义类时，如果预先定义好允许绑定的属性，就可以节省内存空间
#  并且避免由于拼写错误而引起的属性错误，这时就可以使用 __slots__ 变量
class Person:
    __slots__ = ('name', 'age')  # 用 tuple 定义允许绑定的属性名称, 或者使用括号括起来的单个属性名称
    pass

class Student(Person):
    __slots__ = ('stuID')  # 子类中也可以定义 __slots__ 变量
    pass

class Teacher(Person):
    __slots__ = ('teacherID')  # 子类中也可以定义 __slots__ 变量
    pass

if __name__ == '__main__':
    p = Person()
    p.name = 'XiaoHong'
    p.age = 18
    # p.score = 99  # AttributeError: 'Person' object has no attribute 'score'

    s = Student()
    s.name = 'XiaoMing'
    s.age = 20
    s.stuID = 'S00001'
    # s.address = 'Beijing'  # AttributeError: 'Student' object has no attribute 'address'

    t = Teacher()
    t.name = 'Mr. Wang'
    t.age = 40
    t.teacherID = 'T0001'
    # t.department = 'Math'  # AttributeError: 'Teacher' object has no attribute 'department'
