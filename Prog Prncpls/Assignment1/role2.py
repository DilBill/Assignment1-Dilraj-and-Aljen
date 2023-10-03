def bio():
    msg = '''\nName: James "Byte" Reynolds
Age: 29
Background: James Reynolds, known by his alias "Byte" in the underground hacking world, 
had always danced on the edge of legality. Raised in the bustling urban sprawl of a metropolis,
he had an insatiable curiosity for all things digital from a young age. His affinity for computers
and coding led him down a path few understood or dared to tread.
Tech Savant: James was a self-taught tech savant, mastering the intricacies of computer systems, cryptography, and cybersecurity.
His skills made him a sought-after figure in the cyber-underground, where he navigated the labyrinth of the dark web 
and orchestrated hacks that often blurred the lines between activism and cybercrime.'''
    print(msg)
    
    
def attrb():
    attrb = []
    st = 1
    cr = 2
    iq = 2
    attrb.append(st)
    attrb.append(cr)
    attrb.append(iq)
    return attrb

def challenges(c1):
    challenge1 = 'you need to get out of your cell,\n you have to steal the keys to the cell from the guard | (you need a 6 or higher to win)'
    challenge2 = "Great now that your out of your cell you need to get to the security room and take out the guard make sure you don't get caught!(roll more than a 8 or you get caught)"
    challenge3 = "Your alsmost out, you just need to get over the fence but remeber you need to wait for james's signal(roll less than 6 or you won't get the signal)"
    if c1 == 1: 
        print(challenge1) 
    elif c1 == 2:
        print(challenge2)

    elif c1 == 3:
        print(challenge3)
        
    
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
    