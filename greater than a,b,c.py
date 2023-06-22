a=int(input("Enter a Number :"))
b=int(input("Enter b Number :"))
c=int(input("Enter c Number :"))

if(a>b) and (a>c):
    print("A is greater than B and C")
elif(b>a) and (b>c):
    print("B is greater than A and C")
elif(c>a) and (c>b):
    print("C is greater than A and B")
else:
    print("A,B,C all are equal") 
    
