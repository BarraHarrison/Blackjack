# test_helpers file is for when your codebase grows
# You can test specific parts of the codebase
# More detailed and focussed tests

import pytest
from src.blackjack import Card, Deck, Hand, calculate_hand_value, deal_initial_cards, check_bust

@pytest.fixture
def setup_hands():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    return deck, player_hand, dealer_hand

def test_calculate_hand_value():
    hand = Hand()
    hand.add_card(Card('Hearts', 'Ace'))
    hand.add_card(Card('Diamonds', '7'))
    assert calculate_hand_value(hand) == 18

    hand.add_card(Card('Clubs', '5'))
    assert calculate_hand_value(hand) == 13 # Ace now counts as 1

    hand.add_card(Card('Spades', '10'))
    assert calculate_hand_value(hand) == 23 # This would result in a bust

def test_deal_initial_cards(setup_hands):
    deck, player_hand, dealer_hand = setup_hands
    deal_initial_cards(deck, player_hand, dealer_hand)

    assert len(player_hand.cards) == 2
    assert len(dealer_hand.cards) == 2
    assert len(deck.cards) == 48 # 52 - 4 cards dealt

def test_check_bust():
    hand = Hand()
    hand.add_card(Card('Hearts', '10'))
    hand.add_card(Card('Diamonds', 'King'))
    hand.add_card(Card('Clubs', '2'))

    assert check_bust(hand) == True # Hand value is 22, so it's a bust

    hand = Hand()
    hand.add_card(Card('Hearts', '10'))
    hand.add_card(Card('Diamonds', '8'))

    assert check_bust(hand) == False # Hand value is 18, so not a bust
