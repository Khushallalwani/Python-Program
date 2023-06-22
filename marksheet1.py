from tkinter import *
root = Tk()
frame1=Frame(root)
frame2=Frame(root)
height = 5
width = 1
li=[]
li1=[]
data=[]
delta=0
for i in range(height): #Rows
  for j in range(width): #Columns
      li.append(Label(frame1,text="label"))
      li[i].grid(row=i, column=j,pady=4)
for i in range(height): #Rows
  for j in range(width): #Columns
    li1.append(Entry(frame2, text="",width=8))
    li1[i].grid(row=i, column=j,pady=5)
def click():
    for i in range(height):
        data.append(li1[i].get())
    print(data)
button=Button(root,text="click",command=click)
button.pack()
frame1.place(x=0,y=0)
frame2.place(x=50,y=0)
mainloop()