i=input("Enter Character +,-,*,/ :")

if (i=='+'):
    def add():
        a=int(input("Enter a Number :"))
        b=int(input("Enter b Number :"))
        c=a+b
        print(c)
      
elif(i=='-'):      
    def sub():
        a=int(input("Enter a Number :"))
        b=int(input("Enter b Number :"))
        c=a+b
        print(c)
        

elif(i=='*'):
    def multi():
        a=int(input("Enter a Number :"))
        b=int(input("Enter b Number :"))
        c=a*b
        print(c)
        

elif(i=='/'):
    def div():
        a=int(input("Enter a Number :"))
        b=int(input("Enter b Number :"))
        c=a/b
        print(c)
        
else:
    print("type right character")


if(i=='+'):
    add()
elif(i=='-'):
    sub()
elif(i=='*'):
    multi()
elif(i=='/'):
    div()
else:
    print("Choose right choice")