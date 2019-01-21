#coding:utf-8
#list  a = ['str',int,bool]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'prnnies', 2, 'dimes', 3, 'quarters']
#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
#we can also build lists, first start with an empty one
elements = []
#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i#追加函数，在列表末未添加新的对象
	elements.append(i)#相当于逐个添加,每次的参数都被命名为i；
#函数结束后，参数的值为最后一次参与函数运算的值；
#局部参数i，在循环开始时被定义，在循环结束时被释放，带不出函数
'''
等价于：
elements = []
elements += range(0, 6)
'''
#now we can print them out too
for i in elements:
	print "Element was: %d" % i