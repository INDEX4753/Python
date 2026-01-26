"""
4-4 字典
"""

# 初始化一个字典
# d.fromkeys(seq[, value])
stu1 = dict.fromkeys(['name', 'age', 'gender'], 'unknown')
print(stu1)  # 输出: {'name': 'unknown', 'age': 'unknown', 'gender': 'unknown'}

# 访问字典中的值
print(stu1['name'])  # 输出: unknown
print(stu1.get('age'))  # 输出: unknown
print(stu1.get('height', 'not found'))  # 输出: not found

# 修改字典中的值
stu2 = {'name': 'Alice', 'age': 20}
stu2['age'] = 21
print(stu2)  # 输出: {'name': 'Alice', 'age': 21}
stu2.update({'gender': 'female'})

# 删除字典中的元素
stu3 = dict(stuID = '181011', name = 'LiMing', age = 19)

del stu3['age']
del stu3['name']
stuID = stu3.pop('stuID')
print(stu3)
major = stu3.pop('major', 'not found')

# 字典的深拷贝和浅拷贝
import copy 
stu4 = stu2 # 指向同一个字典对象
stu4.update({'score': {'Python': 95, 'C++': 90, 'Java': 85}})
stu5 = stu2.copy() # 是浅拷贝
print(id(stu2), id(stu4), id(stu5))
stu4['score']['Python'] = 100
print(stu2)  # stu2和stu4的'score'都会被修改
print(id(stu5['score']), id(stu2['score'])) # 地址一样，也会被同时修改，不具有独立性
## 问题： 为什么stu5的'score'地址和stu2的一样呢？因为stu5是浅拷贝，拷贝的是引用地址，并没有创建新的'score'字典对象
stu6 = copy.deepcopy(stu2) # 是深拷贝
stu6['score']['C++'] = 98
print(stu6, id(stu6), id(stu6['score'])) # 地址不一样，具有独立性

# 判断字典中是否存在某个键
stu7 = {'name': 'ZhangSan', 'age': 22}
print('name' in stu7)  # 输出: True
print(stu7.get('gender', 'not found'))  # 输出: not found

# 拼接字典
stu8 = {'city': 'Beijing', 'country': 'China'}
stu9 = {**stu7, **stu8}  # 使用字典解包
stu10 = stu7.copy()
stu10.update(stu8)  # 使用update方法
stu11 = dict(stu7, **stu8)  # 使用dict()函数

# 字典长度
dic = {'a': 1, 'b': 2, 'c': 3}
print(len(dic))  # 输出: 3

# 清除字典
dic.clear()
print(dic)  # 输出: {}

# 获取键集合
dic2 = {'x': 10, 'y': 20, 'z': 30}
keys = dic2.keys()
print(keys)  # 输出: dict_keys(['x', 'y', 'z'])

# 获取值集合
values = dic2.values()
print(values)  # 输出: dict_values([10, 20, 30])