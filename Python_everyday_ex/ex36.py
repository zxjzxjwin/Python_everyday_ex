from sys import exit
def start():
    print "There are four doors. Which will you choose?\n(input ordinal number):"
    
    try:
        next = int(raw_input(">"))

    except ValueError:
            print "I don't know what you mean. Choose again."
            start()
            
    else:        
        if next == 1:
            fire()

        elif next == 2:
            Cthulhu()

        elif next == 3:
            duel()

        elif next == 4:
            gold()
        else:
            print("There isn't this number! Try again!")
            start()
    
def fire():
    print "You are surrounded by flames."
    print "Fire in the hole!"
    dead("Stupid man!")

def Cthulhu():
    print "You see Cthulhu! It is staring you!"
    print """
    What will you do?\n(input ordinal number):
    1. run away
    2. fight it
    3. be its slave
    """
    try:
        next = int(raw_input(">"))

    except ValueError:
            print "Input ordinal number!<Cthulhu>"
            Cthulhu()
            
    else:        
        if next == 1:
            print "You run to the starting point!"
            start()

        elif next == 2:
            dead("Weak man!")

        elif next == 3:
            print "Nice choice. Before your sacrifice, I shall give you some gold."
            gold()
            
        else:
            print("There isn't this number! Try again!")
            start()
    

        
def duel():
    print "Face the thunder of Zeus!"
    print "What will you do?\n(input ordinal number):"
    print  '''
    1. use the power of Cthulhu
    2. use the power of Magic
    3. sit down and have a cup of tea
    '''

    Polymorph = False
    
    while True:
        
        next = raw_input(">")
        
        if next == "1":
            print "You defeat the Zeus! \nHowever the power of Cthulhu leads you into its room!"
            Cthulhu()

        elif Polymorph and next == "2":
            print "'Fire Magic!'\nYou kill the Zeus! Go to the gold room and get your awards!"
            gold()

        elif next == "2":
            print "You use Polymorph!The Zeus has been a sheep!"
            print "Choose again to kill it!"
            Polymorph = True

        elif Polymorph and next == "3":
            dead("Before you finish your tea, the Zeus recovers and kill you!\nWhy not use power?")

        elif next == "3":
            dead("Coooooooooooool!")

        else:
            print "Input ordinal number!<duel>"
        
def gold(): 
    print "There are lots of gold! How much will you take?"
   
    try:
        next = float(raw_input(">"))
    
    except ValueError:
        dead("Learn to input number!")
    
    else:
        
        if 0 <= next and 6 > next:#nexrt < 6 & next >= 0
            win_fake()
       
        elif next >= 6:#next >= 6
            dead("Greed man!")
        
        else:          #next < 0
            win_true()

'''def gold(): 
    print "There are a large number of bags of gold! How many bags will you take away?"
    next = raw_input(">")
   
    try:
        f.next = "%f" % next#不可以这么做！py2和py3都不行！
    
    except[ValueError]:
        dead("Learn to input number!")
    
    else:
        
        if 0 <= float.next and 6 > next:#nexrt < 6 & next >= 0
            win_fake()
       
        elif float.next >= 6:#next >= 6
            dead("Greed man!")
        
        else:          #next < 0
            win_true()'''
            
'''    next = raw_input(">")
    
    if not next.isdigit():
        dead("Learn input a number,Man!")
        
    else:
        int_next = int(next)
        
        if 0 <= next <= 5:
            win_fake()
            
        elif 0 >= next:
            win_true()
            
        else:
            dead("Gred man!")'''
    
def dead(tips):
    print "You died!" , tips
    exit(0)
    
def win_fake():
    print "You win! Good job!"
    print "Then catching your gold and receiving sacrifices of Cthulhu!"
    
def win_true():
    print "Thanks your sacrifice! So the Cthulhu let you live!"
    exit(0)
    
start()