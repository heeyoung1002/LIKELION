age = int(input('나이가 어떻게 되세요?: '))

if age < 30:
    print('30대 미만입니다.')
elif 30 <= age <= 32:
    print('30대 초반입니다.')
elif 32 < age <= 36:
    print('30대 중반입니다.')
elif 36 < age <= 39:
    print('30대 후반입니다.')
else:
    print('40대 이상입니다.')