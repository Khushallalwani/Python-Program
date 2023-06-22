import tkinter as tk
def compare_data():
    with open('day1.txt', 'r') as file:
        file_data = file.read()

    widget_data = text_widget.get('1.0', tk.END)
    print(widget_data)
    print(type(widget_data))
    print(file_data)
    if file_data == widget_data:
        print("The data matches!")
    else:
        print("The data does not match.")

window = tk.Tk()

text_widget = tk.Text(window)
text_widget.pack()

with open('day1.txt', 'r') as file:
    initial_data = file.read()
    text_widget.insert(tk.END, initial_data)

compare_button = tk.Button(window, text="Compare", command=compare_data)
compare_button.pack()
window.mainloop()