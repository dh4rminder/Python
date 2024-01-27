import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deckOfCards = []

for suit in suits:
    for rank in ranks:
        deckOfCards.append(rank + " of " + suit)
#        print(f'{rank} of {suit}')

# print(deckOfCards)

print(f'There are {len(deckOfCards)} cards in the deck.')

print ("Dealing ...")

dealtCards = []
count = 0

while count < 5:
    
    dealtCard = random.randint(1, (52-count))
    count += 1
    #print(deckOfCards[dealtCard])
    dealtCards.append(deckOfCards[dealtCard])
    #print(f'Dealt cards {dealtCards}')

    deckOfCards.remove(deckOfCards[dealtCard])
    #print(len(deckOfCards))

print(f'There are {52-count} cards in the deck')
print("Player has the following cards in their hand:")
print(dealtCards)