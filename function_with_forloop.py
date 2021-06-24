#students라는 변수를 같은 리스트
students = [
    "James",
    "Daniel",
    "BROWN",
    "Sally",
]
#check_assignment 함수
def check_assignment (name):
    print(f"{name} 님 안녕하세요")
    print(f"과제는 다 해오셨나요 {name}님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

#studens 라는 리스트안에 있는 변수하나하나가 student이고, 이것들이 인자가 되어서 check_assignment 파라미터에 적용되서 출력된다
for student in students:
    check_assignment(student)