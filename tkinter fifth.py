import tkinter as tk
window=tk.Tk()
window.geometry("400x300")
tb1=tk.Text(bg='black',fg='white')
tb1.pack()
tb1.insert('1.0','hello')
a=tb1.get('1.0')
tb1.delete('1.0',tk.END)
print(a)
window.mainloop()