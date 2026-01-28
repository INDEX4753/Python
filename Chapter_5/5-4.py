"""
5-4 方法重写和鸭子类型
"""

# 方法重写示例
class Person:
    def __init__(self, name):
        self.name = str(name)
    
    def introduce(self):
        return f"大家好，我是{self.name}。"

class Student(Person):
    def introduce(self):
        return f"大家好，我是学生{self.name}，很高兴认识大家！"

def PrintIntroduction(individual):
    print(individual.introduce())

if __name__ == '__main__':
    person = Person("张三")
    student = Student("李四")
    PrintIntroduction(person)
    PrintIntroduction(student)

# 鸭子类型示例
class Cat:
    def speak(self):
        return "喵喵喵"
class Dog:
    def speak(self):
        return "汪汪汪"

def animal_sound(animal):
    print(animal.speak())

if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    animal_sound(cat)
    animal_sound(dog)

## Python中借助鸭子类型实现多重继承的功能，不需要显式地声明继承自某个类。