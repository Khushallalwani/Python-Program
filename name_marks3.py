a=[]
for i in range(0,4,1):
    b=input("Enter Name :")
    print(b)
    a.append(b)
    for j in range(0,4,1):
        c=int(input("Enter a Marks :"))
        print(c)
        a.append(c)
        print(a[j])
        if a[1]>a[j]:
           print(a[1])
        elif a[3]>a[j]:
           print(a[3])
        elif a[5]>a[j]:
           print(a[5])
        else:
           print(a[7]) 
        break 
print(a)