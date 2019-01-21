
# coding: utf-8

# In[16]:


#字符串扩展至多行
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
#exact
#转义字符组合格式化字符串
print "111,\n%s" % tabby_cat
#%r 搭配单引号和双引号转义字符打印；和%s比较
print "222,\t%s" % persian_cat
print "222,\t%r" % persian_cat#将字符串的原始数据展示出来

