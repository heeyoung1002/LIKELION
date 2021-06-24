class Car: #첫글자를 대문자로 지정하고 class를 선언한다
    def __init__(self, name, color, fuel): #클레스에는 데이터와 함수를 저장해서 사용할 수 있다 이를 method라 부른다
        self.name = name
        self.color = color
        self.fuel = fuel
        self.mileage = 0

    def accel(self):
        self.fuel -= 2
        self.mileage += 10

    car = Car("Genesis", "black", 30)
    print(car.name, car.colo, car.fuel)
    car.accel()