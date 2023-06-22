import random
a=[]
for i in range(15):
    r=random.randint(1, 50)
    
    if r not in a:
        a.append(r)
print(a)
