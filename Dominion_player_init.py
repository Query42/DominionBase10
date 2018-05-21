import Dominion_player_class
import Dominion_base_card_class
import time
import random

def Player_init():
    NumberofPlayers = 0 #declare the number of players to 0
    PlayerList = []
    while NumberofPlayers<4: #loop until there are 4 players
        NumberofPlayers = NumberofPlayers + 1 #increment NumberofPlayers
        print("What is the ", NumberofPlayers,"st player's name?")
        PlayerName = input("??")
        PlayerName = Dominion_player_class.Player(PlayerName)
        #Player PlayerName #declare Player classes with Dominion_classes.py
        PlayerList.append(PlayerName)
    random.shuffle(PlayerList)
    return PlayerList


#Player_list = Player_init()



