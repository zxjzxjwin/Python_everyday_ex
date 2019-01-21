
# coding: utf-8

# In[ ]:


#读写文件
#从代码块调用argv模组
from sys import argv
#输入参数
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."
#指示输入
raw_input("?")
#打开文档
print "Opening the file..."
target = open(filename, 'w+')#'w'不读只写，'w+'可读可写
#清空文档，但不用单独清空，w覆盖写
print "Truncating the file. Goodbye!"
#target.truncate()
#文档已清空
#用户输入
print "Now I'm going to ask you for three lines."
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
#程序写入到空白文档
# target.write(raw_input("line1:"))
# target.write("\n")
# target.write(raw_input("line2:"))
# target.write("\n")
# target.write(raw_input("line3:"))
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#再读取修改后文档
print "Now you can see the result.\n"
#close(target)
target.seek(0)#文件指针回到开头
# target2 = open(target,'r')
print target.read()
print "And finally, we close it."
#关闭已打开文档
target.close()