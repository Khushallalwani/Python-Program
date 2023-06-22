n=int(input("Enter Number :"))
f=int(input("Enter Factorial Number :"))

if n<0:
    print("Negative Number have no Factorial")
elif n==0:
    print("Factorial of 0 is",f)
else:
    for i in range(1,n+1):
        f=f*i
    print("Factorial of",n,"is",f)
        