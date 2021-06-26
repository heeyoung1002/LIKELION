#if문 안에 if문

looks_young = True 

if looks_young: # (1)
    age = int(input('동안이시네요, 몇 살이세요?(ex. 19): '))

    if age >= 20: # (2)
        print('소주 한 병 1800원입니다.')
    else:
        print('미성년자에게 술은 판매하지 않습니다.')

    print('감사합니다~ 또 오세요 ^^')

else:
    print('소주 한 병 1800원입니다.')
