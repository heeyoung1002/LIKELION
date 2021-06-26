class Car:

    def __init__(self, name, color, fuel):
        self.name = name
        self.color = color
        self.fuel = fuel
        self.mileage = 0


    def accel(self):
        self.fuel -= 2
        self.mileage += 10


class Ferrari(Car):
    
    def __init__(self):
        super().__init__("Ferrari", "Rosso Corsa", 50)
        self.slogan = "We are the competition"


class Lamborghini(Car):

    def __init__(self):
        super().__init__("Lamborghini", "Giallo Spica", 40)
        self.slogan = "We are not supercars. We are Lamborghini."

ferrari = Ferrari()
lamborghini = Lamborghini()

print(ferrari)
print(lamborghini)

ferrari.accel()
lamborghini.accel()

print(f"Car count : {Car.count}")

ferrari = Ferrari()
lamborghini = Lamborghini()

print(ferrari)
print(lamborghini)

ferrari.accel()
lamborghini.accel()

print(f"Car count : {Car.count}")