from tkinter import *

def test_action():
    if checkbtn_var.get() == True:
        print("Test")
    else:
        print("...")

root = Tk()
root.title("Checkbox")
root.geometry("300x300")

checkbtn_var = BooleanVar()

checkbtn_1 = Checkbutton(root, text = "<- Click here", variable = checkbtn_var, command = test_action)
checkbtn_1.pack()

checkbtn_2 = Checkbutton(root, text = "Dont click")
checkbtn_2.pack()

root.mainloop()

