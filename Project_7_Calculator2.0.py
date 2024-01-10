from tkinter import *

root = Tk()
root.title("Calculator 2.0")
root.geometry("300x400")

def action_plus():
    if var_plus.get():
        result = int(num_1.get()) + int(num_2.get())
        plus.config(text = num_1.get() + " + " + num_2.get() + " = " + str(result))
    else:
        plus.config(text = "")

def action_minus():
    if var_minus.get():
        result = int(num_1.get()) - int(num_2.get())
        minus.config(text = f"{num_1.get()} - {num_2.get()} = {result}")
    else:
        minus.config(text = "")

def action_multi():
    if var_multi.get():
        result = int(num_1.get()) * int(num_2.get())
        multi.config(text = f"{num_1.get()} * {num_2.get()} = {result}")
    else:
        multi.config(text = "")

def action_divide():
    if var_divide.get():
        result = int(num_1.get()) / int(num_2.get())
        divide.config(text = f"{num_1.get()} / {num_2.get()} = {result}")
    else:
        divide.config(text = "")

num_1 = Entry()
num_2 = Entry()
num_1.pack()
num_2.pack()

var_plus = BooleanVar()
checkbtn_plus = Checkbutton(root, text = "+", variable = var_plus, command = action_plus)
checkbtn_plus.pack()

var_minus = BooleanVar()
checkbtn_minus = Checkbutton(root, text = "-", variable = var_minus, command = action_minus)
checkbtn_minus.pack()

var_multi = BooleanVar()
checkbtn_multi = Checkbutton(root, text = "*", variable = var_multi, command = action_multi)
checkbtn_multi.pack()

var_divide = BooleanVar()
checkbtn_divide = Checkbutton(root, text = "/", variable = var_divide, command = action_divide)
checkbtn_divide.pack()

plus = Label(root)
plus.pack()

minus = Label(root)
minus.pack()

multi = Label(root)
multi.pack()

divide = Label(root)
divide.pack()

root.mainloop()
