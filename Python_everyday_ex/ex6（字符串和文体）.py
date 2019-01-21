#定义x为str
x = "There are %d types of people." % 10
#定义binary为str
binary = "binary"
#定义do_not为str
do_not = "don't"
#定义y为str，用binary 和 do_not表示
y = "There who know %s and those who %s." % (binary, do_not)
print x
print y
#print x + y
#+ 和 , 在输出多个变量时的区别
#print x,
#print y
print "I said: %r." % x#%r会输出变量的原始数据，如输出字符串时会自带单引号''
print "I also said: '%s'." % y
hilarious =False
joke_evaluaion = "Isn't that joke so funny?! %r"
print joke_evaluaion % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w+e








