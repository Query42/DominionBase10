import time
import random

import Dominion_base_card_class


class Player():
    """Player object. Tracks states of individual players."""
    def __init__(self, name):
        self.name = name
        self.deck = ['Estate', 'Estate', 'Estate', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper']
        self.handsize = 5
        self.turncount = 0
        self.activeturn = 0
        self.baseactions = 1
        self.remainingactions = 0
        self.gained_ = []

def player_init():
    """
    Prompt for names of four players. Create player objects.
    Randomize turn order. Return randomized list of player objects.
    """
    player_count = 0 #declare the number of players to 0
    player_list = []
    while player_count<4: #loop until there are 4 players
        player_count = player_count + 1 #increment player_count
        print("What is the name of player {}?".format(player_count))
        #I changed the above input prompt to avoid "4st"
        player_name = input("> ")
        #player_name = Player(player_name)
        #Line above: this is going to throw an error as you're trying to assign a
        #string as a variable name. Changing implementation
        #Player player_name #declare Player classes with Dominion_classes.py
        #player_list.append(player_name)
        player_list.append(Player(player_name))
        #This implementation just adds the new player object to the player list. We
        #can examine it by calling for the player object's names if necessary.
    random.shuffle(player_list)
    return player_list

player_list = player_init()

for player_obj in player_list:
    print(player_obj.name)
