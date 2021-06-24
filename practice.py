names = ['Camilla', 'Prada', 'Bagi']

def check_homework (name, assignment):
    print(f"{name}님 숙제는 다 하셨나요?")
    print(f"{name}님 항상 화이팅입니다")
    print(f"다음번 과제는 {assignment}입니다")

for name in names:
    real_name = input("What is your name?")
    real_assignment = input("What is assignment?")
    check_homework(real_name, real_assignment)

    