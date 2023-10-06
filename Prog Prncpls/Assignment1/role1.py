''' the function bio is used to print the bio to the user upon request'''
def bio():
    msg = '''\nName: Mason "Bulldog" Connolly
Age: 34
Background: Born and raised in a rough neighborhood on the outskirts of a gritty industrial town, 
Mason Connolly's life had always been a battle. He grew up in a family torn apart by poverty and addiction, 
learning to fend for himself from a young age. With his chiseled frame and shaved head, 
Mason appeared every bit the tough-as-nails ex-Marine he was. 
Mason joined the United States Marine Corps straight out of high school, 
seeking discipline and a way out of the chaos that had defined his early years. During his service, 
he became known as "Bulldog" among his fellow soldiers for his unwavering determination and fierce loyalty to his unit.
His strongest attribute is his strength. '''
    print(msg)
    
    
'''the attrb function is used to hard code the attrb values to a list which is returned when called'''
def attrb():
    attrb = []
    st = 2
    cr = 2
    iq = 1
    attrb.append(st)
    attrb.append(cr)
    attrb.append(iq)
    return attrb

'''the challenges function creates the roles own challenges 
which will then be print depending on the parameter c1 (e.g. if c1 == 1 --> print challenge1)'''
def challenges(c1):
    challenge1 = 'Challenge 1:\nYou need to get out of your cell, you must steal the keys to the cell from the guard.\n(you need a 6 or higher to obtain the keys)'
    challenge2 = "Challenge 2:\nYou need to get to the security room and take out the guard. Make sure you don't get caught!\n(roll more than a 7 or you'll get caught)"
    challenge3 = "Challenge 3:\nYou are almost out, you just need to get over the fence but remember, you need to wait for James's signal\n(roll more than 8 or you won't get the signal)"
    if c1 == 1: 
        print(challenge1) 
    elif c1 == 2:
        print(challenge2)

    elif c1 == 3:
        print(challenge3)
        
 
 
'''the challengeOutcome function returns the outcome of the challenge based on what you rolled with the diceRoll function'''   
def challengeOutcome(c1):
    if c1 == 1: 
        c1Loss = "Oh no! The guard caught you trying to steal his keys. You lost -1 Strength."
        c1Win = "Cool! You got the keys, Good job! You have been added +1 Strength."
        return c1Win,c1Loss
        
    elif c1 == 2:
        c2Loss = "Too bad! The guard spotted you. You lost -1 Courage."
        c2Win = "Great! You took the guard down, Good job! You have gained +1 Courage."
        return c2Win,c2Loss
        
    elif c1 == 3:
        c3Loss = "Ouch! You were impatient and got caught, you lost -1 IQ."
        c3Win = "You won, you finally ESCAPED! You learned something new, +1 IQ."   
        return c3Win, c3Loss
    