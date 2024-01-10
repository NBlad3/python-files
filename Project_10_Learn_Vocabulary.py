from tkinter import *
import random

word_global = ""
meaning_global = ""

def show_word():
    global word_global, meaning_global
    word, mean = random.choice(list(vocab.items()))
    word_global = word
    meaning_global = mean
    word_label.config(text=word, font=("Arial", 32))
    meaning_label.config(text="")
    ans_user.delete(0, END)

def check_ans():
    user_answer = ans_user.get()
    if user_answer.lower() == meaning_global:
        meaning_label.config(text=f"Đúng, {word_global} nghĩa là {meaning_global}", fg="Green")
    else:
        meaning_label.config(text=f"Sai, {word_global} nghĩa là {meaning_global}", fg = "Red")

vocab = {
    "Apple": "quả táo",
    "Banana": "quả chuối",
    "Car": "ô tô"
}


root = Tk()
root.geometry("500x500")
root.title("English test")

word_label = Label(root)
meaning_label = Label(root, font=("Arial", 25))
ans_user = Entry(root)
check_ans_button = Button(root, text="Kiểm tra", command= check_ans)
new_word = Button(root, text="Từ mới", command=show_word)

word_label.pack()
meaning_label.pack(pady=10)
ans_user.pack()
check_ans_button.pack()
new_word.pack()

show_word()
root.mainloop()
