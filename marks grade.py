a=input("Enter Name:")
b=input("Enter class:")

c=int(input("Enter MATHS Number:"))
d=int(input("Enter DBMS Number:"))
e=int(input("Enter C++ Number:"))
f=int(input("Enter Networking Number:"))
g=int(input("Enter fundamentals Number:"))

total=c+d+e+f+g
x=total/500*100
print(x)

if(x>=90):
    print("Grade A")
elif(x>=80):
    print("Grade B") 
elif(x>=65):
    print("Grade C")
elif(x>=50):
    print("Grade D")
elif(x>=35):
    print("PASS") 
else:
    print("Fail")      
