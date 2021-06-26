class Dog: #클라스 선언
    
    count = 0

    def __init__(self, breed, age, size): #클라스를 바탕으로 시렞 인스턴스를 찍어낼때 사용하는것
        self.breed = breed
        self.age = age
        self.size = size
        Dog.count += 1

    def __str__(self):
        return f'{self.breed} {self.age} {self.size}'

    def bark(self):
        self.age -= 2
        self.size += 3

#커스터마이징한 코카스페이널의 클래스
class Cokerspaniel(Dog):

    def __init__(self):
        super().__init__("Cokerspaniel", 7, 8)
        self.color = "Brown"

    def __str__(self):
        return f'{self.breed} {self.age} {self.size} {self.color}'

#커스터마이징한 코기의 클래스
class Corgi(Dog):

    def __init__(self):
        super().__init__("Corgi", 8, 7) 
        self.color = "Light Brown"

    def __str__(self):
        return f'{self.breed} {self.age} {self.size} {self.color}'
    
    def bark(self):
        self.age -= 2
        self.size += 4


print(f'Dog Count: {Dog.count}')

print()
cokerspaniel = Cokerspaniel()
corgi = Corgi()

print(cokerspaniel)
print(corgi)

cokerspaniel.bark()
corgi.bark()

print(cokerspaniel)
print(corgi)

print(f'Dog Count: {Dog.count}')
