import unittest

import player_init


class PlayerInitTestCase(unittest.TestCase):
    """Tests for 'player_init.py'"""

    def setUp(self):
        self.player = player_init.Player('Test Player')

    def test_player_init(self):
        self.assertEqual(self.player.name, 'Test Player')
        self.assertEqual(len(self.player.deck), 5)
        self.assertEqual(len(self.player.hand), 5)
        self.assertEqual(self.player.discard_pile, [])
        self.assertEqual(
            sorted(self.player.deck + self.player.hand),
            ['Copper', 'Copper', 'Copper', 'Copper', 'Copper', 'Copper',
             'Copper', 'Estate', 'Estate', 'Estate'])

    def test__turn(self):
        pass

    def test__turn_setup(self):
        pass

    def test__action_phase(self):
        pass

    def test__buy_phase(self):
        pass

    def test__cleanup(self):
        pass

    def test_play_card(self):
        pass

    def test_do_action(self):
        pass

    def test_print_hand(self):
        pass

    def test_gain_card(self):
        pass

    def test_draw_cards(self):
        pass

    def test__shuffle(self):
        pass


if __name__ == '__main__':
    unittest.main()
