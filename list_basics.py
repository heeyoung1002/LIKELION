singers = ['김법수', '나얼', '박효신', '이수']

print(singers[2])

print(singers[0:2])

print(len(singers))

print(len(singers[0:2]))

singers.append('BTS')
print(singers)

idols = ['black pink']

singers.extend(idols)
print(singers)

singers[4] = 'Mango'

print(singers)