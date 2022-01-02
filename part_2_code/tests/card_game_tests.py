import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.cardGame = CardGame()
        self.ace = Card("Hearts", 1)
        self.card1 = Card("Spades", 5)
        self.card2 = Card("Diamonds", 7)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace__True(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.ace))

    def test_check_for_ace__False(self):
        self.assertEqual(False, self.cardGame.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.cardGame.highest_card(
            self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 12",
                         self.cardGame.cards_total(self.cards))
