import tkinter as tk
'''
window=tk.Tk()
window.geometry("300x300")
tk.Label(text="Hello").pack()
window.mainloop()
'''

'''
window=tk.Tk()
window.geometry("300x300")
greeting=tk.Label(text="Hello")
greeting=tk.Label(text="veer",fg="white",background="black")
greeting.pack()
'''


window=tk.Tk()
window.geometry("300x300")
greeting=tk.Label(text="Hello").pack()

entry=tk.Entry(fg='brown',bg='white',width=50)
entry.insert(0,"khushal")
entry.insert(0,"Veer")
entry.pack()
name=entry.get()
entry.delete(0)


#entry.insert(0,"python")
#entry.insert(0,'real')
greeting=tk.Label(text="veer",fg="white",background="black")
tk.Button(text="click",width=10,height=2,bg="blue",fg="yellow").pack()
window.mainloop()
