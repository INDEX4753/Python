"""
5-5 super() 函数的使用
"""

# super([type[, object-or-type]])
# super() 函数用于调用父类(超类)的一个方法。
# 它通常用于子类重写父类的方法后，仍然希望调用父类的方法。

class Person:
    def __init__(self, name):
        print("调用 Person 的构造函数")
        self.name = str(name)
    
    def introduce(self):
        return f"大家好，我是{self.name}。"

class Student(Person):
    def __init__(self, name, student_id):
        print("调用 Student 的构造函数")
        super().__init__(name)  # 调用父类的构造函数
        self.student_id = student_id
    
    def introduce(self):
        parent_intro = super().introduce()  # 调用父类的方法
        return f"{parent_intro} 我是学生，学号是{self.student_id}。"

class Postgraduate(Student):
    def __init__(self, name, student_id, research_topic):
        print("调用 Postgraduate 的构造函数")
        super().__init__(name, student_id)  # 调用父类的构造函数
        self.research_topic = research_topic
    
    def introduce(self):
        parent_intro = super().introduce()  # 调用父类的方法
        # super()可以传参为super(Postgraduate, self)
        return f"{parent_intro} 我的研究课题是{self.research_topic}。"
    
if __name__ == '__main__':
    pg = Postgraduate("张三", "S12345", "人工智能")
    print(pg.introduce())
