import random
import sys

def menu():
    print("-------------------------------------------")
    print("----------WELCOME TO LOTTERY GAME----------")
    print("-------------------------------------------")
    print("                           ")
    print("1. START GAME")
    print("2. SHOW THE WINNER")
    print("3. SHOW THE LOSER")
    print("4. Exit")
    choice=int(input("Enter any Choice :"))
    return choice


def start_game():
    print("-------------------------------------------")
    print("How much amount You Will Spend")
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
        kk=int(input("How Many Tickets You Want :"))
        kkk=[]
        for w in range(kk):
            kkk=int(input("Enter Ticket Number :"))
            print(kkk)
        print("--------------------------------------------")

        global b
        b=input("Enter Second Person :")
        az=int(input("How Many Tickets You Want :"))
        er=[]
        for w in range(az):
           er[w]=int(input("Enter Ticket Number :"))
           print(er)
        print("--------------------------------------------") 
        
        global c
        c=input("Enter Third Person :")
        bz=int(input("How Many Tickets You Want :"))
        re=[]
        for w in range(bz):
            re[w]=int(input("Enter Ticket Number :"))
            print(re[w])
        print("--------------------------------------------")

        global d
        d=input("Enter Fourth Person :")
        cz=int(input("How Many Tickets You Want :"))
        ke=[]
        for w in range(cz):
            ke[w]=int(input("Enter Ticket Number :"))
            print(ke)
        print("--------------------------------------------")
        for i in range(3):
           global z
           z=random.randint(0,10) 
           print("Random Number :",z)
           
           for t in range(w):
               
               if z==kkk[w]:
                   print("Congratulations You Won the Lottery :",a)
                   break
               elif z==er[w]:
                   print("Congratulations You Won the Lottery :",b)
                   break
               elif z==re[w]:
                   print("Congratulations You Won the Lottery :",c)
                   break
               elif z==ke[w]:
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
    print("Choose Any Option")
    print("1. 50")
    print("2. 100")
    print("3. 500")
    choice=int(input("Enter your Choice :"))
    return choice

l
def winamount50():
    print("-------------------------------------------")
    
    if z==aa:
      print("You Won 150 Rupees :",a)
     
    elif z==bb:
      print("You won 150 Rupees :",b)
     
    elif z==cc:
      print("You won 150 Rupees :",c)
     
    elif z==dd:
      print("You won 150 Rupees :",d)
     
    else:
      print("NoBody Can Win Money")
      
    
def winamount100():
    print("------------------------------------------")
    
    if rz==p:
      print("You won 350 Rupees :",ab)
      
    elif rz==v:
      print("You won 350 Rupees :",bc)
     
    elif rz==w:
      print("You won 350 Rupees :",cd)
      
    elif rz==y:
      print("You won 350 Rupees :",de)
      
    else:
      print("Nobody Can Win Money")
        
    
def winamount500():
    print("-------------------------------------------")
    
    if zq==s:
      print("You won 1500 Rupees :",af)
      
    elif zq==j:
      print("You won 1500 Rupees :",bg)
     
    elif zq==k:
      print("You won 1500 Rupees :",ck)
     
    elif zq==l:
      print("You won 1500 Rupees :",dq)
     
    else:
      print("Nobody Can Win Money")
    
    
    
    
def loseamount50():
    print("-------------------------------------------")
    
    if z==aa:
      print("You Lose 50 Rupees :",b)
      print("You Lose 50 Rupees :",c)
      print("You Lose 50 Rupees :",d)
      
    elif z==bb:
      print("You Lose 50 Rupees :",a)
      print("You Lose 50 Rupees :",c)
      print("You Lose 50 Rupees :",d)
    elif z==cc:
      print("You Lose 50 Rupees :",b)
      print("You Lose 50 Rupees :",a)
      print("You Lose 50 Rupees :",d)
     
    elif z==dd:
      print("You Lose 50 Rupees :",a)
      print("You Lose 50 Rupees :",b)
      print("You Lose 50 Rupees :",c)
    else:
      print("NoBody Can Win Money")
      
    
def loseamount100():
    print("------------------------------------------")
    
    if rz==p:
      print("You Lose 100 Rupees :",bc)
      print("You Lose 100 Rupees :",cd)
      print("You Lose 100 Rupees :",de)
      
    elif rz==v:
      print("You Lose 100 Rupees :",ab)
      print("You Lose 100 Rupees :",cd)
      print("You Lose 100 Rupees :",de)

     
    elif rz==w:
      print("You Lose 100 Rupees :",bc)
      print("You Lose 100 Rupees :",ab)
      print("You Lose 100 Rupees :",de)

      
    elif rz==y:
      print("You Lose 100 Rupees :",ab)
      print("You Lose 100 Rupees :",bc)
      print("You Lose 100 Rupees :",cd)

      
    else:
      print("Nobody Can Win Money")
        
    
def loseamount500():
    print("-------------------------------------------")
    
    if zq==s:
        print("You Lose 500 Rupees :",bg)
        print("You Lose 500 Rupees :",ck)
        print("You Lose 500 Rupees :",dq)
      
    elif zq==j:
        print("You Lose 500 Rupees :",af)
        print("You Lose 500 Rupees :",ck)
        print("You Lose 500 Rupees :",dq)
     
    elif zq==k:
        print("You Lose 500 Rupees :",bg)
        print("You Lose 500 Rupees :",af)
        print("You Lose 500 Rupees :",dq)
     
    elif zq==l:
        print("You Lose 500 Rupees :",bg)
        print("You Lose 500 Rupees :",ck)
        print("You Lose 500 Rupees :",af)
     
    else:
        print("Nobody Can Win Money")
    
    
def thanks():
        print("Thank you For Playing")
        sys.exit()



ch=1
while ch !=4:
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
             winamount50()
             break
           elif qw==2:
             winamount100()
             break
           elif qw==3:
             winamount500()
             break
           else:
               print("Choose Correct Option")
   elif ch==3:
        while ch in(1,2,3):
            vk=showamount()
            if vk==1:
                loseamount50()
                break
            elif vk==2:
                loseamount100()
                break
            elif vk==3:
                loseamount500()
                break
            else:
                print("Choose Correct Option")
   elif ch==4: 
     thanks()
   elif ch>=5:
       print("Choose Correct Option")
       continue
 