import random
import sys

v=0
def menu():
    print("-------------------------------------------")
    print("----------WELCOME TO LOTTERY GAME----------")
    print("-------------------------------------------")
    print("              Entry Fees 50                ")
    print("1. Start Game")
    print("2. Show the Winning Amount")
    print("3. Exit")
    choice=int(input("Enter any Choice :"))
    return choice


def start_game():
  a=input("Enter First Person :")
  aaa=int(input("Enter Amount 1st Person"))
  aa=int(input("Enter Lottery Number :"))
  
  b=input("Enter Second Person :")
  bbb=int(input("Enter Amount 2nd Person"))
  bb=int(input("Enter Lottery Number :"))

  c=input("Enter Third Person :")
  ccc=int(input("Enter Amount 3rd Person"))  
  cc=int(input("Enter Lottery Number :"))

  d=input("Enter Fourth Person :")
  ddd=int(input("Enter Amount 4th Person"))
  dd=int(input("Enter Lottery number :"))
  
  for i in range(3):

     z=random.randint(0,8) 
     print(z)

     if z==aa:
       print("Congratulations You Won the Lottery :",a)
       global v
       v=1
       break
     elif z==bb:
       print("Congratulations You Won the Lottery :",b)
       break
     elif z==cc:
       print("Congratulations You Won the Lottery :",c)
       break
     elif z==dd:
       print("Congratulations You Won the Lottery :",d)
       break
     else:
       print("Lottery Fail")
       continue

def amount():
    if v==1:
        print(a,"won 1500 rupees")
        print(b,"lose 500 rupees")
        print(c,"lose 500 rupees")
        print(d,"lose 500 rupees")

def thanks():
    print("Thank you For Playing")
    sys.exit()


ch=1
while ch in(1,2,3):
    ch=menu()
    if ch==1:
       start_game()
    elif ch==2:
       amount()
    else:
       thanks()       
    