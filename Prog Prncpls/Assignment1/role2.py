def bio():
    msg = '''\nName: James "Byte" Reynolds
Age: 29
Background: James Reynolds, known by his alias "Byte" in the underground hacking world, 
had always danced on the edge of legality. Raised in the bustling urban sprawl of a metropolis,
he had an insatiable curiosity for all things digital from a young age. His affinity for computers
and coding led him down a path few understood or dared to tread.
James was a self-taught tech savant, mastering the intricacies of computer systems, cryptography, and cybersecurity.
His greatest attribute is his IQ.'''
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
    challenge1 = "Challenge 1:\n You must escape your cell. You have to use your hacking skills to bypass the electronic lock in your cell.\n (roll higher than 6 to crack the system)"
    challenge2 = "Challenge 2:\n You're out of your cell but you are surrounded by surveillance systems. You must disable the system to avoid detection.\n (roll higher than 7 to deactivate it)"
    challenge3 = "Challenge 3:\n You're on the last obstacle. James is waiting for you on the other side but he needs help disabling the security protocol.\n (roll higher than 8 to help him)"
    if c1 == 1: 
        print(challenge1) 
    elif c1 == 2:
        print(challenge2)

    elif c1 == 3:
        print(challenge3)
        
    
def challengeOutcome(c1):
    if c1 == 1: 
        c1Loss = "Oh no! The alarms went off! You have been caught. -1 Strength!"
        c1Win = "Great! You succesfully bypassed the locks. +1 Strength"
        return c1Win,c1Loss
        
    elif c1 == 2:
        c2Loss = "Beep! The camera spotted you. -1 Courage"
        c2Win = "Awesome! The entire surveillance system is now disabled."
        return c2Win,c2Loss
        
    elif c1 == 3:
        c3Loss = "Yikes! The nearby guard caught you. -1 IQ"
        c3Win = "Woo! You and James have escaped. Freedom! +1 IQ"   
        return c3Win, c3Loss
    