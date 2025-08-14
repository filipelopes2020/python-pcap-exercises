class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        self.wheel_count = wheel_count
        Vehicle.__init__(self, speed)
        #super().__init__(speed)  # Alternative way to call the parent constructor

class Car(LandVehicle):
    def __init__(self, model):
        self.model = model
        LandVehicle.__init__(self, speed, wheel_count=)
    #def __init__(self, colour):
    #    self.colour = colour
    
#my_car = Car(200,3)
my_car = Car("mazda",5)
print(my_car.__dict__)

#print(my_car.speed)
#print(my_car.wheel_count)
#print(my_car.__dir__())
