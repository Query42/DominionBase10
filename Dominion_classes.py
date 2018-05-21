class Player(object):
    def __init__(self, name='Anonymous'):
        self.name = name
        self.hand = []
        self.deck = ['Estate', 'Estate', 'Estate', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper',]
        self.handsize = 5
        self.turncount = 0
        self.actions_remaining = 1
        self.remainingactions = 0
        self.gained_last_turn = []


class Card(object):
    def __init__(self, cardtype, cardsubtype, costtobuy, vpvalue):
        self.cardtype = cardtype
        self.cardsubtype = cardsubtype
        self.cardcost = costtobuy
        self.cardvpvalue = vpvalue

