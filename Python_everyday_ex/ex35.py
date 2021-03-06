#coding:utf-8
#分支和函数
from sys import exit
def gold_room():
    print "This room is full of gold. How much do you take?"
    next = raw_input(">")
    if next.isdigit():       #如何判断输入的是不是数字？ n.isdigit()函数，为真则n为数字
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

#以下两组函数，相当于用while和if两种形式，写了无限循环
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?\n1.take honey\n2.taunt bear\n3.open door"
    bear_moved = False
    while True:
        next = raw_input(">")
        if next == "take honey":
            dead("The bear looks at yo then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    next = raw_input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()          
            
def dead(a):
    print ("%s" % a), "Good job!"
    exit(0)                       #退出且程序正常
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    next = raw_input(">")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the toom until you starve.")
        
start()