import turtle as t
import random


def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading() #current angle
    while t.ycor() > 0:  #make line as curve. but not exactly curve. pretend to curve
        t.forward(15)
        t.right(5)

    d = t.distance(target,0) #get distance b/w turtle and target
    t.sety(random.randint(10,100))

    if d< 25:  #success
        t.color("blue")
        t.write("Good!",False,"center",("",15) )

    else:   #fail
        t.color("red")
        t.write("Bad",False,"center",("",15) )

ang=0       
t.color("black")
t.goto(-200,10) #set to start point
t.setheading(ang) #set to start angle


#draw land
t.goto(-300,0)
t.down()
t.goto(300,0)

# #목표 지점을 설정하고 그립니다.

target = random.randint(50, 150) # 목표 지점을 50~150 사이에 있는 임의의 수로 지정합니다.

t.pensize(3)

t.color("green")

t.up()

t.goto(target - 25, 2)

t.down()

t.goto(target + 25, 2)

 

# #거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌립니다.

t.color("black")

t.up()

t.goto(-200, 10)

t.setheading(20)
t.shape("turtle")
 

# 거북이가 동작하는 데 필요한 설정을 합니다.

t.onkeypress(turn_up, "Up")      # ↑를 누르면 turn_up 함수를 실행합니다.

t.onkeypress(turn_down, "Down")  # ↓를 누르면 turn_down 함수를 실행합니다.

t.onkeypress(fire, "space")      # SpaceBar를 누르면 fire 함수를 실행합니다.

t.listen()                       # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
