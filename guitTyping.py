import tkinter as tk
window=tk.Tk()
window.geometry("900x700")
def show():
    label.config(text=clicked.get())
option=["Lesson 1","Lesson 2","Lesson 3","Lesson 4","Lesson 5","Lesson 6"
        ,"Lesson 7","Lesson 8","Lesson 9","Lesson 10","Lesson 11","Lesson 12","Lesson 13"
        ,"Lesson 14","Lesson 15","Lesson 16"]
lesson1=["Day1","Day2","Day3","Day4","Day5","Day6","Day7"]
clicked=tk.StringVar()
drop=tk.OptionMenu(window,clicked, *option)
drop.pack()
button=tk.Button(text="click",command=show)
button.pack()
label=tk.Label(window,text=" ")
label.pack()
window.mainloop()
