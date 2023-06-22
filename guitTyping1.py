import tkinter as tk
window=tk.Tk()
window.geometry("900x700")
def show():
    if clicked.get()=="Lesson 1":
        droplesson1=tk.OptionMenu(window,dayclicked, *lesson1)
        droplesson1.place(x=90,y=5)
        if dayclicked.get()=="Day 1":
            f=open("day1.txt","r")
            for i in f:
                print(text[i])
            f.close()
    elif clicked.get()=="Lesson 2":
        droplesson1=tk.OptionMenu(window,dayclicked, *lesson2)
        droplesson1.place(x=90,y=5)
        
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
text=tk.Text(bg="blue",fg="red")
text.place(x=170,y=90)
window.mainloop()
