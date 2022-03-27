#https://thebook.io/007026/day19/04/01/
import random

total = 1000000                    # 실험을 백만 번 합니다.
ev = 0                             # 뽑힌 점이 사분원 안에 있는 횟수


for i in range(total):              # total 횟수만큼 반복
    x = random.random()             # 0.0 <= x < 1.0 인 실수 (예: x = 0.878313)
    y = random.random()             # 0.0 <= y < 1.0 인 실수 (예: y = 0.398144)

    if x * x + y * y <= 1.0:            # 원점과의 거리가 1 이하인 경우

        ev = ev + 1                     # 사분원 안에 있는 횟수를 1 증가시킵니다.

print((ev / total) * 4)             # ev를 total로 나눈 평균에 4를 곱해서 출력합니다.

print((ev / total) /1) 



for i in range(total):              # total 횟수만큼 반복
    x = random.random()             # 0.0 <= x < 1.0 인 실수 (예: x = 0.878313)
    y = random.random()             # 0.0 <= y < 1.0 인 실수 (예: y = 0.398144)

    if (x**2 + y**2)**(0.5) <= 1.0:            # 원점과의 거리가 1 이하인 경우

        ev = ev + 1                     # 사분원 안에 있는 횟수를 1 증가시킵니다.

print((ev / total)) 


