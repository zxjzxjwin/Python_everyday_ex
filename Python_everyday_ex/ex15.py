#coding:utf-8
#使用ex15.py打开ex15_sample.txt
#从代码库sys中取出argv这个模组
from sys import argv
#把argv拆分 赋值给script和filename
script, filename = argv
#打开输入文件名的文件
'''
a = '输入文件名'
a1 = a.decode('utf-8')
b1 = a1.encode('gbk')
filename = raw_input(b1)
'''
txt = open(filename)
#展示输入的文件名
print "Here's your file %r:" % filename
#读取已经打开的文件
print txt.read()
#提示符
print "Type the filename again"
#再次读取文件名
file_again = raw_input(">")
print repr(file_again)
#再次打开输入文件名的文件
txt_again = open(file_again)#输入地址\名字时，不能加引号""；仅当输入方式为argv时可加引号
#再次读取输入文件名的文件
print txt_again.read()
#关闭open后的文件
txt.close();txt_again.close()