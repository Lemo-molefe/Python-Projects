class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road 🚗."

class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky ✈️."

class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on the water ⛵."

class Bicycle(Vehicle):
    def move(self):
        return f"{self.name} is pedaling down the path 🚴."

# Create instances of each vehicle
car = Car("Sedan")
plane = Plane("Jetliner")
boat = Boat("Sailboat")
bicycle = Bicycle("Mountain Bike")

# Demonstrating polymorphism
vehicles = [car, plane, boat, bicycle]

for vehicle in vehicles:
    print(vehicle.move())
