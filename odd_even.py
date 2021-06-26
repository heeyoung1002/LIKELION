#함수 선언 - 짝수일때
def is_even (number):
    if number % 2 == 0:
        return True
    else:
        return False

number_fromuser = int(input("What is the number: "))

result = is_even(number_fromuser)

if result == True:
    print(f"{number_fromuser}는 짝수입니다")
else:
    print(f"{number_fromuser}는 홀수입니다")
