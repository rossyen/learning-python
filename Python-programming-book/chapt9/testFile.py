import random

def hasAce(value):
    return value == 1

def cardDealing():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardScore = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cardDealt = random.choice(cards) # Takes a random card from cards
    indexCards = cards.index(cardDealt) 
    indexScore = cardScore[indexCards] # Takes the index from cards to find value of card
    return cardDealt, indexScore

def aceOnHand(cardsOnHand):
    listCardsOnHand = cardsOnHand
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardScore = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    newCards = []
    for i in listCardsOnHand:
        newCards.append(cardScore[cards.index(i)])
    return sum(newCards)
    
def handBusted(handValue):
    return handValue <= 21 

def simulatePlayers():
    cardsOnHand = []
    card1Face, card1Value = "A", 1 #cardDealing()
    if hasAce(card1Value) == True:
        card1Value = 11
    print(f"CardValue: {card1Value} | CardFace: {card1Face}")
    cardsOnHand.append(card1Face)
    
    card2Face, card2Value = cardDealing()
    if hasAce(card2Value) == True:
        card2Value = 11
    print(f"CardValue: {card2Value} | CardFace: {card2Face}")
    cardsOnHand.append(card2Face)

    sumCards = card1Value + card2Value
    newSumCardsOnHand = 0
    
    if handBusted(sumCards) == True:
        hitOrPass = input(f"Do you wan to hit or pass? (type 'h' or 'p')")
        while hitOrPass == 'h':
            newCardFace, newCardValue  = cardDealing()
            cardsOnHand.append(newCardFace)
            if sumCards <= 10:
                if hasAce(newCardValue):
                    newCardValue = 11
            print(f"CardValue: {newCardValue} | CardFace: {newCardFace}")
            sumCards = sumCards + newCardValue
            
            if handBusted(sumCards) == False:
                newSumCardsOnHand = aceOnHand(cardsOnHand)
                if handBusted(newSumCardsOnHand) == False:
                    print(f"Player busted. Hand score new sum = {newSumCardsOnHand}")                
                else:
                    print(f"Player busted. Hand score sum cards = {sumCards}")
                    
            hitOrPass = input(f"Do you wan to hit or pass? (type 'h' or 'p')")
        
        if hitOrPass == 'p':
            if newSumCardsOnHand == 0:
                print(f"\nYou stand with card score of  old sum {sumCards}| cards on hand {cardsOnHand}")
            else:
                print(f"\nYou stand with card score of new sum{newSumCardsOnHand} | cards on hand {cardsOnHand}")

simulatePlayers()



