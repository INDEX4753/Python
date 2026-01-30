"""
6-1 字符串基础
"""

# 引号的使用
single_quoted_string = '这是一个单引号字符串'
double_quoted_string = "这是一个双引号字符串"
triple_quoted_string = '''这是一个三引号字符串，可以跨越多行'''
## 双引号和单引号的嵌套
nested_string = "他说：'你好，世界！'"
nested_string_2 = '她回答说："你好！"'
## 三引号的嵌套
nested_triple_string = '''他说："""你好，世界！"""'''
nested_triple_string_2 = """她回答说：'''你好！'''"""
### 使用不一样的引号来尽可能避免转义字符

# 分行书写的注意要点
## 单引号和双引号换行书写需要加续行符\
print('Hello\
      world')
## 单引号和双引号输出换行需要加\n换行
print('Hello world!\n你好，世界！')
## 三引号可以直接输出多段文本
print('''人生苦短，
我用Python。''')
 