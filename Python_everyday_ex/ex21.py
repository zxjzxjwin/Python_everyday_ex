#coding:utf-8
#用=和return将变量设成“一个函数的值”
#定义函数：求和
def add(a, b):#!!!!!!!冒号！！！！！！！！
    print "ADDING %d + %d" % (a, b)
    return a+b
#定义函数：求差
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a-b
#定义函数：求积
def multiply(a, b):
    print "MULTIPLY %d * %d" % (a, b)
    return a*b
#定义函数：求商
def divide(a, b):#######
	print "DIVIDING %d / %d" % (a, b)
	return a/b
#主函数
print "Let's do some math with just functions!"
age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)
#print age, height, weight, iq
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq )
#A puzzle(难题) for the extra credit, type it in anyway.
print "Here is a puzzle."
#多次运算
what = add(age, subtract(height,multiply(weight,divide(iq,2))))
#==
# a = divide(iq, 2)
# b = multiply(weight,a)
# c = subtract(height,b)
# whats = add(age,c)
# print whats
print "That becomes: ", what, "Can you do it by hand?"
#颠倒
how = subtract(divide(subtract(subtract(-4391, age),-height),weight),iq)
print how