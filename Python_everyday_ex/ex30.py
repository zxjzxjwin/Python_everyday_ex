#coding:utf-8
people = 30								#定义变量
cars = 10								#定义变量
buses = 100								#定义变量
if cars > people:						#car大于people
	print "We should take the cars."	
elif cars < people:#中间的用elif 最后的用else	#car小于people					
	print "We shoule not take the cars."
else:									#cars等于people
	print "We can't decide."
if buses > cars:						#bus大于car
	print "That's too many buses."
elif buses < cars:						#bus小于car
	print "Maybe wo could take the buses."
else:									#bus等于car
		print "We still can't decide."
if people > buses:						#people大于bus
	print "Alright,let's just take the buses."
else:									#people小于等于bus
		print "Fine, let's stay home then."
# if people > buses or people == buses:	#people大于等于bus
# if people >= buses:						#people大于等于bus
