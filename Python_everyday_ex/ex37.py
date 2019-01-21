#coding:utf-8
# 一、  类 class
class Test1(object):							#class [类名](继承):    类名通常是大写开头的单词，继承通用为 object						
#若不需要类带参数，则此处无小括号：若需要类中带参数，则带小括号单里面不写参数名；self表示实力本身，仅在class行里不用手写
	def __init__(self, name):					#__init__ 必须绑定的属性
		self.a = name
		pass
	
	def __enter__(self):
		print "You have enter the %s" % self.a
		return self
												#进入函数必须有返回值，不然相当于后续函数没有了参数
		
#	def __exit__(self):							#如果调用时使用with...as: 格式，则__exit__()函数的小括号里必须写出self以外的其他3个参数；若调用格式为直接和间接调用，则有参数self即可
	def __exit__(self, a, b, c):				#__exit__(self, type, value, trace):	type ---- 异常的类型,value/message ---- 异常的信息或者参数,traceback ---- 包含调用栈信息的对象。
		print "You have exit the %s" % self.a
		pass
		
	def do_something(self):						#同类被定义的函数被称为“方法”，其中变量为 实例变量，相对于 类变量
		print "You have done the %s" % self.a

with Test1("a") as model1:						#这里的 model1 即是”实例（instance)“，是一个变量，将类赋予给实例时要加小括号 ()
	model1.do_something()
	
# model1 = Test1("a")
# print type(model1)
# model1.do_something()
	
	
#例1： 类中无参
class Sample:
  def __enter__(self):
    print "In __enter__()"
    return "Foo"
  
  def __exit__(self, type, value, trace):
    print "In __exit__()"

with Sample() as sample:
  print "sample:", sample, sample == "Foo"
 
#例2： 类中含一个参 name
class WithTest():
  def __init__(self,name):
    self.name = name
    pass
 
  def __enter__(self):
    print "This is enter function"
    return self
 
  def __exit__(self,e_t,e_v,t_b):
    print "Now, you are exit"
 
  def playNow(self):
    print "Now, I am playing"
 
print "**********"
with WithTest("coolboy") as test:
  print type(test)
  test.playNow() 
  print test.name
print "**********"


#二、  set集合
1. 格式： s = set([int, "str", bool])#注意！！！输入为([]),输出为{}
 显示： >>>s
	   {1, 2, 3}	
其中s为集合名，set为集合标签，需要提供一个list作为输入集。【注！】此list不代表输入的格式为列表！只是书写形式
2. 存储规则类似dict，即key必须是不可变对象；但只存储key而不存储value
【注】传入的参数虽然是list，但输出时已经变成集合set格式；
显示的{1, 2, 3}	只代表set内部有这几个元素；显示的顺序也不代表set是有序的
重复元素在set中被自动过滤：
		>>>s = set([1, 2, 2, 3, 1])
		>>>s
		{1, 2, 3}
3. 方法函数：
	3.1  添加元素  set.add(key)#【注】区别于列表的‘追加’函数，集合为无序集故只有‘添加’函数
	3.2  删除元素  set.remove(key)
	
