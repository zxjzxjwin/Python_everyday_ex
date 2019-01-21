
# coding: utf-8

# In[3]:


from sys import argv
script, user_sex, user_name = argv
prompt = '>'
print "Hi %s %s, I'm the %s script." % (user_sex, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What  kind of computer do you have?"
computer = raw_input(prompt)
print  """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And yo have a %r compyter. Nice.
""" % (likes, lives, computer)

