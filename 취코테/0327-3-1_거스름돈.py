#거스름돈 동전 개수 세기
N=int(input(""))
if N<0:
    N=int(input("type larger than 0"))

#거스름돈은 10의 배수
    
n500, n100, n50, n10 = 0,0,0,0
while N>=500:
    N=N-500
    n500=n500+1

while N>=100:
    N=N-100
    n100 = n100 + 1

while N>=50:
    N=N-50
    n50 = n50+1

while N>0:
    N=N-10
    n10 = n10 + 1


print(n500,n100,n50,n10)
print(n500+n100+n50+n10)


