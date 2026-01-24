'''
2-6 Dictionary(字典)
'''
# 无序的映射集合 键值对 类似于C++里面的set

dict1 = {} # 空字典
dict2 = dict() # 也是空字典
dict3 = {"one":1, "two":2, "three":3}
dict4 = dict(one = 1, two = 2, three = 3)
dict5 = dict(zip(['one','two','three'],[1,2,3]))
dict6 = dict(dict1)
print(dict3)
print(dict4)
print(dict5)
student_info1 = {'name':'张三', 'age':19, 'score':{'py':100, 'C++':99}}
print(student_info1)
print(student_info1['name'])
print(student_info1['score']['py'])
