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


    

    
    