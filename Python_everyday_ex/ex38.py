#coding:utf-8
#abbreviation n. 缩写
#create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}
'''
type(states) = dict -> dictionary 字典，格式  d = {key1 : value1, key2 : value2}
定义：
1. 键一般是唯一的，如果重复则最后的一个键值对会替换前面的，值不需要唯一
2. 值可以取任何数据类型，但‘键’必须是不可变（不可变:改变时地址跟着改变）的，即’索引‘不能变，如字符串、数字和元组可以，但
        列表  ['', int]
        集合  {'', int}
        字典  {key : value, key : value }
        是可变数据类型，不可以
   如:  dict = {['Name']: 'Zara', 'Age': 7} 
'''


#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

'''
3. 访问： dict[key] -> [outputs] value ; dict[value] -> [Error] 不能用值找键（类比函数中，知y找x）
4. 添加:  dict[add_key] = add_value  但默认dict[]里的一定是键
5. 删除： del dict[key]  删除键为‘key’的条目
          dict.clear()  清空词典所有条目
          del dict  删除词典
6. 内置函数：
    cmp(dict1, dict2)  比较两个字典元素,若完全一样返回0，不同且前多于后返回1，不同且前少于后返回-1
    len(dict)  计算字典元素个数，即键值对的总数 或 键的总数
    str(dict)  输出字典可打印的字符串表示
        【注】返回值类似直接引用，但类型一定是str，而直接引用的类型一定是dict
    type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型
7. 内置方法：
    7.1  dict.clear()  清空词典所有条目【注】没有返回值
    7.2  dict.copy()  返回一个字典的浅复制
    7.3    7.3.1  d;d1 = d  地址相同，跟着变
           7.3.2  d;d1 同数据重写     完全无关
           7.3.3  d;d1 = d.copy()#浅拷贝，对复杂对象里的复杂对象只添加标签  地址不同，跟着变
                     = copy.copy(d)                       地址不同，跟着变
           7.3.4  d;d1 = copy.deepcopy(d)#深拷贝  完全无关
 -  7.4  dict.get(key,default = None)  返回指定键的值，如果不在字典中返回default的值【注】在Python的交互环境里，直接调用None时格式为None，不可见；转义后才显示
    7.5  dict.has_key(key)  如果键在字典dict里返回true，否则返回False
    7.6  dict.items()  以列表格式返回可遍历的（键，值）二元元组
          [(元组1)       ,(元组2)      ]
          [(key1, value1),(key2,value2)]
    7.7  dict.keys()  以列表返回一个字典的所有的键
    7.8  dict.values()  以列表返回一个字典的所有的值
 -  7.9  dict.setdefault(key, default = None)  和get()类似，单如果键不在字典字典中将会添加键并将值设为default
    7.10  dict.update(dict2)  把dict2的键值对更新到dict中
    7.11  dict.pop(key,[default])  删除字典给定键key所对应的值，返回值为被删除的值。key必须给出，否则返回default值
    7.12  dict.popitem()  随机删除并返回字典中的一对键和值
'''  

#print out some cities
print '-' * 10
print "NY State has:", cities['NY']

#print some states
print "-" * 10
print "Michigan's abbreviation is:", states['Florida']

#do it by using the state then cities dict
print "-" * 10
print "Michigan has:", cities[states['Michigan']]# == cities['MI']
print "Florida has:", cities[states['Florida']]

#print every state abbreviation
print "-" * 10
for state, abbrev in states.items():#此处的key, value标签临时定，不用提前定
    print "%s is abbreviated %s" % (state, abbrev )    #dict.items -> D.items() , list of D's(key,value)pairs,as 2-tuples(2元语义)
#print every city in state
print "-" * 10
for abbrev, city in cities.items():
    print "%s is in %s" % (city, abbrev)
    
'''
print "-" * 10
for abbrev.1, city in cities.items():
    print "%s is in %s" % (city, abbrev)
    
[outputs]
Jacksonville is in NY
San Francisco is in NY
Detroit is in NY
Portland is in NY
New York is in NY

【注】推测，二元数组在读取时也依靠指针，故连续读取统一数组，当定义标签同名时，指针自动归零；当定义标签不同名时，指针不动，即便签只能指向上一次读取的停止位置对应值
'''

    
print "-" * 10
for state, abbrev in states.items():
    print "%s is in %s which is abbreviated %s." % (cities[abbrev],abbrev, state )
    
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print 'Sorry, no Texas.'
    
#state = states.has_key('Texas')#注意加下划线

#if not state:
#    print 'Sorry, no Texas.'


#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is : %s" % city

