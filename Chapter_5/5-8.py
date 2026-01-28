"""
5-8 @property 装饰器的使用
"""

import datetime
class Student:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth  # birth 应该是一个 datetime.date 对象
    # 定义 getter 方法
    @property
    def score(self):
        return self._score 
    # 定义 setter 方法
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("Score must be between 0 and 100")
        self._score = value
    # 定义只读属性 age
    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
    
if __name__ == '__main__':
    stu =  Student('XiaoMing', datetime.date(2000, 5, 15))
    stu.score = 85  # 调用 setter 方法
    print(f"{stu.name}'s score is: {stu.score}")  # 调用 getter 方法
    print(f"{stu.name}'s age is: {stu.age}")  # 访问只读属性 age