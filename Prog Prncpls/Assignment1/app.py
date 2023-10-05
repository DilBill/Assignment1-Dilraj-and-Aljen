import os,time,platform
import role1,role2,game

'''this function is used to quickly check what os the user is using '''
def osChecker():
    clean = ''
    if platform.system() == "Windows":
        clean = 'cls'
    elif platform.system() == "macOS":
        clean = 'clear'
    
    return clean

'''The mainMenu function will show the user a basic menu that will allow them to either start the game quit or read the rules,
If the user wants to read the rules they will be redreicted to the mainmenu to either start or quit'''
def mainMenu(clean):
    while True:
        #show the user the options they have and allow them to input their choice
        userIn = input("\n    S to Start\n    Q to Quit\n    R for Rules\n\n --> ")
        # os.system('cls') is used to clear the terminal 
        os.system(clean)
        if userIn.lower() == 's':
            return userIn
        elif userIn.lower() == 'q':
            return userIn
        elif userIn.lower() == 'r':
            print("Rules: \n    In this game everything is done with a pair of dice,\n Each role has their own atrrbs and challenges\n Each Challenge corelates to a atrrb\n if you win the challenge the atrrb will rise if you lose it will lower the atrrb. \n Also if you are to fail the challenge then you will be brought to the next challenge as if you had won the previous one")
            #If the user does not input a vaild value they well be asked to try again
        elif userIn != 's' or userIn != 'q' or userIn != 'r':
            print('Invaild Try Again')
            
'''The welcomeMsg function is used to print the intro stroy to the user,
so that they can get a breif understanding of what is going on, Also I use 
os.system('clear') to clear the terminal so that as the program starts the user gets a clear display'''
def welcomeMsg(clean):
    # prints the story and roles to the user
    os.system(clean)
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
    
'''The load function is used for displaying a simple loading screen which is just for asthetics 
when this function is called the user will be shown a loading screen that will run for 10 - 20 secs'''
def load(clean):
    #simple animation for smoother transtions between function
    startMsg1 = 'Loading /'
    startMsg2 = 'Loading -'
    startMsg3 = 'Loading \\'
    startMsg4 = 'Loading |'
    numLoop = 0
    while numLoop <= 3:
        # time.sleep(0.5) is used to to pause the program for the give time in seconds
        time.sleep(0.5)
        # we then clear the terminal
        os.system(clean)
        # then we print the message
        print(startMsg1)
        time.sleep(0.5)
        os.system(clean)
        print(startMsg2)
        time.sleep(0.5)
        os.system(clean)
        print(startMsg3)
        time.sleep(0.5)
        os.system(clean)
        print(startMsg4)
        numLoop += 1
    os.system(clean)
    return 

'''The charSelect allows the user to select a role from the ones presented,
when a user selects a role they will then be presented with the loading screen
and then the bio of the role for example the age, name and background story'''
def charSelect(choice):
    while True:
        # function that allows the user to choice a role and than retrives the attributes from role1 or role2
        if choice == '1':
            # run the load function for effect
            load()
            # we then call the function bio from the role1 or 2 file
            role1.bio()
            #we store the attrbs into a list called attrb
            attrb = role1.attrb()
            # then print the attrbs to the user
            print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
        
        elif choice == '2':
            load()
            role2.bio()
            attrb = role2.attrb()
            print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
        else:
            print('Invaild Try Again')
        return 

clean = osChecker()
load()
while True:
    # call the function mainMenu and store it to userStrt
    userStrt = mainMenu()
    if userStrt == 's':
        load(clean)
        # call the welcomeMsg function
        welcomeMsg(clean)
        # ask the user what character they want to use
        choice = input('Which character would you like to choose? | 1 for Mason | 2 for James: ')
        # call the charSelect function and pass choice as the parameter
        charSelect(choice)
        # call the quest function from the game.py file and pass choice as the parameter
        game.quest(choice,clean)
    elif userStrt == 'q':
        # if the user decides to quit then print "you have quit" and then break
        print('You Have Quit')
        break


    



    

    
    