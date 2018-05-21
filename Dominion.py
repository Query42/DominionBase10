import Dominion_player_class
import time
#Dominion in python3 
#version 1.0 started 20180518

#Initialize gamestate
    #Announce kingdom cards
    #Ensure supply count of each card

#Welcome message
print("Dominion implemented in python 3. ")

#Ask for player names
#Initialize players with player name input
Player_list = Player_init()

#Randomize turn order
#Announce turn order

while True: #commence play loop
    #Rotate to next player
    #Run turn function

#Endstate
    #Announce game over
    #Count VPs
    #In event of tie, count turn order
    #Announce scores and winner(s)

def player_turn():
    #Set actions/buys/hand size to 5
    #Announce cards in hand to player
    #If Actions present in hand:
        #While actions remaining > 0:
            #Prompt player to play actions
            #If player plays an action
                #Execute action function
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

def draw_cards(draw_count):
    """Takes cards from top of deck equal to draw_count and returns them as a list"""
    drawn_cards = []
    for item in range(1, draw_count):
        if #player has cards in deck:
            #pop out the top card in the deck/add it to drawn_cards
        else:
            drawn_cards += #shuffle function
            #pop out top card of deck/add it to drawn_cards

def shuffle():
    """Shuffles discard pile (if present) into deck and draws/returns top card"""
    pass
