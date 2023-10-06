'''Game.py -- this file holds all of the game data and logic so that it can later be accessed by app.py to be implemented '''

# imports
import os
import random
import role1, role2


def diceRoll():
    # function to roll the dice
    return (random.randint(2, 12))

    
'''The quest function allows the user to play the game as the quest function
gathers information from either role1 or role2 and uses the load and diceRoll functions
this function then uses conditonal statments to implement the game logic'''
def quest(r1,clean):
    challengeIdx = 1
    if r1 == '1':
        # creates a list to hold the attrbs of role10
        attrb = role1.attrb()
        result = 0
        while challengeIdx != 4:
            # using the challengeIdx we access the challenge for the role
            role1.challenges(challengeIdx)
            # stores the possible outcomes to a list
            outcome = role1.challengeOutcome(challengeIdx)
            roll = input("\ndo you want to roll the dice or do you want to give up? (roll/giveup) ")
            # the use if .lower() is to remove all capatials in the string to minimize errors
            if roll.lower() == 'roll':
                rolled = diceRoll()
                # clears the terminal to allow for a clean display and a better user experince
                os.system(clean)
                # this conditional statement checks whether the player has won or not by comparing their score
                if rolled < 6 + challengeIdx - 1:
                    # we are printing the outcome of the challenge with the list we created earlier
                    print("\n",outcome[1],'Challenge lost')
                    # we now want to change the attrb value down 1 as the user lost the challenge
                    result = attrb[challengeIdx - 1]
                    result -= 1
                    attrb[challengeIdx - 1] = result
                    print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
                    challengeIdx += 1
                # this conditional statement checks whether the player has won or not by comparing their score    
                elif rolled >= 6 + challengeIdx:
                    #print the outcome of the challenge using the outcome list
                    print("\n",outcome[0])
                    # change the value of the attrb 
                    result = attrb[challengeIdx - 1]
                    result += 1
                    attrb[challengeIdx - 1] = result
                    print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
                    challengeIdx += 1
            
            elif roll.lower() == 'giveup':
                # if the user wants to stop then print "Game Over" and break out the loop
                print('Game Over')
                break
                
            elif roll.lower() != 'roll' or roll.lower() != 'giveup':
                # checks if the user inputed a vaild value if not print "Invaild Try Again" and let them try again
                print('\nInvaild Try Again\n')
            
    elif r1 == '2':
        attrb = role2.attrb()
        result = 0
        while challengeIdx != 4:
            role2.challenges(challengeIdx)
            outcome = role2.challengeOutcome(challengeIdx)
            roll = input("do you want to roll the dice or do you want to give up? (roll/giveup) ")
            
            if roll.lower() == 'roll':
                rolled = diceRoll()
                os.system(clean)
                
                if rolled < 6 + challengeIdx - 1:
                    print("\n",outcome[1],'Challenge lost')
                    result = attrb[challengeIdx - 1]
                    result -= 1
                    attrb[challengeIdx - 1] = result
                    print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2])
                    challengeIdx += 1
                    
                elif rolled >= 6 + challengeIdx:
                    print("\n",outcome[0])
                    result = attrb[challengeIdx - 1]
                    result += 1
                    attrb[challengeIdx - 1] = result
                    print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2])
                    challengeIdx += 1
                
            elif roll.lower() == 'giveup':
                print('Game Over')
                break
                
            elif roll.lower() != 'roll' or roll.lower() != 'giveup':
                print('\nInvaild Try again\n')                   
    return
    
    


        
    