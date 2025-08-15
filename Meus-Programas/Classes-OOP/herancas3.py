class Animal():
    def __init__(self):
        self.species = 'general'
    
    def produce_sound(self):
        print('General animal sound')
        
    def present(self):
        print('I can do the following sound:')
        self.produce_sound()

class Dog(Animal):
    def __init__(self):
        self.species = 'Canis familiaris'
        
    def produce_sound(self):
        print('woof, woof!')
        
        
my_dog = Dog()
print(my_dog.species)   
print(my_dog.__dict__,"\n")

my_dog.present()

print('\n')
print()
