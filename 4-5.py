"""
4-5 切片和列表生成器
"""

# 切片操作
list1 = list(range(10))  # 创建一个包含0到9的列表
print(list1)  # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublst1 = list1[1:7:2]  # 从索引1到6，步长为2
print(sublst1)  # 输出: [1, 3, 5]
sublst2 = list1[:5]  # 从开始到索引4
print(sublst2)  # 输出: [0, 1, 2, 3, 4]
sublst3 = list1[5:]  # 从索引5到结束
print(sublst3)  # 输出: [5, 6, 7, 8, 9]
sublst4 = list1[::-1]  # 反转列表
print(sublst4)  # 输出: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sublst5 = list1[-3:]  # 最后3个元素
print(sublst5)  # 输出: [7, 8, 9]

# 列表生成器
squares = [x**2 for x in range(10)]  # 生成0到9的平方列表
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # 生成0到9中偶数的平方列表
print(even_squares)  # 输出: [0, 4, 16, 36, 64]
nested_list = [(x, y) for x in range(3) for y in range(2)]  # 生成笛卡尔积列表
print(nested_list)  # 输出: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
filtered_list = [x for x in range(20) if x % 3 == 0]  # 生成0到19中能被3整除的数列表
print(filtered_list)  # 输出: [0, 3, 6, 9, 12, 15, 18]