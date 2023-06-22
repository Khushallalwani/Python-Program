import random
import sys

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
  b=input("Enter Second Person :")
  c=input("Enter Third Person :")
  d=input("Enter Fourth Person :")
  
  
  for i in range(3):
      z=int(input("Enter Lottery Number :"))
      print(z)

      p=random.randint(0,4)
      q=random.randint(0,4)
      r=random.randint(0,4)
      s=random.randint(0,4)
      print(a,p)
      print(b,q)
      print(c,r)
      print(d,s)

      if z==p:
          print("Congratulations You Won the Lottery :",a)
          break
      elif z==q:
          print("Congratulations You Won the Lottery :",b)
          break
      elif z==r:
          print("Congratulations You Won the Lottery :",c)
          break
      elif z==s:
          print("Congratulations You Won the Lottery :",d)
      else:
          print("Lottery Fail")
          continue
      return a,b,c,d 
  

def thanks():
    print("Thank you For Playing")
    sys.exit()

z=random.randint(0,100)

ch=1
while ch in(1,2,3):
    ch=menu()
    if ch==1:
       start_game()
    elif ch==2:
       print("500") 
    else:
       thanks()       
    