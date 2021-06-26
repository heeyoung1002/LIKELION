students = [
    "Danny",
    "Camilla",
    "Sally"
]

#나이값 계산을 위한 함수 선언
def get_age(name):
    born = int(input(f"{name}님 태어나신 년도는 어떻게 되시나요?: ")) #받는 input이 string이기 때문에 int로 형전환
    age = 2021 - born + 1
    return age

for student in students:
    age = get_age(student)
    print(f"{student}님은 올해 {age}입니다.")

