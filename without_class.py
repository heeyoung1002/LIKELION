ferrari = {
    "name" : "Ferrari", 
    "color" : "Rosso Corsa",
    "fuel" : 50,
    "mileage": 0
}

lamborghini = {
    "name" : "lamborghini", 
    "color" : "Giallo Spica",
    "fuel" : 40,
    "mileage": 0
}


def ferrari_accel():
    ferrari["fuel"] -= 2
    ferrari["mileage"] += 10

def lamborghini_accel():
    lamborghini["fuel"] -= 3
    lamborghini["mileage"] +=12


print(ferrari)
print(lamborghini)

ferrari_accel()
lamborghini_accel()

print(ferrari)
print(lamborghini)
