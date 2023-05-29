import tkinter as tk
from madlibEn import *
from madlibHu import *
from madlibEs import *
from madlibIt import *
from madlibGe import *


def language_selected(lang):
    print(f"Selected language: {lang}")
    if lang == "English":
        eng_main()
    elif lang == "Magyar":
        hun_main()
    elif lang == "Español":
        esp_main()
    elif lang == "Italiano":
        ita_main()
    elif lang == "Deutsch":
        ger_main()


def create_language_option_page():
    window = Tk()
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.overrideredirect(1)
    window.geometry("%dx%d+0+0" % (w, h))
    window.configure(bg='lightblue')
    window.title("Language Options")
    label_text = "Choose a language!"
    label = tk.Label(window, text=label_text, justify="center", anchor="center", font='helvetica 50 bold', pady='40', bg='lightblue')
    label.pack()

    languages = ["English", "Magyar", "Español", "Italiano", "Deutsch"]
    for lang in languages:
        button = tk.Button(window, text=lang, command=lambda lang=lang: language_selected(lang), bg='white', font='Helvetica 30')
        button.pack(pady=3)

    exit_button = Button(window, text="Exit", command=window.destroy, bg='white', font='helvetica 30')
    exit_button.pack(pady=70)

    window.mainloop()


create_language_option_page()
