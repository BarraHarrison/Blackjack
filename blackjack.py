import random

# Card deck and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 # Keep track of the aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
            self.adjust_for_ace()

    def adjust_for_ace(self):
        # adjust if the hand value goes over 21 and there's an ace
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Function to display hands
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <hidden card>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Player's Hand Value: {player.value}")

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print(f"Dealer's Hand Value: {dealer.value}")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Player's Hand Value: {player.value}")

# Game Logic Functions
def player_busts(player, dealer):
    print("Player busts! Dealer wins!")
    return True

def player_wins(player, dealer):
    print("Player wins!")
    return True

def dealer_busts(player, dealer):
    print("Dealer busts! Player wins!")
    return True

def dealer_wins(player, dealer):
    print("Dealer wins!")
    return True

def push(player, dealer):
    print("It's a draw! Push.")
    return True

# Main Game Function
def play_blackjack():
    print("Welcome to BlackJack")

    while True:
        # Create and shuffle deck, deal two cards to each
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

        # Show cards
        show_some(player_hand, dealer_hand)

        playing = True

        while playing: # Player's turn
            hit_or_stand = input("\nWould you like to hit or stand? Enter 'h' or 's': ")

            if hit_or_stand[0].lower() == 'h':
                player_hand.add_card(deck.deal_one())
                show_some(player_hand, dealer_hand)

                if player_hand.value > 21:
                    player_busts(player_hand, dealer_hand)
                    playing = False

            elif hit_or_stand[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                playing = False
            else:
                print("Sorry, please enter 'h' or 's'.")
                continue

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                dealer_hand.add_card(deck.deal_one())

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand)
            else:
                push(player_hand, dealer_hand)

        new_game = input("\nWould you like to play another hand? Enter 'y' or 'n': ")
        if new_game[0].lower() != 'y':
            print("Thanks for playing!")
            break

# Run the game
# This was amended for the test_blackjack file
if __name__ == "__main__":
    play_blackjack()
