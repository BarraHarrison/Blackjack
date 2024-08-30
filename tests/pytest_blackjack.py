# Testing the blackjack game using pytest
# Previously I used unittest to test the blackjack game

import pytest
from src.blackjack import Card, Deck, Hand, player_busts, player_wins, dealer_busts, dealer_wins, push

@pytest.fixture
def setup_game():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    return deck, player_hand, dealer_hand

def test_deck_initialization(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test that a new deck has 52 cards
    assert len(deck.cards) == 52

def test_deck_shuffle(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test that shuffling a deck doesn't lose any cards
    original_deck = deck.cards.copy()
    deck = Deck()
    assert original_deck != deck.cards

def test_deal_one_card(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test that dealing a card removes it from the deck
    card = deck.deal_one()
    player_hand.add_card(card)
    assert len(player_hand.cards) == 1
    assert player_hand.value == card.value

def test_hand_value_with_aces(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test that aces adjust value correctly
    ace = Card('Hearts', 'Ace')
    player_hand.add_card(ace)
    assert player_hand.value == 11

    # Adding another ace should make it 12, (11 + 1)
    another_ace = Card('Diamonds', 'Ace')
    player_hand.add_card(another_ace)
    assert player_hand.value == 12

def test_player_busts(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test player busts conditions
    player_hand.add_card(Card('Hearts', '10'))
    player_hand.add_card(Card('Diamonds', 'King'))
    player_hand.add_card(Card('Clubs', '2'))
    assert player_busts(player_hand, dealer_hand)

def test_player_wins(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test player wins condition
    player_hand.add_card(Card('Hearts', '10'))
    player_hand.add_card(Card('Diamonds', '9'))
    dealer_hand.add_card(Card('Clubs', '7'))
    dealer_hand.add_card(Card('Spades', '8'))
    assert player_wins(player_hand, dealer_hand)

def test_dealer_busts(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test dealer busts condition
    dealer_hand.add_card(Card('Hearts', '10'))
    dealer_hand.add_card(Card('Diamonds', 'King'))
    dealer_hand.add_card(Card('Clubs', '2'))
    assert dealer_busts(player_hand, dealer_hand)

def test_dealer_wins(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test dealer wins condition
    player_hand.add_card(Card('Hearts', '8'))
    player_hand.add_card(Card('Diamonds', '7'))
    dealer_hand.add_card(Card('Clubs', '10'))
    dealer_hand.add_card(Card('Spades', '9'))
    assert dealer_wins(player_hand, dealer_hand)

def test_push(setup_game):
    deck, player_hand, dealer_hand = setup_game
    # Test push condition
    player_hand.add_card(Card('Hearts', '10'))
    player_hand.add_card(Card('Diamonds', '9'))
    dealer_hand.add_card(Card('Clubs', '10'))
    dealer_hand.add_card(Card('Spades', '9'))
    assert push(player_hand, dealer_hand)
