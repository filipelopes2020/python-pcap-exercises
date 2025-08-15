class Vehicle():
    pass
        
class Rideable():
    pass
        
class PetrolVehicle(Vehicle):
    pass
        
class Car(PetrolVehicle, Rideable):    
    def __init__(self, fuel_capacity, wheels):
        self.fuel_capacity = fuel_capacity
        self.wheels = wheels    
    


my_vehicle = Vehicle()
my_land_vehicle = Rideable()    
my_car = Car(42,4)

print("Vehicle herda de: ",Vehicle.__bases__)
print("Rideable herda de: ", Rideable.__bases__)
print("PetrolVehicle herda de: ", PetrolVehicle.__bases__)
print("Car herda de: ", Car.__bases__)

#print(Vehicle.__mro__)  
#print(Rideable.__mro__)
#print(PetrolVehicle.__mro__)    
#print(Car.__mro__)

print("isinstance(my_car, Vehicle)? ",isinstance(my_car, Vehicle))  # True

print("Dicionario: ",my_car.__dict__)
print("dir: ",my_car.__dir__)

