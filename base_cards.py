class Card():
    def __init__(
        self, card_types, buy_cost, subtype=None, vp_value=None, coin_value=None
        ):
        self.types = card_types
        self.cost = buy_cost
        self.subtype = subtype
        self.vp_value = vp_value
        self.coin_value = coin_value
        