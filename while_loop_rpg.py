# RPG 게임
kill_count = 0

#10보다 작았을 때 whila문이 돈다 (10이되면 컨디션을 통과하지 못한다)
while (kill_count<10):
    print("몬스터를 더 잡아야합니다")
    kill_count += 1

    if kill_count == 10:
        print("level up")