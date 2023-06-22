import tkinter as tk
window=tk.Tk()
window.geometry("400x400")
label=tk.Label(text="Name:",height=2,fg="red").place(x=10,y=10)
entry1=tk.Entry(width=30)
entry1.place(x=70,y=20)
label=tk.Label(text="DOB:",height=2,fg="red").place(x=10,y=50)
entry2=tk.Entry(width=30)
entry2.place(x=70,y=60)
entry3=tk.Entry(width=5)
entry3.place(x=100,y=130)
tk.Label(text="Calculator").place(x=150,y=90)
entry4=tk.Entry(width=5)
entry4.place(x=150,y=130)
tk.Label(text="=").place(x=180,y=130)
entry5=tk.Entry(width=8)
entry5.place(x=210,y=130)

def add():
   z=str(int(entry3.get())+int(entry4.get()))
   entry5.insert(0,z) 

def subtract():
   z=str(int(entry3.get())-int(entry4.get()))
   entry5.insert(0,z) 
def multiply():
   z=str(int(entry3.get())*int(entry4.get()))
   entry5.insert(0,z) 
def divide():
   z=str(int(entry3.get())/int(entry4.get()))
   entry5.insert(0,z) 

def back():
    entry3.delete(0)
    entry4.delete(0)
    entry5.delete(0)
    
def onclick():
    li=[entry1.get(),",",entry2.get(),",",entry5.get(),"\n"]
    file=open("veer3.csv",'a+')
    for i in range(6):    
        file.write(str(li[i]))
    file.close()
    

    

    
    
button1=tk.Button(text="+",bg='black',fg='white',width=3,height=1,command=add).place(x=100,y=180)
button2=tk.Button(text="-",bg='black',fg='white',width=3,height=1,command=subtract).place(x=140,y=180)
button3=tk.Button(text="*",bg='black',fg='white',width=3,height=1,command=multiply).place(x=180,y=180)
button4=tk.Button(text="/",bg='black',fg='white',width=3,height=1,command=divide).place(x=220,y=180)
button5=tk.Button(text="<-",bg='black',fg='white',width=2,height=1,command=back).place(x=270,y=130)
button=tk.Button(text="submit",bg='blue',width=5,height=2,command=onclick).place(x=100,y=220)
window.mainloop()