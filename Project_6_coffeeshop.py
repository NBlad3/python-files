from tkinter import *

def select():
    if sugar_var.get() == True:
        option1.config(text = "Sugar")
    else:
        option1.config(text = "")
    if cream_var.get() == True:
        option2.config(text = "Cream")
    else:
        option2.config(text = "")
    if ice_var.get() == True:
        option3.config(text = "Ice")
    else:
        option3.config(text = "")

root = Tk()
root.title("Order your drink")
root.geometry("300x400")

sugar_var = BooleanVar()
cream_var = BooleanVar()
ice_var = BooleanVar()

sugar = Checkbutton(root, text = "sugar", variable = sugar_var, command = select)
cream = Checkbutton(root, text = "cream", variable = cream_var, command = select)
ice   = Checkbutton(root, text = "ice",   variable = ice_var,   command = select)

sugar.pack()
cream.pack()
ice.pack()

text = Label(root, text = "Lua chon cua ban la:")
option1 = Label(root, text = "")
option2 = Label(root, text = "")
option3 = Label(root, text = "")

text.pack()
option1.pack()
option2.pack()
option3.pack()

root.mainloop()
