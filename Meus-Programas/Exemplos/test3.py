import random

#print(random.seed(0))
print(random.random())  # Gera um número aleatório entre 1 e 10
print(random.random())
print(random.random())

random.seed(0) 
numbers = [1,2,3,4,5,6,7,8,9,10]
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print(random.choice(numbers))  # Escolhe um número aleatório da lista
print(random.choice(names))  # Escolhe um número aleatório da lista
random.seed()

 # Define a semente para reprodutibilidade
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    #print(random.choice(numbers))  # Escolhe um número aleatório da lista
    print(random.sample(numbers, 3))  # Escolhe 3 números aleatórios da lista