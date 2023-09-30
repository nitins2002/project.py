'''
Language Detector
-------------------------------------------------------------
pip install langdetect
'''

from langdetect import detect
import tkinter as tk

def check_language():
    new_text = text.get()
    try:
        lang = detect(new_text)
        result_label.config(text=lang)
    except:
        result_label.config(text="Language detection failed")

def detect_lang():
    window = tk.Tk()
    window.geometry('600x400')
    window.title('Language Detector')

    head = tk.Label(window, text='Language Detector', font=('Calibri', 15))
    head.pack(pady=20)

    global text
    text = tk.StringVar()

    entry = tk.Entry(window, textvariable=text)
    entry.place(x=200, y=80, height=30, width=280)

    check_button = tk.Button(window, text='Check Language', command=check_language)
    check_button.place(x=285, y=150)

    global result_label
    result_label = tk.Label(window, text='', font=('Calibri', 15))
    result_label.place(x=260, y=200)

    window.mainloop()

if __name__ == '__main__':
    detect_lang()
