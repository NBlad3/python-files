from tkinter import *

root = Tk()
root.title("Frames")
root.geometry("300x400")

frame1 = Frame(root, bg= "blue", bd = 10)
frame1.pack()
btn1 = Button(frame1, text = ":)")
btn1.pack()

frame2 = Frame(root, bg = "darkorange", bd = 10)
frame2.pack()
btn2 = Button(frame2, text = ":(")
btn2.pack()

root.mainloop()
