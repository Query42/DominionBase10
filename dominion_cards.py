from base_cards import Card


class Smithy(Card):
    def action(player):
        player.hand += draw_cards(player, 3)
        return

class Cellar(Card):
    def action(player):
        debug_count = len(player.hand)
        player.actions_left += 1
        discarded_cards = []
        while len(player.hand) > 0:
            player.print_hand(player)
            print("What would you like to discard?")
            print(
                "(Type the card name, 'Cancel' to cancel, or 'Done' to stop discarding.)"
                )
            discard = input("> ")
            if str(discard).lower() == 'cancel': 
                discarded_cards.append('Cellar')
                player.hand += discarded_cards #return discarded cards and cellar to hand
                return
            elif str(discard).lower() == 'done':
                continue
            elif str(discard).capitalize() in player.hand:
                player.hand.remove(discard)
                discarded_cards.append(discard)
            else:
                print("Sorry, that's not a card in your hand.")
        player.discard_pile += discarded_cards
        if len(player.hand) == 0:
            print("All cards discarded!")
        print("Drawing {} cards.".format(len(discarded_cards)))
        player.hand += draw_cards(player, len(discarded_cards))
        assert len(player.hand) == debug_count, "Cellar lost a card."
        return

class Village(Card):
    pass

class Thief(Card):
    pass

class Market(Card):
    pass

class Woodcutter(Card):
    pass

class Remodel(Card):
    pass

class Workshop(Card):
    pass

class Mine(Card):
    pass

class Library(Card):
    pass
