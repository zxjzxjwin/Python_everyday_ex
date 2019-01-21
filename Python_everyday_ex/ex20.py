#coding:utf-8
from sys import argv
script, input_file = argv#输入操作文件
#定义函数:读取全部内容
def print_all(f):
    print f.read()#,'\n'    手动输入空行
#定义函数2：指针归零
def rewind(f):
    f.seek(0)
#定义函数3：行读取并打印
def print_a_line(line_count, f):#注意，line_count不是函数，只是个名字，提醒要输入的是第几行,完完全全不影响行读取
    print line_count, f.readline(),
#打开操作文件为中间变量
current_file = open(input_file)
print "First let's print the whole file:\n"
#调用函数1，读取中间变量的全部内容
print_all(current_file)
#如果不指针归零，马上再读取一次，则读不出内容（即读空白，输出空白）
#print_all(current_file)
print "Now let's rewind, kind of like a tape."
#调用函数，指针归零
rewind(current_file)
'''
如果不指针归零，则之后的任何读取都读不出来,结果：
Let's print three lines:
1  2  3
'''
print "Let's print three lines:"
#定义变量：行数为第一行
current_line = 1
#调用函数：行读取并打印
# print_a_line(current_line, current_file)
# print_a_line(current_line, current_file)
# print_a_line(current_line, current_file)
# '''
# 1 There are two primary choices in life: to accept conditions as they exist,

# 1 、or accept responsibility for changing them.”——Denis Waitley

# 1 Catch the star that holds your destiny the one that forever twinkles in your h
# eart.
# 说明，反复调用readline()时，指针位置不重置
# '''
print_a_line(current_line, current_file)#如果希望去掉空行，不要再这里加逗号，要在函数中的print指令末尾加逗号
#计数+1，指针位置不变，则输入参数不变
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)