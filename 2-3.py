'''
2-3 列表(List)
'''

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1[1:4]
print(lst1, '\n', lst2)
# 正索引和负索引与String相同
# 同一个List里面可以存储不一样的数据类型

idx = input()
print(lst1[idx], '\n')
print(lst2[0])

# 元素修改
print(lst1, '\n')
lst1[2] = 15
print(lst1)
# 也可以构造列表替换
# 反正替换比较宽松
lst1 = [] # 置空
print(lst1)
lst2[1:3] = [] # 删除1 - 3之间的元素
print(lst2)