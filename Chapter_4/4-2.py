"""
4-2 元组
"""

# 创建元组
tpl1 = (1, 2, 3)
tpl2 = ()

lst = [4, 5, 6]
tpl3 = tuple(lst)
tpl0 = (0,)
itg = (0)
print(type(tpl0), type(itg))

# 拼接元组
tpl4 = tpl1 + tpl3
print(tpl4)

# 获取最大最小值
max1 = max(tpl4)
min1 = min(tpl4)
print(max1, min1)