#day14

import random
def make_question():
    a = random.randint(1,40)
    b = random.randint(1,40)
    op = random.randint(1,3)
    q=str(a)

    if op == 1:
        q=q+"+"+str(b)
    elif op == 2:
        q=q+"-"+str(b)  
    else:
        q=q+"*"+str(b)
    return q
        

sc1 = 0
sc2 = 0
for i in range(5):
    q = make_question()
    print(q)
    ans = input("=")

    if(int(ans) == eval(q)):
        sc1 = sc1 +1

    else: sc2 = sc2+1

print(sc1,"/5")
if sc1 == 5:
    print("천재~")
        
    
    



