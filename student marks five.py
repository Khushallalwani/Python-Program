a=input("Enter Name :")
a1=int(input("Enter Marks :"))
b=input("Enter Name :")
b1=int(input("Enter Marks :"))
c=input("Enter Name :")
c1=int(input("Enter Marks :"))
d=input("Enter Name :")
d1=int(input("Enter Marks :"))
e=input("Enter Name :")
e1=int(input("Enter Marks :"))

if a1>b1 and a1>c1 and a1>d1 and a1>e1:
    print(a,a1)
elif b1>a1 and b1>c1 and b1>d1 and b1>e1:
    print(b,b1) 
elif c1>a1 and c1>b1 and c1>d1 and c1>e1:
    print(c,c1)
elif d1>a1 and d1>b1 and d1>c1 and d1>e1:
    print(d,d1)
elif e1>a1 and e1>b1 and e1>c1 and e1>d1:
    print(e,e1)
else:
    print("All Are Equal")    