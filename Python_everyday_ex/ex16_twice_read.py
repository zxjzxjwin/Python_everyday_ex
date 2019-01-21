#coding=utf-8
#再读取改后文档
from sys import argv
script, filename = argv
print "Now I will read the file which havend beem rewrite."
txt = open(filename)
print txt.read()
print "Now you have see the newest file, I shall close it."
txt.close()