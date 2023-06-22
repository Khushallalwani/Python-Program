x=str(input("Enter Name :"))
m=int(input("Enter Maths Marks :"))
c=int(input("Enter C++ Marks :"))
j=int(input("Enter Java Marks :"))
p=int(input("Enter Python Marks :"))
i=int(input("Enter Internet Programming Marks :"))
cc=int(input("Enter Cloud Computing Marks :"))

t=m+c+j+p+i+cc
z=t/420*100

if z>90:
    print("GRADE A",z)
elif z>80 and z<90:
    print("GRADE B")
elif z>70 and z<80:
    print("GRADE C")
elif z>60 and z<70:
    print("GRADE D")
elif z<60:
    print("GRADE F")
else:
    print("FAIL")