import tkinter as tk
window=tk.Tk()
window.geometry("300x300")
entry=tk.Entry(fg='brown',bg='white',width=50)
window.mainloop()

a=open('day1.txt','r')
for i in a:
    print(i)
    