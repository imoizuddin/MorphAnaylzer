import self as self

import MainCode
from tkinter import *
from tkinter.messagebox import *


def show_answer():
    # inputString = hindi_string.get()
    inputString = self.MyEntryBox.get("1.0", END)
    stemDict = MainCode.mainfunctioncode(inputString)
    output2.insert('1.0', stemDict)


main = Tk()
main.title("Morphological_Analyzer")
main.configure(background="#dddddd")
main.geometry("1920x1080")
Label(main, text="Enter \nSentence:", bg="#dddddd",
      fg="black", font="none 12 bold").place(x=15, y=10)
Label(main, text="Tokens:", bg="#dddddd",
      fg="black", font="none 12 bold").place(x=15, y=220)
Label(main, text="Root \nWords:", bg="#dddddd",
      fg="black", font="none 12 bold").place(x=15, y=350)
Label(main, text="POS Tags:", bg="#dddddd",
      fg="black", font="none 12 bold").place(x=15, y=510)

self.MyEntryBox = Text(main, height=3, width=170, relief=RIDGE)
self.MyEntryBox.place(x=120, y=15)

output = Text(main, width=170, height=9, wrap=WORD, background="white")
output.place(x=120, y=170)

output1 = Text(main, width=170, height=9, wrap=WORD, background="white")
output1.place(x=120, y=330)

output2 = Text(main, width=170, height=9, wrap=WORD, background="white")
output2.place(x=120, y=490)

Button(main, text='Quit', width=25, height=3, command=main.destroy).place(
    x=1100, y=700)
Button(main, text='Show', width=25, height=3, command=show_answer).place(
    x=700, y=75)

mainloop()
