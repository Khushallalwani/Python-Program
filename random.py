import random
x=int(input("Enter a Number :"))

for i in range(3):
     y=random.randint(0,2000)
     if x==y:
        print("Match Successfull",y)
        break
     else:
       print("Match not successfull",y)    