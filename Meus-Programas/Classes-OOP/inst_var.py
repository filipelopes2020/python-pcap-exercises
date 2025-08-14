class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_pet = Dog('Rex', 5)
print(my_pet.__dict__)

my_pet.colour='black'
print(my_pet.__dict__)

del my_pet.age
print(my_pet.__dict__)

#print(my_pet.name)  # Output: Rex
#print(my_pet.age)   # Output: 5 
