
# coding: utf-8

# In[ ]:


#把数据读到程序里——1接受输入；2改变输入；3打印出改变后的输入
'''
print "How old are you?",
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weight?",
weight = raw_input()
'''
print "So,you're %r old, %r tall and %r heavy." % (
    raw_input("How old are you?"),raw_input("How 
    tall are you?"),raw_input("How much do you weight?"
    ))
#结果：So,you're '1' old, '6"2\'' tall and '1' heavy.    注意‘ 前的\


# In[2]:


#用int读取用户输入的数字
print ("Now you are %r tall and %s tall(restriced).") % (raw_input("How tall are you"),int(raw_input("How tall are you?")))


# In[ ]:


# encoding = utf-8
#raw_input    读取用户输入的数字进行计算
a = '请输入两个数字:'#u8
u1 = a.decode('utf-8')#u
g1 = u1.encode('gbk')#gbk
a = int(raw_input(g1))
#a *= int(raw_input(u"我将计算它们之乘积"))
print a
print repr(a)
print repr(u1)
print repr(g1)


# In[ ]:


a = '请输入两个数字:'#u8
u1 = a.decode('utf-8')#u
g1 = u1.encode('gbk')#gbk


# In[ ]:


tips='请输入披萨配料： '
tips+='\n（若输入quit可退出）'
active=True
while active==True:
	message=input(tips)
	if message=='quit':
		active=False
	else:
		print(message)

