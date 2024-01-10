from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import ttk

def translate_word():
    translator = Translator()
    word = input_word.get()
    lang = lang_var.get()
    output_word = translator.translate(word, lang)
    output.config(text = output_word.text)

root = Tk()
root.title("Translator")
root.geometry("500x200")

note_input = Label(root, text = "Word:", font = ("Calibri, 14"))
note_input.pack()
input_word = Entry(root, font = ("Calibri, 14"))
input_word.pack()

note_language = Label(root, text = "Language:", font = ("Calibri, 14"))
note_language.pack()
lang_var = StringVar(root)
lang_var.set("english")
lang_dropdown = ttk.Combobox(root, textvariable = lang_var, values= list(LANGUAGES.values()), font = ("Calibri, 14"))
lang_dropdown.pack()

translate_button = Button(root, text = "Translate", command = translate_word, font = ("Calibri, 14"), bg = "lightgreen")
translate_button.pack()

output = Label(root, font = ("Calibri, 14"))
output.pack()

root.mainloop()
