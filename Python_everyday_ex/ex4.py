
# coding: utf-8

# In[14]:


#车的数量
cars = 100
#每辆车的容量
space_in_a_car = 4.0
#司机的数量
drivers = 30
#乘客的数量
passengers = 90
#无效车的数量
cars_not_driven = cars - drivers
#司机的数量
cars_driven = drivers
#同一时刻最大容量之和
carpool_capacity = cars_driven * space_in_a_car
#每辆车客人数量
average_passengers_per_car = passengers / cars_driven#相比用 carpool_capacity/passenger,他的结果时每个人有多少空间；这里的结果是每个司机能拉多少人
print "There are",cars,"cars available."
print "There are only",drivers,"drivers available"
print "There will be",cars_not_driven,"empty cars today"
print "We can transport",carpool_capacity,"people today"
print "We have",passengers,"to carpool today"
print "We have",passengers,"to carpool today"
print "We need to put about",average_passengers_per_car,"in each car"

