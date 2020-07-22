import self as self

import MainCode
from tkinter import *
from tkinter.messagebox import *


def show_answer():
    inputString = self.MyEntryBox.get("1.0", END)
    tokens = MainCode.mainfunctioncodet(inputString)
    stemmer = MainCode.mainfunctioncodestem(inputString)
    postagg = MainCode.mainfunctioncodepos(inputString)

    output.insert('1.0', tokens)
    output1.insert('1.0', stemmer)
    output2.insert('1.0', postagg)


main = Tk()
main.title("Morphological_Analyzer")
main.configure(background="#F5F5F5")
main.geometry("1920x1080")
Label(main, text="Enter \nSentence:", bg="#F5F5F5",
      fg="#000000", font="none 12 bold").place(x=15, y=16)
Label(main, text="Tokens:", bg="#F5F5F5",
      fg="#000000", font="none 12 bold").place(x=15, y=250)
Label(main, text="Root \nWords:", bg="#F5F5F5",
      fg="#000000", font="none 12 bold").place(x=17, y=380)
Label(main, text="POS \nTags:", bg="#F5F5F5",
      fg="#000000", font="none 12 bold").place(x=17, y=540)

self.MyEntryBox = Text(main, height=4, width=170, relief=RIDGE)
self.MyEntryBox.place(x=120, y=17)

output = Text(main, width=170, height=9, wrap=WORD, background="white")
output.place(x=120, y=170)

output1 = Text(main, width=170, height=9, wrap=WORD, background="white")
output1.place(x=120, y=330)

output2 = Text(main, width=170, height=9, wrap=WORD, background="white")
output2.place(x=120, y=490)

Button(main, text='Quit', width=25, height=3, command=main.destroy).place(
    x=1170, y=700)
Button(main, text='Show', width=25, height=3, command=show_answer).place(
    x=700, y=95)

mainloop()
