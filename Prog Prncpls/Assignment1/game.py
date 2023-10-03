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


        
    