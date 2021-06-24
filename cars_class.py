class Car:
    def __init__(self, name, color, fuel):
        print("자동차를만듭니다")
        self.name = name
        self.color = color
        self.fuel = fuel
        self.mileage = 0

Genesis = Car("Genesis", "black", 50)
Ferrari = Car("Ferrari", "Rosso Corsa", 40)

print(Genesis)
print(Ferrari)
