a=int(input("Enter a Number :"))
if(a<=10):
    b=a*11
    print(b)
elif(a>10) and (a<=90):
    b=110+(a-10)*10
    print(b)
elif(a>90):
    b=1010+(a-10)*9
    print(b)
else:
    print("zero")
    