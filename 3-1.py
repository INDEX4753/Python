'''
3-1 函数
'''

def CalCirAre(a):
    s = 3.14 * a * a
    return s

def CalRecAre(a ,b):
    s = a * b
    return s

s = CalCirAre(eval(input('请输入圆的半径：')))
print("%.5f" %(s))

a = eval(input('请输入长方形的一边：'))
b = eval(input('请输入长方形的另一边：'))
print('%.5f' %(CalRecAre(a, b)))

def StuInfo(name, nation = 'China', grade = 'good'):    # 默认值参数，即如果不传参，参数为默认值
    print('%s %s %s' %(name, nation, grade))

StuInfo('Liming')
StuInfo('Dawei', 'Amercan', 'common')   # 位置（传）参数
StuInfo('Shanben', grade = 'not pass')  # 关键字（传）参数，不要求参数位置，但是关键字参数必须在后

## 不定长参数

def StudentInfo1(name, *args):  # *args是不定长参数，以元组的方式记录参数，是位置参数
    print('姓名：', name, '，其他：', args)
def StudentInfo2(name, **args): # **args 是不定长参数，以字典的方式记录参数，是关键字参数
    print('姓名：', name, '，其他：', args)
def StudentInfo3(name, *args, country='中国'):  # *args是不定长参数， 如果后面还有参数，必须是关键字参数
    print('姓名：', name, '，国家：', country, '，其他：', args)
StudentInfo1('李晓明', '良好', '中国')
StudentInfo2('李晓明', 中文水平='良好', 国家='中国')    # 关键字传参
StudentInfo3('李晓明', 19, '良好')  # 19, '良好' 均传到了不定长参数
StudentInfo3('大卫', 19, '良好', country='美国')    # country='美国' 以关键字参数的方式传到了 country

## 拆分参数列表

# 其中列表、元组拆分出来的结果作为位置参数，
# 而字典拆分出来的结果作为关键字参数。

# 例：不通过拆分方法传递参数示例

def SumVal(*args): 
    sum=0
    for i in args:
        sum+=i
    print('求和结果为：',sum)

ls=[3,5.2,7,1]
SumVal(ls[0],ls[1],ls[2],ls[3])

# 例：通过拆分方法传递参数示例

def SumVal(*args):     
    sum=0
    for i in args:
        sum+=i
    print('求和结果为：',sum)

ls=[3,5.2,7,1]
SumVal(*ls)

"""---------------------
提示：*ls的作用是把列表ls
中的所有元素拆分出来作为
SumVal的实参，即等价于
SumVal(3, 5.2, 7, 1) 
----------------------"""

## 例：通过return返回字符串、列表、元组等数据

def GetList(): #定义函数GetList
    return [1,2,3] #将包含3个元素的列表返回
def GetTuple(): #定义函数GetTuple
    return (1,2,3) #将包含3个元素的元组返回
def GetElements(): #定义函数GetElements
    return 1,2,3 #返回3个数值数据，实际上会将这3个数据封装成一个元组返回
print(type(GetList()))
print(GetList())
print(type(GetTuple()))
print(GetTuple())
print(type(GetElements()))
print(GetElements())
