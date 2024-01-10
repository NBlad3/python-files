from tkinter import *
import ast

i = 0
def insert_number(num):
    global i
    display.insert(i, num)
    i += 1

def insert_operation(op):
    global i
    length = len(op)
    display.insert(i, op)
    i += length

def delete():
    current_display = display.get()
    if len(current_display):
        new_display = current_display[:-1]
        display.delete(0, END)
        display.insert(0, new_display)

def calculate():
    current_display = display.get()
    try:
        node = ast.parse(current_display, mode = "eval")
        result = eval(compile(node, "<string>", "eval"))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def clear_all():
    display.delete(0, END)

root = Tk()
root.title("Calculator²")
root.geometry("300x400")

display = Entry(root)
display.grid(row = 1, columnspan = 9, sticky = W+E)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(0, 3):
    for y in range(0,3):
        btn_text = numbers[counter]
        btn = Button(root, text = btn_text, width = 4, height = 2, command = lambda get_num = btn_text: insert_number(get_num))
        btn.grid(row = x + 2, column = y)
        counter += 1
text_0 = 0
btn_0 = Button(text = text_0, width = 4, height = 2, command = lambda get_0 = text_0: insert_number(get_0))
btn_0.grid(row = 5, column = 1)

operations = ['+', '-', '*', '/', '%', '3.14', '(', ')', '**', '**2']
count = 0
for x in range(0, 4):
    for y in range(0, 3):
        if count < len(operations):
            btn_text = operations[count]
            btn = Button(root, text = btn_text, width=4, height=2, command = lambda get_op = btn_text: insert_operation(get_op))
            btn.grid(row = x+2, column = y+3)
            count += 1
btn_del = Button(text = "<--", width = 4, height = 2, command = delete)
btn_del.grid(row = 5, column = 4)

btn_enter = Button(bg = "lightblue", text = "=", width = 4, height = 2, command = calculate)
btn_enter.grid(row = 5, column = 2)

Button(text = "AC", width = 4, height = 2,command= clear_all).grid(row = 5, column = 5)

root.mainloop()
