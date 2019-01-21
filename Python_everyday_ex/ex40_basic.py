#coding:utf-8
#40.  模块、类、对象（共性：key:value 格式的数据容器）
#     sys  class  object(instance实例化后的结果
'''
1.  module 模块
 法1
from sys import argv
from os.path import exists
script, filename = argv
print exists(filename)

 法2
import sys
script, filename = sys.argv
with open(filename) as f:
	print f.read()

 自定义
 #this goes in mystuff.py
 def function1():
	print "You are using function1"
#this just a variable in the .py file
target = "xxx"
\\
import mystuff:
	mystuff.function1()#调用函数
	print mystuff.target#调用变量
\\	
from mystuff import function1:
	function1()#调用函数
	print target#调用变量

'''


#三种方法从某个东西里获取它的内容
#dict style
print dict[key]  ->  value
#module style
import module
print module.variable  ->  variable   
module.function(argument)
#class style
instance = class()
print instance.attribute  -> attribute
instance.function(argument)