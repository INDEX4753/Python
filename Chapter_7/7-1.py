"""
7-1 os模块的基本操作
"""

import os

# 查看系统平台
print(f"当前系统平台: {os.name}")
## win用字符串nt，unix用字符串posix

# 获取当前系统平台的路径分隔符
print(f"当前系统平台的路径分隔符: {os.sep}")
## win用反斜杠\，unix用正斜杠/
## 注意win反斜杠是转义字符，所以在字符串中表示为\\

# 获取当前工作目录
print(f"当前工作目录: {os.getcwd()}")
## 输出当前Python脚本所在目录
# 访问子目录data中的test.bat文件
test_bat_path = os.path.join(os.getcwd(), 'data', 'test.bat')
print(f"test.bat文件路径: {test_bat_path}")

# 获取环境变量
print(f"PATH环境变量: {os.environ['PATH']}")
## 输出系统环境变量PATH的值

# 获取文件和目录列表
print(f"当前目录下的文件和目录列表: {os.listdir()}")
## 输出当前目录下的所有文件和目录名

# 创建目录
new_dir = os.path.join(os.getcwd(), 'new_dir')
os.mkdir(new_dir)
print(f"创建目录: {new_dir}")
## 创建一个新目录new_dir
sub_dir = os.path.join(new_dir, 'new_dir','sub_dir','sub_sub_dir')
os.makedirs(sub_dir)
print(f"创建子目录: {sub_dir}")
## 创建一个新目录new_dir/sub_dir/sub_sub_dir

# 删除目录
## os.rmdir(path)只能删除空目录
## os.removedirs(path)可以删除多级空目录
os.removedirs(sub_dir)
print(f"删除子目录: {sub_dir}")
## 删除目录new_dir/sub_dir/sub_sub_dir
## 异常抛出FileNotFoundError
## 如果目录不存在，会抛出异常
## 如果目录不是空目录，会抛出异常
