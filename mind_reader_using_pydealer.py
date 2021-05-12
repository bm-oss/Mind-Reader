import pydealer

#mind reader using pydealer module

deck = pydealer.Deck()
hand = pydealer.Stack()

'''shuffle deck'''
deck.shuffle()


'''initial 4 cards'''
dealt_cards = deck.deal(4)
memory = input("Memorise a Card from the given options and i will make it disappear!\nPress the enter key when you are ready! ")

'''new hand with extra random card added'''
hand.add(dealt_cards[0:3])
hand.add(deck.deal(1))
hand.shuffle()


print(dealt_cards)

mindFreak = input("Did I manage to remove the card you were thinking of?(y or n): ")

print(hand)

if mindFreak == "y":
  print("I am the best Mind-Reader!!!")
else:
  print("I will try again :(")
