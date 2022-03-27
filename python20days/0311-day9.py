import turtle as t

import random



for x in range(5):
    print(random.randint(1, 20))

t.shape("turtle")           # ‘거북이’ 모양의 거북이 그래픽을 사용합니다.

t.speed(0)

 

for x in range(50):        # 거북이를 500번 움직입니다.

    a = random.randint(1, 360) # 1~360에서 아무 수나 골라 a에 저장합니다.

    t.setheading(a)         # 거북이 방향을 a 각도로 돌립니다.

    t.forward(random.randint(1, 20))
    

##
a = random.randint(1, 30) # a에 1~30 사이의 임의의 수를 저장합니다.

b = random.randint(1, 30) # b에 1~30 사이의 임의의 수를 저장합니다.

 

print(a, "+", b, "=")     # 문제를 출력합니다..

x = input()               # 답을 입력받아 x에 저장합니다(문자열로 저장됩니다).

c = int(x)                # 비교를 위해 문자열을 정수로 바꿉니다.

 

if a + b == c:
    print("천재!")    

else:
    print("바보?")
