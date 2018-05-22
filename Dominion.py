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

def player_turn():
    pass
    #Set actions/buys/hand size to 5
    #Announce cards in hand to player
    #If Actions present in hand:
        #While actions remaining > 0:
            #Prompt player to play actions
            #If player plays an action
                #Remove played action from player's hand
                #Decrement actions remaining by 1
                #Execute action function
                #Announce cards in hand to player
            else:
                continue
    #Count money
    #Announce money to player
    while buys > 0:
        #Prompt player for what they want to buy
        if #player buys a card
            if #card still has supply
                #reduce supply of card by one
                #add card to discard pile
        else:
            continue
    #Check for game end
    #Add remainder of hand to discard
    #Draw (hand size) cards

def draw_cards(player, draw_target):
    """Takes cards from top of deck equal to draw_count and returns them as a list."""
    deck_cycled = False
    drawn_cards = []
    drawn_count = 0
    for item in range(draw_target):
        if player.deck:
            drawn_cards.append(player.deck.pop(0))
            drawn_count += 1
        elif player.discard_pile:
            print("Drew {} card(s): {}.".format(
                drawn_count,
                drawn_cards
                ))
            if deck_cycled:
                print("Deck exhausted.")
                break
            else:
                print("Shuffling the deck...")
                drawn_cards += shuffle(player)
                deck_cycled = True
        else:
            print("No cards remaining in deck!")
    return drawn_cards

def shuffle(player):
    """Shuffles discard pile (if present) into deck and draws/returns top card."""
    player.deck += player.discard_pile
    player.discard_pile = []
    random.shuffle(player.deck)
    return player.deck.pop(0)
