import self as self

import MainCode
from tkinter import *
from tkinter.messagebox import *


def show_answer():
    # inputString = hindi_string.get()
    inputString = self.MyEntryBox.get("1.0", END)
    stemDict = MainCode.mainfunctioncode(inputString)
    output.insert('1.0', stemDict)


main = Tk()
main.title("Morphological_Analyzer")
main.configure(background="#dddddd")
main.geometry("1920x1080")
Label(main, text="Enter \nSentence:", bg="#dddddd",
      fg="black", font="none 12 bold").place(x=15, y=10)
Label(main, text="Output:", bg="#dddddd",
      fg="black", font="none 12 bold").place(x=15, y=220)


self.MyEntryBox = Text(main, height=3, width=170, relief=RIDGE)
self.MyEntryBox.place(x=120, y=15)
# hindi_string = Entry(main)
# blank = Entry(main)

output = Text(main, width=170, height=25, wrap=WORD, background="white")
output.place(x=120, y=220)

# hindi_string.grid(row=4, column=5)
# blank.grid(row=15, column=37)


Button(main, text='Quit', width=25, height=3, command=main.destroy).place(
    x=1100, y=700)
Button(main, text='Show', width=25, height=3, command=show_answer).place(
    x=700, y=75)


mainloop()
