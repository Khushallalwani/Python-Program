x=input("Enter Number :")
if x==x[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")    
    

'''

x=int(input("Enter Number :"))
temp=x
rev=0
while x>0:
    d=x%10
    rev=rev*10+d
    x=x//10
if temp==rev:
    print("palindrome")
else:
    print("Not palindrome")
    '''