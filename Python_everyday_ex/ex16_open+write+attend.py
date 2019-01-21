#coding=utf-8
fw = open('D:\zhangxj-2018-12-26\ex-py\ex15_sample - 1.txt','a+')
new_stus = ''#空白文档，准备存储修改后信息
fw.seek(0)#指针归零
for s in fw:#s为每行
    stu = 'A班' + s
    new_stus += stu
#归位并清空
fw.seek(0)
fw.truncate()
#重写
fw.write(new_stus)
#强制写
fw.flush()
#关闭
fw.close()
print "Have done."