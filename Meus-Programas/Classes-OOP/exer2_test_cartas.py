import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Escolhe aleatoriamente um elemento de cada lista
random_suit = random.choice(suits)
random_value = random.choice(values)

# Junta os dois elementos numa lista
random_card = [random_suit, random_value]

print(random_card)
