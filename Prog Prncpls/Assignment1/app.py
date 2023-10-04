import os
import time
import role1,role2,game


def mainMenu():
    while True:
        userIn = input("\n    S to Start\n    Q to Quit\n    R for Rules\n\n --> ")
        os.system('clear')
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
    os.system('clear')
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
        os.system('clear')
        print(startMsg1)
        time.sleep(0.5)
        os.system('clear')
        print(startMsg2)
        time.sleep(0.5)
        os.system('clear')
        print(startMsg3)
        time.sleep(0.5)
        os.system('clear')
        print(startMsg4)
        numLoop += 1
    os.system('clear')
    return 




    



    

    
    