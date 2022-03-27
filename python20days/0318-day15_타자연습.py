import random
import time


list = ["바나나","사과","딸기","키위","파인애플","귤","망고","블루베리"]

print("This is Typing Game.")
print("When you're ready to play, Hit the Enter")

input()

start = time.time() #record starting time


c = 1
while c <=5:
    q = random.choice(list)
    print(q)
    x = input("")
    if x == q:
        print("correct!")
        c = c+1
    else: print("wrong typing! Again")
    
end = time.time()

time = end - start
time = format(time, ".2f")

print("typing time:",time,"sc")
    
    

