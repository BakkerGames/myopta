class Vehicle:
    def __init__(self):
        raise NotImplementedError("Do not create raw Vehicle objects.")

    def __str__(self):
        return self.name

class Motorcycle(Vehicle):
    def __init__(self):
        self.name = "Motorcycle"
        self.wheels = 2

class Car(Vehicle):
    def __init__(self):
       self.name = "Car"
       self.wheels = 4
    
mycar = Car()
print(mycar)
print("Number of wheels = {}".format(mycar.wheels))
