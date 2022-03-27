#day5
s = 0
for i in range(11):
    s = s+i
print(s)

#day6
import turtle as t

# 오각형을 그립니다(다른 값을 입력하면 다른 도형을 그립니다).

t.speed(10)
n = 5               
t.color("purple")
t.shape("turtle")
t.begin_fill()      # 색칠할 영역을 시작합니다.

for x in range(n):  # n번 반복합니다.
    t.forward(50)   # 거북이가 50만큼 앞으로 이동합니다.

    t.left(360/n)   # 거북이가 360/n만큼 왼쪽으로 회전합니다.

t.end_fill()


 # 원을 50개 그립니다.
n = 50                

t.bgcolor("black")     # 배경색을 검은색으로 지정합니다.
t.color("green")       # 펜 색을 녹색으로 지정합니다.
t.speed(0)             # 거북이 속도를 가장 빠르게 지정합니다.

for x in range(n):     # n번 반복합니다.
    t.circle(80)       # 현재 위치에서 반지름이 80인 원을 그립니다.
    t.left(360/n)      # 거북이가 360/n만큼 왼쪽으로 회전합니다.


# 거북이가 왼쪽으로 회전할 각도를 지정합니다(값을 바꿀 수 있음).
angle = 89            

t.color("yellow")     # 펜 색을 노란색으로 지정합니다.

t.speed(0)            # 거북이 속도를 가장 빠르게 지정합니다.

for x in range(200):  # x 값을 0에서 199까지 바꾸면서 200번 실행합니다.
    t.forward(x)      # x만큼 앞으로 이동합니다(실행을 반복하면서 선이 길어짐).
    t.left(angle)     # 거북이가 왼쪽으로 89도 회전합니다.
