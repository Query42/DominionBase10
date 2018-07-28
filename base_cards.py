"""Contains basic Card class, basic cards (Victory, Treasure, Curse), and base card map."""

#Version 1.0 5/24/2018

class Card():
    """Card template class. Base cards are here; Kingdom cards inherit from this."""
    def __init__(
            self, card_types, buy_cost, text, subtype=None, vp_value=None, coin_value=None
        ):
        self.types = card_types
        self.cost = buy_cost
        self.text = text
        self.subtype = subtype
        self.vp_value = vp_value
        self.coin_value = coin_value

estate = Card('Victory', 2, 'Worth 1 VP', vp_value=1)
duchy = Card('Victory', 5, 'Worth 3 VP', vp_value=3)
province = Card('Victory', 8, 'Worth 6 VP', vp_value=6)

copper = Card('Treasure', 0, '$1', coin_value=1)
silver = Card('Treasure', 3, '$2', coin_value=2)
gold = Card('Treasure', 6, '$3', coin_value=3)

curse = Card('Curse', 0, 'Worth -1 VP', vp_value=-1)

card_map = {
    'Estate': estate,
    'Duchy': duchy,
    'Province': province,
    'Copper': copper,
    'Silver': silver,
    'Gold': gold,
    'Curse': curse
}
