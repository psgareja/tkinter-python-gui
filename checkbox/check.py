from tkinter import *

root=Tk()

var=StringVar()
c=Checkbutton(root,text="check",variable=var,onvalue='on',offvalue='off')
c.deselect()
c.pack()

def show():
    myLabel=Label(root,text=var.get()).pack()


myButton=Button(root,text="selection",command=show).pack()
root.mainloop()