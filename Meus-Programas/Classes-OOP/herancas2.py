class Vehicle:
    class_message = 'This is a message from the Vehicle class!'
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(super().class_message)
    
    def speed_up(self):
        self.speed += 5

class Car(LandVehicle):
    def super_speed(self):
        print('Super speed activated!')
        super().speed_up()
        super().speed_up()
        super().speed_up()


my_car = Car(200, 4)
print(my_car.__dict__)
my_car.super_speed()
print(my_car.__dict__)  

my_car.speed_up()
print(my_car.__dict__)  

print("Speed:", my_car.speed)
print("Wheel Count:", my_car.wheel_count)   
print("Fixe:",my_car.class_message)
