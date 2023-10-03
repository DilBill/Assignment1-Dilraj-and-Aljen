

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

