# External module import
import pydealer



def ascii_hand(hand):
    """
        Function that converts pydealer cards into
        an ascii image of the card.
    :param hand: An array of pydealer() cards.
    :return: An ascii representation of a card
    """

    # Instantiating variables
    ascii_hand = ""
    rank = " "
    card_suit = " "

    # Defining suits ascii code
    hearts = "\u2665"
    diamonds = "\u25C6"
    spades = "\u2663"
    clubs = "\u2663"

    # Iterates through array and assigns card_print and suit a value
    for card in hand:
        if card.value in ("King", "Queen", "Jack", "Ace"):
            rank = card.value[0]
        else:
            rank = card.value
        if card.suit == "Hearts":
            card_suit = hearts
        elif card.suit == "Diamonds":
            card_suit = diamonds
        elif card.suit == "Spades":
            card_suit = spades
        else:
            card_suit = clubs

        if rank == "10":
            card_print = f"|{rank}  {card_suit}|"
        else:
            card_print = f"| {rank}  {card_suit}|"

        # Adds the new card to the ascii hand
        ascii_hand += card_print
    print(" ______" * (len(hand)))
    print(ascii_hand)
    print("|     |" * (len(hand)))
    print("|_____|" * (len(hand)))

# initialise a deck of cards
deck = pydealer.Deck()

# initialise a second deck of cards called a "hand"
hand = pydealer.Stack()

# shuffle the deck
deck.shuffle()

# randomly select 4 cards from the intial deck
dealt_cards = deck.deal(4)

# print the initial deck
ascii_hand(dealt_cards)

memory = input(
    "Memorise a Card from the given options and i will make it disappear!\nPress the enter key when you are ready! ")

# second deck of card uses 3 cards from the initial deck
hand.add(dealt_cards[0:3])

# adds one random card to the new deck
hand.add(deck.deal(1))

# shuffle the second deck
hand.shuffle()

# print the second deck
ascii_hand(hand)

mindFreak = input("Did I manage to remove the card you were thinking of?(y or n): ")

if mindFreak == "y":
    print("I am the best Mind-Reader!!!")
else:
    print("I will try again :(")
