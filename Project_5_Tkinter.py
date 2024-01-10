from tkinter import *

def button_1_action():
    number_1 = int(num_1.get())
    number_2 = int(num_2.get())
    result = number_1 + number_2
    answer.config(text = "Ket qua cua phep cong la: " + str(result))

def button_2_action():
    number_1 = int(num_1.get())
    number_2 = int(num_2.get())
    result = number_1 - number_2
    answer.config(text = "Ket qua cua phep tru la: " + str(result))

def button_3_action():
    number_1 = int(num_1.get())
    number_2 = int(num_2.get())
    result = number_1 * number_2
    answer.config(text = "Ket qua cua phep nhan la: " + str(result))

def button_4_action():
    number_1 = int(num_1.get())
    number_2 = int(num_2.get())
    result = number_1 / number_2
    answer.config(text = "Ket qua cua phep chia la: " + str(result))


root = Tk()

root.title("Calculator")

root.geometry("300x400")

num_1 = Entry()
num_2 = Entry()
num_1.pack()
num_2.pack()

button_1 = Button(root, text = "+", command = button_1_action)
button_1.pack()

button_2 = Button(root, text = "-", command = button_2_action)
button_2.pack()

button_3 = Button(root, text = "*", command = button_3_action)
button_3.pack()

button_4 = Button(root, text = "/", command = button_4_action)
button_4.pack()

answer = Label(root)
answer.pack()

root.mainloop()

