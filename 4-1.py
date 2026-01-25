"""
4-1 列表
"""

## 创建列表
lst1 = [1, 2, 3, 4, 5]
lst2 = []

lst3 = list(range(1, 6))
lst4 = list((1, 2, 3))
lst5 = list("hello")
print(lst3[1:-1])
# -1是逆序索引，两者可以混用

## 拼接列表
lst6 = lst1 + lst3
print(lst6)
lst7 = lst1 * 3
print(lst7)

## 列表对象赋值原理
lst8 = lst1
lst8[0] = 100
print(lst1)
print(lst8) # lst1和lst8指向同一个列表对象
print(id(lst1), id(lst8))

## 列表对象拷贝
import copy
lst9 = lst1[:]
lst9[0] = 200
print(lst9)
print(lst1) # lst1和lst9指向不同的列表对象
print(id(lst1), id(lst9))
lst10 = lst1.copy()
lst10[0] = 300
print(id(lst1), id(lst10))
# problem: 列表嵌套时，浅拷贝无法完全拷贝对象
lst11 = [[1, 2], [3, 4]]
lst12 = lst11.copy()
lst12[0][0] = 100
print(lst11) # lst11也被修改了
lst13 = copy.deepcopy(lst11)
lst13[0][0] = 200
print(lst11, id(lst11), id(lst11[0])) # lst11未被修改
print(lst13, id(lst13), id(lst13[0]))

## list元素的查找
lst14 = ['a', 'b', 'c', 'd', 'e', 'a']
print(lst14.index('a')) # 返回第一个匹配元素的索引
print(lst14.index('a', 1)) # 从索引1开始查找

## list元素的插入
lst15 = [1, 2, 3]
lst15.append(4) # 在末尾添加元素
print(lst15)
lst15.insert(1, 100) # 在索引1位置插入元素
print(lst15)
lst15.extend([200, 300]) # 在末尾扩展列表
print(lst15)

## list元素的删除
lst16 = [1, 2, 3, 4, 5, 2]
lst16.remove(2) # 删除第一个匹配元素
print(lst16)
elem = lst16.pop() # 删除并返回末尾元素
print(elem, lst16)
elem = lst16.pop(1) # 删除并返回索引1位置的元素
print(elem, lst16)
del lst16[1] # 删除索引1位置的元素
print(lst16)
lst16[1:3] = [] # 删除索引1到2位置的元素
print(lst16)
lst16.clear() # 清空列表
print(lst16)

## list元素的最大值、最小值
lst17 = [5, 2, 9, 1, 7]
print(max(lst17), lst17.index(max(lst17)))
print(min(lst17), lst17.index(min(lst17)))

## list元素的统计，列表长度
lst18 = ['a', 'b', 'a', 'c', 'a', 'd']
print("lst18内容:", lst18)
print("lst18中元素个数:", len(lst18))
print("lst18中a出现的次数:", lst18.count('a'))

## list元素的排序
lst19 = [5, 2, 9, 1, 7]
lst19.sort() # 升序排序，修改原列表
print("升序排序:", lst19)
lst19.sort(reverse=True) # 降序排序，修改原列表
print("降序排序:", lst19)

import ClassStu
stu1 = ClassStu.Student("Alice", 20, "001")
stu2 = ClassStu.Student("Bob", 22, "002")
stu3 = ClassStu.Student("Charlie", 21, "003")
lst20 = [stu1, stu2, stu3]
lst20.sort(key=lambda stu: stu.age) # 按年龄升序排序
print("按年龄升序排序:")
for stu in lst20:
    print(stu.get_details())
lst20.sort(key=lambda stu: stu.name, reverse=True) # 按姓名降序排序
print("按姓名降序排序:")
for stu in lst20:
    print(stu.get_details())

def GetStuID(stu):
    return stu.student_id
lst20.sort(key=GetStuID) # 按学号升序排序
print("按学号升序排序:")
for stu in lst20:
    print(stu.get_details())

