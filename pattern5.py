r=int(input("Enter Number :"))
k=0
for  i in range(1,r+1):
    for a in range(1,(r-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("*",end=" ")
        k+=1
    k=0
    print()