import tkinter as tk
window=tk.Tk()
window.geometry("1300x700")
stdata=""
err=0
j=0
def comp():
    global stdata
    global err
    stinput=textinput.get("1.0",tk.END)
    for i in range(len(stdata)):
        if stdata[i]!=stinput[i]:
            err=err+1
    print(err)    
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
            print(stdata)
            f.close()
            j=1    
            
        elif dayclicked.get()=="Day 2" and j!=2:
            f=open("day2.txt","r")
            f.close()
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
text=tk.Text(bg="white",fg="black",width=100,height=20)
text.place(x=230,y=30)
textinput=tk.Text(bg="white",fg="black",width=100,height=20)
textinput.place(x=230,y=400)
window.mainloop()
