import turtle as t

 

t.bgcolor("black")       # 배경색을 검은색으로 지정합니다.

t.speed(0)               # 거북이 속도를 가장 빠르게 지정합니다.

 

for x in range(200):     # for 반복 블록을 200번 실행합니다.
    if x % 3 == 0:       # 번갈아 가면서 선 색을 바꿉니다.
        t.color("red")

    if x % 3 == 1:
        t.color("yellow")

    if x % 3 == 2:  
        t.color("blue")

    t.forward(x * 2)     # x*2만큼 앞으로 이동합니다(반복하면서 선이 점점 길어집니다).

    t.left(119)          # 거북이를 119도 왼쪽으로 회전합니다.




import turtle as t

 

def turn_right():                 # 오른쪽으로 이동하는 함수
    t.setheading(0)               # t.seth(0)으로 입력해도 됩니다.
    t.forward(10)                 # t.fd(10)으로 입력해도 됩니다.

 
def turn_up():                    # 위로 이동하는 함수
    t.setheading(90)
    t.forward(10)

 
def turn_left():                  # 왼쪽으로 이동하는 함수
    t.setheading(180)
    t.forward(10)

def turn_down():                  # 아래로 이동하는 함수
    t.setheading(270)
    t.forward(10)

def blank():                      # 화면을 지우는 함수  
    t.clear()


t.shape("turtle")                 # 거북이 모양을 사용합니다.

t.speed(0)                        # 거북이 속도를 가장 빠르게 지정합니다.

t.onkeypress(turn_right, "Right") # →를 누르면 turn_right 함수를 실행합니다.

t.onkeypress(turn_up, "Up")

t.onkeypress(turn_left, "Left")

t.onkeypress(turn_down, "Down")

t.onkeypress(blank, "Escape")     # ESC를 누르면 blank 함수를 실행합니다.

t.listen()                        # 거북이 그래픽 창이 키보드 입력을 받습니다.



import turtle as t

t.speed(0)              # 거북이의 속도를 가장 빠르게 지정합니다.

t.pensize(2)            # 펜 굵기를 2로 지정합니다.

t.hideturtle()          # 거북이를 화면에서 숨깁니다.

t.onscreenclick(t.goto) # 마우스 버튼을 누르면 t.goto 함수를 호출합니다.

             # 그 위치로 거북이가 움직이면서 선을 그립니다.
