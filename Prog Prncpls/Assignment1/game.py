'''Game.py -- this file holds all of the game data and logic so that it can later be accessed by app.py to be implemented '''

# imports
import time
import os
import random
import role1, role2

def diceRoll():
    # function to roll the dice
    return (random.randint(2, 12))

    
'''The quest function allows the user to play the game as the quest function
gathers information from either role1 or role2 and uses the load and dicrRoll functions
this function then uses conditonal statments to implement the game logic'''
def quest(r1):
    # function that implments the game logic and challenges
    challengeIdx = 1
    if r1 == '1':
        attrb = role1.attrb()
        result = 0
        while challengeIdx != 4:
            role1.challenges(challengeIdx)
            outcome = role1.challengeOutcome(challengeIdx)
            roll = input("\ndo you want to roll the dice or do you want to give up? (roll/giveup) ")
            
            if roll.lower() == 'roll':
                rolled = diceRoll()
                os.system('clear')
                
                if rolled < 6 + challengeIdx - 1:
                    print("\n",outcome[1],'Challenge lost')
                    result = attrb[challengeIdx - 1]
                    result -= 1
                    attrb[challengeIdx - 1] = result
                    print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
                    challengeIdx += 1
                    
                elif rolled >= 6 + challengeIdx:
                    print("\n",outcome[0])
                    result = attrb[challengeIdx - 1]
                    result += 1
                    attrb[challengeIdx - 1] = result
                    print('\nStrength =', attrb[0], '| Courage =',attrb[1], '| IQ =', attrb[2],'\n')
                    challengeIdx += 1
            
            elif roll.lower() == 'giveup':
                print('Game Over')
                break
                
            elif roll.lower() != 'roll' or roll.lower() != 'giveup':
                print('\nInvaild Try again\n')
            
    elif r1 == '2':
        attrb = role2.attrb()
        result = 0
        while challengeIdx != 4:
            role2.challenges(challengeIdx)
            outcome = role2.challengeOutcome(challengeIdx)
            roll = input("do you want to roll the dice or do you want to give up? (roll/giveup) ")
            
            if roll.lower() == 'roll':
                rolled = diceRoll()
                os.system('clear')
                
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
    
    


        
    