import random
import sys

def menu():
    print("-------------------------------------------")
    print("----------WELCOME TO LOTTERY GAME----------")
    print("-------------------------------------------")
    print("                           ")
    print("1. Start Game")
    print("2. Show the Winning Amount")
    print("3. Exit")
    choice=int(input("Enter any Choice :"))
    return choice


def start_game():
    print("-------------------------------------------")
    print("How much amount You Spend")
    print("1. 50")
    print("2. 100")
    print("3. 500")
    choice=int(input("Enter your Choice :"))
    return choice

    
def amount50():
        print("--------------------------------------------")
        print("Welcome to Lottery 50 Rupees")
        
        global a
        a=input("Enter First Person :")
        global aa
        aa=int(input("Enter Lottery Number 0-10 :"))
        print("--------------------------------------------")
        
        global b
        b=input("Enter Second Person :")
        global bb
        bb=int(input("Enter Lottery Number 0-10 :"))
        print("--------------------------------------------") 
        
        global c
        c=input("Enter Third Person :")  
        global cc
        cc=int(input("Enter Lottery Number 0-10 :"))
        print("--------------------------------------------")
        
        global d
        d=input("Enter Fourth Person :")
        global dd
        dd=int(input("Enter Lottery number 0-10 :"))
        print("--------------------------------------------")
        for i in range(3):
           global z
           z=random.randint(0,10) 
           print(z)

           if z==aa:
             print("Congratulations You Won the Lottery :",a)
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


def amount100():
    print("--------------------------------------------")
    print("Welcome to Lottery 100 Rupees")
    
    global ab
    ab=input("Enter First Person :")
    global p
    p=int(input("Enter Lottery Number 0-10 :"))
    print("--------------------------------------------")

    global bc
    bc=input("Enter Second Person :")
    global v
    v=int(input("Enter Lottery Number 0-10 :"))
    print("--------------------------------------------")

    global cd
    cd=input("Enter Third Person :")  
    global w
    w=int(input("Enter Lottery Number 0-10 :"))
    print("--------------------------------------------")

    global de
    de=input("Enter Fourth Person :")
    global y
    y=int(input("Enter Lottery number 0-10 :"))
    print("--------------------------------------------")

    for i in range(3):
        global rz
        rz=random.randint(0,10) 
        print(rz)

        if rz==p:
           print("Congratulations You Won the Lottery :",ab)
           break
        elif rz==v:
           print("Congratulations You Won the Lottery :",bc)
           break
        elif rz==w:
            print("Congratulations You Won the Lottery :",cd)
            break
        elif rz==y:
            print("Congratulations You Won the Lottery :",de)
            break
        else:
            print("Lottery Fail")
            continue    

    
def amount500():
    print("--------------------------------------------")
    print("Welcome to Lottery 500 Rupees")
    
    global af
    af=input("Enter First Person :")
    global s
    s=int(input("Enter Lottery Number 0-10 :"))
    print("--------------------------------------------")

    global bg
    bg=input("Enter Second Person :")
    global j
    j=int(input("Enter Lottery Number 0-10:"))
    print("--------------------------------------------")

    global ck
    ck=input("Enter Third Person :")  
    global k
    k=int(input("Enter Lottery Number 0-10 :"))
    print("--------------------------------------------")
    
    global dq
    dq=input("Enter Fourth Person :")
    global l
    l=int(input("Enter Lottery number 0-10 :"))
    print("--------------------------------------------")

    for i in range(3):
        global zq
        zq=random.randint(0,10) 
        print(zq)
        
        if zq==s:
            print("Congratulations You Won the Lottery :",af)
            break
        elif zq==j:
            print("Congratulations You Won the Lottery :",bg)
            break
        elif zq==k:
           print("Congratulations You Won the Lottery :",ck)
           break
        elif zq==l:
           print("Congratulations You Won the Lottery :",dq)
           break
        else:
         print("Lottery Fail")
         continue


def showamount():
    print("-------------------------------------------")
    print("How much amount You Spend")
    print("1. 50")
    print("2. 100")
    print("3. 500")
    choice=int(input("Enter your Choice :"))
    return choice


def showamount50():
    print("-------------------------------------------")
    
    if z==aa:
      print("You Won 150 Rupees :",a)
      print("You Lose 50 Rupees :",b)
      print("You Lose 50 Rupees :",c)
      print("You Lose 50 Rupees :",d)
    elif z==bb:
      print("You won 150 Rupees :",b)
      print("You Lose 50 Rupees :",a)
      print("You Lose 50 Rupees :",c)
      print("You Lose 50 Rupees :",d)
    elif z==cc:
      print("You won 150 Rupees :",c)
      print("You Lose 50 Rupees :",b)
      print("You Lose 50 Rupees :",a)
      print("You Lose 50 Rupees :",d)
    elif z==dd:
      print("You won 150 Rupees :",d)
      print("You Lose 50 Rupees :",b)
      print("You Lose 50 Rupees :",c)
      print("You Lose 50 Rupees :",a)
    else:
      print("NoBody Can Win Money")
      
    
def showamount100():
    print("------------------------------------------")
    
    if rz==p:
      print("You won 350 Rupees :",ab)
      print("You Lose 100 Rupees :",bc)
      print("You Lose 100 Rupees :",cd)
      print("You Lose 100 Rupees :",de)
    elif rz==v:
      print("You won 350 Rupees :",bc)
      print("You Lose 100 Rupees :",ab)
      print("You Lose 100 Rupees :",cd)
      print("You Lose 100 Rupees :",de)
    elif rz==w:
      print("You won 350 Rupees :",cd)
      print("You Lose 100 Rupees :",bc)
      print("You Lose 100 Rupees :",ab)
      print("You Lose 100 Rupees :",de)
    elif rz==y:
      print("You won 350 Rupees :",de)
      print("You Lose 100 Rupees :",bc)
      print("You Lose 100 Rupees :",cd)
      print("You Lose 100 Rupees :",ab)
    else:
      print("Nobody Can Win Money")
        
    
def showamount500():
    print("-------------------------------------------")
    
    if zq==s:
      print("You won 1500 Rupees :",af)
      print("You Lose 500 Rupees :",bg)
      print("You Lose 500 Rupees :",ck)
      print("You Lose 500 Rupees :",dq)
    elif zq==j:
      print("You won 1500 Rupees :",bg)
      print("You Lose 500 Rupees :",af)
      print("You Lose 500 Rupees :",ck)
      print("You Lose 500 Rupees :",dq)
    elif zq==k:
      print("You won 1500 Rupees :",ck)
      print("You Lose 500 Rupees :",bg)
      print("You Lose 500 Rupees :",af)
      print("You Lose 500 Rupees :",dq)
    elif zq==l:
      print("You won 1500 Rupees :",dq)
      print("You Lose 500 Rupees :",bg)
      print("You Lose 500 Rupees :",ck)
      print("You Lose 500 Rupees :",af)
    else:
      print("Nobody Can Win Money")
    
    
def thanks():
    print("Thank you For Playing")
    sys.exit()



ch=1
while ch in(1,2,3):
   ch=menu()
   if ch==1:
       while ch in(1,2,3):
          ze=start_game()
          if ze==1:
            amount50()
            break
          elif ze==2:
            amount100()
            break
          elif ze==3:
            amount500()
            break
          else:
            print("Choose Correct Option")
   elif ch==2:
        while ch in(1,2,3):
           qw=showamount()
           if qw==1:
             showamount50()
             break
           elif qw==2:
             showamount100()
             break
           elif qw==3:
             showamount500()
             break
           else:
               print("Choose Correct Option")
   elif ch==3:
       thanks()       
   elif not ch==1 and not ch==2 and not ch==3:
     print("Choose Correct Option")
     continue