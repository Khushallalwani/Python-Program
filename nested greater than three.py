a=int(input("Enter a Number :"))
b=int(input("Enter b Number :"))
c=int(input("Enter c Number :"))
if a>b:
    if a>c:
         print("A is greater than b and c")
    else:
        print("C is greater than a and b")
else:
    if b>c:
        print("b is greater than a and c")
    else:
        print("c is greater than a and b")