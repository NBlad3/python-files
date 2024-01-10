from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("ROW & COLUMN")

email_text= Label(root, text = "Email: ")
email_text.grid(row = 0, column = 0)

email_entry = Entry(root)
email_entry.grid(row = 0, column = 1)

password_text= Label(root, text = "Passwort: ")
password_text.grid(row = 1, column = 0)

password_entry = Entry(root)
password_entry.grid(row = 1, column = 1)

login = Button(root, text = "Login")
login.grid(row = 2, column = 1)

root.mainloop()


