def hello(name):   # hello 함수를 정의합니다.
    print("Hello Python!")
    print("Hello ",name,"!")
    print("Hello Python!")


def square(n):
    return n*n

def triangle(a,h):
    return a*h/2


def sum_fun(n):
    s=0
    for i in range(1,n+1):
        s = s+i
    return s
        

def factorial(n):
    s = 1
    for i in range(1,n+1):
        s = s*i

    return (s)


 

def polygon2(n, a=50):
    for x in range(n): # n번 반복합니다.
        t.forward(a)    # 거북이를 a만큼 앞으로 이동합니다.

        t.left(360/n)   # 거북이를 360/n만큼 왼쪽으로 회전합니다.

# 그림을 그리지 않고 거북이를 100만큼 이동합니다.

t.up()

t.forward(100)

t.down()
