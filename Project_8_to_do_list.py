from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)


def delete_task():
    try:
        task_index = listbox.curselection()
        for task in reversed(task_index):
            listbox.delete(task)
            message.config(text = "Deleted successfully")

    except:
        message.config(text = "Please choose something to delete")

root = Tk()

root.title("To Do List")

root.geometry("400x500")

frame = Frame(root)
frame.pack()

task_entry = Entry(frame, width = 30)
task_entry.pack(side = LEFT)

add_button = Button(frame, text = "Add", width = 15, command = add_task)
add_button.pack(side = LEFT)

listbox = Listbox(root, height = 10, width = 50, selectmode = MULTIPLE)
listbox.pack()

message = Label(root)
message.pack()

delete_button = Button(root, text = "Delete", width = 10, command = delete_task)
delete_button.pack()

root.mainloop()
