import random
lista = []

def generate_tickets(ticket_count, max_number):
    lista = []
    while len(lista) < ticket_count:
        numero = random.randint(0, max_number)
        if numero not in lista:  # evita repetidos
            lista.append(numero)
    sorti = random.choice(lista)
    return (lista, sorti)

print(generate_tickets(5,100))