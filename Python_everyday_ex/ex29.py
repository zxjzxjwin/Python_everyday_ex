#coding:utf-8
people = 20
cats = 30
dogs = 15
if people < cats:
	print "Too mant cats! The world is doomed!"
if people > cats:								#False,不显示
	print "Nor mant cats! The world is saved!"	#False,不显示
if people < dogs:								#False,不显示
	print "The world is drooled on!"			#False,不显示
if people > dogs:
	print "The world is dru!"
dogs += 5
if people >= dogs:
	print "People are greater than or equal to dogs."
if people <= dogs:
	print "People are less than or equal to dogs."
if people == dogs:
	print "People are dogs."	

# print True and True#True
# print False and False#False
# print 1 == 1 and 2 == 1#False
# print "test" == "test"#T
# print 1 == 1 or 2 == 1#T
# print True and 1 == 1#T
# print False and 0 != 0#False
# print True or 1 == 1#T
# print "test" == "testing"#False
# print 1 != 0 and 2 == 1#False
# print "test" == "testing"#False
# print "test" == 1#False
# print not (True and False)#T
# print not (1 == 1 and 0 != 1)#False
# print not (10 == 1 or 1000 == 1000)#False
# print not (1 != 10 or 3 == 4)#False
# print not ("testing" == "tseting" and "Zed" == "Cool Guy")#True
# print 1 == 1 and not ("testing" == 1 or 1 == 0)#T
# print "chunky" == "bacon" and not(3 == 4 or 3 == 3)#False
# print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")#False
