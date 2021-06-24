#check_assignment이라는 함수를 정의하고 파라미터(입력값)을 name이라 지정한다
def check_assignment (name):
    print(f" {name} 님 안녕하세요")
    print(f"과제는 다 해오셨나요? {name} 님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

check_assignment("Camilla")
check_assignment("Daniel")
check_assignment("Jiho")


def check_assignment (name, assignment):
    print(f" {name} 님 안녕하세요")
    print(f"{assignment} 는 다 해오셨나요? {name} 님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

check_assignment("Camilla", "1st")
check_assignment("Daniel", "2nd")
check_assignment("Jiho", "3rd")