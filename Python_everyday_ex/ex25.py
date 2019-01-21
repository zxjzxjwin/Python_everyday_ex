#coding:utf-8
#u'写程序，逐行研究，弄懂他'
def break_words(stuff):
	"""This funcrion will break up words for us."""#如果希望左侧作为“帮助文档”在“help(ex25)”中显示，则必须放在函数内部第一行；其他位置不在help中显示
	words = stuff.split(' ')#split()#将字符串通过分隔符进行切片，并放入列表中
	return words

def sort_words(words):
	return sorted(words)#sorted()#将列表里的字符串依首字母顺序排列
	"""Sorts the words."""
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)#word.pop(0)???
	print word
	
def print_last_word(words):
	"""Prints the last word after poppint it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorten words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_frint_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def	print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(wordss)

'''
1.	str.split(srt = "",num = string.count(str)) 将字符串以单词分割，并放入列表中

2.	list.sorted(reverse = [bool]) 将列表里的字符串依首字母顺序排列；
reverse“相反”，False时正排序，True时逆排序
3.	list.pop([n]) 移除列表中的第n个元素（0起头；默认最后一个元素），并且返回该元素的值；
例：word.pop(-1)表示移除word中的最后一个元素
4.	def break_words(stuff): 
		"""xxx"""
		如果希望xxx作为“帮助文档”在“help(ex25)”中显示，则必须放在函数内部第一行；
		其他位置不在help中显示
'''