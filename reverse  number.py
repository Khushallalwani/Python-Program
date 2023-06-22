a=int(input("Enter a Number:"))

#print(str(a)[::-1])

b=a%10
a=a//10
c=a%10
a=a//10
d=a%10
a=a//10
i=b*100+c*10+d*1
print(i)