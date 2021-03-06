#0311
#day10


#while 명령으로 반복해서 숫자를 출력하는 프로그램
# while 판단 조건:       # 판단 조건이 True인 동안
#
#반복 실행할 내용    반복 실행할 내용 부분을 반복한다.

print("[1-10]")
s = 0
x = 1

while x <= 10:    # x가 10 이하인 동안 반복합니다(1에서 10까지 실행)

    s = s + x                  # s에 x를 더합니다.

    print("x:", x, " sum:", s) # 현재 x 값과 s 값을 출력합니다.

    x = x + 1     # x에 1을 더해서 저장합니다.



#숫자를 추측해서 맞히는 프로그램
import random

n = random.randint(1, 30)  # 1~30 사이에 있는 임의의 수를 뽑습니다.

while True:                # 영원히 반복합니다.

    x = input("맞혀 보세요? ")
    g = int(x)             # 입력받은 값을 비교할 수 있도록 정수로 바꿉니다.

    if g == n:             # 사용자가 추측한 값과 임의의 수가 같으면 정답입니다.
        print("정답")
        break              # 정답을 맞히면 break로 while 반복 블록을 빠져 나갑니다.

    if g < n:
        print("너무 작아요.")    

    if g > n:
        print("너무 커요.")
