# Tests

import unittest
from blackjack import Card, Deck, Hand, player_busts, player_wins, dealer_busts, dealer_wins, push

class TestBlackjackGame(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def test_deck_initialization(self):
        # Test that a new deck has 52 cards
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_shuffle(self):
        # Test that shuffling a deck doesn't lose any cards
        original_deck = self.deck.cards.copy()
        self.deck = Deck()
        self.assertNotEqual(original_deck, self.deck.cards)

    def test_deal_one_card(self):
        # Test that dealing a card removes it from the deck
        card = self.deck.deal_one()
        self.player_hand.add_card(card)
        self.assertEqual(len(self.player_hand.cards), 1)
        self.assertEqual(self.player_hand.value, card.value)

    def test_hand_value_with_aces(self):
        # Test that aces adjust value correctly
        ace = Card('Hearts', 'Ace')
        self.player_hand.add_card(ace)
        self.assertEqual(self.player_hand.value, 11)

        # adding another ace should make it 12, (11 + 1)
        another_ace = Card('Diamonds', 'Ace')
        self.player_hand.add_card(another_ace)
        self.assertEqual(self.player_hand.value, 12)

    def test_player_busts(self):
        # Test player busts conditions
        self.player_hand.add_card(Card('Hearts', '10'))
        self.player_hand.add_card(Card('Diamonds', 'King'))
        self.player_hand.add_card(Card('Clubs', '2'))
        self.assertTrue(player_busts(self.player_hand, self.dealer_hand))

    def test_player_wins(self):
        # Test player wins condition
        self.player_hand.add_card(Card('Hearts', '10'))
        self.player_hand.add_card(Card('Diamonds', '9'))
        self.dealer_hand.add_card(Card('Clubs', '7'))
        self.dealer_hand.add_card(Card('Spades', '8'))
        self.assertTrue(player_wins(self.player_hand, self.dealer_hand))

    def test_dealer_busts(self):
        # Test dealer busts condition
        self.dealer_hand.add_card(Card('Hearts', '10'))
        self.dealer_hand.add_card(Card('Diamonds', 'King'))
        self.dealer_hand.add_card(Card('Clubs', '2'))
        self.assertTrue(dealer_busts(self.player_hand, self.dealer_hand))

    def test_dealer_wins(self):
        # Test dealer wins condition
        self.player_hand.add_card(Card('Hearts', '8'))
        self.player_hand.add_card(Card('Diamonds', '7'))
        self.dealer_hand.add_card(Card('Clubs', '10'))
        self.dealer_hand.add_card(Card('Spades', '9'))
        self.assertTrue(dealer_wins(self.player_hand, self.dealer_hand))

    def test_push(self):
        # Test push condition
        self.player_hand.add_card(Card('Hearts', '10'))
        self.player_hand.add_card(Card('Diamonds', '9'))
        self.dealer_hand.add_card(Card('Clubs', '10'))
        self.dealer_hand.add_card(Card('Spades', '9'))
        self.assertTrue(push(self.player_hand, self.dealer_hand))

if __name__ == '__main__':
    unittest.main()

    