import Dominion_player_class
import Dominion_base_card_class
import time

def PlayerInit():
    NumberofPlayers = 0 #declare the number of players to 0
    PlayerList = []
    while NumberofPlayers<4: #loop until there are 4 players
        NumberofPlayers = NumberofPlayers + 1 #increment NumberofPlayers
        print("What is the ", NumberofPlayers,"st player's name?")
        PlayerName = input("??")
        PlayerName = Dominion_player_class.Player(PlayerName)
        #Player PlayerName #declare Player classes with Dominion_classes.py
        PlayerList.append(PlayerName)
    return PlayerList

#print(PlayerInit()[1].player_deck)
