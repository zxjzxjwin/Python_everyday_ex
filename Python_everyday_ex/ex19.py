def cheese_and_crackers(cheese_count, boxes_of_crackers):#two variables
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blankers.\n"
#function:print two variables and print two tips
print "We can just give the function numbers directly:"
#调用函数，参数为20、30
cheese_and_crackers(20,30)
print "OR, we can use variables from our script:"
#对两个变量赋值为整型
#将两个变量作为参数代入函数中
amount_of_cheese = 10
amount_of_crackers = 50
#函数内的参数为局部变量，主函数中的为全局变量，不冲突
#下面将主函数中的变量同名于局部变量，不影响结果
#cheese_count = 10
#boxes_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#在参数的输入上，进行单纯整型的输入
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#在参数的输入上，进行变量和整型的混合输入
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)