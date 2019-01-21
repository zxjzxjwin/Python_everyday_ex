#coding:utf-8
#从代码块中引入argv模组
from sys import argv
#从os中引入exists模组
from os.path import exists
script, from_file, to_file = argv
#？？？但是不能打开名字里有空格的文件
print "Copying from %s to %s" % (from_file, to_file)
#we could do these two on one line too, how?
in_file = open(from_file)#将源文件打开为过渡文件in
indata = in_file.read()#将过渡文件in的内容读取进过渡数据indata
#完成读取源文件和源数据
print "The input file is %d bytes long" % len(indata)#？？？len函数
print "Does the output file exist? %r" % exists(to_file)#？？？exists函数
raw_input()
out_file = open(to_file, 'w')#将待备份文件打开为过渡文件out
out_file.write(indata)#将过渡数据indata写入同义文件out
out_file.flush
print "All done."
out_file.close()
#文件在被读取后会自动关闭
#in_file.close()