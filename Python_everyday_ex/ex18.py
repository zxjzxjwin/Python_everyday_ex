#coding:utf-8
def print_two(*args):#*的作用：让python接收函数的所有的参数,专用于函数；而argv为模组
    arg1, arg2 = args#解包、赋值
    print "arg1: %r, arg2: %r" % (arg1, arg2)#为了演示工作原理，将解包后的每个参数都打印出来
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)#跳过解包过程，直接使用（）里的名称作为变量名
def print_one(arg1):#函数接收单个参数
    print "arg1: %r" % arg1
def print_none():#函数不接收参数
    print "I got nothin"
#调用参数  
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()