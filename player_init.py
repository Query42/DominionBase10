import time
import random

import base_cards
#import Dominion


class Player():
    """Player object. Tracks states of individual players."""
    def __init__(self, name):
        self.name = name
        self.deck = ['Estate', 'Estate', 'Estate', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper']
        #self.hand_size = 5 currently no effects change this. May only be necessary in _turn_setup()
        self.hand = []
        self.discard_pile = []
        self.turn_count = 0

    def _turn(self):
        self._turn_setup(self)
        self._action_phase(self)
        self._buy_phase(self)
        self._cleanup(self) #returns "True" if game end conditions met

    def _turn_setup(self):
        self.turn_count += 1
        #resolve duration effects
        #self.hand_size = 5 #reset from Outpost
        self.actions_left = 1
        self.money = 0
        self.buys_left = 1
        self.in_play = []

    def _action_phase(self):
        #if no actions in hand, return
        print("***Action Phase***")
        while True:
            if self.actions_left == 0:
                print("No actions remaining.")
                break
            #elif no actions in hand, print "all actions played", return
            else:
                self.print_hand(self)
                print("What action would you like to play? (Type 'None' to play no action)")
                played_action = input("> ")
                if played_action.lower() == 'none':
                    break
                elif played_action.lower() in self.hand:
                    #ensure card is an action
                    self.play_card(self, played_action)
                    self.do_action(self, played_action)
                    self.actions_left -= 1
                else:
                    print("No such card in hand.")

    def _buy_phase(self):
        print("***Buy Phase***")
        #This will need functionality to loop and select treasures to play in the
        #future (Prosperity, etc.) But for now we can just play all treasures and move on.

        #count player's money
        #while buys remain:
            #list cards in supply
            #prompt player to buy
            #self.gain_card(self, bought_card)
        pass

    def _cleanup(self):
        self.discard_pile += self.in_play
        self.in_play = []
        #re: above lines: once duration cards are added, they will need to check each card
        #and either discard it or move it to a duration zone depending on if it has the 
        #Duration subtype
        self.discard_pile += self.hand
        self.hand = []
        self.draw_cards(self, 5)
        pass

    def play_card(self, played_card):
        """Remove card from hand and place it in play area."""
        self.hand.remove(played_card)
        self.in_play.append(played_card)

    def do_action(self, played_card):
        """Perform the action associated with playing the named card."""
        #play the action
        pass

    def print_hand(self):
        """Print player's current hand in user-friendly format."""
        print("Your current hand:")
        print(self.hand) # rebuild this for nicer ux

    def gain_card(self, gained_card, zone=False):
        """Gain a card from the supply. By default, add to player's discard pile."""
        if not zone:
            zone = self.discard_pile
        card = parse_card(gained_card)
        if card.supply == 0:
            print("The {} supply pile is empty!".format(gained_card))
            return
        card.supply -= 1
        if card.supply == 0:
            if card = Province:
                empty_supplies += 3
            else:
                empty_supplies += 1
        zone.append(gained_card)
        gained_this_turn.append(gained_card)

    def draw_cards(self, draw_target):
        """Takes cards from top of deck equal to draw_count and returns them as a list."""
        deck_cycled = False
        drawn_cards = []
        drawn_count = 0
        for item in range(draw_target):
            if self.deck:
                drawn_cards.append(self.deck.pop(0))
                drawn_count += 1
            elif self.discard_pile:
                print("Drew {} card(s): {}.".format(drawn_count, drawn_cards))
                if deck_cycled:
                    print("Deck exhausted.")
                    break
                else:
                    print("Shuffling the deck...")
                    drawn_cards += self._shuffle(self)
                    deck_cycled = True
            else:
                print("No cards remaining in deck!")
        return drawn_cards

    def _shuffle(self):
        """Shuffles discard pile (if present) into deck and draws/returns top card."""
        self.deck += self.discard_pile
        self.discard_pile = []
        random.shuffle(self.deck)
        return self.deck.pop(0)

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

if __name__ == "__main__":
    player_list = player_init()
    for player_obj in player_list:
        print(player_obj.name)
