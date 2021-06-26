class Dog: #클라스 선언
    count = 0
    def __init__(self, breed, color, size): #클라스를 바탕으로 시렞 인스턴스를 찍어낼때 사용하는것
        self.breed = breed
        self.color = color
        self.size = size
        Dog.count += 1

    def __str__(self):
        return f'{self.breed} {self.color} {self.size}'
        

    #클라스의 모든 메소드는 첫 파라미터로 self를 가진다
    def bark(self):
        self.color -= 2
        self.size += 3

CokerSpaniel = Dog("Coker Spaniel", 10, 7)
Corgi = Dog("Corgi", 8, 6)

print(CokerSpaniel)
CokerSpaniel.bark()
print(CokerSpaniel)

print(f"DogCount: {Dog.count}")