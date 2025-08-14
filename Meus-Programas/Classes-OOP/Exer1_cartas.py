import random

class Deck:
  def __init__(self, cards):
    self.cards = cards
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
              
  def shuffle(self):
    # Escolhe aleatoriamente um elemento de cada lista
    random_suit = random.choice(suits.sort())
    random_value = random.choice(values.sort())    
    # Junta os dois elementos numa lista
    return [random_suit, random_value]

class Card:
  def __init__(self, suite, value):
    self.suite = suite
    self.value = value          
  def present(self):
    return f"{self.value} of {self.suite}"
			
#mycard = Card('Hearts', '10')
#print(mycard.present())

mydeck = Deck([])