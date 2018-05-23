import time
import random

import player_init


#Dominion in python3 
#version 1.0 started 20180518

#Initialize gamestate
    #Announce kingdom cards
    #Ensure supply count of each card

#Welcome message
print("Dominion implemented in python 3. ")

#Ask for player names
#Initialize players with player name input
#Randomize turn order (rolled into init)
player_list = player_init.player_init()

#Announce turn order
print("The turn order is:")
for player in player_list:
    print(player.name)

while True:
    pass
    #commence play loop
    #Rotate to next player
    #Run turn function

#Endstate
    #Announce game over
    #Count VPs
    #In event of tie, count turn order
    #Announce scores and winner(s)
