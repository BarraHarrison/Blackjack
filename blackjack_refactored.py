import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']  
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]  

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Deck class
class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        """Create a new deck of cards."""
        return [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle_deck(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def deal_one(self):
        """Deal one card from the deck."""
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 

    def add_card(self, card):
        """Add a card to the hand and adjust the hand's value."""
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
            self.adjust_for_ace()

    def adjust_for_ace(self):
        """Adjust the hand's value if it contains aces and the value is over 21."""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Helper Functions
def deal_initial_cards(deck, player_hand, dealer_hand):
    """Deal two cards to both player and dealer."""
    for _ in range(2):
        player_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

def display_player_hand(player_hand):
    """Display player's hand and its value."""
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')
    print(f"Player's Hand Value: {player_hand.value}")

def display_dealer_hand_hidden(dealer_hand):
    """Display dealer's hand with one card hidden."""
    print("\nDealer's Hand:")
    if len(dealer_hand.cards) > 1:  
        print(" <hidden card>")
        print('', dealer_hand.cards[1])
    else:
        print("Dealer has only one card.")

def display_dealer_hand_full(dealer_hand):
    """Display dealer's full hand and its value."""
    print("\nDealer's Hand:", *dealer_hand.cards, sep='\n ')
    print(f"Dealer's Hand Value: {dealer_hand.value}")

def player_turn(deck, player_hand, dealer_hand):
    """Handle the player's turn, including hitting or standing."""
    while True:
        hit_or_stand = input("\nWould you like to hit or stand? Enter 'h' or 's': ")

        if hit_or_stand[0].lower() == 'h':
            player_hand.add_card(deck.deal_one())
            display_dealer_hand_hidden(dealer_hand)
            display_player_hand(player_hand)

            if check_bust(player_hand):
                return player_busts(player_hand, dealer_hand)

        elif hit_or_stand[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            break
        else:
            print("Sorry, please enter 'h' or 's'.")
            continue

    return False

def dealer_turn(deck, dealer_hand):
    """Handle the dealer's turn according to the game rules."""
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal_one())

def check_bust(hand):
    """Check if a hand has busted (value exceeds 21)."""
    return hand.value > 21

def player_busts(player_hand, dealer_hand):
    print("Player busts! Dealer wins!")
    return True

def player_wins(player_hand, dealer_hand):
    print("Player wins!")
    return True
    
def dealer_busts(player_hand, dealer_hand):
    print("Dealer busts! Player wins!")
    return True

def dealer_wins(player_hand, dealer_hand):
    print("Dealer wins!")
    return True

def push(player_hand, dealer_hand):
    print("It's a draw! Push.")
    return True

def check_winner(player_hand, dealer_hand):
    """Determine and display the winner."""
    if check_bust(dealer_hand):
        return dealer_busts(player_hand, dealer_hand)  
    if dealer_hand.value > player_hand.value:
        return dealer_wins(player_hand, dealer_hand)
    if dealer_hand.value < player_hand.value:
        return player_wins(player_hand, dealer_hand)
    
    return push(player_hand, dealer_hand)


def play_blackjack():
    print("Welcome to Blackjack")

    while True:
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        deal_initial_cards(deck, player_hand, dealer_hand)
        display_dealer_hand_hidden(dealer_hand)
        display_player_hand(player_hand)

        if not player_turn(deck, player_hand, dealer_hand):
            dealer_turn(deck, dealer_hand)
            display_dealer_hand_full(dealer_hand)
            check_winner(player_hand, dealer_hand)

        new_game = input("\nWould you like to play another hand? Enter 'y' or 'n': ")
        if new_game[0].lower() != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_blackjack()
