

''' the function bio is used to print the bio to the user upon request'''
def bio():
    msg = '''\nName: Mason "Bulldog" Connolly
Age: 34
Background: Born and raised in a rough neighborhood on the outskirts of a gritty industrial town, 
Mason Connolly's life had always been a battle. He grew up in a family torn apart by poverty and addiction, 
learning to fend for himself from a young age. With his chiseled frame and shaved head, 
Mason appeared every bit the tough-as-nails ex-Marine he was.
Military Service: Mason joined the United States Marine Corps straight out of high school, 
seeking discipline and a way out of the chaos that had defined his early years. During his service, 
he became known as "Bulldog" among his fellow soldiers for his unwavering determination and fierce loyalty to his unit.'''
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
    challenge1 = 'you need to get out of your cell,\n you have to steal the keys to the cell from the guard | (you need a 6 or higher to win)'
    challenge2 = "Great now that your out of your cell you need to get to the security room and take out the guard make sure you don't get caught!(roll more than a 7 or you get caught)"
    challenge3 = "Your alsmost out, you just need to get over the fence but remeber you need to wait for james's signal(roll more than 8 or you won't get the signal)"
    if c1 == 1: 
        print(challenge1) 
    elif c1 == 2:
        print(challenge2)

    elif c1 == 3:
        print(challenge3)
        
 
 
'''the challengeOutcome function returns the outcome of the challenge based on what you rolled with the diceRoll function'''   
def challengeOutcome(c1):
    if c1 == 1: 
        c1Loss = "the guard caught you trying to make a hole"
        c1Win = "you got the keys good job!"
        return c1Win,c1Loss
        
    elif c1 == 2:
        c2Loss = "the guard spotted you"
        c2Win = "you took the guard down good job!"
        return c2Win,c2Loss
        
    elif c1 == 3:
        c3Loss = "you were inpatient and got caught"
        c3Win = "you ESCAPED!"   
        return c3Win, c3Loss
    