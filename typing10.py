import tkinter as tk
import time
window1=tk.Tk()
window1.geometry("500x500")
sub=""
sub1=""
stdata=""
err=0
j=0
stmin=0
stsec=0
enmin=0
ensec=0
totalchar=0


def onclick():
    li=[nameentry.get(),",",acnumentry.get(),"\n"]
    file=open("veer4.csv",'a+')
    for i in range(4):    
        file.write(str(li[i]))
    file.close()

def newwin():
    sub=nameentry.get()
    sub1=acnumentry.get()
    onclick()   
    if sub!="" and sub1!="":
        window1.destroy()
        window=tk.Tk()
        window.geometry("1300x700")
       
        
    
    def sttime():
        global stmin,stsec
        mintosec=0.0
        gross_wpm=0.0
        net_wpm=0.0
        accu=0.0
        stmin=int(time.strftime("%M"))
        stsec=int(time.strftime("%S"))
    def entime():
        global enmin,ensec
        enmin=int(time.strftime("%M"))
        ensec=int(time.strftime("%S"))
    def dift():
        global stmin,stsec,enmin,ensec
        ex1=enmin-stmin
        if ensec<stsec:
            ex2=(60-stsec)+ensec
        if ensec>=stsec:
            ex2=ensec-stsec
        mintosec=float(ex2/60)
        if ex1!=0 and ex1<1:
            mintosec=ex1+mintosec
        gross_wpm=float((totalchar/5)/mintosec)
        net_wpm=gross_wpm-(err/mintosec)
        accu=(net_wpm/gross_wpm)*100
        print("Gross speed",gross_wpm)
        print("net speed",net_wpm)
        print("accuracy",accu)
        label.config(text=int(gross_wpm))
        label1.config(text=int(net_wpm))   
        label2.config(text=int(accu))
    def comp():
        global stdata,totalchar
        global err
        stinput=textinput.get("1.0",'end-1c')
        for i in range(len(stdata)):
            if stdata[i]!=stinput[i]:
                err=err+1
            totalchar=totalchar+1 
  
        entime()
        dift()

    def show():
        global j
        global stdata
        if clicked.get()=="Lesson 1":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson1)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 1" and j!=1:
                stdata=""
                f=open("day1.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=1
                
                sttime()
    
            
            elif dayclicked.get()=="Day 2" and j!=2:
                stdata=""
                f=open("day2.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=2
                
                sttime()
            elif dayclicked.get()=="Day 3" and j!=3:
                f=open("day3.txt","r")
                f.close()
            elif dayclicked.get()=="Day 4" and j!=4:
                f=open("day4.txt","r")
            elif dayclicked.get()=="Day 5" and j!=5:
                f=open("day5.txt","r")
           
            elif dayclicked.get()=="Day 6" and j!=6:
                f=open("day6.txt","r")
            elif dayclicked.get()=="Day 7" and j!=7:
                f=open("day7.txt","r")    
           
                f.close()
        elif clicked.get()=="Lesson 2":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson2)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 1" and j!=1:
                f=open("day8.txt","r")
                
     
            elif dayclicked.get()=="Day 2" and j!=2:
                f=open("day9.txt","r")
           
            elif dayclicked.get()=="Day 3" and j!=3:
                f=open("day3.txt","r")
          
            elif dayclicked.get()=="Day 4" and j!=4:
                f=open("day4.txt","r")
     
            elif dayclicked.get()=="Day 5" and j!=5:
                f=open("day5.txt","r")
       
            elif dayclicked.get()=="Day 6" and j!=6:
                f=open("day6.txt","r")
            elif dayclicked.get()=="Day 7" and j!=7:
                f=open("day7.txt","r")    
          
                f.close()

        
    option=["Lesson 1","Lesson 2","Lesson 3","Lesson 4","Lesson 5","Lesson 6"
            ,"Lesson 7","Lesson 8","Lesson 9","Lesson 10","Lesson 11","Lesson 12","Lesson 13"
            ,"Lesson 14","Lesson 15","Lesson 16"]
    lesson1=["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7"]
    lesson2=["Day 8","Day 9","Day 10","Day 11","Day 12"]

    clicked=tk.StringVar()
    dayclicked=tk.StringVar()
    #clicked=set("Lesson 1")
    drop=tk.OptionMenu(window,clicked, *option)
    drop.place(x=2,y=5)

    button=tk.Button(window,text="click",command=show)
    button.place(x=180,y=6)
    submit=tk.Button(window,text="Submit",width=10,height=3,command=comp)
    submit.place(x=1050,y=500)
    text=tk.Text(window,bg="white",fg="black",width=100,height=20)
    text.place(x=230,y=30)
    textinput=tk.Text(window,bg="white",fg="black",width=100,height=20)
    textinput.place(x=230,y=400)
    label=tk.Label(window)
    label.place(x=1050,y=400)
    label1=tk.Label(window)
    label1.place(x=1100,y=400)
    label2=tk.Label(window)
    label2.place(x=1150,y=400)
    window.mainloop()

    
    
namelabel=tk.Label(window1,text="Enter Student Name :")
namelabel.place(x=30,y=10)
nameentry=tk.Entry(window1)
nameentry.place(x=60,y=10)
acnum=tk.Label(window1,text="Enter College Id :")
acnum.place(x=30,y=30)
acnumentry=tk.Entry(window1)
acnumentry.place(x=70,y=30)
stbutton=tk.Button(window1,text="Start",width=9,height=2,command=newwin)
stbutton.place(x=50,y=70)
window1.mainloop()
