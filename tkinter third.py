import tkinter as tk
import pandas as  pd
window=tk.Tk()
window.geometry("400x400")

label=tk.Label(text="Name:",height=2,fg="red").place(x=10,y=10)
label=tk.Label(text="Email:",height=2,fg="red").place(x=10,y=50)
label=tk.Label(text="Country:",height=2,fg="red").place(x=10,y=90)
label=tk.Label(text="City:",height=2,fg="red").place(x=10,y=130)
label=tk.Label(text="Address:",height=2,fg="red").place(x=10,y=170)
entry1=tk.Entry(width=30)
entry1.place(x=70,y=20)
entry2=tk.Entry(width=30)
entry2.place(x=70,y=60)
entry3=tk.Entry(width=30)
entry3.place(x=70,y=100)
entry4=tk.Entry(width=30)
entry4.place(x=70,y=140)
entry5=tk.Entry(width=30)
entry5.place(x=70,y=180)

def onclick():
    li=[entry1.get(),",",entry2.get(),",",entry3.get(),",",entry4.get(),",",entry5.get(),"\n"]
    file=open("veer3.csv",'a+')
    for i in range(10):    
        file.write(str(li[i]))
    file.close()
    
button=tk.Button(text="submit",bg='blue',width=5,height=2,command=onclick).place(x=100,y=220)
window.mainloop()


a=pd.read_csv('veer2.csv')
print(a)