class Dog:
    latin = 'canis'
    def __init__(self, colour = 'brown'):
        self.colour = colour
        Dog.latin += colour
    
first = Dog()
second = Dog('red')
third = Dog('white')
print(second.latin)

