# Creating a class

class Vehicle:

    # class attribute
    class_att = "this is  vehicle class"

    @classmethod
    def class_meth(cls):
        print("This is class method")

    @staticmethod
    def static_method():
        print("This is static method")

    # Create a constructor

    def __init__(self, name, color):
        self.name = name
        self.color = color

     # instance method
    def display_info(self):
        print(f"{vehicle.name}, {vehicle.color} in color")


# Create an Object
vehicle = Vehicle("BMW", "Black")
vehicle.display_info()


# Inheritance
class Car(Vehicle):
    # Constructor Override
    def __init__(self, name, color, fuel_type):
        # access name and color from parent class
        super().__init__(name, color)

        self.fuel_type = fuel_type

    # Override methods
    def display_info(self):
        print(
            f"Name : {self.name}, Color : {self.color}, Fuel type:{self.fuel_type}")


car = Car('CoolCar', 'Red', "patrol")
car.display_info()

print(Vehicle.class_att)
Vehicle.class_meth()
