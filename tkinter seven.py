import tkinter as tk
window=tk.Tk()
window.geometry("400x400")
frame1=tk.Frame()

frame1.pack()
frame2=tk.Frame()
frame2.pack()
label1=tk.Label(master=frame1,text="I'M in frame 1")
label2=tk.Label(master=frame2,text="I'M in frame 2")
label1.pack()
label2.pack()
window.mainloop()