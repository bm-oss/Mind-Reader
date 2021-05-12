import pydealer

#mind reader using pydealer module

deck = pydealer.Deck()
hand = pydealer.Stack()

'''shuffle deck'''
deck.shuffle()


'''initial 4 cards'''
dealt_cards = deck.deal(4)

'''new hand with extra random card added'''
hand.add(dealt_cards[0:3])
hand.add(deck.deal(1))
hand.shuffle()



print("old hand")
print(dealt_cards)
print("new hand")
print(hand)