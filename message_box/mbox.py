from tkinter import *
from tkinter import messagebox
root=Tk()

def popup():
    messagebox.showinfo("This is my Popup!","Hello World!")
Button(root,text="Popup",command=popup).pack()


mainloop()