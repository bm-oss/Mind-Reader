import random

names = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["Spades","Hearts","Clubs","Diamonds"]


def createADeck():
  deck = []
  for s in suits:
    for v in names:
      deck.append((v,"of",s))
  return deck
  
deck = createADeck()

random.shuffle(deck)

initialFour = random.sample(deck, 4)

print(initialFour)

memory = input("Memorise a Card from the given options and i will make it disappear! \nPress the enter key when you are ready! ")

random.shuffle(initialFour)
oldThree = initialFour[0:3]
newCard = random.sample(deck, 1)
print(oldThree + newCard)

mindFreak = input("Did I manage to remove the card you were thinking of?(y or n): ")

if mindFreak == "y":
  print("I am the best Mind-Reader!!!")
else:
  print("I will try again :(")




