'''
2-5  Set
'''

set1 = {0, 1, 2}
str1 = "Hello World"
set2 = set(str1)
lst1 = [1, 1, 4, 5, 1, 4]
set3 = set(lst1)
week = ("MON", "TEU", "WEDN", "THU", "FRI", "SAT", "SUN")
set4 = set(week)
print(set1,'\n', set2, '\n', set3,'\n',set4)
# 会将内部的元素进行哈希化处理，便于检索，检索的时间复杂度为o(log(n))
# 集合主要是方便检索以及做交并运算
