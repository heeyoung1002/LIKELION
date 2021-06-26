#list 선언
numbers = [1,3,5,7,9,2,4,6,8,10]
print(numbers)

#list를 순서대로 배열
numbers.sort()
print(numbers)

#숫자를 거꾸로 배열
numbers.reverse()
print(numbers)

#마지막숫자를 없애기
last_number = numbers.pop()
print(last_number) 
print(numbers)

#3번째에 9를 넣기 
numbers.insert(3,9)
print(numbers)

print(numbers.count(9))

#앞에 있는 item을 지운다 (가장 먼저 발견한 것)
numbers.remove(9) 
print(numbers)
numbers.remove(9) 
print(numbers)

print(numbers.index(3))
