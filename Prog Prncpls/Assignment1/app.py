import os
import time
import role1,role2,game


def mainMenu():
    while True:
        userIn = input("\n    S to Start\n    Q to Quit\n    R for Rules\n\n --> ")
        os.system('cls')
        if userIn.lower() == 's':
            return userIn
        elif userIn.lower() == 'q':
            return userIn
        elif userIn.lower() == 'r':
            print("Rules: \n    In this game everything is done with a pair of dice,\n Each role has their own atrrbs and challenges\n Each Challenge corelates to a atrrb\n if you win the challenge the atrrb will rise if you lose it will lower the atrrb. \n Also if you are to fail the challenge then you will be brought to the next challenge as if you had won the previous one")
        elif userIn != 's' or userIn != 'q' or userIn != 'r':
            print('Invaild Try Again')
            
'''The welcomeMsg function is used to print the intro stroy to the user,
so that they can get a breif understanding of what is going on, Also I use 
os.system('clear') to clear the terminal so that as the program starts the user gets a clear display'''
def welcomeMsg():
    # prints the story and roles to the user
    os.system('cls')
    msg = '''    Welcome to Cell Block-C
    In this game your goal is to escape the prison
    
    Game Story: In the dimly lit confines of Cell Block C, 
    two unlikely allies forged a desperate bond. Mason, a burly ex-Marine with a shaved head and a troubled past, 
    had been imprisoned for a crime he swore he didn't commit. His cellmate, James, a wiry and street-smart hacker, 
    had ended up behind bars due to his underground dealings in the digital underworld. Fate had brought them together,
    but a shared desire for freedom would make them brothers in a daring quest.
    Behind the cold steel bars, they whispered secrets in the shadows, 
    plotting an elaborate escape plan that would test their wits, their courage, and their loyalty.
 '''
    print(msg)
    
'''The load function is used for displaying a simple loading screen whihc is just for asthetics 
when this function is called the user will be shown a loading screen that will run for 10 - 20 secs'''
def load():
    #simple animation for smoother transtions between function
    startMsg1 = 'Loading /'
    startMsg2 = 'Loading -'
    startMsg3 = 'Loading \\'
    startMsg4 = 'Loading |'
    numLoop = 0
    while numLoop <= 3:
        time.sleep(0.5)
        os.system('cls')
        print(startMsg1)
        time.sleep(0.5)
        os.system('cls')
        print(startMsg2)
        time.sleep(0.5)
        os.system('cls')
        print(startMsg3)
        time.sleep(0.5)
        os.system('cls')
        print(startMsg4)
        numLoop += 1
    os.system('cls')
    return 

'''The charSelect allows the user to select a role from the ones presented,
when a user selects a role they will then be presented with the loading screen
and then the bio of the role for example the age, name and background story'''
def charSelect(choice):
    while True:
        # function that allows the user to choice a role and than retrives the attributes from role1 or role2
        if choice == '1':
            load()
            role1.bio()
            attrb = role1.attrb()
            print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
        
        elif choice == '2':
            load()
            role2.bio()
            attrb = role2.attrb()
            print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
        else:
            print('Invaild Try Again')
        return 


load()
while True:
    userStrt = mainMenu()
    if userStrt == 's':
        load()
        welcomeMsg()

        choice = input('Which character would you like to choose? | 1 for Mason | 2 for James: ')

        charSelect(choice)
        game.quest(choice)
    elif userStrt == 'q':
        print('You Have Quit')
        break


    



    

    
    