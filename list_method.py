numbers = [1,3,5,7,9,2,4,6,8,10]
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

last_number = numbers.pop()
print(last_number) 
print(numbers)

numbers.insert(3,9)
print(numbers)

print(numbers.count(9))

numbers.remove(9) #앞에 있는 item을 지운다 (가장 먼저 발견한 것)
print(numbers)
numbers.remove(9) 
print(numbers)

print(numbers.index(3))
