import tkinter as tk
window=tk.Tk()
window.geometry("600x500")
frame1=tk.Frame(width=450,height=350)
a=open('question2.csv','r')
li=[]
li1=[]
st1=""
k=0
for i in a:
    li.append(i)
st=li[0]
for k in st:
    if k!=',':
        st1=st1+k
    if k==',':
            li1.append(st1)
            st1=""
print(li1)

def selection():
    st=str(radio.get())
    label.config(text=st)
qution_lb=tk.Label(master=frame1,text=li[0])
qution_lb.place(x=10,y=10)
radio=tk.IntVar()
op1=tk.Radiobutton(master=frame1,text=li[1],variable=radio,value=1,command=selection)
op1.place(x=10,y=40,)
op2=tk.Radiobutton(master=frame1,text=li[2],variable=radio,value=2,command=selection)
op2.place(x=10,y=70)
op3=tk.Radiobutton(master=frame1,text=li[3],variable=radio,value=3,command=selection)
op3.place(x=10,y=100)
op4=tk.Radiobutton(master=frame1,text=li[4],variable=radio,value=4,command=selection)
op4.place(x=10,y=130)
label=tk.Label(master=frame1)
label.place(x=10,y=100)
frame1.place(x=80,y=40)
window.mainloop()
