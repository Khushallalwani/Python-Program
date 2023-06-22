import tkinter as tk
window1=tk.Tk()
window1.geometry("600x500")
li=[]
li1=[]
st1=""
st=""
select1=0
next1=1
nextind=1
nextend=1
marks=0


def onclick():
    li=[nameentry.get(),",",acnumentry.get(),"\n"]
    file=open("data5.csv",'a+')
    for i in range(4):    
        file.write(str(li[i]))
    file.close()

def newwin():
    global st1
    sub=nameentry.get()
    sub1=acnumentry.get() 
    onclick()
    if sub!="" and sub1!="":
        window1.destroy()
        window=tk.Tk()
        window.geometry("1300x800")
        frame1=tk.Frame(window,width=450,height=350,bg="light blue")
        a=open('question2.csv','r')
        for i in a:
            li.append(i)
        st=li[0]
        for k in st:
            if k!=',':
                st1=st1+k
            if k==',':
                li1.append(st1)
                st1=""
    def nextqu():
        global nextind,st1,st,next1,select1,nextend,li
        radioin()
        if next1==0 and nextend<len(li):
            li1.clear()
            st=li[nextind]
            for k in st:
                if k!=',':
                    st1=st1+k
                if k==',':
                    li1.append(st1)
                    st1=""
            nextind=nextind+1
            qution_lb.configure(text=li1[0])
            op1.configure(text=li1[1],variable=radio,value=1)
            op2.configure(text=li1[2],variable=radio,value=2)
            op3.configure(text=li1[3],variable=radio,value=3)
            op4.configure(text=li1[4],variable=radio,value=4)
            change_color2()
            select1=0
            next1=1
            nextend=nextend+1
        if nextend==len(li):
            nextbutton.configure(text="Complete")
    
    def radioin():
        radio.set(-1)
    def change_color():
        button.configure(bg="green", fg= "white")
    def change_color1():
        button.configure(bg="red", fg= "white")
    def change_color2():
        button.configure(bg="black", fg= "white")
    def selection():
        global select1,next1,marks
        if select1==0 and radio.get()!=0:
            if li1[5]==li1[1] and radio.get()==1:
                change_color()
                marks=marks+1
            elif li1[5]==li1[2] and radio.get()==2:
                change_color()
                marks=marks+1
            elif li1[5]==li1[3] and radio.get()==3:
                change_color()
                marks=marks+1
            elif li1[5]==li1[4] and radio.get()==4:
                change_color()
                marks=marks+1
            else:
                change_color1()
            select1=1
            next1=0
            markslabel1.configure(text=marks)

    qution_lb=tk.Label(master=frame1,text=li1[0])
    qution_lb.place(x=10,y=10)
    radio=tk.IntVar()
    op1=tk.Radiobutton(master=frame1,text=li1[1],variable=radio,value=1)
    op1.place(x=10,y=40,)
    op2=tk.Radiobutton(master=frame1,text=li1[2],variable=radio,value=2)
    op2.place(x=10,y=70)
    op3=tk.Radiobutton(master=frame1,text=li1[3],variable=radio,value=3)
    op3.place(x=10,y=100)
    op4=tk.Radiobutton(master=frame1,text=li1[4],variable=radio,value=4)
    op4.place(x=10,y=130)
    button=tk.Button(master=frame1,text="Submit",command=selection)
    button.place(x=100,y=250)
    button.configure(bg="black", fg= "white")
    nextbutton=tk.Button(master=frame1,text="Next->",bg="black",fg="white",command=nextqu)
    nextbutton.place(x=300,y=250)
    markslabel=tk.Label(window,text="Marks : ")
    markslabel.place(x=400,y=15)
    markslabel1=tk.Label(window)
    markslabel1.place(x=440,y=15)
    frame1.place(x=80,y=40)
    window.mainloop()

namelabel=tk.Label(window1,text="Enter Name")
namelabel.place(x=30,y=10)
nameentry=tk.Entry(window1)
nameentry.place(x=120,y=10)

acnum=tk.Label(window1,text="Enter College Id")
acnum.place(x=30,y=40)
acnumentry=tk.Entry(window1)
acnumentry.place(x=120,y=40)
startbtn=tk.Button(window1,text="submit",command=newwin)
startbtn.place(x=50,y=90)
window1.mainloop()
