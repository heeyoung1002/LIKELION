def check_assignment ():
    print("Camilla 님 안녕하세요")
    print("과제는 다 해오셨나요?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

check_assignment()

def check_assignment (name):
    print(f"{name} 님 안녕하세요")
    print(f"과제는 다 해오셨나요 {name}님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

check_assignment("Camilla")

def check_assignment (name):
    print(f"{name} 님 안녕하세요")
    print(f"과제는 다 해오셨나요 {name}님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

real_name = input("What is your name?: ")
check_assignment(f"{real_name}")


def check_assignment (name, assignment):
    print(f"{name} 님 안녕하세요")
    print(f"{assignment}는 다 해오셨나요 {name}님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

check_assignment("Daniel", "Coding")


def check_assignment (name, assignment):
    print(f"{name} 님 안녕하세요")
    print(f"{assignment}는 다 해오셨나요 {name}님?")
    print("고생많으셨습니다. 또 과제를 드리겠습니다")

real_name = input("What is your name: ")
real_assignment = input("What is your assignment: ")

check_assignment(f"{real_name}", f"{real_assignment}")
