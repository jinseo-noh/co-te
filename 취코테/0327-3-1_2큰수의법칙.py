#주어진 숫자 읽기
#space 로 나누기..
# M >= K
#N,M,K = map(int,input.split())
#list = list(map(int, input.split()))
N=5
M=8
K=3

list=[2,4,5,4,6]

max1 = max(list)
list.remove(max1)
max2 = max(list)


print(max1,max2)
sum=0
if max1 == max2:
    sum=max1*K

else:
    if M == K:
        sum = max1*K

    else:  #M>=K+1
        sum = (M%(K+1))*max1
        sum += (M//(K+1))*(K*max1 + max2)

print(sum)
    
