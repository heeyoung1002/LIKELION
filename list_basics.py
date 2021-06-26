#list 선언
singers = ['김법수', '나얼', '박효신', '이수']

#두번째 index 출력
print(singers[2])

#0이상 2미만까지 출력
print(singers[0:2])

#list의 길이 출력
print(len(singers))

print(len(singers[0:2]))

singers.append('BTS')
print(singers)

idols = ['black pink']

singers.extend(idols)
print(singers)

singers[4] = 'Mango'

print(singers)
