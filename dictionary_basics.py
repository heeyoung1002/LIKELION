#user라는 변수를 선언하여 key : value 로 딕셔너리 
user = {'name' : 'Camilla', 'age' : 30}
print(user ['name'])
print(user ['age'])

#value로써 list를 담고 있는 딕셔너라도 만들 수 있는데
English = {
    'Daniel': ['Wonders', 'Speaking'],
    'James': ['Phoincs', 'Speaking']
}
print(English['Daniel']) #English에서 Daniel 이라는 Key로 접근하면 그 Key의 value가 출력된다

#새로운 Key를 추가하고 싶을 때 
English['Claire'] = ['Writing', 'Speaking']
print(English)

#없는 값은 none이라 돌려준다
print(English.get('지수'))

#있는 값을 key로 받아 올때
print(English.get('Daniel'))

#Dictionary의 key value pair가 몇개 있는지 알려준다
print(len(English))

#원하는 key value를 삭제 가능하다
del(English['Claire'])
print(English)

Claire = {'Claire': ['Writing', 'Speaking']}
Claire2 = {'Claire': ['Writings', 'Speakings']}

#기존 딕셔너리에 새로운 딕셔너리를 더하는 것
English.update(Claire)
print(English)

#원래 딕셔너리를 업데이트하는 것(Key가 같은경우)
print(Claire)
Claire.update(Claire2)
print(Claire) #업에이트한 값 출력
