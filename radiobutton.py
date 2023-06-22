import tkinter as tk
window=tk.Tk()
window.geometry("300x300")
def selection():
    a=open('question2.csv','r')
    li=[]
    for i in a:
        li.append(i)