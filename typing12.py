import tkinter as tk
import time
window1=tk.Tk()
window1.geometry("400x300")
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
    file=open("data.csv",'a+')
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
        window.geometry("1300x800")
       
    def sttime():
        global stmin,stsec
        global mintosec 
        global gross_wpm
        global net_wpm
        global accu
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
                f=open("day1.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=1
                sttime()
    
            
            elif dayclicked.get()=="Day 2" and j!=1:
                f=open("day2.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=1
                sttime()
            elif dayclicked.get()=="Day 3" and j!=3:
                f=open("day3.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=3
                sttime()
    
            elif dayclicked.get()=="Day 4" and j!=4:
                f=open("day4.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=4
                sttime()
    
            elif dayclicked.get()=="Day 5" and j!=5:
                f=open("day5.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=5
                sttime()
    
            elif dayclicked.get()=="Day 6" and j!=6:
                f=open("day6.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=6
                sttime()
    
            elif dayclicked.get()=="Day 7" and j!=7:
                f=open("day7.txt","r")    
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=7
                sttime()

        elif clicked.get()=="Lesson 2":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson2)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 8" and j!=8:
                f=open("day8.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=8
                sttime()
                
            elif dayclicked.get()=="Day 9" and j!=9:
                f=open("day9.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=9
                sttime()
                
            elif dayclicked.get()=="Day 10" and j!=10:
                f=open("day10.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=10
                sttime()
        
        elif clicked.get()=="Lesson 3":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson3)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 11" and j!=11:
                f=open("day11.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=11
                sttime()
            elif dayclicked.get()=="Day 12" and j!=12:
                f=open("day10.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=12
                sttime()
            elif dayclicked.get()=="Day 13" and j!=13:
                f=open("day13.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=13
                sttime()
            elif dayclicked.get()=="Day 14" and j!=14:
                f=open("day14.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=14
                sttime()   
        elif clicked.get()=="Lesson 4":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson4)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 15" and j!=15:
                f=open("day15.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=15
                sttime()
            elif dayclicked.get()=="Day 16" and j!=16:
                f=open("day16.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=16
                sttime()
            elif dayclicked.get()=="Day 17" and j!=17:
                f=open("day17.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=17
                sttime()
            elif dayclicked.get()=="Day 18" and j!=18:
                f=open("day18.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=18
                sttime()                 
        elif clicked.get()=="Lesson 5":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson5)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 19" and j!=19:
                f=open("day19.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=19
                sttime()
            elif dayclicked.get()=="Day 20" and j!=20:
                f=open("day20.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=20
                sttime()
            elif dayclicked.get()=="Day 21" and j!=21:
                f=open("day21.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=21
                sttime()
            elif dayclicked.get()=="Day 22" and j!=22:
                f=open("day22.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=22
                sttime()
            elif dayclicked.get()=="Day 23" and j!=23:
                f=open("day23.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=23
                sttime() 
        elif clicked.get()=="Lesson 6":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson6)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 24" and j!=24:
                f=open("day24.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=24
                sttime()
            elif dayclicked.get()=="Day 25" and j!=25:
                f=open("day25.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=25
                sttime()
            elif dayclicked.get()=="Day 26" and j!=26:
                f=open("day26.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=26
                sttime()
            elif dayclicked.get()=="Day 27" and j!=27:
                f=open("day27.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=27
                sttime()
            elif dayclicked.get()=="Day 28" and j!=28:
                f=open("day28.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=28
                sttime() 
                
            elif dayclicked.get()=="Day 29" and j!=29:
                f=open("day29.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=29
                sttime() 
                
        elif clicked.get()=="Lesson 7":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson7)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 30" and j!=30:
                f=open("day30.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=30
                sttime()
            elif dayclicked.get()=="Day 31" and j!=31:
                f=open("day31.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=31
                sttime()
            elif dayclicked.get()=="Day 32" and j!=32:
                f=open("day32.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=32
                sttime()
            elif dayclicked.get()=="Day 33" and j!=33:
                f=open("day33.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=33
                sttime()
            elif dayclicked.get()=="Day 34" and j!=34:
                f=open("day34.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=34
                sttime() 
        elif clicked.get()=="Lesson 8":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson8)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 35" and j!=35:
                f=open("day35.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=35
                sttime()
            elif dayclicked.get()=="Day 36" and j!=36:
                f=open("day36.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=36
                sttime()
            elif dayclicked.get()=="Day 37" and j!=37:
                f=open("day37.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=37
                sttime()
            elif dayclicked.get()=="Day 38" and j!=38:
                f=open("day38.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=38
                sttime()
            elif dayclicked.get()=="Day 39" and j!=39:
                f=open("day39.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=39
                sttime() 
        elif clicked.get()=="Lesson 9":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson9)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 40" and j!=40:
                f=open("day40.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=40
                sttime()
            elif dayclicked.get()=="Day 41" and j!=41:
                f=open("day41.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=41
                sttime()
            elif dayclicked.get()=="Day 42" and j!=42:
                f=open("day42.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=42
                sttime()
            elif dayclicked.get()=="Day 43" and j!=43:
                f=open("day43.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=43
                sttime()
        elif clicked.get()=="Lesson 10":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson10)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 44" and j!=44:
                f=open("day44.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=44
                sttime()
            elif dayclicked.get()=="Day 45" and j!=45:
                f=open("day45.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=45
                sttime()
            elif dayclicked.get()=="Day 46" and j!=46:
                f=open("day46.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=46
                sttime()
            elif dayclicked.get()=="Day 47" and j!=47:
                f=open("day47.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=47
                sttime()
            elif dayclicked.get()=="Day 48" and j!=48:
                f=open("day48.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=48
                sttime()
        elif clicked.get()=="Lesson 11":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson11)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 49" and j!=49:
                f=open("day49.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=49
                sttime()
            elif dayclicked.get()=="Day 50" and j!=50:
                f=open("day50.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=50
                sttime()
            elif dayclicked.get()=="Day 51" and j!=51:
                f=open("day51.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=51
                sttime()
            elif dayclicked.get()=="Day 52" and j!=52:
                f=open("day52.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=52
                sttime()
        elif clicked.get()=="Lesson 12":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson12)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 53" and j!=53:
                f=open("day53.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=53
                sttime()
            elif dayclicked.get()=="Day 54" and j!=54:
                f=open("day54.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=54
                sttime()
            elif dayclicked.get()=="Day 55" and j!=55:
                f=open("day55.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=55
                sttime()
            elif dayclicked.get()=="Day 56" and j!=56:
                f=open("day56.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close() 
                j=56
                sttime()
        elif clicked.get()=="Lesson 13":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson13)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 57" and j!=57:
                f=open("day57.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=57
                sttime()
            elif dayclicked.get()=="Day 58" and j!=58:
                f=open("day58.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=58
                sttime()
        elif clicked.get()=="Lesson 14":
            droplesson1=tk.OptionMenu(window,dayclicked, *lesson14)
            droplesson1.place(x=90,y=5)
            if dayclicked.get()=="Day 59" and j!=59:
                f=open("day59.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=59
                sttime()
            elif dayclicked.get()=="Day 60" and j!=60:
                f=open("day60.txt","r")
                stdata=f.read()
                text.insert("1.0",stdata)
                f.close()
                j=60
                sttime()
    option=["Lesson 1","Lesson 2","Lesson 3","Lesson 4","Lesson 5","Lesson 6"
            ,"Lesson 7","Lesson 8","Lesson 9","Lesson 10","Lesson 11","Lesson 12","Lesson 13"
            ,"Lesson 14"]
    lesson1=["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7"]
    lesson2=["Day 8","Day 9","Day 10"]
    lesson3=["Day 11","Day 12","Day 13","Day 14"]
    lesson4=["Day 15","Day 16","Day 17","Day 18"]
    lesson5=["Day 19","Day 20","Day 21","Day 22","Day 23"]
    lesson6=["Day 24","Day 25","Day 26","Day 27","Day 28","Day 29"]
    lesson7=["Day 30","Day 31","Day 32","Day 33","Day 34"]
    lesson8=["Day 35","Day 36","Day 37","Day 38","Day 39"]
    lesson9=["Day 40","Day 41","Day 42","Day 43"]
    lesson10=["Day 44","Day 45","Day 46","Day 47","Day 48"]
    lesson11=["Day 49","Day 50","Day 51","Day 52"]
    lesson12=["Day 53","Day 54","Day 55","Day 56"]
    lesson13=["Day 57","Day 58"]
    lesson14=["Day 59","Day 60"]
    
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
    text.place(x=230,y=6)
    
    label3=tk.Label(window,text="Start Typing")
    label3.place(x=230,y=360)
    textinput=tk.Text(window,bg="white",fg="black",width=100,height=20)
    textinput.place(x=230,y=380)
    lab=tk.Label(text="Gross Wpm :")
    lab.place(x=1100,y=10)
    label=tk.Label(window)
    label.place(x=1180,y=10)
    lab1=tk.Label(text="Net Wpm :")
    lab1.place(x=1100,y=30)
    lab2=tk.Label(text="Accuracy")
    lab2.place(x=1100,y=50)
    label1=tk.Label(window)
    label1.place(x=1180,y=30)
    label2=tk.Label(window)
    label2.place(x=1180,y=50)
    window.mainloop()

namelabel=tk.Label(window1,text="Enter Name")
namelabel.place(x=30,y=10)
nameentry=tk.Entry(window1)
nameentry.place(x=120,y=10)

acnum=tk.Label(window1,text="Enter College Id")
acnum.place(x=30,y=40)
acnumentry=tk.Entry(window1)
acnumentry.place(x=120,y=40)
label6=tk.Label(window1,text="SBJSR",fg='red')
label6.place(x=180,y=260)
label7=tk.Label(window1,text="Designed by Khushal Lalwani,Pawan kumar",fg='red')
label7.place(x=70,y=280)
stbutton=tk.Button(window1,text="Submit",width=9,height=2,command=newwin)

stbutton.place(x=110,y=100)
window1.mainloop()
