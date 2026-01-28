"""
5-3 类的继承
"""

# 基本的类继承
class Person:
    def SetName(self, name):
        self.name = str(name)

class Student(Person):
    def SetStudentID(self, student_id):
        self.student_id = student_id
    
    def __str__(self):
        return f"学生姓名：{self.name}, 学号：{self.student_id}"

class Teacher(Person):
    def SetTeacherID(self, teacher_id):
        self.teacher_id = teacher_id

    def __str__(self):
        return f"教师姓名：{self.name}, 教师号：{self.teacher_id}"

class TeachingAssistant(Student, Teacher):
    def SetCourse(self, course):
        self.course = course

    def __str__(self):
        return f"助教姓名：{self.name}, 学号：{self.student_id}, 教师号：{self.teacher_id}, 课程：{self.course}"

if __name__ == '__main__':
    stu = Student()
    stu.SetName("张三")
    stu.SetStudentID("S12345")
    print(stu)

    teacher = Teacher()
    teacher.SetName("李老师")
    teacher.SetTeacherID("T67890")
    print(teacher)

    ta = TeachingAssistant()
    ta.SetName("王助教")
    ta.SetStudentID("S54321")
    ta.SetTeacherID("T09876")
    ta.SetCourse("计算机科学导论")
    print(ta) 