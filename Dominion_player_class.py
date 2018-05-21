class Player():
    def __init__(self, name):
        self.player_name = name
        self.player_deck = ['Estate', 'Estate', 'Estate', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper']
        self.player_handsize = 5
        self.player_turncount = 0
        self.player_activeturn = 0
        self.player_baseactions = 1
        self.player_remainingactions = 0
        self.player_purchasehistory = []
