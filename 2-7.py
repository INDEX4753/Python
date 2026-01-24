'''
2-7 逻辑语句
'''

# 条件语句
score1 = eval(input())
if score1 < 60:
    print('不及格')
else:
    print('及格')

score2 = int(input())
print('你的成绩是%2d'%(score2))
if score2 < 60:
    print('不及格')
elif score2 < 70:
    print('just so so')
elif score2 < 80:
    print('ok')
elif score2 < 90:
    print('good')
else:
    print('great')

# 循环语句
lst1 = [1, 2, 3, 4, 5]
sum = 0
for k in lst1:
    print(k)
    sum += k
print(sum)
# 类似于C++里面的范围for

student_info1 = {'name':'张三', 'age':19, 'score':{'py':100, 'C++':99}}
for i in student_info1:
    print(k,student_info1[k])
# 同上

begin = 0
end = 8
step = 2
range(begin, end, step)
lst2 = list(range(begin, end, step))
print(lst2)
for i in range(8):
    print(i)
# range(begin, end, step) 序列生成函数

i = 0
sum = 0
n = eval(input())
while i <= n :
    sum +=i
    i+=1
print(sum)
# 条件循环

week = ("MON", "TEU", "WEDN", "THU", "FRI", "SAT", "SUN")
for idx in range(len(week)) :
    print(k, week[k])

# 索引值
# 或者采用下面的函数
for idx, day in enumerate(week) :
    print(idx, day)
for idx, day in enumerate(week, 1) :    # 从 1 开始索引编号
    print(idx, day)

for num in range(2, 101):
    det = int(num**0.5)
    flag = 1
    for i in range(2, det+1):
        if num % i == 0:
            flag = 0 
            break
    if flag:
        print(num, ' ')

for num in range(2, 101):
    det = int(num**0.5)
    for i in range(2, det+1):
        if num % i == 0:
            break
    else:
        print(num)