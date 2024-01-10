from tkinter import *
import random

dictionary = {"Apple" : "Quả táo",
              "Banana" : "Qủa chuối",
              "Time" : "Giờ",
              "Phone" : "Điện thoại",
              "Computer" : "Maý tính"}

def new_word():
    vocab, meaning = random.choice(list(dictionary.items()))
    english_word.config(text = vocab)
    vietnamese_word.config(text = meaning)

root = Tk()
root.title("Vocabulary")
root.geometry("300x400")

english_word = Label(root)
vietnamese_word = Label(root)
new_word_btn = Button(root, text = "New word", command = new_word)

english_word.pack()
vietnamese_word.pack()
new_word_btn.pack()

root.mainloop()
