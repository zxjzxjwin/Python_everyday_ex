#coding:utf-8
# dict = {"a" : "1", "b" : "2", "c" : "3"}
# dict["d"]=4
# print list
# print dict["a"]
# del dict

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
happy_bday = Song(["Happy birthday to you ", "I don't want to be get sued", "So I;ll stop right there."])#此处输入参数的格式为集合set
bull_on_parade = Song(["They rally around the family", "With pockets full of shells"])
happy_bday.sing_me_a_song()
bull_on_parade.sing_me_a_song()


'''
dict = {
		"a" : "1",
		"b" : "2",
		"c" : "3"
}
print type(dict)

for key_value in dict.items():
	print key_value,type(key_value)

dict = {}	
key = ["a", "b" ,"c"]
value = ["1", "2", "3"]
for i in key, value:        #【注】一个变量对两个列表，loop顺序为先遍历完第一个列表并输出为，再同样做对第二个列表
	dict[key[i]] = value[i]
	
print dict
'''