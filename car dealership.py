x=int(input("Enter To Choose :"))

if(x==1):
    def login():
      a=input("Enter a Name :")
      b=int(input("Enter id"))
      print(a)
      print(b)
elif(x==2):    
    def buy():
        c=input("Enter Car Name :")
        d=input("Eenter Car Color :")
        e=input("Enter Car price :")
        print(c)
        print(d)
        print(e)
elif(x==3):
    def sale():
        a=input("Enter Car Owner Name :")
        z=input("Enter Car Name :")
        b=int(input("Enter Car Sale Price :"))
        c=input("Enter Car Color :")
        d=input("Enter Buyer Name :")
        print(a)
        print(b)
        print(c)
        print(d)
        print(z)
else:
    print("Choose Correct Option")
    
if(x==1):
    login()
elif(x==2):
    buy()
elif(x==3):
    sale()
else:
    print("Choice Right Option")