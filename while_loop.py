password = "likelion"

while True: #while (1)
    
    my_input = input("Password: ")

    if my_input != password:
        print("패스워드를 다시 입력해주세요.")
    else:
        print("로그인 성공!")
        break
