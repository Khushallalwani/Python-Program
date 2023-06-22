import tkinter as tk
window2=tk.Tk()
window2.geometry("200x200")
def openNewWindow():
	Window1=tk.Toplevel(window2)
	window1.geometry("200x200")

btn=tk.Button(window2,text ="Start",command = openNewWindow)
btn.pack(pady = 10)
window2.mainloop()
